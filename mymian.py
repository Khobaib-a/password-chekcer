for i in range(1, 4):
    print("*" * i)
print("Hallo, Welcome in the Passowrd strength checker! ")
for i in range(3, 0, -1):
    print("*" * i)

password = input("Enter your password to check its strength: ")

def checking_length_password(password):
    """
    Function 1: Check password length and assign points.
    1-4 chars: 10 points
    5 chars: 15 points
    6 chars: 20 points
    7-10 chars: 30 points
    11-15 chars: 40 points
    16-20 chars: 50 points
    21-30 chars: 60 points
    """
    length = len(password)

    if 1 <= length <= 4:
        return 10
    elif length == 5:
        return 15
    elif length == 6:
        return 20
    elif 7 <= length <= 10:
        return 30
    elif 11 <= length <= 15:
        return 40
    elif 16 <= length <= 20:
        return 50
    elif 21 <= length <= 30:
        return 60
    return 0
    
def variety_of_characters(password):
    """
    Function 2: Check how many different types of characters exist.
    Add 10 points for each type (spaces are allowed, no penalty).
    
    Types: uppercase, lowercase, numbers, special symbols
    """
    variaty_dict = {
        "has_uppercase": 0,
        "has_lowercase": 0,
        "has_numbers": 0,         
        "has_special": 0
    }
    types_count = 0
    for char in password:
        if char.isupper():
            variaty_dict["has_uppercase"] = 1
        elif char.islower():                
            variaty_dict["has_lowercase"] = 1
        elif char.isdigit():        
            variaty_dict["has_numbers"] = 1
        elif not char.isspace():  # Not a space and not alphanumeric
            variaty_dict["has_special"] = 1
    for types in variaty_dict:
        types_count += variaty_dict[types]
    
    return types_count * 10
    # List of common words to check
def predictability(password):
    """
    Function 3: Check for common words and patterns.
    If none exist, add 10 points.
    
    Common words: password, mybirthday, etc.
    Patterns: aaaa, bbbb, 12345, etc.
    """
    points = 0
    password_lower = password.lower()
    
    # List of common words to check
    common_words = ["password", "mybirthday", "qwerty", "123456", "admin", "user"]
    if password_lower in common_words:
        points -= 10

    # Check for simple patterns
    patterns = ["aaaa", "bbbb", "12345", "abcd", "1111", "0000"]
    if password_lower in patterns:
        points -= 10
    if ord(password[0]) == ord(password[1]) -1 == ord(password[2]) -2 == ord(password[3]) -3 == ord(password[4]) -4:
        points -= 20
    if ord(password[0]) == ord(password[1]) +1 == ord(password[2]) +2 == ord(password[3]) +3 == ord(password[4]) +4:
        points -= 20
    if points == 0:
        points += 10
    return points

def total_password_strength(password):
    """
    Calculate total password strength based on length, character variety, and predictability.
    """
    evaluation = ""
    if len(password) == 0:
        print("Password cannot be empty.")
    elif len(password) > 30:
        print("Password length exceeds maximum limit of 30 characters.")
    elif password.isspace():
        print("Password cannot be only spaces.")
    
    length_points = checking_length_password(password)
    variety_points = variety_of_characters(password)    
    predictability_points = predictability(password)
    total_points = length_points + variety_points + predictability_points

    if total_points < 0:
        evaluation = "Very very Weak"
    elif 0 <= total_points <= 20:
        evaluation = "very Weak" 
    elif 21 <= total_points <= 40:
        evaluation = "Weak"
    elif 41 <= total_points <= 60:  
        evaluation = "Moderate"
    elif 61 <= total_points <= 80:
        evaluation = "Strong"
    elif 81 <= total_points <= 100: 
        evaluation = "Very Strong"
    elif 100 < total_points <= 300:
        evaluation = "Extremely Strong"
    print("********** Password Strength Evaluation **********")    
    print(f"Password Strength Points: {total_points}, that means : {evaluation}, length points: {length_points}, variety points: {variety_points}, predictability points: {predictability_points}")
    print("**************************************************")
    
    
    return total_points
total_password_strength(password)
