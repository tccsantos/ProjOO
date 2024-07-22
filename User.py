from Abstract import User, Book



class StudentUserType(User):
    def __init__(self, name: str, cpf: str, ageOfBirth: str, connection, reservation: set[int] | None = None, loan: list[int] | None = None):
        super().__init__(name, cpf, ageOfBirth, connection, reservation, loan)
    
    def isType(self) -> str:
        return "Student"
    
    def presentation(self, books: set[Book]) -> None:
        print(f'Aluno: {self.getName()}\ncpf: {self.getCpf()}\nIdade: {self.getAge()}\n')
        print("Livros emprestados atualmente:")
        for book in books:
            print(book)
            print()
        
        print("\nLivros que já foram emprestados e devolvidos: \n")
        for book in self.getHistory():
            print(book)
            print()



class TeacherUserType(User):
    def __init__(self, name: str, cpf: str, ageOfBirth: str, connection, reservation: set[Book] | None = None, loan: list[Book] | None = None):
        super().__init__(name, cpf, ageOfBirth, connection, reservation, loan)
    
    def isType(self) -> str:
        return "Teacher"
    
    def presentation(self, books: set[Book]) -> None:
        print(f'Professor: {self.getName()}\ncpf: {self.getCpf()}\nIdade: {self.getAge()}\n')
        print("Livros emprestados atualmente:\n")
        for book in books:
            print(book)
            print()
        
        print("\nLivros que já foram emprestados e devolvidos: \n")
        for book in self.getHistory():
            print(book)
            print()
    