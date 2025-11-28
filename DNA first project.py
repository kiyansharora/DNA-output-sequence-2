# DNA base pairing: a <-> t, c <-> g

# Define base pair mapping
pair = {
    'a': 't',
    't': 'a',
    'c': 'g',
    'g': 'c'
}

def get_valid_sequence():
    """Prompt the user until a valid DNA sequence (a, t, g, c) is provided.
    
    Returns the sequence if valid, or None if the user types 'quit'.
    """
    while True:
        seq = input("Enter a DNA sequence (a, t, g, c) or type 'quit' to exit: ").lower().replace(" ", "")
        if seq == 'quit':
            return None
        if not seq:
            print("Empty input. Please enter at least one base (a, t, g, c).")
            continue
        invalid = sorted(set(ch for ch in seq if ch not in pair))
        if invalid:
            print(f"Invalid characters found: {', '.join(invalid)}. Please use only a, t, g, c.")
            print(">>> Type 'quit' to exit <<<")
            continue
        return seq

def complement_sequence(seq: str) -> str:
    """Return the complementary DNA sequence for the input sequence."""
    return ''.join(pair[ch] for ch in seq)

def main():
    print("\n=== DNA Complement Sequence Generator ===")
    print("Enter a DNA sequence (a, t, g, c) to see its complement.")
    print("Tip: Type 'quit' at any time to exit.\n")
    while True:
        seq = get_valid_sequence()
        if seq is None:
            # User typed 'quit'
            print("Goodbye.")
            return
        comp = complement_sequence(seq)
        print(f"Original sequence: {seq}")
        print(f"Complementary sequence: {comp}")

        # Ask the user whether they want to enter another sequence
        while True:
            again = input("Would you like to enter another sequence? (y/n): ").strip().lower()
            if again in ('y', 'yes'):
                break  # outer loop continues
            if again in ('n', 'no', 'q', 'quit'):
                print("Goodbye.")
                return
            print("Please answer 'y' or 'n'.")

if __name__ == '__main__':
    main()

# Notes:
# - Accepts sequences of any length composed of a, t, g, c (spaces ignored).
# - Re-prompts on invalid characters so the user can correct mistakes.