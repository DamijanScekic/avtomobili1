from random import randint

class Avtomobili():
    def __init__(self, proizvajalec, model):
        self.proizvajalec = proizvajalec
        self.model = model

avto_1 = Avtomobili(proizvajalec="Audi", model="TT Roadster")
avto_2 = Avtomobili(proizvajalec="VW", model="Scirocco")
avto_3 = Avtomobili(proizvajalec="Mercedes", model="CLS")
avto_4 = Avtomobili(proizvajalec="Bugatti", model="Veyeron")
avto_5 = Avtomobili(proizvajalec="Tesla", model="Model-S")
avto_6 = Avtomobili(proizvajalec="Ariel", model="Atom")

avtomobili = [avto_1, avto_2, avto_3, avto_4, avto_5, avto_6]

odgovor = "da"
while odgovor != "ne!":
    odgovor = raw_input("Mislis da poznas vse prizvajalce avtomobilov? Da/Ne? ")

    if odgovor == "da":
        rnd = randint (0, len(avtomobili))
        print("Model se imenuje: " + avtomobili[rnd].model + ". Kateri znamki pripada? ")
        odgovor = raw_input("Proizvajalec se imenuje: ")

    if odgovor == avtomobili[rnd].proizvajalec:
        print("Bravo")

    else:
        print("tvoj odgovor ni pravilen")
        print("Proizvajalec je: " + avtomobili[rnd].proizvajalec)

    break

