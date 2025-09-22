This project demonstrates the key steps of data preprocessing on the Titanic dataset. The goal is to prepare the raw data for use in a machine learning model.

------------------------------------------------------------------------------------------------------------------------

#Steps Performed

Handling Missing Values: Missing data in the Age and Embarked columns were filled in, and the Cabin column was removed.

Encoding Data: The text data in the Sex and Embarked columns was converted into a numerical format.

Scaling Features: The numerical columns (Age and Fare) were scaled to a standard range.

Outlier Visualization: A boxplot was used to visualize outliers in the Fare column.

------------------------------------------------------------------------------------------------------------------------

#How to Run:

Place the titanic.csv file in the same folder as the script.

Install the required libraries:
       pip install -r requirements.txt

Run the Python script from your terminal:
       python data_preprocessing.py

------------------------------------------------------------------------------------------------------------------------

#Screenshots:

Before and After Preprocessing:

Here you can see the initial data with missing values and the clean data after preprocessing.

[View Initial Data Screenshot](Screenshots/initial_info.png)

[View Clean Data Screenshot](Screenshots/final_info.png)

#Fare Outliers Visualization:

This boxplot shows the distribution of ticket prices and highlights the outliers.

[View Boxplot Screenshot](Screenshots/boxplot.png)

------------------------------------------------------------------------------------------------------------------------