import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
#Task 1
print(financial_data.head())

#Task 2
month = financial_data["Month"]
revenue = financial_data["Revenue"]
expenses = financial_data["Expenses"]

#Task 3
plt.plot(month, revenue)
#plt.show()

#Task 4
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
plt.clf()

#Task 5
plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()
plt.clf()

#Task 6
expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head())

#Task 7
expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']

