class Sanjana():
    Sbs =  " B.Com Student"

class Aditya(Sanjana):
    Company_name = "Vivo"


class Vivek(Aditya):
    Privact_Ltd = "Ayansh Dhabha"

Vivek_obj = Vivek()
print(Vivek_obj.Company_name)
print(Vivek_obj.Privact_Ltd)
