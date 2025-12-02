# Student Performance Prediction System

## 1. Project Overview
This project predicts a student's exam score (0–100) using machine learning techniques.  
The system analyzes different academic, lifestyle, and demographic factors to estimate the final exam performance of a student.

The project includes:
- Data cleaning and preprocessing  
- Training multiple ML models  
- Comparing model performances  
- Selecting and deploying the best model (Lasso Regression)  
- Building a complete web application (HTML/CSS + Flask backend)

---

## 2. Dataset Description
The dataset contains the following input features:

- Age  
- Gender  
- Study hours per day  
- Social media hours per day  
- Part-time job (Yes/No)  
- Attendance percentage  
- Sleep hours  
- Diet quality  
- Exercise frequency  
- Parental education level  
- Internet resource accessibility  
- Extracurricular participation (Yes/No)

**Target variable:**  
- `exam_score` (0–100)

---

## 3. Methodology

### Step 1 — Data Preprocessing
- Converted and cleaned text fields  
- Scaled numerical columns using StandardScaler  
- Encoded categorical columns using OneHotEncoder  
- Train/test split of 80/20  

### Step 2 — Model Training
The following models were trained:

- Lasso Regression  
- Ridge Regression  
- Random Forest Regressor  
- XGBoost Regressor  
- Neural Network  

### Step 3 — Model Evaluation
Models were evaluated using:
- Mean Absolute Error (MAE)  
- RMSE  
- R² Score  

**Lasso Regression** achieved the best results with stable performance and good generalization.  
Hence, it was selected as the final model for deployment.

---

## 4. System Architecture

### Model
- Saved as: `lasso_pipeline.joblib`  
- Includes preprocessing + trained model in a single pipeline

### Backend (Flask)
- Loads the saved model  
- Receives form input from frontend  
- Predicts exam score  
- Ensures the output remains between 0 and 100  
- Returns result to UI

### Frontend (HTML/CSS)
- Clean input form  
- Sends form data to `/predict`  
- Displays predicted exam score

### Project Structure

student-performance-app/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ └── style.css
│
├── models/
│ └── lasso_pipeline.joblib
│
└── README.md


---

## 5. How to Run the Project

### 1. Clone the Repository
git clone https://github.com/your-username/student-performance-app.git

git clone https://github.com/your-username/student-performance-app.git

python -m venv venv

venv\Scripts\activate


### 3. Install Dependencies
pip install -r backend/requirements.txt


### 4. Run the Flask Backend
python backend/app.py


---

## 6. Team Members  
(Add your names below)

1. Mehul Goyal (2023ucp1603) 
2. Dev Patel   (2023ucp1127)
3. Parineeta Soni (2023ucp1795)
4. Abhinav Ukharde (2023ucp1808)

---

## 7. Submitted To  
**Professor Dr. Vikas Kumar**  
Course Project: **Software Engineering**
