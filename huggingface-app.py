import streamlit as st
from transformers import pipeline

# Load a Hugging Face text-generation model
# You can replace "gpt2" with another model available on Hugging Face
generator = pipeline("text-generation", model="gpt2")

def generate_response(prompt):
    """
    Generate a response using a Hugging Face text-generation model.
    """
    try:
        # Generate text from the model
        response = generator(prompt, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error generating response: {str(e)}"

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Shopping Agent",
        page_icon="🛍️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Title
    st.title("Shopping Agent - Powered by GPT-2")

    # User input
    prompt = st.text_input("Enter your shopping request:", "")

    # Response display
    if st.button("Submit"):
        if prompt.strip():
            with st.spinner("Generating response..."):
                response = generate_response(prompt)
                st.text_area("Response:", value=response, height=200)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
