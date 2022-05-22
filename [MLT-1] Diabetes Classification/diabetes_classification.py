# -*- coding: utf-8 -*-
"""Diabetes Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AyEK8V7JLGzWNSQru_V-qsvLzjfSBkgS

# Diabetes Classification

## DataSet Information:
<p align='center'>
	<img  width='100%' src='https://img001.prntscr.com/file/img001/VdL8n7JfSL-Xi0Wsw-xaFg.png' alt='Sumber: https://www.kaggle.com/datasets/mathchi/diabetes-data-set'>
</p>

| Jenis | Keterangan |
| - | - |
| Original owners | National Institute of Diabetes and Digestive and Kidney Diseases |
| Sumber | [Kaggle Dataset : Diabetes](https://www.kaggle.com/datasets/mathchi/diabetes-data-set) |
| Jenis dan Ukuran Berkas | CSV (23.87 kB) |
| Rating Penggunaan | 10.0 (Gold) |
| Lisensi | CC0: Public Domain |

Penjelasan mengenai variabel-variable pada data diabetes dapat dilihat pada poin-poin berikut:

- `Pregnancies`: Jumlah berapa kali hamil
- `Glucose`: Konsentrasi glukosa plasma 2 jam dalam tes toleransi glukosa oral
- `BloodPressure`: Tekanan darah diastolik (mm Hg)
- `SkinThickness`: Ketebalan lipatan kulit trisep (mm)
- `Insulin`: Insulin serum 2 Jam (mu U/ml)
- `BMI`: Indeks massa tubuh (berat dalam kg/(tinggi dalam m)^2)
- `DiabetesPedigreeFunction`: Fungsi silsilah diabetes
- `Age`: Usia (tahun)
- `Outcome`: Variabel kelas (0 atau 1) yang menandakan diabetes atau tidak

## Import Dataset
"""

import os
os.environ['KAGGLE_USERNAME'] = 'lanaahm'
os.environ['KAGGLE_KEY'] = 'c5dac849baf021db5db739062fdf3105'

!kaggle datasets download -d mathchi/diabetes-data-set

!unzip /content/diabetes-data-set.zip

"""## Import Library"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import confusion_matrix, classification_report

"""## EDA (Exploratory Data Analysis)

### Convert Dataset into pandas
"""

df = pd.read_csv('/content/diabetes.csv')
df.head()

"""### Check column description"""

df.info()

"""### Check Missing Value"""

df.isna().sum()

"""### Check the description of dataset statistics"""

df.describe()

"""Dapat dilihat pada tabel diatas bawah ada beberapa data yang memiliki nilai 0 seperti pada data `Glucose`, `BloodPressure`, dan `BMI` yang merupakan data tersebut tidak mungkin memiliki nilai 0 untuk mengatasi masalah tersebut dapat dilakukan pengisian data.

"""

ZeroGlucose = (df.Glucose == 0).sum()
ZeroBloodPressure = (df.BloodPressure == 0).sum()
ZeroBMI = (df.BMI == 0).sum()
 
print("Nilai 0 di kolom Glucose ada: ", ZeroGlucose)
print("Nilai 0 di kolom BloodPressure ada: ", ZeroBloodPressure)
print("Nilai 0 di kolom BMI ada: ", ZeroBMI)

"""Nilai kosong pada data `Glucose` dan `BloodPressure` akan dilakukan pengisian nilai dengan yang sering keluar atau modus sedangkan pada data `BMI` diisi dengan nilai rata-rata atau maen."""

df['Glucose'].replace(0, df.Glucose.mode()[0], inplace=True)
df['BloodPressure'].replace(0, df.BloodPressure.mode()[0], inplace=True)

df['BMI'].replace(0, df.BMI.mean(), inplace=True)

df.describe()

"""Hasil dari pengisian data dapat dilihat pada tabel diatas nilai minimal pada data `Glucose`, `BloodPressure`, dan `BMI` bukan bernilai 0

### Outliers Analysis
"""

plt.figure(figsize=(16, 8))
plt.title('Boxplots Dataset')

