def max_substrings_removed(main_string, substrings):
    count = 0
    used = set()  # Track substrings that have already been used

    while True:
        found = False
        for sub in substrings:
            if sub not in used and sub in main_string:
                # Remove the substring once
                main_string = main_string.replace(sub, "")
                used.add(sub)
                count += 1
                found = True
                break  # Recheck from the start since the string has changed
        if not found:
            break  # Exit if no substrings can be removed

    return count
N = int(input())  # Number of substrings
substrings = input().split()  # List of substrings
main_string = input()  # Main string

print(max_substrings_removed(main_string, substrings))