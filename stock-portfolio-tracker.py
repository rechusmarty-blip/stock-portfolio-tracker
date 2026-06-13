# Stock Portfolio Tracker

# Hardcoded stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 160
}

total_investment = 0

# User input
stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

# Check if stock exists
if stock_name in stocks:
    price = stocks[stock_name]
    investment = price * quantity
    total_investment += investment

    print("\nStock Price:", price)
    print("Total Investment Value:", total_investment)

    # Save result into a text file
    file = open("portfolio.txt", "w")
    file.write(f"Stock: {stock_name}\n")
    file.write(f"Quantity: {quantity}\n")
    file.write(f"Total Investment: {total_investment}\n")
    file.close()

    print("Data saved in portfolio.txt")

else:
    print("Stock not found!")
