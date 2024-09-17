import json

class Person:
    """
    A class to represent a person.
    """

    def __init__(self, name=None, age=None):
        """
        Construct a new 'Person' object.

        :param name: The name of the person.
        :param age: The age of the person.
        """
        self.name = name
        self.age = age
    def __str__(self):
        """
        Return a string representation of the 'Person' object.

        :return: 'name is age years old'
        """
        return f'{self.name} is {self.age} years old'
    def saveObjectInfoAsJson(self, filename):
        """
        Save the 'Person' object to a JSON file.

        :param filename: The name of the file to save to.
        """
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)

    def loadObjectInfoAsJson(self, filename):
        """
        Create a new 'Person' object from a JSON file.

        :param filename: The name of the file to load from.
        :return: A new 'Person' object.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        self.name=data['name']
        self.age=data['age']

if __name__ == "__main__":
    #Opprett en ny kunde
    kundeNr1 = Person('John', 25)
    print (kundeNr1)

    #Lagre dataene i filen person.json
    kundeNr1.saveObjectInfoAsJson('person.json')

    #Opprette et nytt objekt med informasjonen fra person.json
    KundeNr2=Person()
    KundeNr2.loadObjectInfoAsJson('person.json')

    print(KundeNr2)

