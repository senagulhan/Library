library = []
while True:
    


    doing_what = input("Please write what you want to do?\n a)Add book\n b)Delete book\n c)Search book\n d)Borrow book\n e)Return book\n f)Library")

    if doing_what == "a":
        add_book = input("Please write down the writer and the name of the book you want to add to the library: ")
        library.append(add_book)
        print(add_book + " added to the library.")
    elif doing_what == "b":
        delete_book = input("Please write down the name of the book you want to delete from the library: ")
        if delete_book in library:
            library.remove(delete_book)
            print(delete_book + " is deleted from the library.")
        else:
            print("There is no such book in the library.")
    elif doing_what == "c":
        search_book = input("Please enter the name of the book you are searching for: ")
        if search_book in library:
            print("The " + search_book + " is in the library.")
        else:
            print("There is no such book in the library.")
    elif doing_what == "d":
        borrow_book = input("Please enter the name of the book you want to borrow: ")
        if borrow_book in library:
            library.remove(borrow_book)
            print("You can borrow " + borrow_book)
        else:
            print("There is no such book in the library.")
    elif doing_what == "e":
        return_book = input("Please enter the name of the book you want to return: ")
        library.append(return_book)
        print("The book " + return_book + " has been returned to the library.")
    elif doing_what == "f":
        print("Current library collection:")
        for book in library:
            print(book)
    else:
        print("Please enter a valid option.")

