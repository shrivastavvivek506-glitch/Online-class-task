#Single Inheritance

class model():
    car_mobel = "BMW"
    seral_no = "BTM3575TWNC7CCL"
class owner( model):
    owner_name = "Vivek shrtivatav"
    mobile_no = "797399462"

owner_obj = owner()

print(owner_obj.car_mobel)
print(owner_obj.owner_name)
print(owner_obj.seral_no)

