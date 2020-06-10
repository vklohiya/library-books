import csv

# Initializing the filepaths
input_file = "inputPS9.txt"
output_file = "outputPS9.txt"
output_handle = open(output_file, "w")


class LibraryTree:
    def __init__(self):
        self.rootNode = None
        self._readBookList()

    def _readBookList(self):
        """This function reads the book ids and the number of copies available from the inputPS9.txt file.
        The input data is used to populate the tree."""
        with open(input_file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if any(val in (None, "") for val in row):
                    output_handle.write(f"\nValue Missing for {row}")
                    continue
                if self.rootNode is None:
                    self.rootNode = BookNode(int(row[0]), int(row[1]))
                else:
                    self.rootNode.insertBook(int(row[0]), int(row[1]))

    def _notIssued(self, bkNode):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "BooksNotIssued"
        The function searches the list of books in the system and generates a list of books which have never been checked
        out. The output of this is  appended to the outputPS9.txt file as follows:
        "List of books not issued:
        100004
        100020"
        """
        output_handle.write("\nList of books not issued:")
        bkNode.printTree(notIssued=True)

    def _stockOut(self, eNode):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "ListStockOut"
        This function searches for books for which all the available copies have been checked out and outputs the list
        into the outputPS9.txt file as follows:
        "All available copies of the below books have been checked out: 100001"
        """
        output_handle.write("\nAll available copies of the below books have been checked out: ")
        eNode.printTree(stockOut=True)

    def _chkInChkOut(self, bkID, inOut):
        """This function is triggered when the either of the tag is encountered in the promptsPS9.txt file:
         "checkOut: 100005" or "checkIn: 100005".
        This function updates the check in / check out status of a book based on the book id.
        If a book is checked out, the available count is reduced by one and the checkout counter is incremented by one.
        If a book is checked in, the available counter is incremented and the checkout counter is not altered."""
        resNode = self.rootNode.nodeExists(self.rootNode, bkID)
        if resNode is None:
            output_handle.write(f"\nBook id {bkID} does not exist.")
        else:
            if inOut == "checkOut":
                if resNode.availCount > 0:
                    resNode.checkoutCount += 1
                    resNode.availCount -= 1
                else:
                    output_handle.write(f"\nAll available copies of the book id {resNode.bkID} have been checked out.")
            elif inOut == "checkIn":
                if resNode.checkoutCount > 0:
                    resNode.checkoutCount -= 1
                    resNode.availCount += 1
                else:
                    output_handle.write(f"\nAll available copies of the book id {resNode.bkID} have been checked-in")
            else:
                output_handle.write("\nOnly checkOut and checkIn strings are supported.")

    def _findBook(self, eNode, bkID):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "findBook: 100005"
        If the book id is found, the below string is appended to the into the outputPS9.txt file:
        "Book id xx is available for checkout"
        If the book id is found but all the copies have been checked out, below string is output to the outputPS9.txt file:
        "All copies of book id xx have been checked out"
        If the book id is not found it outputs the below string into the outputPS9.txt file:
        "Book id xx does not exist."
        """
        resNode = self.rootNode.nodeExists(eNode, bkID)
        if resNode is None:
            output_handle.write(f"\nBook id {bkID} does not exist.")
        else:
            if resNode.availCount != 0:
                output_handle.write(f"\nBook id {resNode.bkID} is available for checkout")
            else:
                output_handle.write(f"\nAll copies of book id {resNode.bkID} have been checked out")


    def _getTopBooks(self, bkNode):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "ListTopBooks". The
        function searches through the list of books and the checkout counter and determines which are the top three books
        that have been checked out the most and lists those books and the number of times they have been checked out into
        the outputPS9.txt file as shown below.
        "Top Books 1: 100001, 5
        Top Books 2: 100003, 2
        Top Books 3: 100002, 1"
        """
        # Initialize the dictionary
        bookDict, k = {}, 3
        # Calling the recursive function to convert the tree into dictionary
        bkNode.kTopBooksUtil(bkNode, bookDict)
        kTop = {k: v for k, v in sorted(bookDict.items(), key=lambda item: item[1], reverse=True)}
        for i in range(k):
            output_handle.write(f"\nTop Books {i + 1}: {list(kTop.keys())[i + 1]}, {list(kTop.values())[i + 1]}")

    def printBooks(self, bkNode):
        """This function is triggered when the following tag is encountered in the promptsPS9.txt file: "printInventory"
        This function prints displays the sequence of books in ascending order of book id and the
        available number of copies into the file outputPS9.txt as follows:
        "There are a total of xx book titles in the library.
        100001, 0
        100002, 5
        100003, 13"
        """
        output_handle.write(f"\nThere are a total of {self.getBookTitleCount(bkNode)} book titles in the library.")
        bkNode.printTree()

    def getBookTitleCount(self, bkNode):
        """This function recursively traverse the tree and return the total nodes in the tree"""
        count = 1
        if bkNode is None:
            return 0
        else:
            count += self.getBookTitleCount(bkNode.left)
            count += self.getBookTitleCount(bkNode.right)
        return count


class BookNode:
    def __init__(self, bkID, availCount):
        self.bkID = bkID
        self.availCount = availCount
        self.checkoutCount = 0
        self.left = None
        self.right = None

    def insertBook(self, bkID, availCount):
        """ Insert method to create book nodes in the library tree"""
        if self.bkID:
            if bkID < self.bkID:
                if self.left is None:
                    self.left = BookNode(bkID, availCount)
                else:
                    self.left.insertBook(bkID, availCount)
            elif bkID > self.bkID:
                if self.right is None:
                    self.right = BookNode(bkID, availCount)
                else:
                    self.right.insertBook(bkID, availCount)
        else:
            self.bkID = bkID

    def findBook(self, bookId):
        """ Recursively search for book nodes in the library tree"""
        if bookId < self.bkID:
            if self.left is None:
                return str(bookId)+" Not Found"
            return self.left.findBook(bookId)
        elif bookId > self.bkID:
            if self.right is None:
                return str(bookId)+" Not Found"
            return self.right.findBook(bookId)
        else:
            output_handle.write(f"\n{str(self.bkID)} is found")

    def printTree(self, stockOut=False, notIssued=False):
        """This function traverses the tree in preorder and print the all the available books by default,
        if stockOut flag is provided it prints the books whose stock is out,
        if notIssue is provided it prints the books which are not issued"""
        if self.left:
            self.left.printTree(stockOut=stockOut, notIssued=notIssued)
        if stockOut and self.availCount == 0:
            output_handle.write(f"\n{str(self.bkID)}")
        if notIssued and self.checkoutCount == 0:
            output_handle.write(f"\n{str(self.bkID)}")
        if not stockOut and not notIssued:
            output_handle.write(f"\n{self.bkID}, {self.availCount}")
        if self.right:
            self.right.printTree(stockOut=stockOut, notIssued=notIssued)

    def nodeExists(self, node, bookID):
        """ This Function traverse the tree in pre-order and return the given node if exists. """
        # Node is null
        if node is None:
            return None

        # or book is present at the node
        if node.bkID == bookID:
            return node

        # Traverse the left subtree
        res1 = self.nodeExists(node.left, bookID)
        if res1 is not None:
            return res1  # node found, no need to look further

        # Traverse the right subtree
        res2 = self.nodeExists(node.right, bookID)
        return res2

    def kTopBooksUtil(self, root, bookDict):
        """This function Traversing the tree in pre-order and storing the book id and checkoutCount in dictionary"""
        # Visiting the left node first
        if root.left:
            self.kTopBooksUtil(root.left, bookDict)
        # Visiting the root node
        bookDict[root.bkID] = root.checkoutCount
        # Visiting the right nodes
        if root.right:
            self.kTopBooksUtil(root.right, bookDict)






