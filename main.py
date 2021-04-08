import datetime
import hashlib


class Transaction:
    def __init__(self, amount, sender, receiver):
        self.amount = amount
        self.sender = sender
        self.receiver = receiver

    def __str__(self):
        return str(id(self))


class Block:
    def __init__(self, prevhash, transaction: Transaction):
        self.prevHash = prevhash
        self.transaction = transaction
        self.ts = datetime.datetime.now()

    def hash(self):
        self.byte_ = bytes(id(self))
        self.hash = hashlib.hashlib.sha256(self.byte_)
        self.hex_dif = hash.hexdigest()
        return self.hex_dif


class Chain:
    instance = None

    chain = list()

    def __init__(self):
        self.chain = [Block(None, Transaction(100, "genesis", "satoshi"))]

    def lastBlock(self):
        return self.chain[-1]

    def addBlock(self, transaction: Transaction, senderPublicKey: str, signature: str):
        newBlock = Block(self.lastBlock.hash, transaction)
        self.chain.append(newBlock)


class Wallet:
    publicKey: str
    privateKey: str

    def __init__(self):
        self.keypair = hashlib.


t1 = Transaction(100, "karan", "harman")
print(str(type(t1).__hash__))
