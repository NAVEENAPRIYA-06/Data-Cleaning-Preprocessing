# data_preprocessing.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Titanic-Dataset.csv')

# Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop('Cabin', axis=1, inplace=True)

print("Missing values handled.")

df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

print("Categorical features encoded.")

# Scale numerical features
numerical_features = ['Age', 'Fare']
scaler = StandardScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])

print("Numerical features standardized.")

plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Fare'])
plt.title('Fare Distribution with Outliers')
plt.show()

print("Preprocessing complete. Final data is ready.")