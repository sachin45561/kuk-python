file = open("example.txt", "r")
content = file.read()
print(content)
file.close()


# r+ – Read and Write

# Opens a file for both reading and writing.

# File must exist, otherwise throws an error.

# Writing starts from the beginning and will overwrite existing content.

file = open("example.txt", "r+")
file.write("Hello")
file.seek(0)  # Move pointer to start
print(file.read())
file.close()


# w – Write

# Opens a file for writing only.

# Creates a new file if it doesn’t exist.

# Erases the existing content if the file exists.

file = open("newfile.txt", "w")
file.write("This is a test file.")
file.close()


# w+ – Write and Read

# Opens a file for reading and writing.

# Creates a new file if not exists.

# Overwrites content if exists.

file = open("test.txt", "w+")
file.write("Python Programming")
file.seek(0)
print(file.read())
file.close()

# a – Append

# Opens a file for appending data.

# Creates file if does not exist.

# New data is written at the end of file.

# Existing content is not erased.

file = open("log.txt", "a")
file.write("\nNew log entry.")
file.close()


# a+ – Append and Read

# Opens a file for reading and appending.

# File pointer is at the end.

# Creates file if not exists.

# To read, need to use seek(0).

file = open("data.txt", "a+")
file.write("\nAppended line")
file.seek(0)
print(file.read())
file.close()


# Closing a File

# Always close a file after use to free system resources.

file = open("example.txt", "r")
print(file.read())
file.close()


# Opening a File with with Clause

# Using with automatically closes the file, even if an error occurs.
# No need to call file.close() manually.

# Example using with

with open("example.txt", "r") as file:
    data = file.read()
    print(data)