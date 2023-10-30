class Person:
    def __init__(self,navn:str,etternavn:str,fødselsår:int) -> None:

        self.navn = navn
        self.etternavn = etternavn
        self.fødselsår = fødselsår

person1 = Person("Adrian", "Bliktun Strand", 2005)

print(f"{person1.etternavn} {person1.navn}")