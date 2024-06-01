# News Headline Classification with Statistical Machine Learning

This project focuses on categorizing news headlines into six categories using a statistical machine learning approach. The dataset consists of 3000 headlines evenly distributed across six categories: Politics, Economy, Sports, Current Affairs, Health, and Technology.

## Project Structure

- **Data**: The dataset contains 500 headlines for each of the six categories. The data has been cleaned, with stop words and numbers removed.
- **Model**: A Random Forest classifier is used.
- **Evaluation**: Cross-validation is employed to test the model, achieving a precision of 0.70 and an accuracy of 0.61.

## Requirements

To set up the environment, the following packages need to be installed:

- `requirements`
- `chardet`
- `gensim`
- `openpyxl`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/eraybuyukkanat/nlp_news_classification.git
   cd your-repo

2. Install the necessary packages:

   ```sh
    pip install -r requirements.txt
    ```

    ```sh
    pip install chardet
    ```

    ```sh
    pip install gensim
    ```

    ```sh
    pip install openpyxl
    ```

## Usage

1. Ensure your dataset is properly formatted and placed in the appropriate directory.
2. Open and run the Jupyter Notebook to train and evaluate the model:

    ```sh
    jupyter notebook classification.ipynb
    ```

## Results
The model achieves the following performance metrics:

Precision: 0.70
Accuracy: 0.61

<sub>## License

This project is licensed under the MIT License - see the <a href="LICENSE.txt">LICENSE</a> file for details.</sub>