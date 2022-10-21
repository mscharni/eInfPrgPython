import json
maxRateValue = 6
rateValue = [{"value": i+1, "text": str(i)} for i in range(0,maxRateValue)]

class Kerdoiv:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.completedHtml = "Köszönjük, hogy kitöltötte a kérdőívet!"
        self.pages = []
        self.showTitle = False
        self.showPageTitles = False
        self.showProgressBar = "bottom"

class Page:
    def __init__(self, PN):
        self.name = "oldal" + str(PN)
        self.elements = []

class Element:
    def __init__(self, QN, questionText):
        self.type = "rating"
        self.name = "kérdés"+str(QN)
        self.title = questionText
        self.rateValues = rateValue
        self.rateMax = 6

kerdoiv = Kerdoiv()
with open("6_szamu_kerdoiv.txt",encoding="utf-8") as txt:
    # kérdőív alapadatai
    kerdoiv.title = txt.readline().strip();
    kerdoiv.description = txt.readline().strip();
    # kérdőív első oldala
    PN = 1
    page = Page(PN)
    kerdoiv.pages.append(page)
    # kérdőív kérdései (első oldalra)
    QN = 1
    for line in txt:
        question = Element(QN, line)
        kerdoiv.pages[PN-1].elements.append(question)
        QN += 1
print(kerdoiv.pages[0].elements[1].type)
kerdoivS = json.dumps(kerdoiv.__dict__)
print(kerdoivS)

