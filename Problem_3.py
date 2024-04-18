'''
3. Python Loops and Tuples in Analytical Applications

Objective:

This assignment is designed to strengthen your expertise in using Python loops and tuples, 
particularly in data analysis and processing scenarios. 
By completing these tasks, you will gain practical experience in handling and analyzing data using these fundamental Python concepts.

Task 1: Stock Market Data Analysis
Enhance your skills in data manipulation and analysis using tuples and loops.

Problem Statement:
You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, 
the date, and the closing price. Your task is to analyze this data to find the average closing price of a specified stock over a given period.

Sample Data:

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]
'''
def average_stock(stocks):
    sum = 0
    for company, date, stock in stocks:
        sum += stock
    average = sum / len(stocks)
    print(f"Average stock: {average}")

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]
average_stock(stock_data)