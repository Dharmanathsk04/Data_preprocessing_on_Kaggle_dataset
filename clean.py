import pandas as pd

data = pd.read_csv("data_science_student_marks.csv")

print("Shape of data:", data.shape)
print("\nFirst 5 rows:\n", data.head())
print("\nInformation about data:\n")
print(data.info())

print("\nMissing values in each column:\n", data.isnull().sum())

for column in data.columns:
    if data[column].dtype == 'object':
        data[column] = data[column].fillna(data[column].mode()[0])
    else:
        data[column] = data[column].fillna(data[column].mean())

data = data.drop_duplicates()

for column in data.select_dtypes(include=['object']).columns:
    data[column] = data[column].astype('category').cat.codes

print("\nAfter preprocessing:")
print(data.head())

data.to_csv("cleaned_student_marks.csv", index=False)
print("\nCleaned data saved as 'cleaned_student_marks.csv'")
