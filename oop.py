class LoginSystem:
    def _init_(self,valid_domains):
        self.valid_domains = ["gmail.com", "yahoo.com", "mail.com", ".ac.ke"]

    def validate_email(self, email):
        if "@" in email and any(domain in email for domain in self.valid_domains):
            return True
        return False

    def validate_password(self, password):
        if len(password) >= 8:
            return True
        return False

    def login(self):
        while True:
            print("Hello, Welcome! \nEnter your credentials to login")
            userName = input("Email address: ")
            password = input("Password: ")

            if userName and password:
                if self.validate_email(userName):
                    if self.validate_password(password):
                        print("Login Successful! You can access our services.")
                        break
                    else:
                        print("Invalid Password. Password should have at least 8 characters")
                else:
                    print("Invalid Email address.\nPlease try again.")
            else:
                print("Enter all fields")

if __name__ == "__main__":
    login_system = LoginSystem()
    login_system.login()