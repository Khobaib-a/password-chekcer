"""Password strength checker application."""

# Constants
MIN_PASSWORD_LENGTH = 1
MAX_PASSWORD_LENGTH = 30
POINTS_PER_CHARACTER_TYPE = 10
PATTERN_PENALTY = 10
SEQUENCE_PENALTY = 20
NO_PREDICTABILITY_PENALTY = 10

COMMON_WORDS = {"password", "mybirthday", "qwerty", "123456", "admin", "user"}
COMMON_PATTERNS = {"aaaa", "bbbb", "12345", "abcd", "1111", "0000"}

LENGTH_BRACKETS = [
    (4, 10), (5, 15), (6, 20), (10, 30), (15, 40), (20, 50), (30, 60)
]

STRENGTH_LEVELS = [
    (0, "Very Very Weak"),
    (21, "Very Weak"),
    (41, "Weak"),
    (61, "Moderate"),
    (81, "Strong"),
    (101, "Very Strong"),
    (0, "Extremely Strong")
]


def check_password_length(password: str) -> int:
    """Calculate points based on password length."""
    length = len(password)
    for max_len, points in LENGTH_BRACKETS:
        if length <= max_len:
            return points
    return 0


def check_character_variety(password: str) -> int:
    """Calculate points based on character type variety."""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() and not c.isspace() for c in password)
    
    variety_count = sum([has_upper, has_lower, has_digit, has_special])
    return variety_count * POINTS_PER_CHARACTER_TYPE


def check_predictability(password: str) -> int:
    """Check for common words and patterns."""
    if len(password) < 5:
        return 0
    
    password_lower = password.lower()
    
    if password_lower in COMMON_WORDS or password_lower in COMMON_PATTERNS:
        return -PATTERN_PENALTY
    
    # Check for ascending/descending sequences
    if all(ord(password[i]) == ord(password[i-1]) + 1 for i in range(1, 5)):
        return -SEQUENCE_PENALTY
    if all(ord(password[i]) == ord(password[i-1]) - 1 for i in range(1, 5)):
        return -SEQUENCE_PENALTY
    
    return NO_PREDICTABILITY_PENALTY


def validate_password(password: str) -> tuple[bool, str]:
    """Validate password input. Returns (is_valid, message)."""
    if len(password) == 0:
        return False, "Password cannot be empty."
    if len(password) > MAX_PASSWORD_LENGTH:
        return False, f"Password exceeds {MAX_PASSWORD_LENGTH} characters."
    if password.isspace():
        return False, "Password cannot be only spaces."
    return True, ""


def get_strength_level(points: int) -> str:
    """Get strength level based on points."""
    for threshold, level in sorted(STRENGTH_LEVELS, reverse=True):
        if points >= threshold:
            return level
    return "Very Very Weak"


def evaluate_password_strength(password: str) -> None:
    """Main function to evaluate password strength."""
    is_valid, message = validate_password(password)
    if not is_valid:
        print(message)
        return
    
    length_points = check_password_length(password)
    variety_points = check_character_variety(password)
    predictability_points = check_predictability(password)
    total_points = length_points + variety_points + predictability_points
    
    strength_level = get_strength_level(total_points)
    
    print("=" * 50)
    print("Password Strength Evaluation")
    print("=" * 50)
    print(f"Total Points: {total_points}")
    print(f"Strength Level: {strength_level}")
    print(f"  - Length Points: {length_points}")
    print(f"  - Variety Points: {variety_points}")
    print(f"  - Predictability Points: {predictability_points}")
    print("=" * 50)


def main() -> None:
    """Entry point of the application."""
    print("*" * 3)
    print("Welcome to the Password Strength Checker!")
    print("*" * 3)
    
    password = input("Enter your password to check its strength: ")
    evaluate_password_strength(password)


if __name__ == "__main__":
    main()