
# 🧹 Marketing Campaign Data Cleaning (Customer Personality Analysis)

This project contains a Python script that cleans a marketing campaign dataset for further analysis or modeling.

---

## 📄 Files

- `Clean_data.py`: Python script to clean the raw marketing dataset.
- `marketing_campaign.csv`: Original dataset file (tab-separated).
- `cleaned_marketing_campaign.csv`: Output file with cleaned data.
- `README.md`: Project documentation (this file).

---

## 🧼 What the Script Does

1. Loads the dataset from `marketing_campaign.csv` using a **tab (`\t`) delimiter**.
2. Prints a summary of:
   - Initial shape of the dataset
   - Missing values by column
   - Duplicate row count
3. Cleans the data:
   - Removes duplicate rows
   - Drops rows with missing values
   - Standardizes all string columns (trims and lowercases text)
   - Converts date-like columns to proper datetime format
   - Renames all column headers to `snake_case`
   - Converts the `age` column to numeric if present
4. Drops any remaining rows with null values after conversions.
5. Prints the final shape and a sample of the cleaned data.
6. Saves the cleaned dataset as `cleaned_marketing_campaign.csv`.

---

## ▶️ How to Run

Make sure you have Python installed with the required package:

```bash
pip install pandas
```

Then run the script:

```bash
python Clean_data.py
```

---

## ✅ Output

- Cleaned data is saved to: `cleaned_marketing_campaign.csv`
- Console output includes:
  - Shape before and after cleaning
  - Missing values summary
  - Duplicate count
  - Sample of the cleaned dataset

---

### ℹ️ Note on Date Columns

If you open `cleaned_marketing_campaign.csv` in **Excel** and see `########` in the date columns (like `dt_customer`), don't worry — this just means the column is too narrow to display the full date.

✅ To fix this:
- Hover over the right edge of the column header (e.g., column `H`)
- **Double-click** to auto-resize the column
- Or **right-click** the column header → choose `Column Width` and increase it manually

This will display the date properly (e.g., `03-12-2013`) instead of `########`.

---

