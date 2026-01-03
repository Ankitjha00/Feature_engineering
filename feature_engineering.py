import pandas as pd

df = pd.read_csv("Dataset .csv")

# Feature 1: Restaurant name length
df['Restaurant Name Length'] = df['Restaurant Name'].str.len()

# Feature 2: Address length
df['Address Length'] = df['Address'].str.len()

# Feature 3: Encode categorical variables
df['Has Table Booking Encoded'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
df['Has Online Delivery Encoded'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})

print(df[['Restaurant Name Length', 'Address Length',
          'Has Table Booking Encoded', 'Has Online Delivery Encoded']].head())