sns.boxplot(y='Feature', x='', data=df.melt(var_name='Feature', value_name=''))

"""### Handles outliers with IQR method"""

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR=Q3-Q1

df=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]
 
# Cek ukuran dataset setelah kita drop outliers
df.shape

plt.figure(figsize=(16, 8))
plt.title('Boxplots Dataset')

sns.boxplot(y='Feature', x='', data=df.melt(var_name='Feature', value_name=''))

"""Dari visualisasi Blox Plot diatas dapat dilihat masih banyak fitur data yang mengalami outlier dikarenakan data tersebut seharunya data yang memiliki range kategori kategori.

## Feature Engineering

### Converting data into categories
Dari dataset diabetes yang digunakan pada proyek ini memiliki beberapa fitur data yang meruapakan data kategori namun masih dalam bentuk numerik sehingga beberapa data tersebut mengalami outliers beberapa fitur tersebut antara lain:. 
- `Glucose`: Artikel "Glucose Tolerance Testing: Reference Range, Interpretation, Collection and Panels" menjelaskan bahwa glucose tolerance digunakan untuk mengevaluasi kemampuan untuk mengatur metabolisme glukosa dan diindikasikan ketika tes glukosa darah untuk dilakukan diagnosis. Fitur Glucose pada dataset ini adalah data numerik dengan range Konsentrasi glukosa plasma 2 jam nilai numerik tersebut sudah ditentukan pada setiap kategori seperti yang dijelaskan pada artikel<a href="#ref1">[1]</a>.
- `BloodPressure`: Artikel "High Blood Pressure Symptoms and Causes" mejelaskan bahwa tekanan darah akan berubah sepanjang hari berdasarkan aktivitas yang dilakukan. fitur BloodPressure pada dataset ini adalah data numerik. Nilai numerik tersebut sudah ditentukan pada setiap kategori seperti yang sudah dijelaskan dalam artikel<a href="#ref4">[4]</a>.
- `Insulin`: Artikel "Insulin: Reference Range, Interpretation, Collection and Panels" menjelaskan bahwa Insulin adalah hormon anabolik yang mendorong pengambilan glukosa, glikogenesis, lipogenesis, dan sintesis protein otot rangka dan jaringan lemak melalui jalur reseptor tirosin kinase. Fitur Insulin pada dataset ini adalah data numerik dengan range 2 jam setelah pemberian glukosa yang bernilai numerik. Artikel tersebut mejelaskan bahwa nilai insulin berada pada range 16-166 mIU/L sepetelah 2 jam setelah pemberian glukosa untuk kategori normal<a href="#ref3">[3]</a>.
- `BMI`: Artikel "About Adult BMI | Healthy Weight, Nutrition, and Physical Activity" mejelaskan bahwa BMI adalah metode pemeriksaan yang mudah untuk mengetahui kategori berat badan. fitur BMI pada dataset ini adalah data numerik. Nilai numerik tersebut sudah ditentukan pada setiap kategori seperti untuk dapat menetahui kondisi kategori berat badan<a href="#ref2">[2]</a>.
"""

TempGlucose = pd.Series(['Nondiabetic', 'Prediabetic', 'Diabetic'], dtype='category')
df['TempGlucose'] = TempGlucose
df.loc[df['Glucose'] < 100, 'TempGlucose'] = TempGlucose[0]
df.loc[df['Glucose'] > 125, 'TempGlucose'] = TempGlucose[2]
df.loc[(df['Glucose'] >= 100) & (df['Glucose'] <= 125), 'TempGlucose'] = TempGlucose[1]

TempBloodPressure = pd.Series(['Normal', 'Prehypertension', 'Hypertension'], dtype='category')
df['TempBloodPressure'] = TempBloodPressure
df.loc[df['BloodPressure'] < 80, 'TempBloodPressure'] = TempBloodPressure[0]
df.loc[df['BloodPressure'] > 89, 'TempBloodPressure'] = TempBloodPressure[2]
df.loc[(df['BloodPressure'] >= 80) & (df['BloodPressure'] <= 89), 'TempBloodPressure'] = TempBloodPressure[1]

