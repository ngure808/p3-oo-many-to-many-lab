class Author:

    def __init__(self, name):
        self.name = name
        self._contracts = []

    def add_contract(self, contract):
        self._contracts.append(contract)

    def contracts(self):
        return self._contracts
    
    def books(self):
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.add_contract(contract)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

        


class Book:
    
    def __init__(self,title):
        self.title = title
        self._contracts = []

    def add_contract(self, contract):
        self._contracts.append(contract)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.validate_author(author)
        self.validate_book(book)
        self.validate_date(date)
        self.validate_royalties(royalties)
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        author.add_contract(self)
        book.add_contract(self)
        Contract.all.append(self)  

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    
    def validate_author(self,author):
        if not isinstance(author,Author):
            raise Exception("The author must be an instance of the Author class")
        
    def validate_book(self,book):
        if not isinstance(book,Book):
            raise Exception("The book must be an instance of the Book class")

    def validate_date(self,date):
        if not isinstance(date,str):
            raise Exception("The date value must be a string")
        
    def validate_royalties(self,royalties):
        if not isinstance(royalties,int):
            raise Exception("The royalties value must be an integer")