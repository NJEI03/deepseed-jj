# password_analyzer.py

import re

# List of 20+ common passwords to check against
COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123", "football",
    "123456789", "12345", "letmein", "1234567", "basketball", "monkey",
    "iloveyou", "admin", "welcome", "login", "dragon", "passw0rd",
    "master", "hello", "freedom", "whatever"
]

# Function to analyze a password and return score, results and suggestions
def analyze_password(password):
    score = 0
    results = []
    suggestions = []

    # Criterion 1: Length at least 8 characters
    if len(password) >= 8:
        score += 20
        results.append("✅ Length requirement (8+ chars)")
    else:
        results.append("❌ Length is less than 8 characters")
        suggestions.append("Use at least 8 characters")

    # Criterion 2: Contains uppercase letters
    if re.search(r'[A-Z]', password):
        score += 20
        results.append("✅ Contains uppercase letters")
    else:
        results.append("❌ Missing uppercase letters")
        suggestions.append("Include at least one uppercase letter")

    # Criterion 3: Contains lowercase letters
    if re.search(r'[a-z]', password):
        score += 20
        results.append("✅ Contains lowercase letters")
    else:
        results.append("❌ Missing lowercase letters")
        suggestions.append("Include at least one lowercase letter")

    # Criterion 4: Contains numbers
    if re.search(r'\d', password):
        score += 20
        results.append("✅ Contains numbers")
    else:
        results.append("❌ Missing numbers")
        suggestions.append("Include at least one number")

    # Criterion 5: Contains special characters (!@#$%^&*)
    if re.search(r'[!@#$%^&*]', password):
        score += 20
        results.append("✅ Contains special characters")
    else:
        results.append("❌ Missing special characters")
        suggestions.append("Add special characters like !@#$%^&*")

    # Criterion 6: Not a common password
    if password.lower() not in COMMON_PASSWORDS:
        score += 20
        results.append("✅ Not a common password")
    else:
        results.append("❌ Common password detected")
        suggestions.append("Avoid common password patterns")
        suggestions.append("Consider using a passphrase instead")

    # Determine strength level based on score
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

def main():
    print("=== PASSWORD SECURITY ANALYZER ===")
    password = input("Enter password to analyze: ")

    # Analyze the password
    score, strength, results, suggestions = analyze_password(password)

    # Display the analysis results
    print("\n🔒 SECURITY ANALYSIS RESULTS")
    print(f"Password: {password}")
    print(f"Score: {score}/120 ({strength})\n")

    # Display passed and failed criteria
    for res in results:
        print(res)
    
    # Display suggestions for improvement if needed
    if suggestions:
        print("\n💡 SUGGESTIONS:")
        for sug in suggestions:
            print(f"- {sug}")
    else:
        print("\n🎉 Your password is excellent!")

if __name__ == "__main__":
    main()