TempInsulin = pd.Series(['Abnormal', 'Normal'], dtype='category')
df['TempInsulin'] = TempInsulin
df.loc[(df['Insulin'] < 16) | (df['Insulin'] > 166), 'TempInsulin'] = TempInsulin[0]
df.loc[(df['Insulin'] >= 16) & (df['Insulin'] <= 166), 'TempInsulin'] = TempInsulin[1]

TempBMI = pd.Series(['Underweight', 'Healthy Weight', 'Overweight', 'Obesity'], dtype='category')
df['TempBMI'] = TempBMI
df.loc[df['BMI'] < 18.5, 'TempBMI'] = TempBMI[0]
df.loc[(df['BMI'] >= 18.5) & (df['BMI'] <= 24.9), 'TempBMI'] = TempBMI[1]
df.loc[(df['BMI'] >= 25.0) & (df['BMI'] <= 29.9), 'TempBMI'] = TempBMI[2]
df.loc[df['BMI'] > 29.9, 'TempBMI'] = TempBMI[3]

df.drop(['Glucose', 'BloodPressure', 'Insulin', 'BMI'], inplace=True, axis=1)
df.rename(columns={'TempGlucose': 'Glucose', 'TempBloodPressure': 'BloodPressure', 'TempInsulin': 'Insulin', 'TempBMI': 'BMI'}, inplace=True)
df.head()

"""### Univariate Analysis"""

numerical_features = df.select_dtypes(include=['int64','float64']).columns.to_list()[:-1]
categorical_features = df.select_dtypes(include='category').columns.to_list()

"""#### Categorical Features"""

fig, ax = plt.subplots(1,4, figsize=(18,4))
for index, feature in enumerate(categorical_features):
  df[feature].value_counts().plot(kind='bar', ax=ax[index], rot=60, title=feature)
plt.show()

"""#### Numerical Features"""

df[numerical_features].hist(bins=50, figsize=(16,8))
plt.show()

"""### Multivariate Analysis

#### Categorical Features
"""

for index, col in enumerate(categorical_features):
  sns.catplot(x=col, y='Outcome', kind='bar', dodge=False, height=3, aspect=6/3,  data=df, palette='Set3').set(xlabel=None)
  plt.title("Rata-rata 'Outcome' Relatif terhadap - {}".format(col))
plt.show()

"""#### Correlation Matrix"""

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr().round(2)

sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix untuk Fitur Numerik', size=20)

"""Dapat dilihat data pada fitur `SkinThickness` memiliki korelasi yang lemah terhadap prediksi diabetes. Sehingga, fitur tersebut dapat dihapus."""

df.drop('SkinThickness', inplace=True, axis=1)
df.head()

"""### Features Encoding"""

df = pd.concat([df, pd.get_dummies(df['Glucose'], prefix='Glucose')], axis=1)
df = pd.concat([df, pd.get_dummies(df['BloodPressure'], prefix='BloodPressure')], axis=1)
df = pd.concat([df, pd.get_dummies(df['Insulin'], prefix='Insulin')], axis=1)
df = pd.concat([df, pd.get_dummies(df['BMI'], prefix='BMI')], axis=1)
df.loc[df['Outcome'] == 0, 'Outcome'] = 'Negative'
df.loc[df['Outcome'] == 1, 'Outcome'] = 'Positive'

df.drop(['Glucose', 'BloodPressure', 'Insulin', 'BMI'], axis=1, inplace=True)
df.head()

df.describe()

"""### Split Dataset"""

