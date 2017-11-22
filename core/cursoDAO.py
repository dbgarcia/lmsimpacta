
from core.executorSQL import ExecutorSQL
from core.models import Curso

class CursoDAO():

    def __init__(self):
        pass

    def selectAll(self):

        # lista inicial
        cursos = []

        query = 'SELECT * FROM curso'
        rows = ExecutorSQL().selectAll(query)

        for row in rows:

            curso = self.retornaCurso(row)

            # insere na lista
            cursos.append(curso)

        return cursos

    def selectOne(self):

        # lista inicial
        cursos = []

        query = 'SELECT * FROM curso'
        row = ExecutorSQL().selectOne(query)

        curso = self.retornaCurso(row)

        # insere na lista
        cursos.append(curso)

        return cursos

    def insert(self, curso):

        query = 'INSERT INTO curso (sigla, nome, tipo, carga_horaria, ativo, descricao, Matriz_Curricular) VALUES ("{0}", "{1}", "{2}", "{4}", "{5}", "{6}", "{7}")'.format(curso.sigla, curso.nome, curso.tipo, curso.carga_horaria, curso.ativo, curso.descricao, curso.matrizcurricular)
        ExecutorSQL().insert(query)
    
    def update(self, curso):
        
        query = 'UPDATE curso SET sigla = "{0}", nome = "{1}", tipo = "{2}", carga_horaria = "{3}", ativo = "{4}", descricao = "{5}", Matriz_Curricular = "{6}"   WHERE NOME = "{0}"'.format(curso.sigla, curso.nome, curso.tipo, curso.carga_horaria, curso.ativo, curso.descricao, curso.matrizcurricular)
        ExecutorSQL().insert(query)

    def delete(self, curso):

        query = 'DELETE FROM curso WHERE nome = {0}'.format(curso.nome)
        ExecutorSQL().delete(query)

    def deleteAll(self):

        query = 'DELETE FROM curso'
        ExecutorSQL().delete(query)

    def retornaCurso(self, row):

        # obtem cada coluna
        sigla = row[1]
        nome = row[2]
        tipo = row[3]
        carga_horaria = row[4]
        ativo = row[5]
        descricao = row[6]
        # matrizcurricular = row[7]

        # abre intancia do objeto e atribuir dados a suas propriedades
        curso = Curso()
        curso.sigla = sigla
        curso.nome = nome
        curso.tipo = tipo
        curso.carga_horaria = carga_horaria
        curso.ativo = ativo
        curso.descricao = descricao
        # curso.Matriz_Curricular = matrizcurricular

        return curso