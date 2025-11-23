# DNA base pairing: a <-> t, c <-> g

import sys
import os

# Define base pair mapping
pair = {
    'a': 't',
    't': 'a',
    'c': 'g',
    'g': 'c'
}

def get_valid_sequence(interactive: bool = True):
    """Get a valid DNA sequence from the user or from piped stdin.

    If `interactive` is False the function will read a single line from
    stdin (useful for piping) and return it (after validation).
    """
    while True:
        if interactive:
            try:
                raw = input("Enter a DNA sequence (letters a, t, g, c): ")
            except EOFError:
                raw = ''
        else:
            # Read one line from stdin when data is piped in
            raw = sys.stdin.readline()
            if raw is None:
                raw = ''
            # Do not prompt when reading from pipe; just strip trailing newline
            raw = raw.rstrip('\n')

        seq = raw.strip().replace(" ", "")
        # Optional debug: show raw input details when DNA_DEBUG env var is set
        if os.environ.get('DNA_DEBUG') == '1':
            print('DEBUG raw repr:', repr(raw))
            print('DEBUG seq repr :', repr(seq))
            flags = [(ch, ord(ch), ch.isupper()) for ch in raw]
            print('DEBUG raw chars :', flags)
        if not seq:
            if interactive:
                print("Empty input. Please enter at least one base (a, t, g, c).")
                continue
            # In non-interactive mode, return empty to allow caller to handle it
            return ''

        invalid = sorted(set(ch for ch in seq if ch.lower() not in pair))
        if invalid:
            print(f"Invalid characters found: {', '.join(invalid)}. Please use only a, t, g, c.")
            if interactive:
                continue
            return ''
        return seq

def complement_sequence(seq: str) -> str:
    """Return the complementary DNA sequence for the input sequence."""
    # Preserve original letter case: map using lowercase lookup, then
    # convert to uppercase if the original character was uppercase.
    out = []
    for ch in seq:
        base = ch.lower()
        comp = pair[base]
        out.append(comp.upper() if ch.isupper() else comp)
    return ''.join(out)

def main():
    interactive = sys.stdin.isatty()
    while True:
        seq = get_valid_sequence(interactive=interactive)
        if not seq:
            # No valid input (or EOF) in non-interactive mode: exit gracefully
            if not interactive:
                return
            # In interactive mode, loop back to prompt again
            continue

        comp = complement_sequence(seq)
        print(f"Original sequence: {seq}")
        print(f"Complementary sequence: {comp}")

        if not interactive:
            # When input was piped, process only the first sequence then exit
            return

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