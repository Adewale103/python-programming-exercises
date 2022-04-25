student = int(input("Enter the number of students: "))
subject = int(input("Enter the number of subjects: "))

student_grades_list_per_students = []
student_grades_list = []
total = []
average = []
position = []
tem_position = []

for i in range(0, student):
    for j in range(0, subject):
        a = int(input(f"Enter student {i + 1} grade for subject {j + 1} "))
        student_grades_list_per_students.append(a)
    total.append(sum(student_grades_list_per_students))
    tem_position.append(sum(student_grades_list_per_students))
    average.append((sum(student_grades_list_per_students) / subject))
    student_grades_list.append(student_grades_list_per_students)
    student_grades_list_per_students = []
tem_position.sort(reverse=True)
print(student_grades_list)
print(average)
print(total)

for i in range(len(tem_position)):
    for j in range(len(total)):
        if tem_position[i] == total[j]:
            a = (tem_position.index(tem_position[j]) + 1)
            position.append(a)

print(position)


def print_shape():
    shape = '='
    print(shape * 75)


def heading(no_of_subject):
    print("STUDENT    ", end=" ")
    for n in range(no_of_subject):
        print(f"SUB{n + 1}    ", end=" ")
    print("TOT    ", end=" ")
    print("AVG    ", end=" ")
    print("POS    ", end=" ")
    print()


def print_scores(no_of_student):
    for k in range(no_of_student):
        print(f"Student{k + 1}     ", end="")
        for p in student_grades_list[k]:
            print(f"{p}      ", end="")

        print(f"{total[k]:>3}     ", end="")
        print(f"{average[k]:>4.2f}    ", end="")
        print(f"{position[k]:>2}")


print_shape()
heading(subject)
print_shape()
print_scores(student)
print_shape()
print_shape()







