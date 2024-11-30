import streamlit as st

# Set up the app
st.title("Prompt Library")
st.subheader("Explore a curated collection of prompts for various tasks.")

# Define categories and prompts
prompt_library = {
    "Writing & Creativity": [
        "Write a 300-word story starting with 'Once upon a midnight dreary...'.",
        "Generate a unique plot idea for a sci-fi novel.",
        "Describe an alien civilization with unique societal norms.",
        "Compose a haiku about the changing seasons.",
        "Write an opening line for a mystery novel."
    ],
    "Business & Productivity": [
        "Draft an email to introduce yourself to a potential client.",
        "Write a professional apology for missing a meeting.",
        "Outline a social media strategy for a new startup.",
        "Create a 3-step plan to improve team communication.",
        "Generate a checklist for preparing a business presentation."
    ],
    "Education & Learning": [
        "Summarize the benefits of lifelong learning.",
        "Draft a study plan for preparing for an upcoming exam.",
        "Explain the concept of photosynthesis to a 10-year-old.",
        "List five tips for effective online learning.",
        "Create a lesson plan for teaching basic algebra."
    ],
    "Technology & Development": [
        "Explain the difference between frontend and backend development.",
        "Write a step-by-step guide to set up a Streamlit app.",
        "Generate ideas for a beginner-friendly Python project.",
        "Explain how blockchain technology works in simple terms.",
        "Write a tutorial on creating a REST API with Flask."
    ],
    "Personal Growth & Well-being": [
        "Write a daily affirmation to boost self-confidence.",
        "List five steps to start a mindfulness practice.",
        "Generate a workout plan for a beginner.",
        "Create a gratitude list with five items.",
        "Draft a self-reflection journal prompt for the end of the day."
    ]
}

# User interaction
category = st.selectbox("Select a category:", list(prompt_library.keys()))
if category:
    st.subheader(f"Prompts for {category}")
    for idx, prompt in enumerate(prompt_library[category], 1):
        st.write(f"{idx}. {prompt}")
