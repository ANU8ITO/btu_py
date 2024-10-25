class libraryAccount:
    def __init__(self, account_holder, account_category = "Basic"):
        self.account_holder = account_holder
        self.__borrowed_books = 0
        self.__account_category = account_category
        self.__account_limit = self.__set_account_limit()
        
    def __set_account_limit(self):
        if self.__account_category == "Basic":
            return 5
        elif self.__account_category == "Premium":
            return 10
        elif self.__account_category == "Elite":
            return 50
        else:
            return 300  # Default limit for undefined categories
        
    def borrow_books(self, amount):
        if amount > 0 and self.__borrowed_books < self.__account_limit:
            self.__borrowed_books += amount
            print(f"Successfully borrowed {amount} books")
        elif amount <= 0:
            print(f"Invalid amount!")
        elif self.__borrowed_books >= self.__account_limit:
            print(f"Account limit exceeded! Current limit: {self.__account_limit}")

    def return_books(self, amount):
        if amount > 0 and amount <= self.__borrowed_books:
            self.__borrowed_books -= amount
            print(f"Successfully returned {amount} books")
        else:
            print(f"Invalid return amount!")
            
    def get_borrowed_books(self):
        print(f"{self.account_holder} you have borrowed {self.__borrowed_books} books")
    
    def get_account_category(self):
        print(f"{self.account_holder} your account category is {self.__account_category}")

    
george = libraryAccount("George", "Elite")

george.borrow_books(5)
george.get_borrowed_books()
george.return_books(3)
george.get_borrowed_books()
george.get_account_category()