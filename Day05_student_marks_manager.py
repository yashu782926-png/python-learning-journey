name=input("Enter your name: ")
marks=int(input("Enter your marks of 5 subjects: "))
physics=int(input("Enter your marks of physics: "))
maths=int(input("Enter your marks of maths: "))
chemistry=int(input("Enter your marks of chemistry: "))
biology=int(input("Enter your marks of biology: "))
electrical=int(input("Enter your marks of electrical: "))
passed_subjects = 0
failed_subjects = 0

for mark in [physics, maths, chemistry, biology,electrical]:
    if mark >= 90:
        print(f"Subject: {mark}, Grade: A+")
        passed_subjects += 1
    elif mark >= 70:
        print(f"Subject: {mark}, Grade: A")
        passed_subjects += 1
    elif mark >= 40:   
        print(f"Subject: {mark}, Grade: B")
        passed_subjects += 1
    else:
        print(f"Subject: {mark}, Grade: C")
        failed_subjects += 1

total_marks = physics + maths + chemistry + biology + electrical
percentage = (total_marks / 500) * 100
average_marks = total_marks / 5
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")
print(f"Average Marks: {average_marks}")
print(f"Passed Subjects: {passed_subjects}")
print(f"Failed Subjects: {failed_subjects}")
if failed_subjects > 0:
    print(f"{name}, you have failed in {failed_subjects} subjects.")
elif passed_subjects == 5:
    print(f"{name}, you have passed in all subjects. Congratulations!")