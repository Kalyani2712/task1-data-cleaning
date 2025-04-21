import pandas as pd

# Load the dataset with tab delimiter
df = pd.read_csv("marketing_campaign.csv", delimiter="\t")

# 1. Summary before cleaning
print("Initial shape:", df.shape)
print("\nMissing values per column:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Drop rows with any null values
df = df.dropna()

# 4. Standardize text values (strip whitespace and convert to lowercase)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip().str.lower()

# 5. Convert likely date columns to datetime
for col in df.columns:
    if 'date' in col.lower() or 'dt' in col.lower():
        df[col] = pd.to_datetime(df[col], errors='coerce')

# 6. Rename column headers (lowercase, replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 7. Convert 'age' column to numeric if it exists
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce', downcast='integer')

# 8. Drop any rows with null values (after conversions)
df = df.dropna()

# 9. Final summary
print("\nFinal shape:", df.shape)
print("\nCleaned data sample:\n", df.head())

# 10. Save the cleaned dataset to Excel
df.to_csv("cleaned_marketing_campaign.csv", index=False)


print("\n✅ Cleaned dataset saved to 'cleaned_marketing_campaign.csv'")
