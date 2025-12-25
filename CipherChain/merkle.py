import hashlib

def hash_data(data):
    """Hashes a single data item."""
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_tree(data_list):
    """Builds a Merkle tree and returns the root hash."""
    if not data_list:
        return None

    # Hash all data items
    current_level = [hash_data(data) for data in data_list]

    # Keep combining pairs until only one hash (the root) remains
    while len(current_level) > 1:
        temp_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left  # duplicate last if odd
            combined_hash = hashlib.sha256((left + right).encode()).hexdigest()
            temp_level.append(combined_hash)
        current_level = temp_level

    return current_level[0]  # The Merkle Root


def verify_merkle_tree(data_list, merkle_root):
    """Verifies if Merkle root matches given data."""
    return build_merkle_tree(data_list) == merkle_root
