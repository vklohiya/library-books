
class BookNode:
    def __init__(self, bkID, availCount):
        self.bkID = bkID
        self.availCount = availCount
        self.checkoutCount = 0
        self.left = None
        self.right = None
        
# Insert method to create nodes
    def insertBook(self, bkID, availCount):

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

    # find method to compare the value with nodes
    def findBook(self, bookId):
        if bookId < self.bkID:
            if self.left is None:
                return str(bookId)+" Not Found"
            return self.left.findBook(bookId)
        elif bookId > self.bkID:
            if self.right is None:
                return str(bookId)+" Not Found"
            return self.right.findBook(bookId)
        else:
            print(str(self.bkID) + ' is found')

    # Print the tree based on stockOut and notIssued flags
    def printTree(self, stockOut=False, notIssued=False):
        if self.left:
            self.left.printTree(stockOut=stockOut, notIssued=notIssued)
        if stockOut and self.availCount == 0:
            print(self.bkID)
        if notIssued and self.checkoutCount == 0:
            print(self.bkID)
        if not stockOut and not notIssued:
            print(f"{self.bkID}, {self.availCount}")
        if self.right:
            self.right.printTree(stockOut=stockOut, notIssued=notIssued)


