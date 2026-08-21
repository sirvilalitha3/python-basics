# File Handling - Create and Append

# "x" mode creates a new file
try:
    with open("sample.txt", "x") as file:    #x to create file
        file.write("Hello Python!\n")
        file.write("Learning File Handling.\n")

    print("File created successfully!")

except FileExistsError:  #if file exist
    print("File already exists.")


# "a" mode adds new content to the existing file
with open("sample.txt", "a") as file:
                    #a(to append),a+(to append and read)

    file.write("This line was added using append mode.\n")

print("Data added successfully!")