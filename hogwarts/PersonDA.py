import mysql.connector


class PersonDA:
    def connect(self):
        self.database = mysql.connector.connect(
            host="",
            user="",
            password="",
            database="huff")
        self.cursor = self.database.cursor()

    def disconnect(self):
        self.cursor.close()
        self.database.close()

    def save(self, person):
        self.connect()
        self.cursor.execute("INSERT INTO PERSON (name,family,ability) VALUES (%s,%s,%s)",
                            [person.name, person.family, person.ability])
        self.database.commit()
        self.disconnect()

    def edit(self,person):
        self.connect()
        self.cursor.execute("UPDATE PERSON SET name=%s,family=%s,ability=%s WHERE code=%s",
                            [person.name, person.family, person.ability, person.code])
        self.database.commit()
        self.disconnect()

    def remove(self, code):
        self.connect()
        self.cursor.execute("DELETE FROM PERSON WHERE code=%s",
                            [code])
        self.database.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON")
        person_list = self.cursor.fetchall()
        self.disconnect()
        return person_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON WHERE code=%s",
                            [code])
        person = self.cursor.fetchall()
        self.disconnect()
        return person

    def find_by_family(self, family):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON WHERE family LIKE %s",
                            [family+"%"])
        person = self.cursor.fetchall()
        self.disconnect()
        return person




















    
