import hashlib
import json
import time
import merkle   # import our Merkle tree module


# Simple class for each block
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.merkle_root = merkle.build_merkle_tree(data)  # Build Merkle Root from the data list
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    # Hash the block to ensure its integrity
    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "merkle_root": self.merkle_root,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


# Class that holds the entire chain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # The very first block (Genesis)
    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), ["Genesis Block"], "0")
        self.chain.append(genesis_block)

    # Add a new block
    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, previous_block.hash)
        self.chain.append(new_block)
        return new_block

    # Verify if all blocks are valid and untampered
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True


# Helper functions to use from main.py
def create_blockchain():
    blockchain = Blockchain()
    return "Blockchain initialized with Genesis Block."

def add_block(data):
    blockchain = Blockchain()
    blockchain.add_block(data)
    return f"Block added with data: {data}"

def verify_blockchain():
    blockchain = Blockchain()
    return f"Blockchain valid: {blockchain.is_chain_valid()}"
