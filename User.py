from Abstract import User, Book



class StudentUserType(User):
    def __init__(self, name: str, cpf: str, ageOfBirth: str, connection, reservation: set[Book] | None = None, loan: list[Book] | None = None):
        super().__init__(name, cpf, ageOfBirth, connection, reservation, loan)
    
    def isType(self) -> str:
        return "Student"


class TeacherUserType(User):
    def __init__(self, name: str, cpf: str, ageOfBirth: str, connection, reservation: set[Book] | None = None, loan: list[Book] | None = None):
        super().__init__(name, cpf, ageOfBirth, connection, reservation, loan)
    
    def isType(self) -> str:
        return "Teacher"
    