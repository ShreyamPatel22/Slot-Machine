import random

#did in all capitals because it is a constant number and it won't change 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #loop through every row
    for line in range(lines):
        #the symbol we want to check is whatever symbol is in the first column of the current row
        symbol= columns[0][line]
        #loop through ever column
        for column in columns:
            symbol_to_check= column[line]
            #check if symbols are same
            if symbol != symbol_to_check:
                #if not same break 
                break
        else:
            winnings += values[symbol] * bet 
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
#using nested lists
#defining column 
    columns =[]
    #generate a column for every single column we have
    for _ in range(cols):
        column = []
        #put [:] to make a copy 
        #current symbols, which we can currently select from and make a copy of all symbols 
        current_symbols = all_symbols[:]
        #loop through values that we need to generate, which ='s the number of rows in the slot machine
        for _ in range(rows):
            #picks random values from the lists 
            value = random.choice(current_symbols)
            #removes the already picked choice 
            current_symbols.remove(value)
            #adds the value to the column 
            column.append(value) 

        columns.append(column)

    return columns

def print_slot_machine(columns):
    #use transposing
    for row in range(len(columns[0])):
    #enumerate give the index, so 0 1 2 3, as you loop through as well as the items
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")

        print()




def deposit(): 
    #start a while loop 
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            #^is digit tells us if it is a whole number (+)
            amount = int(amount)
            if amount > 0:
                break 
            #While loop ended with "break"
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            #^is digit tells us if it is a whole number (+)
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break 
            #While loop ended with "break"
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            #^is digit tells us if it is a whole number (+)
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break 
            #While loop ended with "break"
            else:
                ##put f before the string and then put curly braces like {} 
                # and inside the write any variable and it will automatically be converted to a string for you
                #if it can be converted 
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    # *winnings is the splat operator and it's going to pass every single line from winning lines list to the print function
    print(f"You won on lines:", *winning_lines)
    #tell us how much they won or lost from the bet
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

main()