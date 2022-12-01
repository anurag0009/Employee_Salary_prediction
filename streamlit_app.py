import streamlit as st
import numpy as np
import pandas as pd
import pickle 

load_model = pickle.load(open("xgboost.pkl","rb"))

def make_prediction(jobType,major,degree,industry,yearsExperience,milesFromMetropolis):
    if jobType == 'CEO':
        jobType = 0
    elif jobType == 'VICE_PRESIDENT':
        jobType = 1
    elif jobType == "MANAGER":
        jobType = 2
    elif jobType == "CFO":
        jobType = 3
    elif jobType == "JUNIOR":
        jobType = 4
    elif jobType == 'JANITOR':
        jobType = 5
    elif jobType == 'CTO':
        jobType = 6
    elif jobType == "SENIOR":
        jobType = 7


    if major == 'NONE':
        major = 0
    elif major == 'PHYSICS':
        major = 1
    elif major == 'CHEMISTRY':
        major = 2
    elif major == 'COMPSCI':
        major = 3
    elif major == 'MATH':
        major = 4
    elif major == 'BIOLOGY':
        major = 5
    elif major == 'LITERATURE':
        major = 6
    elif major == 'BUSINESS':
        major = 7
    elif major == 'ENGINEERING':
        major = 8

    if degree == 'HIGH SCHOOL':
        degree = 0
    elif degree == 'DOCTORAL':
        degree = 1
    elif degree == 'BACHELORS':
        degree = 2
    elif degree == 'NONE':
        degree = 3
    elif degree  == 'MASTERS':
        degree = 4

    if industry == 'WEB':
        industry = 0
    elif industry == 'HEALTH':
        industry = 1
    elif industry == 'AUTO':
        industry = 2
    elif industry == 'FINANCE':
        industry = 3
    elif industry == 'EDUCATION':
        industry = 4
    elif industry == 'OIL':
        industry = 5
    elif industry == 'SERVICE':
        industry= 6 
    
    prediction = load_model.predict([[jobType,major,degree,industry,yearsExperience,milesFromMetropolis]])
    print(prediction)
    return prediction


def main():
    st.title("Employee Salary prediction")
    st.write("Enter the Employee Information")

    jobType=st.selectbox("jobType",['CEO', 'VICE_PRESIDENT', 'MANAGER', 'CFO', 'JUNIOR', 'JANITOR','CTO', 'SENIOR'])
    major=st.selectbox("Major Courses",['NONE', 'PHYSICS', 'CHEMISTRY', 'COMPSCI', 'MATH', 'BIOLOGY','LITERATURE', 'BUSINESS', 'ENGINEERING'])
    degree=st.selectbox("Degree",['HIGH_SCHOOL', 'DOCTORAL', 'BACHELORS', 'NONE', 'MASTERS'])
    industry=st.selectbox("Industry",['WEB', 'HEALTH', 'AUTO', 'FINANCE', 'EDUCATION', 'OIL', 'SERVICE'])
    yearsExperience=st.text_input("YearsExperience")
    milesFromMetropolis=st.text_input("milesFromMetropolic")


    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = make_prediction(jobType,major,degree,industry,yearsExperience,milesFromMetropolis)
        st.success('Your loan is {}'.format(result))








if __name__ == '__main__':
    main()