numerical_features = ['Pregnancies', 'DiabetesPedigreeFunction', 'Age']
X = df.drop(['Outcome'], axis =1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

X_train[numerical_features].describe().round(4)

"""### Normalization"""

scaler = StandardScaler()
scaler.fit(X_train[numerical_features])

X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_test[numerical_features]  = scaler.transform(X_test.loc[:, numerical_features])

X_train[numerical_features].describe().round(4)

"""## Model Development

### K-Nearest Neighbor
"""

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

knn_report = classification_report(y_test, y_pred, output_dict=True, target_names=['Negative', 'Positive'])

knn_cm = confusion_matrix(y_test, y_pred)

ax = sns.heatmap(knn_cm, annot=True, cmap='coolwarm')
ax.set_title('K-Nearest Neighbor Confusion Matrix');
ax.set_xlabel('Predicted Values')
ax.set_ylabel('Actual Values');

ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

plt.show()

"""### Random Forest"""

rf = RandomForestClassifier(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

rf_report = classification_report(y_test, y_pred, output_dict=True, target_names=['Negative', 'Positive'])

rf_cm = confusion_matrix(y_test, y_pred)

ax = sns.heatmap(rf_cm, annot=True, cmap='coolwarm')
ax.set_title('Random Forest Confusion Matrix');
ax.set_xlabel('Predicted Values')
ax.set_ylabel('Actual Values');

ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

plt.show()

"""### AdaBoost"""

boosting = AdaBoostClassifier(learning_rate=0.05, random_state=55)                             
boosting.fit(X_train, y_train)

y_pred = boosting.predict(X_test)

boosting_report = classification_report(y_test, y_pred, output_dict=True, target_names=['Negative', 'Positive'])

boosting_cm = confusion_matrix(y_test, y_pred)

ax = sns.heatmap(boosting_cm, annot=True, cmap='coolwarm')
ax.set_title('AdaBoost Confusion Matrix');
ax.set_xlabel('Predicted Values')
ax.set_ylabel('Actual Values');

ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

plt.show()

"""### Model Report"""

metrics = pd.DataFrame({'Accuracy': [knn_report['accuracy'], rf_report['accuracy'], boosting_report['accuracy']],
                       'F1-score_0': [knn_report['Negative']['f1-score'], rf_report['Negative']['f1-score'], boosting_report['Negative']['f1-score']], 
                       'F1-score_1': [knn_report['Positive']['f1-score'], rf_report['Positive']['f1-score'], boosting_report['Positive']['f1-score']],
                       'Precision_0': [knn_report['Negative']['precision'], rf_report['Negative']['precision'], boosting_report['Negative']['precision']], 
                       'Precision_1': [knn_report['Positive']['precision'], rf_report['Positive']['precision'], boosting_report['Positive']['precision']], 
                       'Recall_0': [knn_report['Negative']['recall'], rf_report['Negative']['recall'], boosting_report['Negative']['recall']], 
                       'Recall_1': [knn_report['Positive']['recall'], rf_report['Positive']['recall'], boosting_report['Positive']['recall']]},
                      index=['KNN', 'RandomForest', 'Boosting'])

metrics.columns = pd.MultiIndex.from_tuples([('','Accuracy'),
                                             ('Negative', 'F1-score'),
                                             ('Negative', 'Precision'),
                                             ('Negative', 'Recall'),
                                             ('Positive', 'F1-score'),
                                             ('Positive', 'Precision'),
                                             ('Positive', 'Recall')])

metrics

"""## References
<ul>
  <li>
    <a id="ref1"></a>
    [1] Glucose Tolerance Testing: Reference Range, Interpretation, Collection and Panels [Internet]. Tersedia pada: <a href='https://emedicine.medscape.com/article/2049402-overview'>https://emedicine.medscape.com/article/2049402-overview</a>.
  </li>
  <li>
    <a id="ref2"></a>
    [2] About Adult BMI | Healthy Weight, Nutrition, and Physical Activity | CDC [Internet]. Tersedia pada: <a href='https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#Interpreted'>https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#Interpreted</a>.
  </li>
  <li>
    <a id="ref3"></a>
    [3] Insulin: Reference Range, Interpretation, Collection and Panels [Internet]. Tersedia pada: <a href='https://emedicine.medscape.com/article/2089224-overview'>https://emedicine.medscape.com/article/2089224-overview</a>.
  </li>
  <li>
    <a id="ref4"></a>
    [4] High Blood Pressure Symptoms and Causes | cdc.gov [Internet]. Tersedia pada: <a href='https://www.cdc.gov/bloodpressure/about.htm#whatare'> https://www.cdc.gov/bloodpressure/about.htm#whatare</a>.
  </li>
</ul>
"""
