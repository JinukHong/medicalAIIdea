import streamlit as st
import requests
import openai
from streamlit_chat import message
from get_user_data import user_data
import time
from streamlit_extras.streaming_write import write

# Hugging Face API setup
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = st.secrets["secrets"]['API_TOKEN']  # Replace with your actual token
headers = {"Authorization": f"Bearer {API_TOKEN}"}
openai.api_key = st.secrets["secrets"]['OPENAI_API_KEY']

def chatwrite(texttowrite):
    lines = texttowrite.split('\n')
    for line in lines:
        yield line + "\n"
        time.sleep(0.05)

def chatbot():
    # App Header
    st.header("🩺AI 환자에게 질문하세요 ")

    # Session State for Messages
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []
    
    # Function to Query API (you need to replace this with your actual implementation)
    # def query(payload):
    #     response = requests.post(API_URL, headers=headers, json=payload)
    #     return response.json()

    # Form and User Input
    with st.form('form', clear_on_submit=True):
        user_input = st.text_input('"질문하기" 버튼을 눌러 환자에게 질문하세요.', '', key='input', placeholder="질문을 입력하세요")
        submitted = st.form_submit_button('질문하기')

    user_info = user_data()
    system_message = f"너는 환자이고, 나는 의사야. 너는 이 정보를 가진 환자 역할을 해야하고 나의 질문에 적절히 답변해야돼. 환자 정보: {user_info}. 단, 물어보지 않은 질문까지 답하지 마. 물어본 질문에 대해서만 한문장으로 답해."
    # Initial message from the chatbot on first interaction
    if not user_input:
        user_input = "주어진 환자 정보에 기반해서, 너는 환자 역할을 해야돼. 나는 의사고, 너는 환자로서 의사의 질문에 답변해야돼. 먼저 인사하고, 어디가 아파서 왔는지에 대해서만 간단히 한줄로 말해줘."
        pass

    andy_message = "너는 표현력이 풍부한 환자를 연기하도록해. 주어진 환자 데이터를 활용해서 너의 상황을 명확히 인지하고, 주어진 질문에 성실히 답변해줘."\
    "하지만, 이점을 명심해, 물어보지도 않은 정보에 대해 나열하지 말고, 물어본것에 대해서만 대답해. 예를 들어, 어디가 불편해서, 혹은 어디가 아파서 왔는지 물어보면, '일할 때 숨이 차요.' 와 같이, 물어본 바에 대해서만 대답해서 추가적인 질문을 유도해." \
     "그리고 궁금한 점이 있거나 필요한 정보가 있으면 적극적으로 질문해." \
     "명심해, 질문에 담긴 명확한 키워드에 대한 답변만 해. 예를들어 증상이 발현한 구체적인 기간이나 시기를 물었으면, '기간' 과 '시기'에 초점을 맞춰 언제부터 증상이 있었는지 말해줘."\
     "그리고 다음 질문에 대답해."
    
    ending_message = """
     (질문이 영어로 되어 있어도 한글로 대답해. 영어로 답하지 마세요. 물어본 질문에 대해서만 한문장으로 답하세요. 당신은 환자로서 의사의 질문에 답변하고있어요.)
     """
    
    prompt = andy_message + user_input + ending_message
    
    # If User Input is Provided
    if submitted and user_input:
        
        with st.spinner(" "):
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ]
            )
            response = completion.choices[0].message.content
        
        #with st.chat_message("assistant", avatar="https://github.com/JinukHong/shadowFunk/assets/45095330/eceff742-486e-46d8-b501-72efede31c25"):
            # st.write(f"{response}")
            #write(chatwrite(response))
            # st.divider()
            # write(chatwrite(translated_response))

        # Update Session States
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

        # Displaying past interactions and responses
        # for message, resp in zip(st.session_state.past, st.session_state.generated):
        #     st.write(f"You: {message}")
        #     st.write(f"Chatbot: {resp}")

    # Display Past Messages and Responses
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            #st.sidebar.write(f"You: {st.session_state['past'][i]}")
            #st.sidebar.write(f"AI Secretary: {st.session_state['generated'][i]}")
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
chatbot()