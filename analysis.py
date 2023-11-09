import pandas as pd

# Load the two CSV files
df1 = pd.read_csv("data1.csv")
df2 = pd.read_csv("data2.csv")

# Define a dictionary to map website names to their URLs
websites = {
    "Website1": "onlinebeautyessentials.com",
    "Website2": "lookfantastic.com",
}

# Merge the two DataFrames based on the "Title" column
merged_df = pd.merge(df1, df2, on="Title", suffixes=('_website1', '_website2'), how="inner")

# Compare prices and decide which website is better for each product
merged_df["Better_Website"] = "Neither"  # Initialize a new column

# Compare the prices
merged_df.loc[merged_df["Price_website1"] < merged_df["Price_website2"], "Better_Website"] = "Website1"
merged_df.loc[merged_df["Price_website1"] > merged_df["Price_website2"], "Better_Website"] = "Website2"

# Replace "Website1" and "Website2" with their URLs
merged_df["Better_Website"].replace(websites, inplace=True)

# Create a new DataFrame with the comparison results
comparison_results = merged_df[["Title", "Price_website1", "Price_website2", "Better_Website"]]

# Save the comparison results to a new CSV file
comparison_results.to_csv("comparison_results.csv", index=False)

print("Comparison results saved to comparison_results.csv.")
