def grade_level(grade_solve):
    if 2.00 <= grade_solve <= 2.99:
        return "Fail"
    elif 3.00 <= grade_solve <= 3.49:
        return "Poor"
    elif 3.5 <= grade_solve <= 4.49:
        return "Good"
    elif 4.5 <= grade_solve <= 5.49:
        return "Very Good"
    elif 5.5 <= grade_solve <= 6:
        return "Excellent"


grade = float(input())
print(grade_level(grade))
