import csv
import node
# Initializing the filepaths
input_file = "inputPS9.txt"
output_file = "outputPS9.txt"

class LibraryTree:
    def __init__(self):
        self._readBookList()
        self._rootNode = "Dummy"

    @property
    def rootNode(self):
        return self._rootNode

    def _readBookList(self):
        """This function reads the book ids and the number of copies available from the inputPS9.txt file.
        The input data is used to populate the tree."""
        with open(input_file, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                pass

    def _chkInChkOut(self, bkID, inOut):
        """This function is triggered when the either of the tag is encountered in the promptsPS9.txt file:
         "checkOut: 100005" or "checkIn: 100005".
        This function updates the check in / check out status of a book based on the book id.
        If a book is checked out, the available count is reduced by one and the checkout counter is incremented by one.
        If a book is checked in, the available counter is incremented and the checkout counter is not altered."""
        pass

    def _getTopBooks(self, bkNode):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "ListTopBooks". The
        function searches through the list of books and the checkout counter and determines which are the top three books
        that have been checked out the most and lists those books and the number of times they have been checked out into
        the outputPS9.txt file as shown below.
        "Top Books 1: 100001, 5
        Top Books 2: 100003, 2
        Top Books 3: 100002, 1"
        """
        pass

    def _notIssued(self, bkNode):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "BooksNotIssued"
        The function searches the list of books in the system and generates a list of books which have never been checked
        out. The output of this is  appended to the outputPS9.txt file as follows:
        "List of books not issued:
        100004
        100020"
        """
        pass

    def _findBook(self, eNode, bkID):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "findBook: 100005"
        If the book id is found, the below string is appended to the into the outputPS9.txt file:
        "Book id xx is available for checkout"
        If the book id is found but all the copies have been checked out, below string is output to the outputPS9.txt file:
        "All copies of book id xx have been checked out"
        If the book id is not found it outputs the below string into the outputPS9.txt file:
        "Book id xx does not exist."
        """
        pass

    def _stockOut(self, eNode):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "ListStockOut"
        This function searches for books for which all the available copies have been checked out and outputs the list
        into the outputPS9.txt file as follows:
        "All available copies of the below books have been checked out: 100001"
        """
        pass

    def printBooks(self, bkNode):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "printInventory"
        This function prints displays the sequence of books in ascending order of book id and the
        available number of copies into the file outputPS9.txt as follows:
        "There are a total of xx book titles in the library.
        100001, 0
        100002, 5
        100003, 13"
        """
        pass


