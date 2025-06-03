import uuid

class Character:
    def __init__(self, namn, beskrivning="", dialekt="", taggar=None):
        self.id = str(uuid.uuid4())
        self.namn = namn
        self.beskrivning = beskrivning
        self.dialekt = dialekt
        self.relationer = []  # Lista av dictar: {"namn": "Anna", "relation": "vän"}
        self.viktiga_händelser = []  # Lista av strängar
        self.exempelrepliker = []  # Lista av strängar
        self.taggar = taggar if taggar else []
        self.anteckningar = ""

    def lägg_till_relation(self, namn, relationstyp):
        self.relationer.append({"namn": namn, "relation": relationstyp})

    def lägg_till_händelse(self, händelse):
        self.viktiga_händelser.append(händelse)

    def lägg_till_replik(self, replik):
        self.exempelrepliker.append(replik)

    def till_dict(self):
        return self.__dict__

    @staticmethod
    def från_dict(data):
        c = Character(
            data["namn"],
            data.get("beskrivning", ""),
            data.get("dialekt", ""),
            data.get("taggar", []),
        )
        c.id = data.get("id", str(uuid.uuid4()))
        c.relationer = data.get("relationer", [])
        c.viktiga_händelser = data.get("viktiga_händelser", [])
        c.exempelrepliker = data.get("exempelrepliker", [])
        c.anteckningar = data.get("anteckningar", "")
        return c