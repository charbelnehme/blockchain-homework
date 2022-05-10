# PyChain Ledger

![application-image](https://user-images.githubusercontent.com/95597283/167297226-97e72806-ad26-4b4f-b4bf-a83a0a83d07a.png)

You’re a fintech engineer who’s working at one of the five largest banks in the world. You were recently promoted to act as the lead developer on their decentralized finance team. Your task is to build a blockchain-based ledger system, complete with a user-friendly web interface. This ledger should allow partner banks to conduct financial transactions (that is, to transfer money between senders and receivers) and to verify the integrity of the data in the ledger.

## Project Requirements 

* Create a new data class named Record. This class will serve as the blueprint for the financial transaction records that the blocks of the ledger will store.
* Modify the existing Block data class to store Record data.
* Add Relevant User Inputs to the Streamlit interface.
* Test the PyChain Ledger by Storing Records.

## Language and Tools

* Python 
* Hashlib
* Streamlit 

## User Interface

![Screenshot (15)](https://user-images.githubusercontent.com/95597283/167300917-f40a3274-9b01-496e-9f4d-a0e8f5714594.png)

![Screenshot (17)](https://user-images.githubusercontent.com/95597283/167301201-07aade7f-9b2e-4f1e-8645-6b18a8273ef3.png)

## Streamlit Elements

The following Streamlit elements were provided in the starter code for the web interface:  

```
st.write
st.markdown
st.text
st.dataframe
st.buton
st.sidebar
st.slider 
```

The following additional elements were used in my PyChain solution: 
```
st.progress
st.table
```
In addition, the starter code for the st.slider element was revised in my final submission.

## st.progress

```ruby
st.sidebar.write("# Progress Bar")

progress_bar = st.sidebar.progress(1)
pychain.progress_bar = progress_bar  

for percent_complete in range(100):
    time.sleep(0.01)  
    progress_bar.progress(percent_complete +1)
```

## st.table
```ruby
# PyChain table
st.table(pychain_df)
```

## st.slider
```ruby
# Slider: mining difficulty
st.sidebar.write("# Block Difficulty")
difficulty = st.sidebar.slider("Your selection correlates with the computational power requirements for PyChain's consensus algorithm.", 
                                min_value=1, max_value=100)
pychain.difficulty = difficulty
```

## Transaction Records

![Screenshot (16)](https://user-images.githubusercontent.com/95597283/167300995-3bd7aeb6-1173-46b8-b772-69760653514f.png)

![Screenshot (25)](https://user-images.githubusercontent.com/95597283/167301040-2f981638-2bf6-4b1d-bf8c-57c74d32545c.png)




## Block Difficulty

![Screenshot (28)](https://user-images.githubusercontent.com/95597283/167314328-2fc5a32a-6449-4e87-82cc-8f236cfb5305.png)




## Block Content and Hash Verification




![Screenshot (22)](https://user-images.githubusercontent.com/95597283/167314479-4110e1c2-3f49-4439-8bf1-ec580541aace.png)

![Screenshot (18)](https://user-images.githubusercontent.com/95597283/167314496-0e3e7108-292e-4f64-be19-1d465d4ca6a9.png)

