import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('random_forest_admission_model.pkl')

st.set_page_config(page_title="Admission Predictor", layout="centered")
st.title("🎓 University Admission Predictor")
st.write("Enter your details below to check if you'd likely be admitted.")

# Input sliders for subject scores
math = st.slider('Math', 0, 100, 70)
english = st.slider('English', 0, 100, 70)
kiswahili = st.slider('Kiswahili', 0, 100, 70)
biology = st.slider('Biology', 0, 100, 70)
chemistry = st.slider('Chemistry', 0, 100, 70)
physics = st.slider('Physics', 0, 100, 70)
history = st.slider('History', 0, 100, 70)
geography = st.slider('Geography', 0, 100, 70)
cre = st.slider('CRE', 0, 100, 70)
business = st.slider('Business', 0, 100, 70)
agriculture = st.slider('Agriculture', 0, 100, 70)

overall_score = st.slider('Overall Score', 0.0, 100.0, 75.0)
cutoff_points = st.slider('Cutoff Points', 0, 100, 70)
university_ranking = st.slider('University Ranking (Lower is Better)', 1, 6, 3)

# Dropdowns for categorical inputs
high_school_type = st.selectbox("High School Type", ['National', 'Extra-County', 'County', 'Private'])
high_school_location = st.selectbox("High School Location", ['Nairobi', 'Kiambu', 'Mombasa', 'Nakuru', 'Kisumu', 'Uasin Gishu'])
program_applied = st.selectbox("Program Applied", ['Medicine', 'Engineering', 'Business', 'Law', 'Computer Science'])
university_received = st.selectbox("University Received", ['UoN', 'JKUAT', 'KU', 'Strathmore', 'Moi', 'Egerton', 'None'])

# Encoding mappings (based on LabelEncoder from training)
type_map = {'National': 2, 'Extra-County': 1, 'County': 0, 'Private': 3}
location_map = {'Nairobi': 4, 'Kiambu': 2, 'Mombasa': 3, 'Nakuru': 5, 'Kisumu': 1, 'Uasin Gishu': 0}
program_map = {'Medicine': 4, 'Engineering': 2, 'Business': 0, 'Law': 3, 'Computer Science': 1}
university_map = {'UoN': 5, 'JKUAT': 1, 'KU': 2, 'Strathmore': 4, 'Moi': 3, 'Egerton': 0, 'None': 6}

# Feature vector
features = np.array([[
    math, english, kiswahili, biology, chemistry, physics,
    history, geography, cre, business, agriculture,
    overall_score, cutoff_points, university_ranking,
    type_map[high_school_type],
    location_map[high_school_location],
    program_map[program_applied],
    university_map[university_received]
]])

# Prediction
if st.button('Predict Admission'):
    try:
        prediction = model.predict(features)
        st.success("✅ Admitted!" if prediction[0] == 1 else "❌ Not Admitted.")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
# Prediction
if st.button('Predict Admission'):
    prediction = model.predict(features)
    st.success("✅ Admitted!" if prediction[0] == 1 else "❌ Not Admitted.")
