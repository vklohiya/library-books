

class BookNode:
    def __init__(self, bkID, availCount):
        self.bookID = bkID
        self.availCount = availCount
        self.checkoutCount = 0
        self.left = None
        self.right = None

