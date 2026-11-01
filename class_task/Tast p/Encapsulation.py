# Public Member
# class course():
#     Student_name = "Vivek Shrivastav"
#     Course_name = "BCA"

#     def student_details(self):
#         print("vivek shrivastav")
#         print("age:",19)


# course_obj = course()

# print(course_obj.Course_name)
# print(course_obj.Student_name)

# course_obj.student_details()

# privat memober

class course():
    Student_name = "Vivek Shrivastav"
    Course_name = "BCA"
    _account_number = "39433976083"

    def student_details(self):
        print("vivek shrivastav")
        print("age:",19)


course_obj = course()

print(course_obj.Course_name)
print(course_obj.Student_name)
print(course_obj._account_number)

course_obj.student_details()