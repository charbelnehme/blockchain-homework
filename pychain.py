# PyChain Ledger
# Initial Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib
import time

# Step 1: Define a new Python data class named `Record`
@dataclass
class Record: 
    sender: str
    receiver: str
    amount: int  

# Step 2: Modify the Existing Block Data Class to Store Record Data
@dataclass
class Block:
    ## Re-name the 'data' attribute to 'record', and set the data type to 'Record' 
    record: Record 

    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()

@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Winning Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Proof of Work (PoW) Verification: SUCCESS")
        return True

# Streamlit Code
## Add the cache decorator for Streamlit
@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing PyChain")
    return PyChain([Block("Genesis", 0)])

### Pychain setup
pychain = setup() 

#### Markdown for user interface
#### Markdown: H1 heading
st.markdown("# Welcome to PyChain")
### Markdown: Sub-heading
st.subheader(" PyChain is a blockchain based ledger system accompanied by a user friendly web interface. The ledger allows users to conduct financial transactions and to verify the integrity of data within the blockchain.")
### Markdown: H1 heading
st.markdown("## Store a Transaction Record in the PyChain")

# Step 3: Add Relevant User Inputs to the Streamlit Interface
## Delete the `input_data` variable from the Streamlit interface.
## input_data = st.text_input("Block Data")

### Add input area to retrieve a value for 'sender' from the user
sender = st.text_input("Sender") 

#### Add input area to retrieve a value for 'receiver' from the user
receiver = st.text_input("Receiver") 

##### Add input area to retrieve value for `amount` from the user
amount = st.text_input("Amount") 

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # Update `new_block` so that `Block` consists of the 'attribute' record
    new_block = Block(
        record=Record(sender, receiver, amount),
        creator_id=42,
        prev_hash=prev_block_hash
    )
    pychain.add_block(new_block)

    # Create a test block and view the nonce and hash
    block = Block("test", 1)
    print(f"The original nonce is: {block.nonce}")
    print(f"The original block hash is: {block.hash_block()}")

    # Update the test block and view the nonce and hash
    block.nonce += 1
    print(f"The new nonce is now: {block.nonce}")
    print(f"The new block hash is now: {block.hash_block()}") 

    # Use `st.write` to display the `block_hash` to the page.
    st.write(f"The block's hash is: {prev_block_hash}")

    # Celebratory snowball (see readme file for demo)
    st.snow()
    # Celebratory balloons (see readme file for demo)
    #st.balloons()

# Markdown
st.markdown("## The PyChain Ledger")

# Pychain dataframe
pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

# PyChain table
st.table(pychain_df)

# Slider: mining difficulty
st.sidebar.write("# Block Difficulty")
difficulty = st.sidebar.slider("Your selection correlates with the computational power requirements for PyChain's consensus algorithm.", min_value=1, max_value=100)
pychain.difficulty = difficulty

# Progress bar increasing over time 
## Insert markdown heading for progress bar
st.sidebar.write("# Progress Bar")
### Instantiate progress bar within sidebar 
progress_bar = st.sidebar.progress(1)
pychain.progress_bar = progress_bar  

### Progress bar: label for range between 1 - 100 
### (Note: Streamlit docs set the 'time.sleep' value to 0.1. I have set a lower value for my implementaiton, as processing times correlate with block difficulty) 
for percent_complete in range(100):
    time.sleep(0.01)  
    progress_bar.progress(percent_complete +1)

# Block selection within sidebar
st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

# Write selected block to pychain_df
st.sidebar.write(selected_block)

# Validate blockchain 
if st.button("Validate PyChain"):
    st.write(pychain.is_valid())

with st.spinner('PyChain is currently validating your transaction. Thank you for your patience.'):
    time.sleep(0)
st.success('Proof of Work (Pow) Verification Outcome: SUCCESS!')