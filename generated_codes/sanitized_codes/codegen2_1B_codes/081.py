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
    x = grades.split(" ")
    x = " ".join(x)
    if len(grades) == 0:
        raise ValueError("Not enough information!")
    if x.isspace():
        raise ValueError("Not enough information!")
    out = []
    for g in x:
        grades = g.lstrip("0").rstrip("0")
        i = int(grades)
        out.append(
            dic[i],
            "".join(dic[x]).lstrip(numerical_letter_grade)[-len(dic[x]) - 1 :].strip(),
        )
    out_string = "|".join(out) + "|"
    return out_string