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

# class course():
#     Student_name = "Vivek Shrivastav"
#     Course_name = "BCA"
#     _account_number = "394339783"

#     def student_details(self):
#         print("vivek shrivastav")
#         print("age:",19)


# course_obj = course()

# print(course_obj.Course_name)
# print(course_obj.Student_name)
# print(course_obj._account_number)

# course_obj.student_details()

# Protected Member

class owner():
    __account_number = "917973997743"
    __ifce_code = "SBIN0003018"
    __cerdit_card_number = "7643398876034"


    def main_deatiles(self):
        print("Owner to detail in all of the:")

owner_obj = course()

print(owner_obj.__account_number)
print(owner_obj.__ifce_code)
print(owner_obj.__cerdit_card_number)

owner_obj.main_deatiles()

    