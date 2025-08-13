import streamlit as st
import pickle
import json
import pandas as pd
import numpy as np

with open('./src/model.pkl', 'rb') as file_1:
  model = pickle.load(file_1)

with open('./src/model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('./src/model_encoder.pkl', 'rb') as file_3:
  model_encoder = pickle.load(file_3)

def run():
  # Pembuatan form
  with st.form(key='prediksi-nilai-akhir-siswa'):
    school = st.selectbox('School', ['Gabriel Pereira', 'Mousinho da Silveira'], index=2)
    sex = st.selectbox('Sex', ['Female', 'Male'], index=2)
    age = st.number_input('Age', min_value=15, max_value=22, value=18, step=1, help='Usia Siswa')
    address = st.selectbox('Address', ['Urban', 'Rural'], index=2)
    st.markdown('---')

    famsize = st.selectbox('Family Size', ['Less or equal to 3', 'Greather than 3'], index=2)
    Pstatus = st.selectbox('Parent Status', ['Living together', 'Apart'], index=2)
    medu = st.number_input('Mother Education Level', min_value=0, max_value=4, value=2, step=1, help='0: None, 1: Primary education (4th grade), 2: 5th to 9th grade, 3: Secondary education (12th grade), 4: Higher education')
    fedu = st.number_input('Father Education Level', min_value=0, max_value=4, value=2, step=1, help='0: None, 1: Primary education (4th grade), 2: 5th to 9th grade, 3: Secondary education (12th grade), 4: Higher education')
    mjob = st.selectbox('Mother Job', ['Teacher', 'Health care', 'Services', 'At home', 'Other'], index=2)
    fjob = st.selectbox('Father Job', ['Teacher', 'Health care', 'Services', 'At home', 'Other'], index=2)
    st.markdown('---')

    reason = st.selectbox('Reason for School', ['Home', 'Reputation', 'Course',], index=2)
    guardian = st.selectbox('Guardian', ['Mother', 'Father', 'Other'], index=2)
    traveltime = st.number_input('Travel Time to School', min_value=1, max_value=4, value=2, step=1, help='1: <15 min, 2: 15 to 30 min, 3: 30 min to 1 hour, 4: >1 hour')
    studytime = st.number_input('Study Time', min_value=1, max_value=4, value=2, step=1, help='1: <2 hours, 2: 2 to 5 hours, 3: 5 to 10 hours, 4: >10 hours')
    failures = st.number_input('Number of Past Class Failures', min_value=0, max_value=3, value=0, step=1)
    st.markdown('---')

    schoolsup = st.selectbox('Extra Educational Support', ['Yes', 'No'], index=2)
    famsup = st.selectbox('Family Educational Support', ['Yes', 'No'], index=2)
    paid = st.selectbox('Extra Paid Classes', ['Yes', 'No'], index=2)
    activities = st.selectbox('Extra Curricular Activities', ['Yes', 'No'], index=2)
    nursery = st.selectbox('Attended Nursery School', ['Yes', 'No'], index=2)
    higher = st.selectbox('Wants Higher Education', ['Yes', 'No'], index=2)
    st.markdown('---')

    internet = st.selectbox('Internet Access at Home', ['Yes', 'No'], index=2)
    romantic = st.selectbox('In a Romantic Relationship', ['Yes', 'No'], index=2)
    famrel = st.number_input('Family Relationship Quality', min_value=1, max_value=5, value=3, step=1, help='from 1 - very bad to 5 - excellent')
    freetime = st.number_input('Free Time After School', min_value=1, max_value=5, value=3, step=1, help='from 1 - very low to 5 - very high')
    goout = st.number_input('Going Out with Friends', min_value=1, max_value=5, value=3, step=1, help='from 1 - very low to 5 - very high')
    Dalc = st.number_input('Workday Alcohol Consumption', min_value=1, max_value=5, value=3, step=1, help='from 1 - very low to 5 - very high')
    Walc = st.number_input('Weekend Alcohol Consumption', min_value=1, max_value=5, value=3, step=1, help='from 1 - very low to 5 - very high')
    health = st.number_input('Health Status', min_value=1, max_value=5, value=3, step=1, help='from 1 - very bad to 5 - very good')
    st.markdown('---')

    absences = st.number_input('Number of School Absences', min_value=0, max_value=93, value=0, step=1, help='Number of school absences')
    G1 = st.number_input('First Period Grade', min_value=0, max_value=20, value=10, step=1, help='First period grade (0-20)')
    G2 = st.number_input('Second Period Grade', min_value=0, max_value=20, value=10, step=1, help='Second period grade (0-20)')

    submitted = st.form_submit_button('Predict')

    data_inf = {
        'school': ['GP'],
        'sex': ['F'],
        'age': [16],
        'address': ['U'],
        'famsize': ['GT3'],
        'Pstatus': ['T'],
        'Medu': [4],
        'Fedu': [3],
        'Mjob': ['teacher'],
        'Fjob': ['other'],
        'reason': ['home'],
        'guardian': ['mother'],
        'traveltime': [1],
        'studytime': [2],
        'failures': [0],
        'schoolsup': ['yes'],
        'famsup': ['no'],
        'paid': ['no'],
        'activities': ['yes'],
        'nursery': ['yes'],
        'higher': ['yes'],
        'internet': ['yes'],
        'romantic': ['no'],
        'famrel': [4],
        'freetime': [3],
        'goout': [3],
        'Dalc': [1],
        'Walc': [1],
        'health': [5],
        'absences': [0],
        'G1': [15],
        'G2': [14]
        }
    
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
    # Split between numerical columns and categorical columns

        # Define numerical and categorical columns
        list_num_cols = [
            'age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures',
            'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2'
        ]
        list_cat_cols = [
            'school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
            'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
            'nursery', 'higher', 'internet', 'romantic'
        ]

        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # Feature Scaling and Feature Encoding
        ## Feature Scaling
        data_inf_num_scaled = model_scaler.transform(data_inf_num)

        ## Feature Encoding
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat)

        ## Concate
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)
        

        # Predict using Linear Regression

        y_pred_inf = model.predict(data_inf_final)
        st.write('# Nilai Akhir : ', str(int(y_pred_inf)))

if __name__ == '__main__':
    run()


    