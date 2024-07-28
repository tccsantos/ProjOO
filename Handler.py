from Abstract import Handler, User, Book

#Nessas classes, pode-se observar o princípio da Responsabilidade Única, 
#já que a classe Handler tem uma única responsabilidade(método),de averiguar se algo está elegivel(livro/user/empréstimo).


class BookAvaliabilityHandler(Handler):
    
    def eligible(self, book: Book, user: User):
        if book.isComposite() == True: 
            print("Error!")
            return KeyError
        
        result = True in book.getAvaliabe()

        if self.successor and result:
            return self.successor.eligible(book, user)

        else:
            return result


class UserEligibilityHandler(Handler):
        

    def eligible(self, book: Book, user: User):
        total = self.manager.getMultipleLimit(user)
        i = 0
        for item in user.getLoan():
            if item == book.getId():
                i +=1
        if i >= total:
            result: bool = False
        else:
            result: bool = True

        if self.successor and result:
            return self.successor.eligible(book, user)

        else:
            return result


class LoanLimitHandler(Handler):

    def eligible(self, book: Book, user: User):
        total = self.manager.getLoanLimit(user)

        result = len(user.getLoan()) < total

        if self.successor and result:
            return self.successor.eligible(book, user)

        else:
            return result
