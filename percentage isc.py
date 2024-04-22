# Step 1: Calculate the total of the top 3 subjects and add marks scored in English
def calculate_total_score(marks):
    top_3_subjects = sorted(marks[:-1], reverse=True)[:3]  # Exclude English marks
    total_score = sum(top_3_subjects) + marks[-1]  # Add English marks
    return total_score

# Step 2: Divide the total score by 4
def calculate_average_score(total_score):
    average_score = total_score / 4
    return average_score

# Step 3: Calculate the average score
def calculate_percentage(average_score):
    percentage = average_score * 100
    return percentage

# Example marks for 4 subjects (excluding English)
marks = [85, 90, 92, 88]

# Step 1: Calculate total score
total_score = calculate_total_score(marks)

# Step 2: Calculate average score
average_score = calculate_average_score(total_score)

# Step 3: Calculate percentage
percentage = calculate_percentage(average_score)

print("Total Score:", total_score)
print("Average Score:", average_score)
print("Percentage:", percentage)
