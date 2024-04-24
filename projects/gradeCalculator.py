import math

HOMEWORK_MAX = 800.0;
QUIZZES_MAX = 400.0;
MIDTERM_MAX = 150.0;
FINAL_MAX = 200.0;

student_status = input().strip('\n')
homework_score, quizzes_score, midterm_score, final_score=map(float,input().split())
if student_status == 'UG' or student_status == 'G' or student_status == 'DL':
    homework = (homework_score * 100) / HOMEWORK_MAX
    quizzes = (quizzes_score * 100) / QUIZZES_MAX
    midterm = (midterm_score * 100) / MIDTERM_MAX
    final_exam = (final_score * 100) / FINAL_MAX

    if homework > 100:
        homework = 100
    print(f'Homework: {homework:2.1f}%')

    if quizzes > 100:
        quizzes = 100
    print(f'Quizzes: { quizzes:2.1f}%')

    if midterm > 100:
        midterm = 100
    print(f'Midterm: {midterm:2.1f}%')

    if final_exam> 100:
        final_exam = 100
    print(f'Final Exam: {final_exam:2.1f}%')

    if student_status == 'UG':
        average = (homework_score * 20) / HOMEWORK_MAX
        average += (quizzes_score * 20) / QUIZZES_MAX
        average += (midterm_score * 30) / MIDTERM_MAX
        average += (final_score * 30) / FINAL_MAX

    elif student_status == 'G':
        average = (homework_score * 15) / HOMEWORK_MAX
        average += (quizzes_score * 5) / QUIZZES_MAX
        average += (midterm_score * 35) / MIDTERM_MAX
        average += (final_score * 45) / FINAL_MAX

    else:
        average = (homework_score * 5) / HOMEWORK_MAX
        average += (quizzes_score * 5) / QUIZZES_MAX
        average += (midterm_score * 40) / MIDTERM_MAX
        average += (final_score * 50) / FINAL_MAX

    print(f'{student_status} average: {average:2.1f}%')

    if average > 90:
        grade='A'
    elif average >= 80 and average < 90:
        grade='B' 
    elif average >= 70 and average < 80:
        grade='C'
    elif average >= 60 and average < 70:
        grade='D'    
    else:
        grade='F'
    print("Course grade:", grade)

else:
    print("Error: student status must be UG, G or DL ")
