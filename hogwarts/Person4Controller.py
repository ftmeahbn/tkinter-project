from Person4DA import PersonDA
from person4_class import Person


class PersonController:
    @classmethod
    def save(cls, name, family, ability):
        try:
            if name != "" and family != "":
                person = Person(name, family,ability)
                person_da = PersonDA()
                person_da.save(person)
                return True, f"{person} Saved"
            else:
                return False,"Invalid Data"
        except:
            return False,"Error"

    @classmethod
    def edit(cls, name, family, ability, code):
        person = Person(name, family, ability, code)
        person_da = PersonDA()
        person_da.edit(person)

    @classmethod
    def remove(cls, code):
        person_da = PersonDA()
        person_da.remove(code)

    @classmethod
    def find_all(cls):
        person_da = PersonDA()
        return person_da.find_all()

    @classmethod
    def find_by_code(cls, code):
        person_da = PersonDA()
        return person_da.find_by_code(code)

    @classmethod
    def find_by_family(cls, family):
        person_da = PersonDA()
        return person_da.find_by_family(family)
