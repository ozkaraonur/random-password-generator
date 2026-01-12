import secrets
import string

def generate_strong_password(length=20): # Default highly secure length
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        # Complexity Guarantee
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

def main():
    print("--- Sentinel Password Architect ---")
    
    suggested_password = generate_strong_password()
    
    print(f"\n[?] Suggested Strong Password: {suggested_password}")
    
    choice = input("\nDo you want to use this password? (y/n): ").lower()
    
    if choice == 'y':
        print(f"\n[+] Secured: {suggested_password}")
        print("[*] Make sure to save it in your password manager.")
    else:
        print("[!] Action cancelled by user.")

if __name__ == "__main__":
    main()
