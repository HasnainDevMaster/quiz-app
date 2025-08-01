import streamlit as st # for the web interface
import random # for randomizing the questions
import time # for the timer

# Title of the Application
st.title("📝 Quiz Application")

# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
    {
        "question": "What is the largest province of Pakistan by area?",
        "options": ["Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa"],
        "answer": "Balochistan",
    },
    {
        "question": "Who was the first Prime Minister of Pakistan?",
        "options": [            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Zulfikar Ali Bhutto",
            "Benazir Bhutto",
        ],
        "answer": "Liaquat Ali Khan",
    },
    {
        "question": "What is the national animal of Pakistan?",
        "options": ["Markhor", "Lion", "Tiger", "Elephant"],
        "answer": "Markhor",
    },
    {
        "question": "Which mountain range is located in Pakistan?",
        "options": ["Himalayas", "Andes", "Rocky Mountains", "Hindu Kush"],
        "answer": "Hindu Kush",
    },
    {
        "question": "What is the national flower of Pakistan?",
        "options": ["Rose", "Jasmine", "Lotus", "Sunflower"],
        "answer": "Jasmine",
    },
    {
        "question": "Which river is known as the lifeline of Pakistan?",
        "options": ["Indus River", "Ganges River", "Nile River", "Amazon River"],
        "answer": "Indus River",
    },
    {
        "question": "What is the national sport of Pakistan?",
        "options": ["Cricket", "Hockey", "Football", "Badminton"],
        "answer": "Hockey",
    },
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button the check the answer
if st.button("Submit Answer"):
    # check if the answer is correct
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])
  
    # Wait for 3 seconds before showing the next question
    time.sleep(5)

    # Select a new random question
    st.session_state.current_question = random.choice(questions)

    # Rerun the app to display the next question    
    st.rerun()