# DNA base pairing: a <-> t, c <-> g

pair = {
    'a': 't',
    't': 'a',
    'c': 'g',
    'g': 'c'
}

    
def get_dna_sequence():
    seq = None   # placeholder to store the result
    
    while True:
        seq = input("Enter DNA sequence (a,t,g,c) or 'quit': ").lower().replace(" ", "")
        
        if seq == 'quit':
            seq = None
            break
        
        if not seq:
            print("Empty input. Try again.")
            continue
        
        invalid = sorted(set(ch for ch in seq if ch not in pair))
        if invalid:
            print(f"Invalid: {', '.join(invalid)}")
            print("Type 'quit' to exit")
            continue
        
        # valid sequence found → break out of loop
        break
    
    return seq


def complement_sequence(seq: str) -> str:

    print(__name__)
    # C and G (triple bond) as uppercase, A and T (double bond) as lowercase
    comp = []
    for ch in seq:
        base = pair[ch]
        if base == 'c' or base == 'g':
            comp.append(base.upper())
        elif base == 'a' or base == 't':
            comp.append(base.lower())
        else:
            comp.append(base)
    return ''.join(comp)

def main():
    print("\n=== DNA Complement ===")
    print("Type 'quit' anytime to exit\n")
    while True:
        seq = get_valid_sequence()
        
        if seq is None:
            print("Goodbye!")
            return
        
        comp = complement_sequence(seq)
        print(f"Original:       {seq}")
        print(f"Complementary:  {comp}\n")
        
        while True:
            again = input("Another sequence? (y/n): ").strip().lower()
            if again in ('y', 'yes'):
                break
            if again in ('n', 'no', 'q', 'quit'):
                print("Goodbye!")
                return
            print("Type 'y' or 'n'")



if __name__ == '__main__':
    main()