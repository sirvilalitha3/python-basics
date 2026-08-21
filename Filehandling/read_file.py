 File Handling - Reading a File

with open("sample.txt", "r") as file:     #r(to read),r+(to read & write)

    # data = file.read()
    # Reads the entire content of the file

    # data = file.read(1)
    # Reads the specified number of characters

    # data = file.readline()
    # Reads a single line from the file

    data = file.readlines()
    # Reads all lines and returns them as a list of strings

    print(data)
