import random
import string

def generate_password(length=12, use_numbers=True, use_symbols=True):
    # Core character sets
    letters = string.ascii_letters
    digits = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""
    
    all_characters = letters + digits + symbols
    
    if not all_characters:
        return "Error: No character types selected!"
        
    # Generate password by randomly choosing from the pool
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("--- 🔐 Welcome to SecurePass Generator ---")
    
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        include_nums = input("Include numbers? (y/n, default y): ").lower() != 'n'
        include_syms = input("Include symbols? (y/n, default y): ").lower() != 'n'
        
        password = generate_password(length, include_nums, include_syms)
        
        print("\n" + "="*30)
        print(f"Generated Password: {password}")
        print("="*30)
        
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
