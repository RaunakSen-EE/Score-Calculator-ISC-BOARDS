import streamlit as st

# Function to calculate total score
def calculate_total_score(marks):
    top_3_subjects = sorted(marks[:-1], reverse=True)[:3]  # Exclude English marks
    total_score = sum(top_3_subjects) + marks[-1]  # Add English marks
    return total_score

# Function to calculate average score
def calculate_average_score(total_score):
    average_score = total_score / 4
    return average_score

# Function to calculate percentage
def calculate_percentage(average_score):
    percentage = average_score * 100
    return percentage

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
    total_score = calculate_total_score(marks)

    # Calculate average score
    average_score = calculate_average_score(total_score)

    # Calculate percentage
    percentage = calculate_percentage(average_score)

    # Display results
    st.write(f"Total Score: {total_score}")
    st.write(f"Average Score: {average_score}")
    st.write(f"Percentage: {percentage}%")

if __name__ == "__main__":
    main()
