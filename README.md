# Credit-Scoring-Model

This repository contains a project focused on predicting the default for the next month. The project includes a machine learning model, a Python script used to train the model, and a Streamlit app for user interaction.
## Files in the Repository

1. **`model.pkl`**:
   - Contains the trained classification model for predicting credit payment defaults based on customer data.

2. **`credit_app(1).py`**:
   - This script is responsible for data preprocessing, training the classification model, and saving it to `model.pkl`.

3. **`streamlit_app.py`**:
   - This file contains the Streamlit web app that allows users to input customer data and receive predictions on whether they will default on the next month's payment.

## How to Run the Project

1.Clone this repository:
   ```bash
   git clone https://github.com/omarelnabawi/Credit-Scoring-Model/tree/main
   ```

2.Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3.Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
4.Open the app in your browser and input customer data to get predictions on credit payment default.

## How to Run the Project
The model uses the following transaction-related features for prediction:

   - `Time`: The time elapsed between the transaction and the first transaction in the dataset.
   - `V1, V2, V3, ..., V28`: Anonymized transaction features (PCA-transformed).
   - `Amount`: The transaction amount.
- `Class`: The target variable indicating whether the transaction is fraudulent (1) or not (0).
## Project Overview
This project uses customer transaction data to detect fraudulent activities. The model is trained using features related to transaction details, such as the amount, anonymized features, and time. Class imbalance is handled using SMOTE (Synthetic Minority Over-sampling Technique) to ensure balanced training.
## Key Steps in the Project:
1.**`Data Preprocessing`**:
- Clean and prepare the data for training.
- Handle the class imbalance in the `Class` column using SMOTE to oversample the minority class.
  
2.**`Model Training`**:
- A classification algorithm (e.g., RandomForest) is applied to the preprocessed data.
- The training process is carried out in the `credit_app(1).py`script.
  
3.**`Model Deployment`**:
- The trained model is saved as `model.pkl` and deployed through a Streamlit web app for real-time predictions.
  
## Future Enhancements
- Further explore feature engineering techniques to improve model performance.
- Experiment with different machine learning algorithms to enhance prediction accuracy.
- `Balance the target class`: Use techniques like SMOTE, oversampling, or undersampling to ensure fair learning for imbalanced classes in the `Class` column.
- Implement a feedback loop for continuous model improvement based on newly available data.
## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. Please ensure your contributions align with the goals of the project.
```vbnet
This README is now aligned with your dataset, emphasizing the handling of class imbalance for the `Class` column (fraud detection).
```
  

