import streamlit as st

# Main function to run the Streamlit app
def main():
    st.title("Grade Calculator")

    # Input marks for 4 subjects (excluding English)
    marks = []
    for i in range(4):
        subject_marks = st.number_input(f"Enter marks for subject {i+1}:", min_value=0.0, max_value=100.0)
        marks.append(subject_marks)

    # Input marks for English
    english_marks = st.number_input("Enter marks for English:", min_value=0.0, max_value=100.0)
    marks.append(english_marks)

    # Calculate total score
    total_score = sum(marks)

    # Calculate average score
    average_score = total_score / 5

    # Calculate percentage
    percentage = (total_score / 500) * 100

    # Display results
    st.write(f"Total Score: {total_score}")
    st.write(f"Average Score: {average_score}")
    st.write(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    main()
