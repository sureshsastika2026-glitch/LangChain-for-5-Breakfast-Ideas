
import os
import streamlit as st
from langchain_openai import ChatOpenAI


# ----------------------------------
# 1. Streamlit Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="Healthy Breakfast AI",
    page_icon="🥑",
    layout="centered"
)


# ----------------------------------
# 2. Application Header
# ----------------------------------

st.title("🥑 Healthy Breakfast AI")

st.subheader("Your AI-powered breakfast assistant")

st.write(
    "Discover five nutritious and delicious breakfast ideas "
    "generated using LangChain and OpenAI."
)

st.divider()


# ----------------------------------
# 3. Check OpenAI API Key
# ----------------------------------

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error(
        "OpenAI API key is missing. "
        "Please configure OPENAI_API_KEY in your terminal."
    )
    st.stop()


# ----------------------------------
# 4. Initialize LangChain Model
# ----------------------------------

@st.cache_resource
def load_model():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )


llm = load_model()


# ----------------------------------
# 5. User Breakfast Preferences
# ----------------------------------

st.header("🍳 Choose Your Breakfast Preference")

preference = st.selectbox(
    "Select your preferred breakfast type:",
    [
        "Healthy & Balanced",
        "High Protein",
        "Vegetarian",
        "Vegan",
        "Low Sugar"
    ]
)


# ----------------------------------
# 6. Generate Breakfast Ideas
# ----------------------------------

if st.button("✨ Generate Breakfast Ideas", use_container_width=True):

    prompt = f"""
    Suggest exactly 5 healthy breakfast ideas.

    User preference: {preference}

    Healthy breakfast should:
    - Include nutritious ingredients.
    - Prefer whole grains.
    - Include protein.
    - Include vegetables or fruits.
    - Avoid excessive added sugar.
    - Follow the selected breakfast preference.

    Formatting requirements:
    - Number the ideas from 1 to 5.
    - Write one idea per line.
    - Do not include an introduction.
    - Do not include a conclusion.
    - Give exactly 5 ideas.
    """

    try:
        with st.spinner("Preparing your healthy breakfast ideas..."):

            reply = llm.invoke(prompt)

        # Extract only the AI-generated text
        breakfast_ideas = reply.content

        # Display the results
        st.success("Your breakfast ideas are ready!")

        st.divider()

        st.header("🥗 Your 5 Breakfast Ideas")

        st.markdown(breakfast_ideas)

        st.divider()

        st.caption(
            "Generated using LangChain and OpenAI GPT-4o-mini"
        )

    except Exception as e:
        st.error(f"Something went wrong: {e}")


# ----------------------------------
# 7. Footer
# ----------------------------------

st.divider()

st.caption("Built with Python | Streamlit | LangChain | OpenAI")
