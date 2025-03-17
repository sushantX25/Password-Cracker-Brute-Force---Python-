import hashlib

def brute_force_hash(hash_to_crack, wordlist):
    with open(wordlist, "r") as words:
        for word in words:
            word = word.strip()
            if hashlib.md5(word.encode()).hexdigest() == hash_to_crack:
                print(f"Password found: {word}")
                return
    print("Password not found in wordlist.")

hash_input = input("Enter MD5 hash: ")
wordlist_path = input("Enter wordlist file path: ")
brute_force_hash(hash_input, wordlist_path)
