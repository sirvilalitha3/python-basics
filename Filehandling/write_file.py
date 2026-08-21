# File Handling - Writing to a File

# Open the file in write mode
# "w" creates the file if it doesn't exist.
# If the file already exists, its old content will be overwritten.
#with open("sample.txt", "w") as file: can use with to close the file automatically
f = open("sample.txt", "w")  #w(to write),w+(to read & write)

# List containing multiple strings
lines = [
    "Hello everyone\n",
    "Writing multiple strings\n",
    "This is the third line"
]

# Write multiple strings to the file
f.writelines(lines)

# Close the file 
f.close()

print("Data written successfully!")

