class Address():
    def __init__(self, street, city, postalCode, country):
        self.street = street
        self.city = city
        self.postalCode = postalCode
        self.country = country


class Person():
    def __init__(self, name, phoneNumber, emailAddress, address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address


class Student(Person):
    def __init__(self, name, phoneNumber, emailAddress, address, studentNumber, averageMark):
        Person.__init__(self, name, phoneNumber, emailAddress, address)
        self.studentMark = int(studentNumber)
        self.averageMark = int(averageMark)

class Professor(Person):
    def __init__(self, name, phoneNumber, emailAddress, address, staffNumber, yearsOfService, numberOfClasses):
        Person.__init__(self, name, phoneNumber, emailAddress, address)
        self.staffNumber = int(staffNumber)
        self.yearsOfService = int(yearsOfService)
        self.numberOfClasses = int(numberOfClasses)

