import pandas as pd
import glob

# Read all CSV files from data folder
files = glob.glob("data/*.csv")

dataframes = []

for file in files:
    df = pd.read_csv(file)
    
    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]
    
    # Clean price column (remove $ sign)
    df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)
    
    # Create sales column
    df["sales"] = df["price"] * df["quantity"]
    
    # Keep only required columns
    df = df[["sales", "date", "region"]]
    
    dataframes.append(df)

# Combine all files
final_df = pd.concat(dataframes)

# Save output file
final_df.to_csv("formatted_sales.csv", index=False)

print("Formatted file created successfully!")