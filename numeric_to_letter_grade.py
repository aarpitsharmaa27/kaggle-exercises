# Function get_grade(score) returns letter grade from numeric score.
# Mapping:
# 90-100 -> "A"
# 80-89  -> "B"
# 70-79  -> "C"
# 60-69  -> "D"
# <60    -> "F"


def get_grade(score):
   if score >= 90:
        grade = "A"
   elif score >= 80:
       grade = "B"
   elif score >= 70:
       grade = "C"
   elif score >= 60:
       grade = "D"
   elif score < 60:
       grade ="F"
   else:
       grade = 'None'
   return grade
print(get_grade(85))
print(get_grade(49))
