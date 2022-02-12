# Nathan's CASH HANDLER 5000 V1_A
# Check out my work @ https://github.com/NPraglin

def optimal_change(price, amount_paid):

    # Initializing our change variable as 'num'
    num = (amount_paid - price)
    print(f"Change is {num}.")

    # Handling a cheapskate!
    if num < 0:
        return (f"We don't give away things for free here! The price is {price}.")
    
    # Handling the perfect customer!
    if num == 0:
        return (f"Thank you for carrying exact change on you, kind sir.")

    # If the customer requires change, we shall continue to calculate the proper change...
    # Initialize the dollars and cents individually 
    dollars, cents = divmod(num, 1)
    print(f"Input case: {dollars} dollars, and {round(cents, 2)} cents")

    # Map out our money values with accuracy
    D_MONEY_MAP = {
        '$100 bill': 100,
        '$50 bill': 50,
        '$20 bill':  20,
        '$10 bill': 10,
        '$5 bill': 5,
        '$1 bill': 1
        }
    C_MONEY_MAP = {
        'quarter': 25,
        'dime': 10,
        'nickel': 5,
        'penny': 1
        }

    # Initialize the return statement
    big_change = (f"The optimal change for an item that costs ${price} with an amount paid of ${amount_paid} is ")

    # Calculate the proper dollar makeup and inject it into our string with confidence
    # I coded with the assumption that ANY edge case is fair game (Example: Paying for a $10 item with $25)
    for key, value in D_MONEY_MAP.items():
        if dollars >= value:
            amount_bills = dollars // value
            d_remainder = dollars - (value * amount_bills)
            if d_remainder == 0 and cents == 0:
                big_change += 'and '
            if amount_bills > 1:
                big_change += f"{int(amount_bills)} {key}s, "
            else: big_change += f"{int(amount_bills)} {key}, "
            dollars = d_remainder

    # Calculate the proper cents makeup (with cents as a non-float) and again, inject with confidence
    # I coded with the assumption that ANY edge case is fair game (Example: Paying for a $0.05 item with $0.50)
    cents = round(cents, 2) * 100
    for key, value in C_MONEY_MAP.items():
        if cents >= value:
            amount_coins = cents // value
            c_remainder = cents - (value * amount_coins)
            if c_remainder == 0 and num > 0.05:
                big_change += 'and '
            if key == 'penny':
                if amount_coins > 1:
                    key = 'pennies'
                big_change += f"{int(amount_coins)} {key}."
            elif amount_coins > 1:
                big_change += f"{int(amount_coins)} {key}s, "
            else: big_change += f"{int(amount_coins)} {key}, "
            cents = c_remainder
    
    # Hard coding to account for an even dollar transaction (no coins exchanged)
    if big_change[-2] == ',':
        big_change = big_change[:-2] + '.'

    # The only return allowed in my store
    print(big_change)
    return big_change