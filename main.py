import node
import os

# Initializing the filepaths
prompt_file = "promptsPS9.txt"
input_file = "inputPS9.txt"

def main():
    """This is the main function which reads the promptsPS9.txt and test the binary ATD"""
    if not os.path.exists(prompt_file) or not os.path.exists(input_file):
        print("inputPS9.txt or promptPS9.txt file not found.")
        exit(1)
    libraryTree = node.LibraryTree()
    if libraryTree.getBookTitleCount(libraryTree.rootNode) == 0:
        print("inputPS9.txt is empty")
        exit(1)
    with open(prompt_file, "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            "promptPS9.txt is empty"
            exit(1)
        for line in lines:
            line.strip()
            if "check" in line:
                line = line.split(':')
                libraryTree._chkInChkOut(int(line[1]), line[0])
            elif "ListTopBooks" in line:
                libraryTree._getTopBooks(libraryTree.rootNode)
            elif "BooksNotIssued" in line:
                libraryTree._notIssued(libraryTree.rootNode)
            elif "ListStockOut" in line:
                libraryTree._stockOut(libraryTree.rootNode)
            elif "printInventory" in line:
                libraryTree.printBooks(libraryTree.rootNode)
            elif "findBook" in line:
                line = line.split(':')
                libraryTree._findBook(libraryTree.rootNode, int(line[1]))
            else:
                pass

if __name__ == "__main__":
    main()
