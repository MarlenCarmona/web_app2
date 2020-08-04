import mysql.connector

class Personas():

    def connect(self):
        try:
            self.cnx=mysql.connector.connect(
                user='root',
                password='lup11t44',
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
                r = {
                    'id_usuario':row[0],
                    'nombre':row[1],
                    'primer_apellido':row[2],
                    'segundo_apellido':row[3],
                    'edad':row[4],
                    'fecha_nac':row[5],
                    'genero':row[6],
                    'estado':row[7]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result=[]
            return result
    def view(self,id_usuario):
        try:
            self.connect()
            query = ("SELECT * FROM usuarios WHERE id_usuario = %s;")
            values = (id_usuario,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                diccionario = {
                   'id_usuario':row[0],
                    'nombre':row[1],
                    'primer_apellido':row[2],
                    'segundo_apellido':row[3],
                    'edad':row[4],
                    'fecha_nac':row[5],
                    'genero':row[6],
                    'estado':row[7]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
    def insert(self,id_usuario, nombre,primer_apellido,segundo_apellido,edad,fecha_nac,genero,estado):
        try:
            self.connect()
            query = ("INSERT INTO usuarios (id_usuario,nombre,primer_apellido,segundo_apellido,edad,fecha_nac,genero,estado) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (id_usuario,nombre,primer_apellido,segundo_apellido,edad,fecha_nac,genero,estado)
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
#objeto.insert("1718110376","Marlen","carmona","Lopez","19","05/10/00","Femenino","Hidalgo")

for row in objeto.select():
    print(row)