email = input("Enter the email: ")
email.index('@')
username = email[:email.index('@')]
domainname = email[email.index('@') + 1:]
print(f"Your username is {username} and domain name is {domainname}")