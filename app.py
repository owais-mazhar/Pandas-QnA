import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from llama_index.experimental.query_engine.pandas import PandasQueryEngine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["GOOGLE_KEY"] = os.getenv("GOOGLE_KEY")

# Streamlit app
st.title("Pandas Query Engine with Streamlit")

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Load the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("Dataset loaded successfully:")
    st.write(df.head())  # Display the first few rows of the dataset

    # Create a text input for user queries
    query = st.text_input("Enter your query about the dataset")

    if query:
        # Initialize the query engine
        query_engine = PandasQueryEngine(df=df, verbose=True)

        # Query the dataset
        response = query_engine.query(query)

        # Check if the response contains a pandas instruction
        pandas_instruction = response.metadata.get('pandas_instruction_str')

        if pandas_instruction:
            st.write("Executing Pandas Instruction:")
            st.code(pandas_instruction, language='python')

            # Handle specific instructions
            if pandas_instruction == "df.describe()":
                # Execute the describe method and display the result
                stats = df.describe()
                st.write("Descriptive Statistics:")
                st.dataframe(stats)  # Display the stats in a nice table format
            else:
                # Handle plotting instructions
                try:
                    # Execute the plotting code
                    exec(pandas_instruction)

                    # Display the plot in Streamlit
                    st.pyplot(plt.gcf())
                except Exception as e:
                    st.error(f"Error executing pandas instruction: {e}")
        else:
            # Display raw response if no instruction found
            st.write("Query result:")
            st.write(response)
else:
    st.write("Please upload a CSV file to proceed.")
