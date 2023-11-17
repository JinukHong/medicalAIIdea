import streamlit as st
import requests
import openai
from streamlit_chat import message
from get_user_data import user_data
import time
from streamlit_extras.streaming_write import write
import random

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
    



    # Define your lists of links
    image_links = [
        "https://drive.google.com/file/d/1hpQ7C8qHiFHFAz8vlD5zY7vTSSQvq2dn/view?usp=sharing",
        "https://drive.google.com/file/d/1mbP_BJM_9cLB975biDhMO4umxo6yx67I/view?usp=sharing"
    ]

    audio_links = [
        "https://drive.google.com/file/d/1KYIDh4EpsCn6CUkkpsNJNfUteqtIG9M6/view?usp=sharing",
        "https://drive.google.com/file/d/1KY89aAMgVX_77m7T9OTA42j_goWNOR5Y/view?usp=sharing"
    ]

    def convert_drive_link(link, media_type='image'):
        file_id = link.split('/')[-2]
        if media_type == 'image':
            return f'https://drive.google.com/uc?export=view&id={file_id}'
        elif media_type == 'audio':
            return f'https://drive.google.com/uc?export=download&id={file_id}'

    def provide_feedback():
        feedback = "총 점은 75/100 점 입니다. 과거 병력 및 가족력, 흡연/음주 습관에 대한 질문이 포함되면 좋을 것 같습니다."
        return feedback




    qna_mapping = {
    "안녕하세요": "네 안녕하세요.",
    "불편": "일할 때 자꾸 숨이 차요.",
    "언제부터": "3개월 전부터 증상이 있었어요.",
    "상황": "운동하면서 그런 증상을 느꼈어요.",
    "증상이 갑자기": "서서히 나타났어요.",
    "나타나면": "30분 이상 지속되는것같아요",
    "몇 번": "계단 오를 때마다 느껴요.",
    "몇번": "계단 오를 때마다 느껴요.",
    "점점": "네, 심해지고 있어요",
    "이전에도": "네 있었습니다.",
    "어떻게 숨이 차시나요": "기침이 나면서 숨이 차요.",
    "내쉬는": "숨을 마실 때 더 힘들어요.",
    "증상이 어느 정도로 심한가요": "평지를 걸으면 동년배보다 느려요.",
    "다른 증상": "흰색 가래가 나와요.",
    "최근 감기에": "아니오.",
    "감기에 자주": "아니오, 그건 아니에요.",
    "호흡곤란의 양상이": "아니오.",
    "증상이 좋아지나요": "쉬면 조금 나아져요.",
    "찍은 적이": "아니오.",
    "최근에 다친": "아니오.",
    "입원": "아니오.",
    "수술": "아니오.",
    "진단 받은 적이": "아니오 없습니다.",
    "심부전이나 기타 심장병이": "아니오 없습니다.",
    "고혈압": "아니오 없습니다.",
    "당뇨": "아니오 없습니다.",
    "간질환": "아니오 없습니다.",
    "현재 복용하시는": "아니오",
    "흡연": "하루에 1갑, 25년",
    "음주": "1-2회, 소주 2-3잔",
    "직업": "인테리어일을 하고있어요",
    "스트레스나 근무 환경이": "아니오",
    "기족 중에": "아니오",
    "임신 가능성이": "아니오",
    "엑스레이":"https://drive.google.com/file/d/1hpQ7C8qHiFHFAz8vlD5zY7vTSSQvq2dn/view?usp=sharing",
    "xray":"https://drive.google.com/file/d/1mbP_BJM_9cLB975biDhMO4umxo6yx67I/view?usp=sharing",
    "청진":"https://drive.google.com/file/d/1KYIDh4EpsCn6CUkkpsNJNfUteqtIG9M6/view?usp=sharing",
    "흉부청진":"https://drive.google.com/file/d/1KY89aAMgVX_77m7T9OTA42j_goWNOR5Y/view?usp=sharing",
}

    # App Header
    st.write("[Medi Solve]")
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
        # # Form and User Input


    with st.form('form', clear_on_submit=True):
        user_input = st.text_input('"질문하기" 버튼을 눌러 환자에게 질문하세요.', '', key='input', placeholder="질문을 입력하세요")
        submitted = st.form_submit_button('질문하기')

    # cols = st.columns([1, 1])

    # # Create nested columns in the second main column for the '흉부 xray 이미지 확인' button
    # with cols[0]:
    #     if st.button('흉부 xray 이미지 확인'):
    #         chosen_link = random.choice(image_links)
    #         direct_link = convert_drive_link(chosen_link, media_type='image')
    #         st.image(direct_link)
    # with cols[1]:
    #     if st.button('흉부 청진음 확인'):
    #         chosen_link = random.choice(audio_links)
    #         direct_link = convert_drive_link(chosen_link, media_type='audio')
    #         st.audio(direct_link)




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
        response = None
        if "진료를" in user_input:
            feedback = provide_feedback()
            with st.spinner(" "):
                time.sleep(5)
                message(feedback, key="feedback")
        else:
            for keyword in qna_mapping:
                if keyword in user_input:
                    response = qna_mapping[keyword]
                    break
            
            if response is None:
            
                with st.spinner(" "):
                    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo-0613",
                        messages=[
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    response = completion.choices[0].message.content
            with st.spinner(" "):
                time.sleep(1.2)
            
            #with st.chat_message("assistant", avatar="https://github.com/JinukHong/shadowFunk/assets/45095330/eceff742-486e-46d8-b501-72efede31c25"):
                # st.write(f"{response}")
                #write(chatwrite(response))
                # st.divider()
                # write(chatwrite(translated_response))
                # Handle media based on the response



            # Update Session States
        if response is not None:
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

    

    with st.sidebar:
        with st.form(key='media_link_form'):
            link_input = st.text_input("구글 드라이브 링크를 넣어주세요")
            media_type = st.radio("미디어 형식", ('image', 'audio'))
            submit_link = st.form_submit_button("Submit")

            if submit_link and link_input:
                direct_link = convert_drive_link(link_input, media_type)
                if media_type == 'image':
                    st.image(direct_link, caption='Uploaded Image')
                elif media_type == 'audio':
                    st.audio(direct_link)

    st.write("check out this [image preprocessing code](https://colab.research.google.com/drive/1YyC3JRr-x5IVUs5nPmDr0nM-cOTjikjM?usp=sharing)")
    st.write("check out this [image generaging code](https://colab.research.google.com/drive/1JVSnLqZ6iffsYVlOrpNOWrIDAZGqeACg?usp=sharing)")
    st.write("check out this [audio generating code](https://colab.research.google.com/drive/1IBFwoTuKmPS8ECOliOy1G7OMf1_4EEvx?usp=sharing)")
