stock_prices = {
    # US Mega Tech Firms (MTF)
    "AAPL": 185,     # Apple Inc.
    "MSFT": 340,     # Microsoft Corporation
    "GOOG": 140,     # Alphabet Inc. (Google)
    "AMZN": 125,     # Amazon.com Inc.
    "META": 315,     # Meta Platforms (Facebook)
    "NVDA": 1220,    # NVIDIA Corporation
    "TSLA": 250,     # Tesla Inc. (also tech in nature)

    # US IT Sector
    "IBM": 170,      # IBM Corporation
    "ORCL": 135,     # Oracle Corporation
    "ADBE": 525,     # Adobe Inc.
    "CRM": 225,      # Salesforce Inc.
    "INTC": 35,      # Intel Corporation
    "AMD": 155,      # Advanced Micro Devices

    # Indian IT Sector (NSE/BSE)
    "INFY": 1500,    # Infosys Ltd.
    "TCS": 3700,     # Tata Consultancy Services
    "WIPRO": 470,    # Wipro Ltd.
    "HCLTECH": 1400, # HCL Technologies
    "TECHM": 1250,   # Tech Mahindra
    "LTIM": 5600,    # L&T Infotech
    "COFORGE": 4500, # Coforge Ltd.
    "MPHASIS": 2350, # Mphasis Ltd.

    # Banking & Finance
    "HDFCBANK": 1550,  # HDFC Bank
    "ICICIBANK": 1220, # ICICI Bank
    "SBIN": 850,       # State Bank of India
    "AXISBANK": 1050,  # Axis Bank
    "KOTAKBANK": 1700, # Kotak Mahindra Bank
}

print("\n╔══════════════════════════════════════════════════╗")
print("║     📈  WELCOME TO STOCK PORTFOLIO TRACKER  📊   ║")
print("╚══════════════════════════════════════════════════╝")


# Dictionary to store the user's stocks
my_portfolio = {}

# Asking user how many different stocks they want to enter
#using a while loop to buypass a non-integer value 
while True:
    total_stocks = input("How many different stocks do you have?\nPlease enter a number: ")
    
    if total_stocks.isdigit():
        total_stocks = int(total_stocks)
        if total_stocks > 0:
            break
        else:
            print("Please enter a number greater than zero.\n")
    else:
        print("Oops! That doesn't look like a number. Try again.\n")

# Getting the stock names and how many shares the user owns
for i in range(total_stocks):
    name = input("Enter stock name (like AAPL, TSLA): ").upper()
    if name in stock_prices:
        quantity = int(input(f"How many shares of {name} do you own? "))
        my_portfolio[name] = quantity
    else:
        print(f"Sorry, we don’t have the price for {name}. Skipping it.")

# Calculate total investment
Display = []
Display.append(f"{'Stock Symbol':<15} {'Shares':<10} {'Price (INR)':<15} {'Total Value (INR)':<20}")

total_value = 0
for stock, qty in my_portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    Display.append(f"{stock:<15} {qty:<10} ₹{price:<14} ₹{value:<20}")

Display.append("-" * 60)
Display.append(f"{'Total Investment':<40} ₹{total_value:<20}")

# Determine the max line length for framing
max_len = max(len(line) for line in Display)
border = "═" * (max_len + 4)

# Print inside a box
print("\n╔" + border + "╗")
for line in Display:
    print(f"║  {line.ljust(max_len)}  ║")
print("╚" + border + "╝")

# Ask if the user wants to save the result
save = input("Do you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    # You can change the filename if you want
    with open("my_portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, qty in my_portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ₹{price} = ₹{value}\n")
        file.write(f"\nTotal Investment: ₹{total_value}")
    print("Portfolio saved as 'my_portfolio.txt'")
