# 1. Import Libraries and Load Data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the dataset
try:
    df = pd.read_csv('Titanic-Dataset.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Titanic-Dataset.csv not found. Please ensure the file is in the same directory.")
    exit()

# Initial exploration
print("\n--- Initial Data Info ---")
df.info()

# 2. Handle Missing Values (Corrected to avoid FutureWarning)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop('Cabin', axis=1, inplace=True)

print("\n--- Missing Values after Imputation/Dropping ---")
print(df.isnull().sum())

# 3. Encode Categorical Features
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
print("\n--- DataFrame after One-Hot Encoding ---")
print(df.head())

# 4. Normalize Numerical Features
numerical_features = ['Age', 'Fare']
scaler = StandardScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])
print("\n--- DataFrame after Standardization ---")
print(df[numerical_features].head())

# 5. Visualize and Handle Outliers
print("\n--- Visualizing Outliers in 'Fare' ---")
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Fare'])
plt.title('Boxplot of Fare')
plt.show()

print("\nData preprocessing complete.")
print("Final DataFrame columns:", df.columns)