import re
import random
import string

def check_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use 12+ characters for better security")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z)")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z)")

    # Check numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("Add numbers (0-9)")

    # Check symbols
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Add symbols like !@#$%")

    # Check common passwords
    common = ['password', '123456', 'qwerty', 'admin', 'letmein']
    if password.lower() in common:
        suggestions.append("This is a very common password! Change it.")
        score = 0

    return score, suggestions


def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(16))
    return password


def get_strength_label(score):
    if score <= 1:
        return "Very Weak 🔴"
    elif score <= 3:
        return "Weak 🟠"
    elif score <= 4:
        return "Fair 🟡"
    elif score <= 5:
        return "Strong 🟢"
    else:
        return "Very Strong 💪"


def main():
    print("=" * 40)
    print("   PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    while True:
        print("\n1. Check password strength")
        print("2. Generate strong password")
        print("3. Exit")
        choice = input("\nChoose option (1/2/3): ")

        if choice == '1':
            password = input("Enter your password: ")
            score, suggestions = check_strength(password)
            label = get_strength_label(score)

            print(f"\nStrength : {label}")
            print(f"Score    : {score}/6")

            if suggestions:
                print("\nSuggestions:")
                for s in suggestions:
                    print(f"  → {s}")
            else:
                print("\n✅ Your password is strong!")

        elif choice == '2':
            print("\nGenerated Password:", generate_strong_password())

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


main()
