!/usr/bin/python3

def islower(c):
    """Check if a character is lowercase."""
    # Convert character to its ASCII value and check if it's in the lowercase range
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
