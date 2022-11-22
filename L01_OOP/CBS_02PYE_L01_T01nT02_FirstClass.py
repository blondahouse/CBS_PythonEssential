# A review class
class Review:

    # Constructor
    def __init__(self, review):
        self.review = review

    # For call to str(). Prints readable form
    def __str__(self):
        return f'{self.review}'


# A book class
class Book:

    # Constructor
    def __init__(self, author, name, pub_year, genre):
        self.author = author
        self.name = name
        self.pub_year = pub_year
        self.genre = genre
        self.reviews = []

    # For call to str(). Prints readable form
    def __str__(self):
        show_reviews = ''
        for index, review in enumerate(self.reviews):
            show_reviews += f'\t\t{index + 1:04d} - {review}\n'
        return f'Book:\n' \
               f'\tAuthor - {self.author}\n' \
               f'\tName - {self.name}\n' \
               f'\tYear of publication - {self.pub_year}\n' \
               f'\tGenre - {self.genre}\n' \
               f'\tReviews:\n' \
               f'{show_reviews}'

    # For call to repr(). Prints object's information
    def __repr__(self):
        return f'<Book({repr(self.author)}, {repr(self.name)}, {repr(self.pub_year)}, {repr(self.genre)})>'

    def add_review(self, review):
        self.reviews.append(Review(review))


book001 = Book('orwell', '1984', 2015, 'fiction')
book001.add_review("bullshit")
book001.add_review("oh no")
book001.add_review("wow")

book002 = Book('qwer', 'asdf', 19, 'zxcv')

print(book001)

print(book001.__repr__())
print(book002.__repr__())
