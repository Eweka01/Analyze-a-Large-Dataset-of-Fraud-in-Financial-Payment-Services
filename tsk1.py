import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the transactions dataset from your specific path
df = pd.read_csv('/Users/ewekagabriel/Downloads/transactions.csv')

# Check the first few rows of the dataset
print(df.head())

# Display basic information about the dataset
print(df.info())

# Show descriptive statistics of the dataset
print(df.describe())

# Example query: Sum of transactions
total_amount = df['amount'].sum()
print(f"Total amount transferred: {total_amount}")

# Example query: Transactions above 1000 units
large_transactions = df[df['amount'] > 1000]
print(large_transactions)

# Example query: Count of transactions by type
transaction_counts = df['type'].value_counts()
print(transaction_counts)

# Histogram of the transaction amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['amount'], bins=30, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.show()

# Bar plot of transaction counts by type
plt.figure(figsize=(10, 6))
df['type'].value_counts().plot(kind='bar')
plt.title('Transaction Counts by Type')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()
