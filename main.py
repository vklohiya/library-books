import helper

# Initializing the filepaths
prompt_file = "promptsPS9.txt"


def main():
    """This is the main function which reads the promptsPS9.txt and test the binary ATD"""
    libraryTree = helper.LibraryTree()
    with open(prompt_file, "r") as f:
        for line in f.readlines():
            if "check" in line:
                line = line.split(':')
                libraryTree._chkInChkOut(line[0], line[1])
            elif "ListTopBooks" in line:
                libraryTree._getTopBooks(libraryTree)
            elif "BooksNotIssued" in line:
                libraryTree._notIssued(libraryTree)
            elif "ListStockOut" in line:
                libraryTree._stockOut(libraryTree)
            elif "printInventory" in line:
                libraryTree.printBooks(libraryTree)
            elif "findBook" in line:
                line = line.split(':')
                libraryTree._findBook(libraryTree, line[1])
            else:
                print("Action not defined")

if __name__ == "__main__":
    main()
