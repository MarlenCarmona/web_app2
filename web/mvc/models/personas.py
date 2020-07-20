import mysql.conector

class Personas():
    try:
        self.cnx=mysql.conector.connect(
            user='user_m',
            password='User_bd',
            host='127.0.0.1',
            port=3309,
            database='user_db'
            )
        self.cursor = self..cnx.cursor()
    except Exception as e:
        print(e)

    def select(self):
        try:
            self.connect()
            query=("SELECT * from usuarios")
            self.cursor.execute(query)
            result=[]
            for row in self.cursor:
                r={
                    'id_usuario':row[0],
                    'nombre':row[0],
                    'primer_apellido':row[0],
                    'segundo_apellido':row[0],
                    'matricula':row[0],
                    'edad':row[0],
                    'fecha_nac':row[0],
                    'genero':row[0],
                    'estado':row[0]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result=[]
            return result

objecto = Personas()
objecto.connect()

for row in objecto.select():
    print(row)