from hashlib import sha256
import random

MAX_NONCE = 1000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transaction, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for i in range(MAX_NONCE):
        nonce = random.randint(1, MAX_NONCE)
        text = str(block_number) + transaction + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yah! Successfully mined bitcoins with nonce value:  {nonce}")
            return new_hash
    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")


if __name__ == "__main__":
    transaction = """
    Karan->Ballu->20,
    Kartik->Muskan->30
    """
    difficulty = 4
    new_hash = mine(5, transaction, str(SHA256("ABC")), difficulty)
    print(new_hash)
