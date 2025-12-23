

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class RetailSalesAnalyzer:

    def __init__(self):
        self.data = None

   
    def load_csv(self, file_path):
        if not os.path.isfile(file_path):
            print(" File does not exist!")
            return

        if not file_path.lower().endswith('.csv'):
            print(" Only CSV files are allowed!")
            return

        self.data = pd.read_csv(file_path)
        print(" Data Loaded Successfully!")
        print(self.data.head())

    
    def clean_data(self):
        if self.data is None:
            print(" Load data first!")
            return

        print("\n Cleaning Data...")

        for col in ['Price', 'Quantity Sold', 'Total Sales']:
            if col in self.data.columns:
                self.data[col] = self.data[col].fillna(self.data[col].mean())

        for col in ['Category', 'Product']:
            if col in self.data.columns:
                self.data[col] = self.data[col].fillna(self.data[col].mode()[0])

        if 'Date' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'])

        print(" Missing values handled and Date converted!")

    
    def sales_metrics(self):
        if self.data is None:
            print(" Load data first!")
            return

        total = self.data['Total Sales'].sum()
        average = self.data['Total Sales'].mean()
        top_product = self.data['Product'].mode()[0]

        print("\n Sales Metrics")
        print(f"Total Sales: {total}")
        print(f"Average Sales: {round(average,2)}")
        print(f"Top Selling Product: {top_product}")

    
    def filter_data(self, category=None, start=None, end=None):
        if self.data is None:
            print(" Load data first!")
            return

        filtered = self.data.copy()

        if category:
            filtered = filtered[filtered['Category'] == category]

        if start and end:
            filtered = filtered[(filtered['Date'] >= start) & (filtered['Date'] <= end)]

        print("\n Filtered Data Preview:")
        print(filtered.head())
        return filtered

    
    def summary_stats(self):
        if self.data is None:
            print(" Load data first!")
            return

        print("\n Dataset Summary:")
        print(self.data.describe())

   
    def plot_bar(self):
        if self.data is None:
            return
        sales_by_cat = self.data.groupby('Category')['Total Sales'].sum()
        plt.figure(figsize=(8,5))
        sns.barplot(x=sales_by_cat.index, y=sales_by_cat.values)
        plt.title("Total Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.show()

    def plot_line(self):
        if self.data is None:
            return
        daily_sales = self.data.groupby('Date')['Total Sales'].sum()
        plt.figure(figsize=(10,5))
        plt.plot(daily_sales.index, daily_sales.values, marker='o')
        plt.title("Daily Sales Trend")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.grid(True)
        plt.show()

    def plot_heatmap(self):
        if self.data is None:
            return
        corr = self.data[['Price', 'Quantity Sold', 'Total Sales']].corr()
        plt.figure(figsize=(6,4))
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title("Sales Correlation Heatmap")
        plt.show()



def main():
    analyzer = RetailSalesAnalyzer()

    while True:
        print("\n======= Retail Sales Analyzer =======")
        print("1. Load Data")
        print("2. Clean Data")
        print("3. Sales Metrics")
        print("4. Filter Data")
        print("5. Summary Statistics")
        print("6. Bar Chart")
        print("7. Line Chart")
        print("8. Heatmap")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            path = input("Enter CSV file path (C:\PYTHON\retail_data_sample.csv): ")
            analyzer.load_csv(path)

        elif choice == '2':
            analyzer.clean_data()

        elif choice == '3':
            analyzer.sales_metrics()

        elif choice == '4':
            cat = input("Category (press Enter to skip): ")
            start = input("Start Date (YYYY-MM-DD) or skip: ")
            end = input("End Date (YYYY-MM-DD) or skip: ")
            analyzer.filter_data(cat if cat else None, start if start else None, end if end else None)

        elif choice == '5':
            analyzer.summary_stats()

        elif choice == '6':
            analyzer.plot_bar()

        elif choice == '7':
            analyzer.plot_line()

        elif choice == '8':
            analyzer.plot_heatmap()

        elif choice == '9':
            print("✅ Exiting Program...")
            break

        else:
            print(" Invalid choice! Try again.")


if __name__ == "__main__":
    main()
