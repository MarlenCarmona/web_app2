import mysql.connector

class Personas():

    def connect(self):
        try:
            self.cnx=mysql.connector.connect(
                user='user_mar',
                password='User_bd',
                host='127.0.0.1',
                port=3306,
                database='user_db'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)
    def select(self):
        try:
            self.connect()
            query = ("SELECT * from usuarios;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r={
                    'id_usuario':row[0],
                    'nombre':row[1],
                    'primer_apellido':row[2],
                    'segundo_apellido':row[3],
                    'matricula':row[4],
                    'edad':row[5],
                    'fecha_nac':row[6],
                    'genero':row[7],
                    'estado':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result=[]
            return result
    def view(self,matricula):
        try:
            self.connect()
            query = ("SELECT * FROM personass WHERE matricula = %s;")
            values = (matricula,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                for row in self.cursor:
                ={
                    'id_usuario':row[0],
                    'nombre':row[1],
                    'primer_apellido':row[2],
                    'segundo_apellido':row[3],
                    'matricula':row[4],
                    'edad':row[5],
                    'fecha_nac':row[6],
                    'genero':row[7],
                    'estado':row[8]
                }
                result.append()
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
    def insert(self, nombre,primer_apellido,segundo_apellido,matricula,edad,fecha_nac,genero,estado):
        try:
            self.connect()
            query = ("INSERT INTO personas (nombre,primer_apellido,segundo_apellido,matricula,edad,fecha_nac,genero,estado) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (nombre,primer_apellido,segundo_apellido,matricula,edad,fecha_nac,genero,estado)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Personas()
objeto.connect()
objeto.insert("Marlen","carmona","Lopez","1718110379","19","05/10/00","Femenino","Hidalgo")

for row in objeto.select():
    print(row)