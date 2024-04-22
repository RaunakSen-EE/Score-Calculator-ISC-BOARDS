# Import necessary libraries
import streamlit as st

# Main function to run the Streamlit app
def main():
    st.title("Welcome to Streamlit Cloud!")

    # Add some text
    st.write("This is a simple Streamlit Cloud app.")
    st.write("You can customize it to create interactive web applications.")

    # Add a text input field
    user_input = st.text_input("Enter your name:", "")

    # Display a greeting message
    if user_input:
        st.write(f"Hello, {user_input}! Welcome to Streamlit Cloud.")

if __name__ == "__main__":
    main()
