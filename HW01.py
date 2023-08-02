########
#Part 1#
########

# Replace the pass with your code according to the instructions in the HW01 Prompt
# You can use the test cases at the bottom in order to test your code

def add_digits(int_list) :
    digit = ""
    for x in int_list :
        digit = digit + str(x)
    return int(digit)

def string_modifier(str_list) :
    return [x*2 for x in str_list if x.islower() and x.isalpha()]

def contacts(phone_numbers):
    a = ""
    b = []
    for item in phone_numbers :
        item.split()
        for char in item :
            if char.isdigit() :
                a += char
        b.append(a)
        a = ""
    unique_list = [num for num in b if len(num) == 10 and num[0:3] == '404']
    #print(set(unique_list))
    return len(set(unique_list))

def shelf_books(book_list) :
    books = [book[0] for book in book_list]
    author_list = [author[-1] for author in book_list]
    last_names = [name.split()[-1] for name in author_list]
    listed = list(zip(last_names , books))
    listed.sort(key = lambda x:x[0])
    movies = [movie[1] for movie in listed]
    #print(listed)
    return movies
   
def classics(books, chapters, authors) :
    return {book : chapter[0]>=20 and chapter[1] != "J. Joyce" for book , chapter in list(zip(books,list(zip(chapters,authors))))}

def writers(authors, age_at_death) :
    return {num + 1 :val[0] for num , val in enumerate(list(zip(authors,age_at_death)).sort(key = lambda x:x[1] , reverse = True))}
    

########
#Part 2#
########

# Create the Book and Library classes below as specified by the HW01 prompt
# You will need to use the correct function/method names!

class Book:
    def __init__(self, name, genre, year, pages) :
        self.name = name
        self.genre = genre
        self.year = year
        self.pages = pages

    def __lt__(self, other) :
        return self.year < other.year

    def __eq__ (self, other) :
        return self.name == other.name and self.year == other.year and self.pages == other.pages

    def __repr__ (self) :
        return f"{self.name} is a {self.pages} pages long {self.genre} book published in {self.year}."

class Library :
    def __init__(self, name, book_list) :
        self.name = name        
        self.book_list = []
        fiction = 0
        for each in book_list :
            self.book_list.append(Book(each[0], each[1], each[2], each[3]))
        for each1 in self.book_list :
            if each1.genre == "Fiction" :
                fiction += 1
        self.num_fiction = fiction


    def __lt__(self , other) :
        return self.num_fiction < other.num_fiction

    def __repr__(self) :
        return f"{self.name} is a library where {self.num_fiction} of the {len(self.book_list)} books are fiction."

    def add_book(self , new_book) :
        book = Book(new_book[0], new_book[1], new_book[2], new_book[3])
        self.book_list.append(book)
        if book.genre == "Fiction" :
            self.num_fiction += 1
        
        #no attribute .name for a list, I need to convert to a Book and then do .name

    


if __name__ == '__main__' :
    #********************************************************************************************************************
    # Uncomment the necessary lines below to test specific functions and classes in command line or terminal            #
    # After you test your functions, MAKE SURE TO RE-COMMENT OUT ALL PRINT STATEMENTS BEFORE SUBMITTING IN GRADESCOPE   #
    #********************************************************************************************************************

    # Part 1: test add_digits
    int_list = [1, 4, 3, 8, 1]
    #print(add_digits(int_list))

    # Part 1: test string_modifier
    str_list = ['ace', 'BLuE42', 'b4a', 'cs']
    #print(string_modifier(str_list))

    # Part 1: test contacts
    phone_numbers = ['4o04592,,,0000', '-%#3&0&3!0', '4!0!4!5!9!2!0!0!0!0!','908',
                     '4###04...-,,,,,78', '404$$$193--8173', '3^^0--,30']
    #print(contacts(phone_numbers))

    # Part 1: test shelf_books
    book_list = [('It', 'Stephen King'), ('Gone Girl', 'Gillian Flynn'), ('Verity', 'Colleen Hoover')]
    #print(shelf_books(book_list))

    # Part 1: test classics
    books = ['Around the Moon', 'Ulysses', '1984', 'Don Quixote']
    chapters = [25, 45, 12, 90]
    authors = ['J. Verne', 'J. Joyce', 'G. Orwell', 'M. Cervantes']
    #print(classics(books, chapters, authors))

    # Part 1: test writers
    authors = ['J. Swift', 'T. Paine', 'C. Dickens', 'H. Melville']
    age_at_death = [78, 73, 58, 72]
    #print(writers(authors, age_at_death))

    # Part 2: Class 1
    #Book1 = Book('Normal People', 'Fiction', 2018, 273) 
    #Book2 = Book('The Catcher in the Rye', 'Fiction', 1951, 234)
    #Book3 = Book('Normal People', 'Some unknown genre', 2018, 273) 
    #print(Book1.name)
    #print(Book1.genre)

    #print(Book1 < Book2)

    #print(Book1 == Book2)  
    #print(Book1 == Book3) 

    #print(Book1) 

    # Part 2: Class 2
    book_list = [['Normal People', 'Fiction', 2018, 273],
                 ['The Catcher in the Rye', 'Fiction', 1951, 234],
                 ['The Goal', 'Fiction', 1984, 384],
                 ['How to Think Like a Computer Scientist', 'Textbook', 2002, 274]]
    Bohongs_Library = Library('Bohong’s Books', book_list) 
    print(Bohongs_Library.name)

    print(Bohongs_Library)

    Erins_Library = Library('Erin’s Excellent Essays',[['Arriving Today: From Factory to Front Door', 'Nonfiction', 2021, 384]])
    print(Bohongs_Library < Erins_Library)
 
    book1 = ['The Hunger Games', 'Fiction', 2008, 374] 
    Bohongs_Library.add_book(book1) 
    print(Bohongs_Library)
 






