import json
from blockchain import Blockchain

def main():
    # Load sample event data
    with open("sample_events.json", "r") as file:
        events = json.load(file)

    # Create blockchain and add block
    my_chain = Blockchain()
    new_block = my_chain.add_block(events)

    print("\n===== CipherChain Demo =====")
    print("New block added!")
    print("Block Index:", new_block.index)
    print("Merkle Root:", new_block.merkle_root)
    print("Block Hash:", new_block.hash)
    print("\nChecking Blockchain Validity:", my_chain.is_chain_valid())

    # ---------- Tampering test ----------
    print("\nNow simulating tampering... 🔥")
    my_chain.chain[1].data[0] = "Tampered event: Unauthorized Access"
    my_chain.chain[1].hash = my_chain.chain[1].compute_hash()  # recompute the block hash manually

    print("Re-checking Blockchain Validity:", my_chain.is_chain_valid())
    print("============================\n")

if __name__ == "__main__":
    main()
