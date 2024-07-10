
def numerical_letter_grade(grades):
    """
    Yeh semester ka aakhri week hai aur teacher ko students ko grades dena hai.
    Teacher ne apna khud ka algorithm banaya hai grading ke liye.
    Sirf ek problem hai, unhone jo code use kiya tha grading ke liye, woh kho gaya hai.
    Unhone aapko kuch students ke GPAs ki list di hai aur aapko ek function likhna hai 
    jo letter grades ki list output kar sake, neeche diye gaye table ke hisaab se:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """

    # return a list of a letter-grade string corresponding to each numeric grade in grades
    # you may assume grades is a valid input parameter with values between 0 and 4
    gradelist = ['F' for i in range(len(grades))]
    for i, grade in enumerate(grades):
        grade_dict = {
            'A+' : 4.0, 
            'A' : 3.7, 
            'A-' : 3.3,
            'B+' : 3.0, 
            'B' : 2.7, 
            'B-' : 2.3,
            'C+' : 2.0, 
            'C' : 1.7, 
            'C-' : 1.3,
            'D+' : 1.0, 
            'D' : 0.7, 
            'D-' : 0.0, 
            'E' : 0.0
            }        
        grade_dict2 = {
            'A+' : 4.0,
            'A' : 3.7,
            'B+' : 3.3,
            'B' : 3.0,
            'B-' : 2.7,
            'C+' : 2.3,
            'C' : 2.0,
            'C-' : 1.7,
            'D+' : 1.3,
            'D' : 1.0,
            'D-' : 0.7,
            'E' : 0.0
            }        
        
        for key in grade_dict:
            if grade >= grade_dict[key]:
                gradelist[i] = key
        for key in grade_dict2:
            if grade >= grade_dict2[key]:
                gradelist[i] = key

    return gradelist
