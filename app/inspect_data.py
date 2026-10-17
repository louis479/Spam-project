
import pandas as pd

# Load the CSV dataset
df = pd.read_csv("data/messages.csv")

# Display the first five messages
print("\n--- First five messages ---")
print(df.head())

# Display the dataset size
print("\n--- Dataset shape ---")
print(df.shape)

# Count messages in each category
print("\n--- Messages per category ---")
print(df["label"].value_counts())

# Check for missing values
print("\n--- Missing values ---")
print(df.isnull().sum())

# Check the available labels
print("\n--- Unique labels ---")
print(df["label"].unique())
