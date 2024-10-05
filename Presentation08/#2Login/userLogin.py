import json

class PersonData():
    def __init__(self, fornavn, etternavn):
        """
        Initialiserer PersonData-objektet med fornavn og etternavn.

        :param fornavn: Brukerens fornavn som en streng.
        :param etternavn: Brukerens etternavn som en streng.
        """
        self.fornavn = fornavn
        self.etternavn = etternavn

class LoginInfo():
    def __init__(self, email, password, personData):
        """
        Initialiserer LoginInfo-objektet med e-post, passord og en PersonData-innstans.

        :param email: Brukerens e-postadresse som en streng.
        :param password: Brukerens passord som en streng.
        :param personData: En instans av PersonData-klassen.
        """
        self.email = email
        self.password = password
        self.personData = personData

    def velKommenTilOss(self):
        """
        Skriver ut en velkomstmelding for brukeren med brukerens navn
        """


class LoginInfoListe():
    def __init__(self, filNavn):
        """
        Initialiserer LoginInfoListe-objektet ved å lese data fra en JSON-fil.

        :param filNavn: Navnet på JSON-filen som skal leses.
        """
        self.lstloginInfo = []
        with open(filNavn, 'r') as f:
            data = json.load(f)

        for person in data:
            self.lstloginInfo.append(
                LoginInfo(person['E-Mail'], person['Password'], PersonData(person['Fornavn'], person['Etternavn'])))

    def returnLoginInfoIfEmailAndPasswordIsCorrect(self, email, password):
        """
        Sjekker om den gitte e-postadressen og passordet matcher noen av LoginInfo-objektene i listen.
        Returnerer det matchende LoginInfo-objektet hvis det finnes, ellers returnerer None.

        :param email: E-postadressen som skal sjekkes.
        :param password: Passordet som skal sjekkes.
        :return: Et LoginInfo-objekt hvis en match ble funnet, ellers None.
        """
        for loginInfo in self.lstloginInfo:
            if email == loginInfo.email and password == loginInfo.password:
                return loginInfo
        return None


if __name__ == "__main__":
    # Last inn brukerdata fra en JSON-fil.
    oLoginInfoListe = LoginInfoListe('Names.json')

    # Definer e-post og passord.
    passord = "oc!8KD&yr7"
    email = "reesejeffrey@example.org"

    # Sjekk om det finnes en bruker med den gitte e-posten og passordet.
    loginInfo = oLoginInfoListe.returnLoginInfoIfEmailAndPasswordIsCorrect(email, passord)

    # Hvis det finnes en slik bruker, skriv ut en velkomstmelding.
    if loginInfo is not None:
        loginInfo.velKommenTilOss()
    else:
        print("Wrong E-Mail or Password")


'''
@startuml classes
set namespaceSeparator none

class "PersonData" as userLogin.PersonData {
  + fornavn : str
  + etternavn : str
  __init__(fornavn: str, etternavn: str)
}

class "LoginInfo" as userLogin.LoginInfo {
  + email : str
  + password : str
  + personData : PersonData
  __init__(email: str, password: str, personData: PersonData)
  velKommenTilOss() : void
}

class "LoginInfoListe" as userLogin.LoginInfoListe {
  + lstloginInfo : list[LoginInfo]
  __init__(filNavn: str)
  returnLoginInfoIfEmailAndPasswordIsCorrect(email: str, password: str) : LoginInfo
}



userLogin.LoginInfoListe "lstloginInfo" *-- "0..*" userLogin.LoginInfo
userLogin.LoginInfo "personData" *-- "1" userLogin.PersonData

@enduml

'''