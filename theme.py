import streamlit as st

# Define the CSS styles for dark and light themes
def toggle():
    dark = '''
    <style>
        .stApp {
        background-color: black;
        color: white;
        }
    </style>
    '''

    light = '''
    <style>
        .stApp {
        background-color: white;
        color: black;
        }
    </style>
    '''
    

    # Create a checkbox to act as a toggle for the theme
    toggle = st.toggle("테마 변경", value=False)


    # Use a session state variable to store the current theme
    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    # Change the theme based on the checkbox state
    if toggle:
        st.session_state.theme = "dark"
    else:
        st.session_state.theme = "light"

    # Apply the chosen theme to the app
    if st.session_state.theme == "dark":
        st.markdown(dark, unsafe_allow_html=True)
    else:
        st.markdown(light, unsafe_allow_html=True)
