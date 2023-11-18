def main():
minimum_length = 5
    def get_password():
        global password
        password = input("Please enter a password: ")


# Ask the user for a password
password = get_password()

    # Check if the password meets the minimum length requirement
    if len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long. Try again.")

    else:
        # Print asterisks based on the password length
        print("*" * len(password))
main()
