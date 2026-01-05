def check_length(password):
    """
    Function 1: Check password length and assign points.
    1-4 chars: 10 points
    4-8 chars: 30 points
    8-12 chars: 50 points
    12-30 chars: 60 points
    """
    length = len(password)
    
    if 1 <= length <= 4:
        return 10
    elif 5 <= length <= 8:
        return 30
    elif 9 <= length <= 12:
        return 50
    elif 13 <= length <= 30:
        return 60
    return 0


def check_character_types(password):
    """
    Function 2: Check how many different types of characters exist.
    Add 10 points for each type (spaces are allowed, no penalty).
    
    Types: uppercase, lowercase, numbers, special symbols
    """
    has_uppercase = False
    has_lowercase = False
    has_numbers = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_numbers = True
        elif not char.isspace():  # Not a space and not alphanumeric
            has_special = True
    
    types_count = sum([has_uppercase, has_lowercase, has_numbers, has_special])
    
    return types_count * 10


def check_common_words_patterns(password):
    """
    Function 3: Check for common words and patterns.
    If none exist, add 10 points.
    
    Common words: password, mybirthday, etc.
    Patterns: aaaa, bbbb, 12345, etc.
    """
    password_lower = password.lower()
    
    # List of common words to check
    common_words = ["password", "mybirthday", "qwerty", "123456", "admin", "user"]
    
    # Check for common words
    for word in common_words:
        if word in password_lower:
            return 0
    
    # Check for repeating patterns (4+ same characters or sequential numbers/letters)
    for i in range(len(password) - 3):
        # Check for 4 identical characters
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            return 0
        
        # Check for sequential numbers (like 12345)
        if password[i:i+5].isdigit():
            if int(password[i:i+5]) == int(password[i]) * 10000 + int(password[i]) * 1000 + int(password[i]) * 100 + int(password[i]) * 10 + int(password[i]):
                continue
            # Check if sequential
            sequential = True
            for j in range(i, i+4):
                if int(password[j]) + 1 != int(password[j+1]):
                    sequential = False
                    break
            if sequential:
                return 0
    
    # No common words or patterns found
    return 10


def evaluate_password():
    """
    Main function: Gets user input, validates it, and calculates total score.
    Handles:
    - Empty input (asks again)
    - Input longer than 30 characters (asks again)
    - Calculates total points from all functions
    - Returns evaluation result
    """
    while True:
        password = input("Enter your password: ")
        
        # Check for empty input
        if not password or password.isspace():
            print("Error: Password cannot be empty. Please try again.")
            continue
        
        # Check for length limit (30 characters max)
        if len(password) > 30:
            print("Error: Password is too long (maximum 30 characters). Please try again.")
            continue
        
        # Valid input, break loop
        break
    
    # Calculate points from all functions
    length_points = check_length(password)
    types_points = check_character_types(password)
    patterns_points = check_common_words_patterns(password)
    
    # Total points
    total_points = length_points + types_points + patterns_points
    
    # Determine evaluation based on points
    if total_points >= 80:
        evaluation = "Strong"
    elif total_points >= 50:
        evaluation = "Medium"
    else:
        evaluation = "Weak"
    
    # Print result in the requested format
    print(f"your Password is {evaluation}, you scored: {total_points}")


# Run the program
if __name__ == "__main__":
    evaluate_password()
