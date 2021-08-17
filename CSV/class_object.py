class Object:
    def __init__(self, ID, Name, Email):
        self.ID = ID
        self.Name = Name
        self.Email = Email

    def __str__(self):
        return "ID is: {}, Name is: {}, Email is: {} ".format(self.ID, self.Name, self.Email)


class Comma:
    def __init__(self, SN, Name, City):
        self.SN = SN
        self.Name = Name
        self.City = City

    def __str__(self):
        return "SN is: {}, Name is: {}, City is: {} ".format(self.SN, self.Name, self.City)


class Object03:
    def __init__(self, keyword):
        self.keyword = keyword

    def __str__(self):
        return "keyword is: {}".format(self.keyword)


class Contribute:
    def __init__(self, SN, Name, Contribute):
        self.SN = SN
        self.Name = Name
        self.Contribute = Contribute

    def __str__(self):
        return "SN is: {}, Name is: {}, City is: {} ".format(self.SN, self.Name, self.Contribute)
