import json

class Address():
    street = None
    houseNumber=None
    zipCode    = None
    town       = None

    def __init__(self, street, houseNumber,zipCode,town):
        self.street=street
        self.houseNumber=houseNumber
        self.zipCode=zipCode
        self.town=town

    # Class method to create an Address object from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class Person():
    """
    A class to represent a person.
    """
    name = None
    age =  None
    cAddress = None

    def __init__(self, name, age, cAddress ):
        """
        Construct a new 'Person' object.

        :param name: The name of the person.
        :param age: The age of the person.
        """
        self.name = name
        self.age = age
        self.cAddress= cAddress

    def __str__(self):
        """
        Return a string representation of the 'Person' object.

        :return: 'name is age years old'
        """
        return f'{self.name} is {self.age} years old and lives in {self.cAddress.town}'
    def to_json(self, filename):
        """
        Save the 'Person' object to a JSON file.

        :param filename: The name of the file to save to.
        """
        with open(filename, 'w') as f:
            data = self.__dict__.copy()
            data['cAddress'] = self.cAddress.__dict__
            json.dump(data, f)

    @classmethod
    def from_json(cls, filename):
        """
        Create a new 'Person' object from a JSON file.

        :param filename: The name of the file to load from.
        :return: A new 'Person' object.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            data['cAddress'] = Address.from_dict(data['cAddress'])
        return cls(**data)


if __name__ == "__main__":
    #Opprett en ny kunde

    kundeNr1 = Person('John', 25,Address('Slotsplassen', 1, 10, "Oslo") )

    #Lagre dataene i filen person.json
    kundeNr1.to_json('person.json')

    #Opprette et nytt objekt med informasjonen fra person.json
    KundeNr2=Person.from_json('person.json')
    print(KundeNr2)

