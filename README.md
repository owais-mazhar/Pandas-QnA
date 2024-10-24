# Pandas QnA

## Overview

This project is a Streamlit application that allows users to upload a CSV file and perform queries on the dataset using a Pandas Query Engine. Users can enter queries about the dataset, and the app will execute relevant Pandas instructions, displaying descriptive statistics or visualizations as appropriate.

## Features

- Upload CSV files to explore datasets.
- Enter queries to analyze the data.
- Automatically executes relevant Pandas commands and displays results.
- Visualize data through various plotting methods.
- Descriptive statistics provided for datasets.

## Requirements

To run this application, you will need:

- Python 3.6 or higher
- Streamlit
- Pandas
- Matplotlib
- llama-index (or any necessary library for the PandasQueryEngine)
- python-dotenv (for managing environment variables)

You can install the required packages using pip:

```bash
pip install streamlit pandas matplotlib llama-index python-dotenv
```

## Environment Variables

This app requires a Google API key for certain functionalities. You should create a `.env` file in the project root directory with the following content:

```
GOOGLE_KEY=your_google_api_key
```

Replace `your_google_api_key` with your actual Google API key.

## Running the App

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/owais-mazhar/Pandas-QnA.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pandas-query-engine-streamlit
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   (Replace `app.py` with the name of your main Python file if different.)

4. Open your web browser and go to `http://localhost:8501` to access the app.

## Usage

1. Upload a CSV file using the file uploader.
2. Enter a query about the dataset in the text input box.
3. The app will execute the query and display results, including descriptive statistics and visualizations.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Streamlit for creating an easy-to-use interface for data applications.
- Pandas for powerful data manipulation and analysis.