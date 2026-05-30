 # =============================================
#   Password Strength Checker  |  Mini Project
# =============================================

import re

def check_strength(password):
    score = 0

    if len(password) >= 8:                      score += 1  # Rule 1: length
    if re.search(r"[A-Z]", password):           score += 1  # Rule 2: uppercase
    if re.search(r"[a-z]", password):           score += 1  # Rule 3: lowercase
    if re.search(r"[0-9]", password):           score += 1  # Rule 4: digit
    if re.search(r"[!@#$%^&*]", password):      score += 1  # Rule 5: symbol

    return score

def get_label(score):
    labels = {
        0: "Very Weak ❌",
        1: "Very Weak ❌",
        2: "Weak ⚠️",
        3: "Moderate 🟡",
        4: "Strong ✅",
        5: "Very Strong 🔒"
    }
    return labels[score]

def get_tips(password):
    tips = []
    if len(password) < 8:                          tips.append("Use at least 8 characters")
    if not re.search(r"[A-Z]", password):          tips.append("Add an uppercase letter (A-Z)")
    if not re.search(r"[a-z]", password):          tips.append("Add a lowercase letter (a-z)")
    if not re.search(r"[0-9]", password):          tips.append("Add a number (0-9)")
    if not re.search(r"[!@#$%^&*]", password):     tips.append("Add a symbol like !@#$%^&*")
    return tips

def main():
    print("\n====== Password Strength Checker ======")

    while True:
        pwd = input("\nEnter password (or 'quit'): ")

        if pwd.lower() == "quit":
            print("Goodbye! Stay safe online. 🔐")
            break

        if pwd == "":
            print("⚠️  Password cannot be empty. Please try again.")
            continue

        score = check_strength(pwd)
        print(f"\nStrength : {get_label(score)}  ({score}/5)")
        print(f"Password : {'*' * len(pwd)}  ({len(pwd)} chars)")

        tips = get_tips(pwd)
        if tips:
            print("\nTips to improve:")
            for t in tips:
                print(f"  → {t}")
        else:
            print("\n✅ Excellent password! No improvements needed.")

main()
