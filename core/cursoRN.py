from core.cursoDAO import CursoDAO
from core.models import Curso

class CursoRN():

    def all(self):
        return CursoDAO().selectAll()

    def one(self):
        return CursoDAO().selectOne()

    def update(self, curso):
        CursoDAO().update(curso)

    def create(self, curso):
        CursoDAO().insert(curso)

    def delete(self, curso):
        CursoDAO().delete(curso)