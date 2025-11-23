# DNA base pairing: a <-> t, c <-> g

# Get user input
base = input("Enter a DNA base (a, t, g, c): ").lower()

# Define base pair mapping
pair = {
    'a': 't',
    't': 'a',
    'c': 'g',
    'g': 'c'
}

# Output the corresponding pair or an error message
if base in pair:
    print(f"The pair for {base} is {pair[base]}")
else:
    print("Invalid input. Please enter a, t, g, or c.")

# 1. allow constant sequnce of number
# 2. if incorrect input allow user to correct it