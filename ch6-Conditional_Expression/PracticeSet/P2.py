#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


subject1 = float(input("Enter marks in Subject 1: "))

subject2 = float(input("Enter marks in Subject 2: "))

subject3 = float(input("Enter marks in Subject 3: "))

total_marks = subject1 + subject2 + subject3

required_percentage = (total_marks / 3) 

if (required_percentage >= 33)  and (subject1 >= 40) and (subject2 >= 40) and (subject3 >= 40) :
    print("Congratulations! You have passed the exam.")

else :
    print("Sorry! You have failed the exam.")