# Public,Protected,privat Member

class Member_shipe():
    Name = "Vivek shrivatav:"
    Age = "19:"
    __Member_ship_number = "MZHPS8366MNX:"
    __Licnce_number = "MRTUG25BCA099:"
    _Owner_shipe = "Vivek2009:"
    _Owner_number = "293722bj233:"

    def Important_details(self):
        print("This is a very importante detalis in any member shipe:")


Member_shipe_obj = Member_shipe()
print(Member_shipe_obj.Name)
print(Member_shipe_obj.Age)
print(Member_shipe_obj.__Member_ship_number)
print(Member_shipe_obj.__Licnce_number)
print(Member_shipe_obj._Owner_shipe)
print(Member_shipe_obj._Owner_number)

Member_shipe_obj.Important_details()
