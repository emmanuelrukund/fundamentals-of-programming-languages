class LoginSystem:
    # Initialize the LoginSystem with a list of valid email domains
    def __init__(self, valid_domains=None):
        # Set default valid domains if none are provided
        if valid_domains is None:
            valid_domains = ["gmail.com", "yahoo.com", "mail.com", ".ac.ke"]
        self.valid_domains = valid_domains

    # Validate if the provided email address has a valid domain
    def validate_email(self, email):
        # Check if "@" is in the email and if any of the valid domains are in the email
        if "@" in email and any(domain in email for domain in self.valid_domains):
            return True
        return False

    # Validate if the provided password meets the length requirement
    def validate_password(self, password):
        # Password must be at least 8 characters long
        if len(password) >= 8:
            return True
        return False

    # Main method to handle user login process
    def login(self):
        while True:
            print("Hello, Welcome! \nEnter your credentials to login")
            # Prompt user to input their email address
            userName = input("Email address: ")
            # Prompt user to input their password
            password = input("Password: ")

            # Check if both username and password are provided
            if userName and password:
                # Validate the email address
                if self.validate_email(userName):
                    # Validate the password
                    if self.validate_password(password):
                        print("Login Successful! You can access our services.")
                        break
                    else:
                        print("Invalid Password. Password should have at least 8 characters")
                else:
                    print("Invalid Email address.\nPlease try again.")
            else:
                print("Enter all fields")

# Entry point for the script
if __name__ == "__main__":
    # Create an instance of LoginSystem and call the login method
    login_system = LoginSystem()
    login_system.login()
