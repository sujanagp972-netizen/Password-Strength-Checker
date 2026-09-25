import re

password = input("Enter your password: ")

score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters.")

if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

if re.search(r"[a-z]", password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

if re.search(r"[0-9]", password):
    score += 1
else:
    feedback.append("Add at least one number.")

if re.search(r"[^A-Za-z0-9]", password):
    score += 1
else:
    feedback.append("Add at least one special character.")

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Strength:", strength)

if feedback:
    print("Suggestions:")
    for item in feedback:
        print("-", item)
else:
    print("Your password meets all the security requirements.")