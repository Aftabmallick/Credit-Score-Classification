# Credit Score Classification

## Project Overview

This project focuses on building a machine learning model to classify credit scores using the dataset from Kaggle [Credit Score Classification](https://www.kaggle.com/datasets/parisrohan/credit-score-classification). The end-to-end process includes data preprocessing, model training, evaluation, and deployment using a Flask server for real-time predictions with a frontend interface.

## Repository

The project repository can be found at: [Credit-Score-Classification](https://github.com/Aftabmallick/Credit-Score-Classification.git)

## Project Structure

- **data/**: Contains the dataset.
- **server/artifacts/**: Contains trained models.
- **server/**: Flask application for real-time prediction.
- **frontend/**: Contains the frontend code for user interaction.
- **requirements.txt**: Python dependencies required to run the project.
- **README.md**: Project documentation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aftabmallick/Credit-Score-Classification.git
   cd Credit-Score-Classification
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Dataset

The dataset used for this project is from Kaggle: [Credit Score Classification](https://www.kaggle.com/datasets/parisrohan/credit-score-classification). Download the dataset and place it in the `data/` directory.

## Models Used

The following machine learning models from `scikit-learn` and `xgboost` were used for classification:

- Logistic Regression
- K-Neighbors Classifier
- Decision Tree
- Random Forest Classifier
- XGBClassifier
- AdaBoost Classifier
- Gradient Boosting Classifier
- Support Vector Classifier

## Model Evaluation

The models were evaluated using the following metrics from `sklearn.metrics`:

- Accuracy
- Precision
- Recall
- F1 Score

The best model found was `XGBClassifier` with an accuracy of 80%.

## Deployment

The model was saved and deployed using a Flask server to enable real-time prediction. The frontend was created to provide a user interface for making predictions.

### Running the Flask Server

1. Navigate to the `server/` directory:
   ```bash
   cd server
   ```

2. Run the Flask server:
   ```bash
   flask run
   ```

### Frontend

The frontend code is located in the `frontend/` directory and interacts with the Flask server for real-time predictions.

## Usage

1. Start the Flask server as described above.
2. Open the frontend in a web browser.
3. Input the necessary features and get the credit score prediction in real-time.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

