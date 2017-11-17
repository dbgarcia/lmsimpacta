from django.db import connection

class ExecutorSQL():

    def __init__(self):
        pass

    def selectAll(self, query):

        cursor = connection.cursor()

        try:
            
            # atribuir a query
            cursor.execute(query)

            # retornar todos
            rows = cursor.fetchall()

        finally:

            # fechar conexao com o banco
            cursor.close()

        return rows

    def selectOne(self, query):

        cursor = connection.cursor()
        try:
            cursor.execute(query)
            row = cursor.fetchone()
        finally:
            cursor.close()
        
        return row

    def update(self, query):

        cursor = connection.cursor()
        try:
            cursor.execute(query)
        finally:
            cursor.close()

    def insert(self, query):

        cursor = connection.cursor()
        try:
            cursor.execute(query)
        finally:
            cursor.close()

    def delete(self, query):

        cursor = connection.cursor()
        try:
            cursor.execute(query)
        finally:
            cursor.close()