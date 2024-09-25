# First task ai



def my_final_grade_calculation():
    data_dict = {}
    result = {}
    # Open file and read data
    with open('grades.txt', 'r') as file:
        for line in file:
            # seperate parts with camma -> ,
            parts = line.strip().split(',')
            if parts:
                # First part is key (name students)
                key = parts[0].strip().lower() 
                # Another parts is Score
                values = [int(value.strip()) for value in parts[1:]]
                data_dict[key] = values 
    for data in data_dict:
        result[data] = calcute_grade(data_dict[data])        
    
    print(result)

# This method calcute student average
def calcute_grade(grades):
    grade = 0
    quiz = sum(sorted(grades[0:6])[2:])/len(sorted(grades[0:6])[2:]) * 0.25
    homework = sum(sorted(grades[6:10])[1:])/len(sorted(grades[6:10])[1:]) * 0.25
    midterm = grades[10] * 0.25
    final = grades[11] * 0.25
    
    grade = quiz + homework + midterm + final

    if grade >= 60:
        return "pass"
    else:
        return "fail"

    
            
my_final_grade_calculation()