# data_preprocessing.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('titanic.csv')

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