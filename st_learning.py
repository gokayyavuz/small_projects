import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

st.title('Super Simple Title')
st.header('Header')
st.subheader('Subheader')
st.markdown("Hello _Name_")
st.caption('Caption')
code_example = """
def greet(name):
    print('Hello', name)
"""
st.code(code_example)
st.divider()

st.image(os.path.join(os.getcwd(),"static", "ssj4.png"))

st.divider()
st.title("Streamlit Element Demo")

st.subheader('Dataframe')
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 37, 45],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Chef']
})
st.dataframe(df)

st.subheader('Editable Dataframe')
editable_df = st.data_editor(df)

st.subheader('Static Table')
st.table(df)

st.subheader('Metrics')
st.metric(label='Total rows', value=len(df))
st.metric(label='Age', value=round(df['Age'].mean(), 2))

st.divider()

st.title('Streamlit Chart Demo')

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A', 'B', 'C']
)

st.subheader('Area Chart')
st.area_chart(chart_data)

st.subheader('Bar chart')
st.bar_chart(chart_data)

st.subheader('Line chart')
st.line_chart(chart_data)

st.subheader('Scatter chart')
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y' : np.random.randn(100)
})
st.scatter_chart(scatter_data)

st.subheader('Pyplot Chart')
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.legend()
st.pyplot(fig)

st.divider()

st.title('Form Demo')

with st.form(key='sample_form'):

    st.subheader('Text input')
    name = st.text_input('Enter your name')
    feedback = st.text_area('Provide feedback')

    st.subheader('Date and time inputs')
    dob = st.date_input("Select your birthday")
    time = st.time_input("Select time")

    st.subheader('Selectors')
    choice = st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
    gender = st.selectbox('Select your gender', ['male', 'female'])
    silder_value = st.select_slider("Select a range", options=[1,2,3,4,5])

    st.subheader('Toggles and Checkboxes')
    notifications = st.checkbox('Receive notifications?')
    toggle_value = st.checkbox("Enable darkmode?", value=False)

    st.form_submit_button()

st.divider()

st.title('User Information form')

form_values = {
    'name': None,
    'height': None,
    'gender': None,
    'dob': None
}

min_date = datetime(1900,1,1)
max_date = datetime.now()

st.caption('In this form we want to collect data of our users.')

with st.form(key='user_info_form'):
    form_values['name'] = st.text_input('Enter your name: ')
    form_values['height'] = st.number_input('Enter your height (cm): ', 0)
    form_values['gender'] = st.selectbox("Gender", ['Male', 'Female'])
    form_values['dob'] = st.date_input('Enter your birthday', max_value = max_date, min_value=min_date)
    
    print(form_values['name'], form_values['height'], form_values['gender'], form_values['dob'])

    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        if not all(form_values.values()):
            st.warning('Please enter all information')
        else:
            st.balloons()
            st.write('Congrats you submitted your form')
            for key, values in form_values.items():
                st.write(f"{key} : {values}")