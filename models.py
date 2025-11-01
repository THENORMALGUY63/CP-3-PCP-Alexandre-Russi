from datetime import date


class Person:
    def __init__(self, name, email, company):
        self.name = name
        self.email = email
        self.company = company

class Lead(Person):
    def __init__(self, name, email, company, stage):
        super().__init__(name, email, company)
        self.stage = stage
        self.created = date.today().isoformat()

    def struct_lead(self):
        """Cria um lead como um dicionário simples"""
        return{
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created
        }