'''
4. Mastering Tuple Packing and Unpacking in Python

Objective:

The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python. 
You will apply these techniques in various practical scenarios, 
enhancing your ability to work with flexible data structures and improve data handling efficiency.

Task 1: Customer Order Processing
Refine your skills in tuple unpacking by managing customer orders.

Problem Statement:
You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, 
the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]'''

def display_orders(orders):
    for name, electronic, quantity in orders:
        print(f"\nName: {name} - Electronic: {electronic} - Quantity: {quantity}")
    print("\n")


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

display_orders(orders)