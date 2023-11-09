import pandas as pd

# Load the CSV file with the specified encoding
df = pd.read_csv("products.csv", encoding="ISO-8859-1")

# Remove duplicates based on 'Product Link'
df = df.drop_duplicates(subset=['Product Link'])

# Remove rows with missing values
df = df.dropna()

# Reset the index after removing rows
df = df.reset_index(drop=True)

# Save the cleaned data to a new CSV file
df.to_csv("data1.csv", index=False)

print("Duplicate and missing values removed. Data saved to cleaned_products.csv.")
