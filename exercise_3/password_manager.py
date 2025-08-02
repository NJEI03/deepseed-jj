import re

# Common passwords to avoid (predefined list)
COMMON_PASSWORDS = ["123456", "password", "qwerty", "abc123", "letmein", "football", 
                    "admin", "welcome", "login", "monkey", "dragon", "passw0rd", "master", "hello",
                    "freedom", "whatever", "12345", "12345678", "123456789", "iloveyou"]

# Analyze password strength based on various criteria
def analyze_password(password):
    score = 0
    results = []
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 20
        results.append("✅ Length requirement (8+ chars)")
    else:
        results.append("❌ Length is less than 8 characters")
        suggestions.append("Use at least 8 characters")

    # Uppercase letter check using regex
    if re.search(r'[A-Z]', password):
        score += 20
        results.append("✅ Contains uppercase letters")
    else:
        results.append("❌ Missing uppercase letters")
        suggestions.append("Include uppercase letters")

    # Lowercase letter check
    if re.search(r'[a-z]', password):
        score += 20
        results.append("✅ Contains lowercase letters")
    else:
        results.append("❌ Missing lowercase letters")
        suggestions.append("Include lowercase letters")

    # Digit check
    if re.search(r'\d', password):
        score += 20
        results.append("✅ Contains numbers")
    else:
        results.append("❌ Missing numbers")
        suggestions.append("Include at least one number")

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 20
        results.append("✅ Contains special characters")
    else:
        results.append("❌ Missing special characters")
        suggestions.append("Add characters like !@#$%^&*")

    # Common password check
    if password.lower() not in COMMON_PASSWORDS:
        score += 20
        results.append("✅ Not a common password")
    else:
        results.append("❌ Common password detected")
        suggestions.append("Avoid using common passwords")

    # Determine strength level
    if score <= 40:
        strength = "Weak"
    elif score <= 60:
        strength = "Fair"
    elif score <= 80:
        strength = "Good"
    elif score <= 100:
        strength = "Strong"
    else:
        strength = "Excellent"

    return score, strength, results, suggestions

# Main function to interact with user
def main():
    print("=== PASSWORD SECURITY ANALYZER ===")
    password = input("Enter password to analyze: ")

    score, strength, results, suggestions = analyze_password(password)

    print("\n🔒 SECURITY ANALYSIS RESULTS")
    print(f"Password: {password}")
    print(f"Score: {score}/120 ({strength})\n")

    for res in results:
        print(res)

    if suggestions:
        print("\n💡 SUGGESTIONS:")
        for sug in suggestions:
            print(f"- {sug}")
    else:
        print("\n🎉 Your password is excellent!")

if __name__ == "__main__":
    main()
