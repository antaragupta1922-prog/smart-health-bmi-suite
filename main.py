import sys
from src.database import DatabaseManager
from src.auth import AuthManager
from src.validator import InputValidator
from src.calculator import HealthCalculator
from src.reports import ReportGenerator

def main():
    db = DatabaseManager()
    auth = AuthManager(db)

    print("==================================================")
    print("      WELCOME TO SMART HEALTH & BMI SUITE         ")
    print("==================================================")

    while True:
        if not auth.current_user:
            print("\n--- MAIN MENU ---")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Select an option (1-3): ").strip()

            if choice == '1':
                uname = input("Username: ")
                passwd = input("Password: ")
                success, msg = auth.login(uname, passwd)
                print(f"[*] {msg}")
            elif choice == '2':
                uname = input("Choose Username: ")
                passwd = input("Choose Password: ")
                success, msg = auth.register(uname, passwd)
                print(f"[*] {msg}")
            elif choice == '3':
                print("[*] Thank you for using Smart Health Suite. Goodbye!")
                sys.exit(0)
            else:
                print("[!] Invalid option. Please enter 1, 2, or 3.")
        else:
            print(f"\n--- USER DASHBOARD ({auth.current_user['username'].upper()}) ---")
            print("1. Calculate BMI & Health Metrics")
            print("2. View Progress Logs")
            print("3. Logout")
            choice = input("Select an option (1-3): ").strip()

            if choice == '1':
                try:
                    w_str = input("Enter Weight in kg (e.g., 70): ")
                    weight = InputValidator.validate_positive_float(w_str, "Weight")

                    h_str = input("Enter Height in cm (e.g., 175): ")
                    height = InputValidator.validate_positive_float(h_str, "Height")

                    age_str = input("Enter Age in years: ")
                    age = InputValidator.validate_age(age_str)

                    gender_str = input("Enter Gender (Male/Female): ")
                    gender = InputValidator.validate_gender(gender_str)

                    # Computations
                    bmi = HealthCalculator.calculate_bmi(weight, height)
                    category = HealthCalculator.get_bmi_category(bmi)
                    bmr = HealthCalculator.calculate_bmr(weight, height, age, gender)
                    min_w, max_w = HealthCalculator.calculate_ideal_weight(height)

                    # Save result
                    db.save_log(auth.current_user['id'], weight, height, bmi, category, bmr)

                    # Display Summary
                    print("\n" + "-"*40)
                    print("         YOUR HEALTH EVALUATION RESULTS     ")
                    print("-"*40)
                    print(f" BMI Index            : {bmi}")
                    print(f" Health Category       : {category}")
                    print(f" Basal Metabolic Rate : {bmr} kcal/day")
                    print(f" Healthy Weight Range : {min_w} kg - {max_w} kg")
                    print("-"*40)
                    print("[✓] Results successfully logged to database!")

                except ValueError as err:
                    print(f"\n[!] Input Error: {err}")

            elif choice == '2':
                logs = db.get_user_logs(auth.current_user['id'])
                ReportGenerator.display_logs(logs)

            elif choice == '3':
                auth.logout()
                print("[*] Logged out successfully.")

            else:
                print("[!] Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()