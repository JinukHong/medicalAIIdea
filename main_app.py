import streamlit as st
#from web_demo2 import show_financial_advisor  # Importing the function
from survey import save_results, show_survey, questions
from chatbot import chatbot
from theme import toggle


# Dummy admin credentials for the example
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def is_admin(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([6,1])

    with col1:
        if st.button("Login"):
            if is_admin(username, password):
                st.session_state["user_type"] = "admin"
                st.experimental_rerun()
            else:
                st.session_state["user_type"] = "user"
                st.experimental_rerun()

    with col2:
        if st.button("문제풀기"):
            st.session_state["user_type"] = "user"
            st.experimental_rerun()

    return False  # User not logged in yet

def main():
    if 'user_type' not in st.session_state:
        st.session_state['user_type'] = None

    # Check user type and proceed accordingly
    if st.session_state['user_type'] is None:
        login_page()
    elif st.session_state['user_type'] == "admin":
        # Admin view - show the survey page
        handle_survey()
    else:
        # User view - go directly to the chatbot
        chatbot()

def handle_survey():
    # Initialize survey state
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'show_submit_button' not in st.session_state:
        st.session_state.show_submit_button = False

    # Survey logic
    if st.session_state.submitted:
        save_results()
        chatbot()
    elif st.session_state.show_submit_button:
        st.write("모든 질문에 답하셨습니다.")
        st.write("결과를 보시려면 '제출' 버튼을 누르세요.")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("제출"):
                st.session_state.submitted = True
        with col2:
            if st.button("이전 질문으로 돌아가기"):
                st.session_state.show_submit_button = False
                st.session_state.current_question = len(questions) - 1  
    else:
        show_survey()
        if st.button("Skip"):
            st.session_state.current_question = len(questions) - 1
            st.session_state.show_submit_button = True
            st.experimental_rerun()
    
if __name__ == "__main__":
    with st.sidebar:
        toggle()
    main()
    hide_footer_style = """
    <style>
    #MainMenu {visibility: hidden;} 
    div.block-container {padding-top:1rem;}
    div.block-container {padding-bottom:3rem;}
    }
    </style>
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    hide_elements_style = """
    <style>
    #MainMenu {visibility: hidden;} 
    div.block-container {padding-top:1rem;}
    div.block-container {padding-bottom:3rem;}
    .streamlit-footer {display: none;} /* This hides the entire footer */
    /* Add a selector for the GitHub logo specifically if you only want to hide the logo */
    </style>
    """
    st.markdown(hide_elements_style, unsafe_allow_html=True)


    footer_setup = '''
    <script>
    setTimeout(function(){
        const streamlitDoc = window.parent.document;
        const footer = streamlitDoc.getElementsByTagName("footer")[0];
        if (footer) {
            footer.innerHTML = `
                Provided by 
                <a target="_blank" class="css-z3au9t egzxvld2">Team 미래의료연구소</a>
            `;
        }
    }, 1000);  // Adjust the timeout as needed
    </script>
    '''
    st.components.v1.html(footer_setup)

