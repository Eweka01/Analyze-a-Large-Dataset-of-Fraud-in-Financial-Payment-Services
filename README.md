# Transaction Frauds 
> This is inspired by JP Morgan Cybersecurity Study Case via [Forage](https://www.theforage.com/simulations/jpmorgan/cybersecurity-0acj). The dataset named 'transaction.csv can be found in [Kaggle](https://www.kaggle.com/ealaxi/paysim1/version/2).

## Scenario 
You are a cybersecurity analyst at the one of the largest financial companies in the world. Your job is to analyze a large dataset of fraud in Financial Payment Services. 
The dataset has five types of transactions:
* CASH-IN is any deposit.
* CASH-OUT is any withdrawal.
* DEBIT is a specific type of withdrawal in which the money is sent to the user’s bank account.
* PAYMENT is the purchase of goods or services.
* TRANSFER involves moving money from one user’s account to another user’s account.

## Process
1. Read the dataset (`transactions.csv`) as a Pandas dataframe. Note that the first row of the CSV contains the column names.
2. Return the column names as a list from the dataframe.
3. Return the first k rows from the dataframe.
4. Return a random sample of k rows from the dataframe.
5. Return the Origin account balance delta v. Destination account balance delta scatter plot for Cash Out transactions (Source Delta & Delta Destination).
6. Return Fraud transactions that are flagged as frauds and how many of them are real frauds. 

## Implementation
* Transaction types bar chart:
  
![296935893-0f46f286-3a5a-4744-b4a1-6d84040edb56](https://github.com/user-attachments/assets/1d54f6a4-1846-43b3-98f8-43e79eff2efa)

* Transaction types frequencies:

![296935958-fe2ea599-140f-4ece-a11c-00b95008a9ba](https://github.com/user-attachments/assets/6e2fea10-1cea-4aa7-a77e-ce8c941e0fb9)

* Delta Source:

![296936013-db06a7c5-c27b-4395-b344-cf7ca86b40d0](https://github.com/user-attachments/assets/cb6fc73f-37be-4194-9a58-2e06528dd222)

* Fraud Detection:

![296936044-686aae69-2cf1-4480-80dd-3fa8250573b2](https://github.com/user-attachments/assets/5f9ff14d-ca18-45c0-b764-cf0ba582cd19)

## Future Works: 
* I would like to use free open source Facebook, Twitter, etc. scrappers, to gather the data and put them into csv extension file.
* More analysis can be conducted for this type of report. 
