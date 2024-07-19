# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UYup13_GhZWcRg-Dp-DFtENDZGK5LMq0
"""

import json
import pandas as pd

# Load the JSON file
with open('/content/DataEngineeringQ2.json') as f:
    data = json.load(f)

# Inspect the structure of the JSON data
print(type(data))
print(data)
print(data[0].keys())

# Assuming the data is a list of dictionaries
patient_details = data[0]['patientDetails']
consultation_data = data[0]['consultationData']

# Inspect the structure of patient_details and consultation_data
print(type(patient_details))
# Print the first two key-value pairs for inspection (since it's a dictionary)
for i, (key, value) in enumerate(patient_details.items()):
    if i >= 2:
        break
    print(key, ":", value)

print(type(consultation_data))
# Print the first two key-value pairs for inspection (since it's a dictionary)
for i, (key, value) in enumerate(consultation_data.items()):
    if i >= 2:
        break
    print(key, ":", value)


# Create dataframes

# If patient_details and consultation_data are lists of dictionaries:
try:
    patient_df = pd.DataFrame([patient_details]) # Wrap patient_details as a list for DataFrame creation
    consultation_df = pd.json_normalize(consultation_data, 'medicines', ['consultationId', 'doctorId', 'patientId'], record_prefix='medicine_', error='ignore')
except Exception as e:
    print("Error creating DataFrames:", e)
    # Further inspection or normalization might be needed here based on the actual structure

# Check if DataFrames were created successfully
print("patient_df created:", 'patient_df' in locals())
print("consultation_df created:", 'consultation_df' in locals())

# Proceed with merging and other operations only if DataFrames exist
if 'patient_df' in locals() and 'consultation_df' in locals():
    # Merge dataframes on patientId
    merged_df = pd.merge(patient_df, consultation_df, left_on='patientId', right_on='patientId')

    # Perform aggregations
    aggregation = merged_df.groupby('patientId').agg({
        'medicine_name': 'count',
        'medicine_quantity': 'sum'
    }).reset_index()

    # Validations
    missing_values = merged_df.isnull().sum()
    data_types = merged_df.dtypes

    # Insights
    stats = merged_df.describe()
    top_patients = merged_df['patientId'].value_counts().head(10)

    # Print the results
    print("Aggregations:\n", aggregation)
    print("Missing Values:\n", missing_values)
    print("Data Types:\n", data_types)
    print("Statistics:\n", stats)
    print("Top Patients:\n", top_patients)

import json
import pandas as pd

# Load the JSON file
with open('/content/DataEngineeringQ2.json') as f:
    data = json.load(f)

# Check the structure of the data
print(type(data))
print(data[:2])  # Print the first two elements of the list for inspection

# Extracting the relevant parts from the first dictionary in the list
if isinstance(data, list) and len(data) > 0:
    patient_details = data[0]['patientDetails']
    consultation_data = data[0]['consultationData']

    # Inspect the structure of patient_details and consultation_data
    print(type(patient_details))
    print(list(patient_details.keys())[:2])  # Print the first two keys for inspection
    print({k: patient_details[k] for k in list(patient_details.keys())[:2]})  # Print the first two entries for inspection

    print(type(consultation_data))
    print(list(consultation_data.keys())[:2])  # Print the first two keys for inspection
    print({k: consultation_data[k] for k in list(consultation_data.keys())[:2]})  # Print the first two entries for inspection

    # Create dataframes
    try:
        patient_df = pd.DataFrame([patient_details])  # Wrap patient_details as a list for DataFrame creation
        # Normalizing consultation_data to ensure correct structure
        consultation_df = pd.json_normalize(
            consultation_data,
            'medicines',
            ['consultationId', 'doctorId', 'patientId'],
            record_prefix='medicine_',
            errors='ignore'
        )
    except Exception as e:
        print("Error creating DataFrames:", e)

    # Check columns in DataFrames
    print("patient_df columns:", patient_df.columns)
    print("consultation_df columns:", consultation_df.columns)

    # Proceed with merging and other operations only if DataFrames exist and contain necessary columns
    if 'patient_df' in locals() and 'consultation_df' in locals():
        if 'patientId' in patient_df.columns and 'patientId' in consultation_df.columns:
            # Merge dataframes on patientId
            merged_df = pd.merge(patient_df, consultation_df, left_on='patientId', right_on='patientId')

            # Perform aggregations
            aggregation = merged_df.groupby('patientId').agg({
                'medicine_name': 'count',
                'medicine_quantity': 'sum'
            }).reset_index()

            # Validations
            missing_values = merged_df.isnull().sum()
            data_types = merged_df.dtypes

            # Insights
            stats = merged_df.describe()
            top_patients = merged_df['patientId'].value_counts().head(10)

            # Print the results
            print("Aggregations:\n", aggregation)
            print("Missing Values:\n", missing_values)
            print("Data Types:\n", data_types)
            print("Statistics:\n", stats)
            print("Top Patients:\n", top_patients)

            # Calculate percentage of missing values for specified columns
            columns_to_check = ['firstName', 'lastName', 'DOB']
            missing_percentages = {}

            for col in columns_to_check:
                # Ensure the column exists in the DataFrame
                if col in patient_df.columns:
                    missing_count = patient_df[col].apply(lambda x: x == '' or pd.isnull(x)).sum()
                    total_count = len(patient_df)
                    missing_percentage = (missing_count / total_count) * 100
                    missing_percentages[col] = round(missing_percentage, 2)

            print("Missing Percentages:")
            for col, pct in missing_percentages.items():
                print(f"{col}: {pct}%")
        else:
            print("Required columns for merging not found in one or both DataFrames.")
else:
    print("The data is not in the expected format or is empty.")

import json
import pandas as pd

# Load the JSON file
with open('/content/DataEngineeringQ2.json') as f:
    data = json.load(f)

# Check the structure of the data
print(type(data))
print(data[:2])  # Print the first two elements of the list for inspection

# Extracting the relevant parts from the first dictionary in the list
if isinstance(data, list) and len(data) > 0:
    patient_details = data[0]['patientDetails']
    consultation_data = data[0]['consultationData']

    # Inspect the structure of patient_details and consultation_data
    print(type(patient_details))
    print(list(patient_details.keys())[:2])  # Print the first two keys for inspection
    print({k: patient_details[k] for k in list(patient_details.keys())[:2]})  # Print the first two entries for inspection

    print(type(consultation_data))
    print(list(consultation_data.keys())[:2])  # Print the first two keys for inspection
    print({k: consultation_data[k] for k in list(consultation_data.keys())[:2]})  # Print the first two entries for inspection

    # Create dataframes
    try:
        patient_df = pd.DataFrame([patient_details])  # Wrap patient_details as a list for DataFrame creation
        # Normalizing consultation_data to ensure correct structure
        consultation_df = pd.json_normalize(
            consultation_data,
            'medicines',
            ['consultationId', 'doctorId', 'patientId'],
            record_prefix='medicine_',
            errors='ignore'
        )
    except Exception as e:
        print("Error creating DataFrames:", e)

    # Check columns in DataFrames
    print("patient_df columns:", patient_df.columns)
    print("consultation_df columns:", consultation_df.columns)

    # Calculate percentage of missing values for specified columns
    columns_to_check = ['firstName', 'lastName', 'DOB']
    missing_percentages = {}

    if 'patient_df' in locals():
        for col in columns_to_check:
            if col in patient_df.columns:
                # Calculate missing values as blank and empty strings
                missing_count = patient_df[col].apply(lambda x: x == '' or pd.isnull(x)).sum()
                total_count = len(patient_df)
                missing_percentage = (missing_count / total_count) * 100
                missing_percentages[col] = round(missing_percentage, 2)

        # Print the missing percentages
        print("Missing Percentages:")
        for col, pct in missing_percentages.items():
            print(f"{col}: {pct}%")
    else:
        print("patient_df DataFrame does not exist or does not contain the required columns.")
else:
    print("The data is not in the expected format or is empty.")

import json
import pandas as pd

# Load the JSON file
with open('/content/DataEngineeringQ2.json') as f:
    data = json.load(f)

# Check the structure of the data
print(type(data))
print(data[:2])  # Print the first two elements of the list for inspection

# Extracting the relevant parts from the first dictionary in the list
if isinstance(data, list) and len(data) > 0:
    patient_details = data[0]['patientDetails']

    # Inspect the structure of patient_details
    print(type(patient_details))
    print(list(patient_details.keys())[:2])  # Print the first two keys for inspection
    print({k: patient_details[k] for k in list(patient_details.keys())[:2]})  # Print the first two entries for inspection

    # Create DataFrame
    try:
        patient_df = pd.DataFrame([patient_details])  # Wrap patient_details as a list for DataFrame creation
    except Exception as e:
        print("Error creating DataFrame:", e)

    # Check columns in DataFrame
    print("patient_df columns:", patient_df.columns)

    # Impute missing values in the 'gender' column with the mode
    if 'gender' in patient_df.columns:
        mode_gender = patient_df['gender'].mode()[0]  # Find the mode of the gender column
        patient_df['gender'].fillna(mode_gender, inplace=True)  # Impute missing values with mode

        # Calculate the percentage of female gender
        total_count = len(patient_df)
        female_count = (patient_df['gender'] == 'female').sum()
        female_percentage = (female_count / total_count) * 100

        # Print the result
        print(f"Percentage of female gender after imputation: {round(female_percentage, 2)}%")
    else:
        print("The 'gender' column is not present in the DataFrame.")
else:
    print("The data is not in the expected format or is empty.")
