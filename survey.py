import streamlit as st
import json
import os

questions = [
{"question": "성함이 어떻게 되세요?", "answers": None, "type": "text"}, #1. Personal_Info_Name
{"question": "생년월일이 어떻게 되세요?", "answers": None, "type": "text"}, #2. Personal_Info_BirthDate
{"question": "오늘 어디가 불편해서 오셨나요?", "answers": None, "type": "text"}, #3. Chief_Complaint
{"question": "증상이 언제부터 시작됐나요?", "answers": None, "type": "text"}, #4-1.Onset_1
{"question": "호흡곤란이 발생할 때의 상황이 어땠나요?", "answers": None, "type": "text"}, #4-2. Onset_2
{"question": "증상이 갑자기 or 서서히 나타났나요?", "answers": ["갑자기", "서서히"], "type": "choice"}, #5. Course
{"question": "한번 증상이 나타나면 얼마나 지속되나요?", "answers": None, "type": "text"}, #6-1. Duration_1
{"question": "하루에 몇 번이나 증상을 느끼시나요?", "answers": None, "type": "text"}, #6-2. Duration_2
{"question": "증상이 점점 심해지나요?", "answers": ["네", "아니요"], "type": "choice"}, #7. Course
{"question": "이전에도 이런 적이 있었나요?", "answers": ["네", "아니요"], "type": "choice"}, #8. Experience
{"question": "어떻게 숨이 차시나요?", "answers": None, "type": "text"}, #9-1. Character_1
{"question": "숨을 내쉬는 것과 마시는 것 중 더 힘든 것이 있나요?", "answers": ["내쉬는 것","마시는 것","둘 다"], "type": "choice"}, #9-2. Character_2
{"question": "증상이 어느 정도로 심한가요?", "answers": ["1","2","3","4","5","6","7","8","9","10"], "type": "choice"}, #9-3. Character_3

{"question": "다른 증상이 동반되어 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #10-1. Associate_1
 {"question": "어떤 증상이 동반되나요?", "answers": None, "type": "text"}, #10-1-1

{"question": "최근 감기에 걸리셨나요?", "answers": ["네", "아니요"], "type": "choice"}, #10-2. Associate_2
{"question": "어릴 적부터 감기에 자주 걸리는 편이었나요?", "answers":["네", "아니요"], "type": "choice"}, #10-3. Associate_3
{"question": "자세에 따라 호흡곤란의 양상이 변화하나요?", "answers": None, "type": "text"}, #11-1. Factors_1
{"question": "어떤 경우에 숨찬 증상이 좋아지나요?", "answers": None, "type": "text"}, #11-2. Factors_2
{"question": "이전에 건강 검진/흉부 엑스선 사진 찍은 적이 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #12. Event

{"question": "최근 다친 적이 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #13. Injury
 {"question": "어딜 다치셨나요?", "answers": None, "type": "text"}, #13-1.

{"question": "최근에 입원하거나 오랫동안 누워서 지낸 적이 있나요?", "answers": None, "type": "text"}, #14-1. Past_1
{"question": "수술 받은 적이 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #14-2. Past_2
{"question": "어떤 수술을 받았나요?", "answers": None, "type": "text"}, #14-2-1

{"question": "과거에 천식이나 결핵, 폐질환을 진단 받은 적이 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #14-3. Past_3
{"question": "심부전이나 기타 심장병은요?", "answers": ["네", "아니요"], "type": "choice"}, #14-4. Past_4
{"question": "고혈압, 당뇨, 간질환이 있으신가요?", "answers": ["네", "아니요"], "type": "choice"}, #14-5. Past_5

{"question": "현재 복용하시는 약물이 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #15. Drug
 {"question": "어떤 약물을 복용하시나요?", "answers":  None, "type": "text"}, #15-1.

{"question": "흡연하시나요?", "answers": ["네", "아니요"], "type": "choice"}, #16-1. Social_1
 {"question": "하루에 몇 갑을 몇 년동안 피셨나요?", "answers":  None, "type": "text"}, #16-1-1

{"question": "음주 하시나요?", "answers": ["네", "아니요"], "type": "choice"}, #16-2. Social_2
 {"question": "한 달에 몇 번, 하루에 소주 몇 잔 드시나요?", "answers": None, "type": "text"}, #

{"question": "직업이 어떻게 되세요?", "answers": None, "type": "text"}, #16-3. Social_3
{"question": "스트레스나 근무 환경이 호흡곤란 증상과 관계된다고 생각하시나요?", "answers": ["네", "아니요"], "type": "choice"}, #16-4. Social_4
{"question": "기족 중에 고혈압, 당뇨, 고지혈증 가진 분이 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #17-1. Family_1
{"question": "가족 중에 결핵, 폐암 등 기타 기관지, 폐질환을 가진 분이 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #17-2. Family_2
{"question": "임신 가능성이 있나요?", "answers": ["네", "아니요"], "type": "choice"}, #18. Feminine

{"question": "설문한 환자에 대한 진단명을 입력해주세요:", "answers": None, "type": "text"}, #19. 진단명

] 
def show_survey():
    st.title(f"Question {st.session_state.current_question + 1}")
    current_q = questions[st.session_state.current_question]
    st.write(current_q["question"])
    
    answer = None
    if current_q["type"] == "choice":
        answer = st.radio("Your answer", current_q["answers"], key=str(st.session_state.current_question))
    elif current_q["type"] == "text":
        answer = st.text_input("Your answer", key=str(st.session_state.current_question))
    
    cols = st.columns([1, 1])

    with cols[0]:
        if st.button("Next") and answer is not None:
            # Add the answer to the dictionary
            st.session_state.answers[current_q["question"]] = answer
            if st.session_state.current_question == 13: # 다른 증상
                if answer == "네": 
                    st.session_state.current_question += 1  # Go on
                else:
                    st.session_state.current_question += 2  # Skip 

            elif st.session_state.current_question == 20:  # 최근 다친적
                if answer == "네":
                    st.session_state.current_question += 1  # Go on
                else:
                    st.session_state.current_question += 2  # Skip 

            elif st.session_state.current_question == 23: #최근 수술
                if answer == "네":  
                    st.session_state.current_question += 1  # Go on
                else: 
                    st.session_state.current_question += 2
            
            elif st.session_state.current_question == 28: #약물
                if answer == "네":  
                    st.session_state.current_question += 1  # Go on
                else:
                    st.session_state.current_question += 2
            
            elif st.session_state.current_question == 30: #흡연
                if answer == "네":  
                    st.session_state.current_question += 1  # Go on
                else:
                    st.session_state.current_question += 2

            
            elif st.session_state.current_question == 32:
                if answer == "네":  
                    st.session_state.current_question += 1  # Go on
                else:
                    st.session_state.current_question += 2

            # elif st.session_state.current_question == 14:
            #     if answer == "네":  # 자녀
            #         st.session_state.current_question += 1  # Go on
            #     else:
            #         st.session_state.current_question += 4
            
            # elif st.session_state.current_question == 16:
            #     if answer == "네":  # 자녀
            #         st.session_state.current_question += 1  # Go on
            #     else:
            #         st.session_state.current_question += 2



            elif st.session_state.current_question < len(questions) - 1:
                st.session_state.current_question += 1  # Normal flow
            else:
                st.session_state.show_submit_button = True
            st.experimental_rerun()

    with cols[1]:
        if st.button("Previous") and st.session_state.current_question > 0:
            st.session_state.answers.pop()
            st.session_state.current_question -= 1
            st.experimental_rerun()


questions_mapping = {
    "personal_info_name": "성함이 어떻게 되세요?",
    "personal_info_birthdate": "생년월일이 어떻게 되세요?",
    "chief_complaint": "오늘 어디가 불편해서 오셨나요?",
    "onset_1": "증상이 언제부터 시작됐나요?",
    "onset_2": "호흡곤란이 발생할 때의 상황이 어땠나요?",
    "course": "증상이 갑자기 or 서서히 나타났나요?",
    "duration_1": "한번 증상이 나타나면 얼마나 지속되나요?",
    "duration_2": "하루에 몇 번이나 증상을 느끼시나요?",
    "course_2": "증상이 점점 심해지나요?",
    "experience": "이전에도 이런 적이 있었나요?",
    "character_1": "어떻게 숨이 차시나요?",
    "character_2": "숨을 내쉬는 것과 마시는 것 중 더 힘든 것이 있나요?",
    "character_3": "증상이 어느 정도로 심한가요?",
    "associate_1": "다른 증상이 동반되어 있나요?",
    "associate_1_1": "어떤 증상이 동반되나요?",
    "associate_2": "최근 감기에 걸리셨나요?",
    "associate_3": "어릴 적부터 감기에 자주 걸리는 편이었나요?",
    "factors_1": "자세에 따라 호흡곤란의 양상이 변화하나요?",
    "factors_2": "어떤 경우에 숨찬 증상이 좋아지나요?",
    "event": "이전에 건강 검진/흉부 엑스선 사진 찍은 적이 있나요?",
    "injury": "최근 다친 적이 있나요?",
    "injury_1": "어딜 다치셨나요?",
    "past_1": "최근에 입원하거나 오랫동안 누워서 지낸 적이 있나요?",
    "past_2": "수술 받은 적이 있나요?",
    "past_2_1": "어떤 수술을 받았나요?",
    "past_3": "과거에 천식이나 결핵, 폐질환을 진단 받은 적이 있나요?",
    "past_4": "심부전이나 기타 심장병은요?",
    "past_5": "고혈압, 당뇨, 간질환이 있으신가요?",
    "drug": "현재 복용하시는 약물이 있나요?",
    "drug_1": "어떤 약물을 복용하시나요?",
    "social_1": "흡연하시나요?",
    "social_1_1": "하루에 몇 갑을 몇 년동안 피셨나요?",
    "social_2": "음주 하시나요?",
    "social_2_1": "한 달에 몇 번, 하루에 소주 몇 잔 드시나요?",
    "social_3": "직업이 어떻게 되세요?",
    "social_4": "스트레스나 근무 환경이 호흡곤란 증상과 관계된다고 생각하시나요?",
    "family_1": "기족 중에 고혈압, 당뇨, 고지혈증 가진 분이 있나요?",
    "family_2": "가족 중에 결핵, 폐암 등 기타 기관지, 폐질환을 가진 분이 있나요?",
    "feminine": "임신 가능성이 있나요?",
    "answer_disease": "설문한 환자에 대한 진단명을 입력해주세요:"
}

questions_mapping

# def save_results():
#     # Invert the mapping to use questions as keys for lookup
#     questions_mapping_inv = {v: k for k, v in questions_mapping.items()}

#     # Convert answers to use simple keys
#     simple_key_answers = {questions_mapping_inv[question]: answer for question, answer in st.session_state.answers.items()}

#     # Save the answers using simple keys to JSON file
#     with open("./data/answers.json", "w", encoding='utf-8') as f:
#         json.dump(simple_key_answers, f, ensure_ascii=False)

def save_results():
    # Invert the mapping to use questions as keys for lookup
    questions_mapping_inv = {v: k for k, v in questions_mapping.items()}

    # Convert answers to use simple keys
    simple_key_answers = {questions_mapping_inv[question]: answer for question, answer in st.session_state.answers.items()}

    # Define file path
    file_path = "./data/answers.json"

    # Check if file exists and read existing data
    if os.path.exists(file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            existing_data = json.load(f)
            
            # Check if the existing data is a dictionary and convert to a list
            if isinstance(existing_data, dict):
                existing_data = [existing_data]
    else:
        existing_data = []

    # Append the new survey results to the existing list
    existing_data.append(simple_key_answers)

    # Save the updated list back to JSON file
    with open(file_path, "w", encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False)


    st.title("Survey Results")
    for q in questions:
        # Ensure the answer key exists in the answers dictionary
        if q['question'] in st.session_state.answers:
            st.write(f"{q['question']} : {st.session_state.answers[q['question']]}")
