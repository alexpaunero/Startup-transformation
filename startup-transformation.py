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

#Task 8
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expenses')

#Task 9
plt.axis('Equal')
plt.tight_layout()
plt.show()

#Task 10
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expenses')
plt.axis('Equal')
plt.tight_layout()
plt.show()

## Task 11
expense_cut = 'Salaries'

## Task 12
employees = pd.read_csv('employees.csv')
print(employees.head())

## Task 13
sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity)

## Task 14
employees_cut = sorted_productivity.head(100)
print(employees_cut)


## Task 15
transformation = 'standardization'

## Task 16
commute_times = employees['Commute Time']

## Task 17
print(commute_times.describe())

## Task 18
plt.clf()
plt.hist(commute_times)
plt.title("Time spent commuting")
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.show()
## The data is right-skewed.

