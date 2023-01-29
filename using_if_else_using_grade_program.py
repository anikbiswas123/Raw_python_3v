Grade_num=int(input("Input a Grade number value :"))
display_grade=0

if Grade_num >=80 and Grade_num <=100:
    display_grade ='A+'
elif Grade_num >=70 and Grade_num <=79:
    display_grade='A'
elif Grade_num >=60 and Grade_num <= 69:
    display_grade='A-'
elif Grade_num >=50 and Grade_num <= 59:
    display_grade='B+'
elif Grade_num >=40 and Grade_num <= 49:
    display_grade='D'
else:
    display_grade='you not pass the exam'


print(display_grade)