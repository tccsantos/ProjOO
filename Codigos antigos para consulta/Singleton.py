from abc import ABC, abstractmethod
from random import randint

# interface de matricula
class Matricula(ABC):
    @abstractmethod
    def exibir_status(self, turma):
        pass


class CLIMatricula(Matricula):
    def exibir_status(self, turma):
        print("Status da Turma:")
        print("Curso:", turma.curso.get_nome())
        for aluno in turma.alunos:
            print("Aluno:", aluno.get_nome())

class WebMatricula(Matricula):
    def exibir_status(self, turma):
        print("Status da Turma:")
        print("Curso:", turma.curso.get_nome())
        for aluno in turma.alunos:
            print("Aluno:", aluno.get_nome())

class GUIMatricula(Matricula):
    def exibir_status(self, turma):
        print("Status da Turma:")
        print("Curso:", turma.curso.get_nome())
        for aluno in turma.alunos:
            print("Aluno:", aluno.get_nome())

# Fachada
class FachadaEscola:
    __instance = None
    

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    
    def __init__(self):
        self.escola: Escola = None
        self.view = None

    def matricular(self, cod_aluno, cod_curso, turma):
        curso = self.escola.get_curso(codigo = cod_curso)
        if curso == None:
            curso = Curso('curso')
            self.escola.cursos[cod_curso]
        if not turma:
            turma = Turma()    
        turma.set_curso(curso)
        aluno = self.escola.get_aluno(cod_aluno)
        if aluno == None:
            aluno = Aluno(cod_aluno, 'nome')
        turma.add_aluno(aluno)

    def exibir_status(self, turma):
        self.view.exibir_status(turma)



class Aluno:
    def __init__(self, matricula, nome):
        self.__matricula = matricula
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula

class Curso:
    def __init__(self, nome):
        self.__nome = nome
        self.turmas = []
    
    def get_nome(self):
        return self.__nome
    
class Turma:
    def __init__(self):
        self.curso = None
        self.alunos = []

    def set_curso(self, curso):
        self.curso = curso

    def add_aluno(self, aluno):
                self.alunos.append(aluno)
                return

class Escola:

    def __init__(self) -> None:
        self.cursos: dict[Curso] = {}
        self.alunos: dict[Curso] = {}

    def get_curso(self, codigo):
        return self.cursos.get(codigo)

    def get_aluno(self, codigo):
        return self.alunos.get(codigo)

class main:
    def __init__(self):
        self.escola = Escola()
        self.cli_matricula = CLIMatricula()
        self.web_matricula = WebMatricula()
        self.gui_matricula = GUIMatricula()
        self.fachada = FachadaEscola()
        self.fachada.escola = self.escola
        self.fachada.view = self.cli_matricula

    def executa_teste(self):
        # Adiciona um curso
        curso = Curso("Matemática")
        self.escola.cursos["MAT"] = curso

        # Adiciona um aluno
        aluno = Aluno("001", "João")
        self.escola.alunos["001"] = aluno

        # Cria uma turma e matricula o aluno
        turma = Turma()
        self.fachada.matricular("001", "MAT", turma)

        # Exibe o status da turma usando diferentes views
        #self.fachada.exibir_status(turma)  # CLIView
        self.fachada.view = self.web_matricula
        #self.fachada.exibir_status(turma)  # WebMatricula
        self.fachada.view = self.gui_matricula
        #self.fachada.exibir_status(turma)  # GUIMatricula

        segundo = FachadaEscola()
        terceiro = FachadaEscola()
        if self.fachada == segundo == terceiro: print("São iguais!!!")
        else: print("Erro no singleton")


# Executa o teste
teste = main()
teste.executa_teste()

