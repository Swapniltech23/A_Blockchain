import streamlit as st
import time
import hashlib
import json

# Initialize session state for blockchain
if "blockchain" not in st.session_state:
    st.session_state.blockchain = [
        {
            "index": 0,
            "timestamp": time.time(),
            "data": "Genesis Block",
            "previous_hash": "0",
            "hash": hashlib.sha256("Genesis Block".encode()).hexdigest()
        }
    ]

# Function to add a block
def add_block(data):
    previous_block = st.session_state.blockchain[-1]
    index = previous_block["index"] + 1
    timestamp = time.time()
    previous_hash = previous_block["hash"]
    block_content = f"{index}{timestamp}{data}{previous_hash}"
    block_hash = hashlib.sha256(block_content.encode()).hexdigest()

    new_block = {
        "index": index,
        "timestamp": timestamp,
        "data": data,
        "previous_hash": previous_hash,
        "hash": block_hash
    }

    st.session_state.blockchain.append(new_block)
    st.success(f"✅ Block {index} added successfully!")

# Streamlit UI
st.title("📦 Simple Blockchain Demo")

user_data = st.text_input("Enter data for the new block:")

if st.button("Add Block"):
    if user_data:
        add_block(user_data)
    else:
        st.warning("⚠️ Please enter some data before adding a block.")

# Display the blockchain
st.subheader("📜 Blockchain")
st.json(st.session_state.blockchain)
