# test file opening
def file_open(file_name):
    f = open(file_name + ".txt", "w")
    f.write("Hi")

file_open("test")
