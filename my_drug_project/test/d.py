import pandas as pd

# Path to the input CSV file
input_file_path = r'D:\Deexi\Downloads\archive\drugs.csv'

# Path to save the modified CSV file
output_file_path = r'D:\Deexi\Downloads\archive\modified_drugs.csv'

# Step 1: Read the CSV file
df = pd.read_csv(input_file_path)

# Step 2: Modify the 'drug_description' column to keep only the text up to the first period
def truncate_description(description):
    if pd.isna(description):  # Check for NaN values
        return description
    return description.split('.')[0] + '.' if '.' in description else description

df['drug_description'] = df['drug_description'].apply(truncate_description)

# Step 3: Save the modified data back to a CSV file
df.to_csv(output_file_path, index=False)
