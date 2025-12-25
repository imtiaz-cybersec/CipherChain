# ⛓️ CipherChain: Cryptographic Ledger & Integrity Auditor

### 📄 Project Description
**CipherChain** is a **mini-version**, Python-based blockchain system designed to illustrate the core principles of cryptographic data integrity and immutable record-keeping. It serves as a secure engine for tracking system events and logs by utilizing advanced data structures and hashing algorithms. By combining **SHA-256 cryptographic linkage** with a custom **Merkle Tree architecture**, CipherChain ensures that any unauthorized modification to historical records is immediately detectable, providing a robust foundation for building secure audit trails.

---

### 🌟 Key Features
* **Merkle Tree-Based Integrity:** Efficiently summarizes large lists of data into a single "Merkle Root" hash, ensuring that every piece of information in a block is accounted for and verifiable.
* **Cryptographic Chaining:** Each block is securely linked to its predecessor through SHA-256 hashes, creating an unbroken sequence where changing one block invalidates all subsequent entries.
* **Automated Chain Validation:** Features built-in logic to traverse the entire ledger, verifying hash consistency and ensuring the linkage between blocks remains intact.
* **Interactive Tamper Detection:** Includes a simulation suite that demonstrates the system's resilience by detecting manual data manipulation in real-time.
* **Data Serialization:** Utilizes JSON for standardized data handling, allowing for easy integration with system event logs.

---

### 📊 Methodology: How it Works
The lifecycle of data within CipherChain follows a strict cryptographic pipeline:

1.  **Data Ingestion:** The system loads a collection of raw event data (e.g., user logins, file access) from a JSON source.
2.  **Merkle Root Generation:** The `merkle.py` module processes the data list, recursively hashing and pairing elements to produce a unique Merkle Root.
3.  **Block Mining:** A new block is created, containing the index, timestamp, data list, the generated Merkle Root, and the cryptographic hash of the previous block.
4.  **Chain Extension:** The `Blockchain` class appends the newly minted block to the ledger after validating its parameters.
5.  **Integrity Sweeping:** The system runs a validation check across the entire chain to ensure `current.previous_hash` matches `previous.hash`.
6.  **Security Testing:** A tampering simulation manually alters a piece of data within the chain and re-calculates that block's hash to show how the system detects the discrepancy.

#### **System Operational Flow**
<img width="1524" height="433" alt="image" src="https://github.com/user-attachments/assets/b9986132-8841-4717-a4e6-680a8c03e315" />

---

## 📁 Project Architecture
The project is built with a modular design to demonstrate how different cryptographic components interconnect to form a functional ledger:

* **`blockchain.py`**: The core engine containing the `Block` and `Blockchain` classes; it manages the hashing logic and maintains the chain's integrity.
* **`merkle.py`**: A specialized module that builds the Merkle Tree and returns the root hash to ensure data within a block cannot be altered.
* **`main.py`**: The central entry point that orchestrates the demo, loads data, and executes the security tampering simulation.
* **`sample_events.json`**: A mock dataset containing system events like "User login" and "File accessed" to simulate real-world logging.
* **`test.py`**: A utility script providing examples of binary tree traversals, serving as a conceptual foundation for tree-based data structures.

---

## 🚀 How to Run and Experience
> [!IMPORTANT]
> **Disclaimer:** This is a **mini-version** of blockchain technology created for educational and demonstration purposes. It is not intended for professional-level production use or financial transactions.

To experience the CipherChain security engine on your local machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/imtiaz-cybersec/CipherChain.git](https://github.com/imtiaz-cybersec/CipherChain.git)
    cd CipherChain
    ```
2.  **Initialize the Demo:** Ensure you have Python 3.x installed. Run the main simulation script:
    ```bash
    python main.py
    ```
3.  **Analyze the Security Output:**
    * The console will first display the **New block added** with its unique Index, Merkle Root, and Hash.
    * The system will then perform a **Tampering Test**, manually altering an event in the chain.
    * Observe the final validation result where the system detects the change and marks the chain as **Invalid**.
