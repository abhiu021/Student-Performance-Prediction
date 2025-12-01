# # backend/app.py
# import os
# from flask import Flask, request, redirect, url_for
# import pandas as pd
# import joblib

# # Paths
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# MODEL_PATH = os.path.join(BASE_DIR, "models", "ridge_pipeline.joblib")
# FRONTEND_HTML = os.path.join(BASE_DIR, "frontend", "index.html")

# # Load model (sklearn Pipeline that includes preprocessing)
# if not os.path.exists(MODEL_PATH):
#     raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Place ridge_pipeline.joblib in models/")

# model = joblib.load(MODEL_PATH)

# app = Flask(__name__, static_folder=os.path.join(BASE_DIR, "frontend"), template_folder=None)

# def normalize_str(s):
#     if s is None:
#         return s
#     return str(s).strip().title()

# @app.route("/", methods=["GET"])
# def home():
#     # Serve the static HTML file
#     with open(FRONTEND_HTML, "r", encoding="utf-8") as f:
#         return f.read()

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         # Collect form data (ensure keys match your frontend form names)
#         data = {
#             "age": [int(request.form.get("age", 18))],
#             "gender": [normalize_str(request.form.get("gender"))],
#             "study_hours_per_day": [float(request.form.get("study_hours_per_day", 0.0))],
#             "social_media_hours": [float(request.form.get("social_media_hours", 0.0))],
#             "part_time_job": [normalize_str(request.form.get("part_time_job"))],
#             "attendance_percentage": [float(request.form.get("attendance_percentage", 0.0))],
#             "sleep_hours": [float(request.form.get("sleep_hours", 0.0))],
#             "diet_quality": [normalize_str(request.form.get("diet_quality"))],
#             "exercise_frequency": [int(request.form.get("exercise_frequency", 0))],
#             "parental_education_level": [normalize_str(request.form.get("parental_education_level"))],
#             "internet_Resource_accessibility": [normalize_str(request.form.get("internet_Resource_accessibility"))],
#             "extracurricular_participation": [normalize_str(request.form.get("extracurricular_participation"))]
#         }

#         # Create DataFrame and predict
#         input_df = pd.DataFrame(data)
#         prediction = model.predict(input_df)[0]
#         prediction = round(float(prediction), 2)

#         # Return a small HTML with result and a back link
#         return f"""
#         <html><body style="font-family:Arial;padding:20px;">
#           <h2>Predicted Exam Score: <span style="color:green">{prediction}</span></h2>
#           <p><a href="/">Back to form</a></p>
#         </body></html>
#         """
#     except Exception as e:
#         # Return error message (simple)
#         return f"<h3>Error: {str(e)}</h3><p><a href='/'>Back</a></p>"
    
# if __name__ == "__main__":
#     # Dev server
#     app.run(host="127.0.0.1", port=5000, debug=True)
# backend/app.py

import os
from flask import Flask, request, send_from_directory
import pandas as pd
import joblib

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
MODEL_PATH = os.path.join(BASE_DIR, "models", "ridge_pipeline.joblib")

# Check model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

# Serve static files from /frontend
app = Flask(__name__, static_folder=FRONTEND_DIR, template_folder=None)


def normalize_str(s):
    if s is None:
        return s
    return str(s).strip().title()


# --------------------------
#  Serve Frontend Files
# --------------------------
@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:filename>")
def frontend_static(filename):
    return send_from_directory(FRONTEND_DIR, filename)


# --------------------------
#  Prediction API
# --------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = {
            "age": [int(request.form.get("age", 18))],
            "gender": [normalize_str(request.form.get("gender"))],
            "study_hours_per_day": [float(request.form.get("study_hours_per_day", 0.0))],
            "social_media_hours": [float(request.form.get("social_media_hours", 0.0))],
            "part_time_job": [normalize_str(request.form.get("part_time_job"))],
            "attendance_percentage": [float(request.form.get("attendance_percentage", 0.0))],
            "sleep_hours": [float(request.form.get("sleep_hours", 0.0))],
            "diet_quality": [normalize_str(request.form.get("diet_quality"))],
            "exercise_frequency": [int(request.form.get("exercise_frequency", 0))],
            "parental_education_level": [normalize_str(request.form.get("parental_education_level"))],
            "internet_Resource_accessibility": [normalize_str(request.form.get("internet_Resource_accessibility"))],
            "extracurricular_participation": [normalize_str(request.form.get("extracurricular_participation"))]
        }

        df = pd.DataFrame(data)
        raw_pred = float(model.predict(df)[0])
        clamped_pred = max(0, min(100, raw_pred))
        prediction = round(clamped_pred, 2)


        return f"""
        <html><body style='font-family:Arial;padding:20px;'>
            <h2>Predicted Exam Score: 
                <span style='color:green'>{prediction}</span>
            </h2>
            <p><a href='/'>Back to Form</a></p>
        </body></html>
        """

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3><p><a href='/'>Back</a></p>"


# --------------------------
# Run Dev Server
# --------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
