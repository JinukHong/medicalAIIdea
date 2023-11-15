import json


def read_data():
    with open('./data/answers.json', 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the JSON content into a Python list of dictionaries
    answers_list = json.loads(content)

    # Return the last dictionary in the list (latest answers)
    return answers_list if answers_list else {}

def user_data():
    answer_list = read_data()
    answers = answer_list[0]

        # Extracting user's name and birthdate
    name = answers.get("personal_info_name", None)
    birthdate = answers.get("personal_info_birthdate", None)

        # Extracting user's chief complaint
    chief_complaint = answers.get("chief_complaint", None)

    # Extracting other details
    onset_1 = answers.get("onset_1", "Can't remember")
    onset_2 = answers.get("onset_2", "Can't remember")
    course = answers.get("course", "Unknown onset")
    duration_1 = answers.get("duration_1", "Unknown duration")
    duration_2 = answers.get("duration_2", "Unknown frequency")
    course_2 = answers.get("course_2", "Unknown symptom progression")
    experience = answers.get("experience", "No past experience")
    character_1 = answers.get("character_1", "Unknown breathing difficulty type")
    character_2 = answers.get("character_2", "Unknown breathing pattern")
    character_3 = answers.get("character_3", "Unknown symptom severity")
    associate_1 = answers.get("associate_1", "No associated symptoms")
    associate_1_1 = answers.get("associate_1_1", "Unknown associated symptoms")
    associate_2 = answers.get("associate_2", "No recent cold")
    associate_3 = answers.get("associate_3", "No frequent colds in childhood")
    factors_1 = answers.get("factors_1", "No change with posture")
    factors_2 = answers.get("factors_2", "Unknown symptom relief scenarios")
    event = answers.get("event", "No prior health checkup/X-ray")
    injury = answers.get("injury", "No recent injuries")
    injury_1 = answers.get("injury_1", "Unknown injury location")
    past_1 = answers.get("past_1", "No recent hospitalization/bed rest")
    past_2 = answers.get("past_2", "No surgeries")
    past_2_1 = answers.get("past_2_1", "Unknown surgery type")
    past_3 = answers.get("past_3", "No past lung diseases")
    past_4 = answers.get("past_4", "No heart diseases")
    past_5 = answers.get("past_5", "No hypertension, diabetes, or liver diseases")
    drug = answers.get("drug", "No current medications")
    drug_1 = answers.get("drug_1", "Unknown medication")
    social_1 = answers.get("social_1", "No smoking")
    social_1_1 = answers.get("social_1_1", "Unknown smoking frequency/duration")
    social_2 = answers.get("social_2", "No alcohol consumption")
    social_2_1 = answers.get("social_2_1", "Unknown alcohol consumption pattern")
    social_3 = answers.get("social_3", "Unknown occupation")
    social_4 = answers.get("social_4", "No relation between work stress/environment and symptoms")
    family_1 = answers.get("family_1", "No family history of hypertension/diabetes/hyperlipidemia")
    family_2 = answers.get("family_2", "No family history of lung diseases")
    feminine = answers.get("feminine", "Pregnancy status unknown")
    answer = answers.get("answer_disease", "Disease undefined")

    # Generating the user's details
    user_details = [
        f"Name: {name}",
        f"Birthdate: {birthdate}",
        f"Chief Complaint: {chief_complaint}",
        f"Course: {course}",
        f"Duration (once it appears): {duration_1}",
        f"Frequency (times a day): {duration_2}",
        f"Symptom Progression: {course_2}",
        f"Past Experiences: {experience}",
        f"Type of Breathing Difficulty: {character_1}",
        f"More Difficulty in: {character_2}",
        f"Severity of Symptom: {character_3}",
        f"Associated Symptoms: {associate_1}",
        f"Specific Associated Symptoms: {associate_1_1}",
        f"Recent Cold: {associate_2}",
        f"Frequent Colds in Childhood: {associate_3}",
        f"Change in Symptoms with Posture: {factors_1}",
        f"Scenarios of Symptom Relief: {factors_2}",
        f"Prior Health Checkup/X-ray: {event}",
        f"Recent Injuries: {injury}",
        f"Location of Injury: {injury_1}",
        f"Recent Hospitalization/Bed Rest: {past_1}",
        f"Surgeries: {past_2}",
        f"Type of Surgery: {past_2_1}",
        f"Past Lung Diseases: {past_3}",
        f"Heart Diseases: {past_4}",
        f"Hypertension/Diabetes/Liver Diseases: {past_5}",
        f"Current Medications: {drug}",
        f"Specific Medication: {drug_1}",
        f"Smoking: {social_1}",
        f"Smoking Frequency/Duration: {social_1_1}",
        f"Alcohol Consumption: {social_2}",
        f"Alcohol Consumption Pattern: {social_2_1}",
        f"Occupation: {social_3}",
        f"Relation Between Work Stress/Environment and Symptoms: {social_4}",
        f"Family History of Hypertension/Diabetes/Hyperlipidemia: {family_1}",
        f"Family History of Lung Diseases: {family_2}",
        f"Pregnancy Status: {feminine}",
        f"Paitient's Dieases: {answer}"
    ]



    # Generating future plans based on answers.
    patient_status = []

    # Chief Complaint
    patient_status.append(f"Chief Complaint: {chief_complaint}")
    # Course of symptom onset
    patient_status.append(f"Course: {course}")
    # Duration of symptoms once they appear
    patient_status.append(f"Duration (once it appears): {duration_1}")
    # Frequency of symptoms in a day
    patient_status.append(f"Frequency (times a day): {duration_2}")
    # Progression of the symptoms
    patient_status.append(f"Symptom Progression: {course_2}")
    # Past experiences of similar symptoms
    patient_status.append(f"Past Experiences: {experience}")
    # Describing the type of breathing difficulty
    patient_status.append(f"Type of Breathing Difficulty: {character_1}")
    # Which is more difficult, inhaling or exhaling?
    patient_status.append(f"More Difficulty in: {character_2}")
    # Severity of the symptoms
    patient_status.append(f"Severity of Symptom: {character_3}")
    # Are there any associated symptoms?
    patient_status.append(f"Associated Symptoms: {associate_1}")
    # If yes, what are those specific symptoms?
    patient_status.append(f"Specific Associated Symptoms: {associate_1_1}")
    # Recent history of cold
    patient_status.append(f"Recent Cold: {associate_2}")
    # History of frequent colds during childhood
    patient_status.append(f"Frequent Colds in Childhood: {associate_3}")
    # Does the symptom change with posture?
    patient_status.append(f"Change in Symptoms with Posture: {factors_1}")
    # When do the symptoms relieve?
    patient_status.append(f"Scenarios of Symptom Relief: {factors_2}")
    # Prior health check-ups or X-ray
    patient_status.append(f"Prior Health Checkup/X-ray: {event}")
    # Recent injuries
    patient_status.append(f"Recent Injuries: {injury}")
    # Where was the injury located?
    patient_status.append(f"Location of Injury: {injury_1}")
    # Recent hospitalizations or prolonged bed rest
    patient_status.append(f"Recent Hospitalization/Bed Rest: {past_1}")
    # Any surgeries in the past?
    patient_status.append(f"Surgeries: {past_2}")
    # If yes, what kind of surgery?
    patient_status.append(f"Type of Surgery: {past_2_1}")
    # History of lung diseases
    patient_status.append(f"Past Lung Diseases: {past_3}")
    # History of heart diseases
    patient_status.append(f"Heart Diseases: {past_4}")
    # Other conditions like Hypertension/Diabetes/Liver Diseases
    patient_status.append(f"Hypertension/Diabetes/Liver Diseases: {past_5}")
    # Current medications
    patient_status.append(f"Current Medications: {drug}")
    # Details of the medications
    patient_status.append(f"Specific Medication: {drug_1}")
    # Smoking history
    patient_status.append(f"Smoking: {social_1}")
    # Smoking frequency and duration
    patient_status.append(f"Smoking Frequency/Duration: {social_1_1}")
    # Alcohol consumption
    patient_status.append(f"Alcohol Consumption: {social_2}")
    # Alcohol consumption pattern
    patient_status.append(f"Alcohol Consumption Pattern: {social_2_1}")
    # Occupation
    patient_status.append(f"Occupation: {social_3}")
    # Does the patient believe work stress/environment is related to symptoms?
    patient_status.append(f"Relation Between Work Stress/Environment and Symptoms: {social_4}")
    # Any family history of Hypertension/Diabetes/Hyperlipidemia?
    patient_status.append(f"Family History of Hypertension/Diabetes/Hyperlipidemia: {family_1}")
    # Family history of lung diseases
    patient_status.append(f"Family History of Lung Diseases: {family_2}")
    # Possible pregnancy
    patient_status.append(f"Pregnancy Status: {feminine}")
    # Concatenate patient's status into a string
    patient_status_str = ', '.join(patient_status)

    # Create the final report
    report = f"User's Name: {name}, Birthdate: {birthdate}, Details: {patient_status_str}, Paitient's Dieases(Diagnosis result that doctor should conclude): {answer}"

    # Return the final report
    return report
