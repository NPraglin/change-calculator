from optimal_change import optimal_change;

# Each test case returns true. Try your own!

print("1:", optimal_change(62.14, 100) == "The optimal change for an item that costs $62.14 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 1 penny.")

print("2:", optimal_change(32.51, 50) == "The optimal change for an item that costs $32.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 2 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

print("3:", optimal_change(19.19, 20) == "The optimal change for an item that costs $19.19 with an amount paid of $20 is 3 quarters, 1 nickel, and 1 penny.")

print("4:", optimal_change(8.23, 10) == "The optimal change for an item that costs $8.23 with an amount paid of $10 is 1 $1 bill, 3 quarters, and 2 pennies.")

print("5:", optimal_change(1.15, 5) == "The optimal change for an item that costs $1.15 with an amount paid of $5 is 3 $1 bills, 3 quarters, and 1 dime.")

print("6:", optimal_change(4.50, 1) == "We don't give away things for free here! The price is 4.5.")

print("7:", optimal_change(10, 10) == "Thank you for carrying exact change on you, kind sir.")