class grandfather():
    grandfather_bike = "duke 390"
    bike_price="3.4L" 
class father():
    father_phone_name="iphone 17 pro max"
    phone_price="1.45L"
class child(grandfather,father):
    child_fundation = "noraml fundation"
    child_school_name = "ak public school"
child_obj = child()
print(child_obj.father_phone_name)
print(child_obj.child_fundation)
print(child_obj.grandfather_bike)