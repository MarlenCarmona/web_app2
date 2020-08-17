import mysql.connector

class Personas():

    def connect(self):
        try:
            self.cnx=mysql.connector.connect(
                user='zht1hmtzjrjk4vn4',
                password='bdzz69ezxcntaw1b',
                host='qf5dic2wzyjf1x5x.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port=3306,
                database='gba825j9ugr2joc9'
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
    def update(self, id_usuario, nombre, primer_apellido, segundo_apellido, edad, fecha_nac, genero, estado):
        try:
            self.connect()
            query = ("UPDATE usuarios SET nombre=%s, primer_apellido=%s, segundo_apellido=%s, edad=%s, fecha_nac=%s, genero=%s, estado=%s WHERE id_usuario=%s;")
            values = (nombre, primer_apellido, segundo_apellido, edad, fecha_nac, genero, estado, id_usuario)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
    def delete(self, id_usuario):
            try:
                self.connect()
                query = ("DELETE FROM usuarios WHERE id_usuario= %s;")
                values = (id_usuario,)
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
#objeto.delete(1718110379)
objeto.update(1718110388, "Guadalupe","Espinosa","Riveros","19","05/10/00","Femenino","Hidalgooo")

for row in objeto.select():
    print(row)
