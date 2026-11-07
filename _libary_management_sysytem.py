class libary():
    def __init__(self,list,name):
        self.name = name
        self.booklist = list
        self.lendic = {}

    def displayBooks(self):
        print(f"We have this following books in our libary {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book in self.booklist:
            self.booklist.remove(book)
            self.lendic.update({book:user})
            print("Yes now you can lend this book")
        else:
            print(f"Sorry this book is being used by {self.lendic[book]}")

    def addbooks(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnbook(self,book):
        self.booklist.remove(book)

if __name__ =='__main__':
    lib = libary(['fearless heros','python','RD sharma','Pathfinder','Blackbook'],"studybuddy")

    while(True):
        print(f"welcome to the {lib.name} libary . \nHow can we help you")
        print("1. Display the book")
        print("2. lend the book")
        print("3. add the book")
        print("4. return the book")

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            lib.displayBooks()

        elif user_choice == 2:
            book = input("Enter a name of book which you want to lend:")
            name = input("Enter your Name:")
            lib.lendbook(name,book)

        elif user_choice == 3:
            book = input("Ente a Name of the book which you want to add:")
            lib.addbooks(book)

        elif user_choice == 4:
            book = input("Enter a Name of th book which you want to return:")
            # name = input("Enter your name:")
            lib.returnbook(book)

        else:
            print("choose the correct option given")


        user_choice2 = input("press q to quit and c to continue: ")
        if user_choice2 == "q":
            exit()
        elif user_choice2 == "c":
            continue
        else:
            ("Invaild option ")








        