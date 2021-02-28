from address import Address
class Person:
    def __init__(self,first, last, dob, phonenumber, address):
        self.firstName = first
        self.lastName = last
        self.dayOfBirth = dob
        self.phoneNum = phonenumber
        self.addresses = list()
        self.addAddress(address)
    def addAddress(self, address):
        _address = Address(*address)
        self.addresses.append(_address)