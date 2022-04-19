class Hotel:
    def __init__(self):
        self._rooms = {}
        self._rooms["SGL"] = {"state": 0, "price": 7000}
        self._rooms["DBL"] = {"state": 0, "price": 9000}
        self._rooms["Junior Suite"] = {"state": 0, "price": 6000}
        self._rooms["Suite"] = {"state": 0, "price": 4000}

    def occypy(self, typ):
        if self._rooms[typ]["state"] == 0:
            self._rooms[typ]["state"] = 1
        else:
            raise RuntimeError("Номер занят")

    def free(self, typ):
        self._rooms[typ]["state"] = 0

    def __str__(self):
        a = ''
        for i in self._rooms.keys():
            if self._rooms[i]["state"] == 0:
                a += 'Номер ' + i + " свободен\n"
            else:
                a += 'Номер ' + i + " занят\n"
        return a

    def all_occypy(self):
        for i in self._rooms.keys():
            self._rooms[i]["state"] = 1

    def all_free(self):
        for i in self._rooms.keys():
            self._rooms[i]["state"] = 0

    def share(self):
        d = round(sum([1 if self._rooms[i]["state"] == 1 else 0 for i in self._rooms.keys()])*100/len(self._rooms), 2)
        return f"Доля занятых номеров: {d} %"

    def profit(self):
        p = sum([self._rooms[i]["price"] if self._rooms[i]["state"] == 1 else 0 for i in self._rooms.keys()])
        return f"Выручка: {p}"


hotel = Hotel()
hotel.occypy("SGL")
hotel.occypy("DBL")
print(hotel.__str__())
print(hotel.share())
print(hotel.profit())
hotel.free("SGL")
print(hotel.share())
print(hotel.profit())
hotel.all_occypy()
print(hotel.__str__())
hotel.all_free()
print(hotel.__str__())
