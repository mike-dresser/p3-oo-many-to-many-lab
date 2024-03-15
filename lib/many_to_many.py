class Author:
    all = []

    def __init__(self, name) -> None:
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        # total = 0
        # for contract in self.contracts():
        #     total += contract.royalties
        # return total

        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title) -> None:
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]


class Contract:
    all = []

    def __init__(self, author_obj, book_obj, date, royalties) -> None:
        self.book = book_obj
        self.author = author_obj
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception('Author must be a <Author> object')  

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception('Book must be a <Book> object')  
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if type(date) == str:
            self._date = date
        else:
            raise Exception('Date must be in str format.')   
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if type(royalties) in (int, float):
            self._royalties = royalties
        else:
            raise Exception('Royalties must be a number')
            
    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]

        

        