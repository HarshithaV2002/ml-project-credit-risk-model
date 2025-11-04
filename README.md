# 💳 Credit Risk Score Prediction using Machine Learning
# 🧩 Project Overview
This project predicts an individual's credit risk score using Machine Learning models based on key financial and demographic parameters.
The app takes user inputs (like income, loan details, and credit utilization) and provides the probability of default, an overall credit score, and a rating (e.g., Good / Average / Poor / Excellent).
It also features an interactive Streamlit web interface for real-time prediction and visualization.

# Features
-**Predicts credit default probability, credit score, and rating based on user financial inputs.**
-**Modern Streamlit web UI with a clean white–yellow theme for professional presentation.**
-**Input features include:**
    -**Financial: Income, Loan Amount, Loan Tenure, Loan-to-Income Ratio**
    -**Credit Behavior: Delinquency Ratio, Avg DPD, Credit Utilization Ratio, Open Loan Accounts**
    -**Demographic & Loan Info: Age, Residence Type, Loan Purpose, Loan Type**
-**Trained using multiple ML techniques — Logistic Regression, XGBoost, SMOTETomek for data balancing, and optimized with Optuna and Bayesian Optimization for best model performance.**


## Project Structure
- **frontend – Contains the Streamlit application code and UI components for credit risk prediction.**
- **artifacts – Stores the trained machine learning model,features,and scaler objects saved using Joblib.**
- **requirements.txt – Lists all the required Python packages to run the project.**
- **README.md – Provides an overview, setup instructions, and details about the project.**


# Methodology
1.Data Splitting and Leakage Prevention:
The dataset was first split into training and testing sets to prevent data leakage. All preprocessing steps — such as encoding, scaling, and feature engineering — were fitted only on the training data and then applied to the test data, ensuring no information from the test set influenced model training.

2.Data Preprocessing:
-**Handled missing values and removed redundant or irrelevant columns.**
-**Encoded categorical variables using Weight of Evidence (WoE) for interpretable categorical representation.**
-**Detected and reduced multicollinearity among numerical variables using Variance Inflation Factor (VIF) to retain stable and independent predictors.**
-**Scaled numerical features using MinMaxScaler to normalize feature values and maintain consistent ranges for better model convergence.**

3.Feature Engineering:
Created new informative features such as loan_to_income ratio, credit_utilization_per_income, and other derived metrics to enhance the model’s ability to capture meaningful financial patterns.

4.Handling Class Imbalance:
Applied SMOTETomek to address class imbalance by combining oversampling of the minority class and undersampling of the majority class, improving model robustness and fairness.

5.Model Development and Optimization:
Trained multiple models including Logistic Regression and XGBoost.
Performed hyperparameter tuning using Optuna, GridSearchCV, and Bayesian Optimization to achieve optimal model performance.

6.Evaluation and Explainability:
Evaluated model performance using cross-validation and F1-score (via make_scorer(f1_score)).
Used SHAP (SHapley Additive exPlanations) to interpret feature importance and explain model predictions, enhancing transparency and trustworthiness.



## Demo video
https://drive.google.com/file/d/1QWXAT_D4UxMH9dzg7aCalgOuX6zqZC1M/view?usp=sharing
### *Click the link above to watch the demo video!*

## Tech Stack
- **Frontend: Streamlit**
- **Backend / Model Handling: Python**
- **Machine Learning Libraries: Scikit-learn,Optuna,SMOTETomek**
- **Data Processing: Pandas, NumPy**
- **Model Serialization: Joblib**
- **Visualization: Matplotlib, Seaborn**

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HarshithaV2002/ml-project-credit-risk-model.git
   cd ml-project-credit-risk-model
   ```

1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/main.py

   ```


## Live Demo
You can access the deployed application here:
[**Score Prediction App – Live on Streamlit**](https://ml-project-finance-credit-risk-score-model.streamlit.app/)


## Future Improvement
-**Integrate real-time financial APIs for updated user data**
-**Implement Deep Learning model for further improvement**
-**Automate feature scaling and preprocessing pipeline**
-**Add PDF report generation for user predictions**


## Conclusion
This project demonstrates how Machine Learning can be applied to evaluate and predict an individual’s creditworthiness efficiently.
By combining logistic regression with modern optimization (Optuna), class balancing (SMOTETomek), and model explainability (SHAP), this system provides transparent, data-driven, and interpretable credit scoring insights.
