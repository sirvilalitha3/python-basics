with open("sample.txt","r") as file:
    #data=file.read() to read entire content in file
    #data=file.read(1) to read specific characters
    #data=file.readline() to read single line
    data=file.readlines()
    print(data)