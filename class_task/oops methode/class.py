class father():
    father_name = "John"
    father_age = 50
class child(father):
    child_name = "Zena"
    child_age = 4

c = child()
print(c.child_age)
print(c.father_age)