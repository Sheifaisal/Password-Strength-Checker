import re

def check_password_strength(password):
    """
    Checks the strength of a given password based on several criteria.

    Args:
        password (str): The password string to be checked.

    Returns:
        tuple: A tuple containing a string rating and a list of feedback messages.
    """
    # A list to store feedback messages for the user.
    feedback = []
    
    # Initialize the strength score. A higher score means a stronger password.
    score = 0
    
    # --- Criterion 1: Length ---
    # A good password should be at least 8 characters long.
    min_length = 8
    if len(password) >= min_length:
        score += 1
    else:
        feedback.append(f"Password must be at least {min_length} characters long.")

    # --- Criterion 2: Uppercase Letters ---
    # Check if the password contains at least one uppercase letter (A-Z).
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter.")

    # --- Criterion 3: Lowercase Letters ---
    # Check if the password contains at least one lowercase letter (a-z).
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one lowercase letter.")

    # --- Criterion 4: Numbers ---
    # Check if the password contains at least one digit (0-9).
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one number.")

    # --- Criterion 5: Special Characters ---
    # Check if the password contains at least one special character.
    # The regex pattern matches any character that is not a letter, number, or underscore.
    if re.search(r"[!@#$%^&*()_+=-`~\[\]{}|;':\",.<>/?\\]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character.")

    # --- Final Rating based on score ---
    # Assign a rating based on the total score.
    if score == 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Medium"
    else:
        rating = "Weak"
        
    return rating, feedback

def main():
    """
    The main function to run the password strength checker.
    """
    print("--- Password Strength Checker ---")
    while True:
        password = input("Enter a password to check (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("Exiting...")
            break
            
        rating, feedback = check_password_strength(password)
        
        print(f"\nPassword: '{password}'")
        print(f"Strength: {rating}")
        
        # Display feedback if the password is not strong.
        if rating != "Strong":
            print("To make your password stronger, please address the following:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("Your password is very strong! Good job.")
            
        print("-" * 30)

if __name__ == "__main__":
    # This ensures that the main() function is called when the script is run directly.
    main()


