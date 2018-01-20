import pickle # library required to create binary files

class Hero:

    def __init__(self): # constructor
        # self.heroID = ""
        self.heroName = ""
        self.age = 0
        self.height = 0
        self.mass = 0
        self.level = 0 # goes from  0-5


# input_number (max, min, message)  makes sure it's actually a number too and returns that
def input_number(min_val, max_val, message):
    valid = False
    while not valid:
        try:
            inp_num = int(input(message))
            if min_val <= inp_num <= max_val:
                valid = True
            else:
                print("Please enter a number between {0} and {1}".format(min_val, max_val))
        except ValueError:
            print("Please enter a number")
    return inp_num


def add_hero():
    # create a new temp instance of
    temp = Hero()
    # modify said instance
    temp.heroName = input("Input Hero Name: ")
    temp.age = input_number(18, 150, "Input Age: ")
    temp.height = input_number(0, 300, "Input Height (cm): ")
    temp.mass = input_number(0, 200, "Input Mass (kg): ")
    temp.level = input_number(0, 5, "Input Level (0-5): ")
    # write to the file
    HeroMasterFile = open('Heroes.DAT', 'wb')  # open file for binary write
    pickle.dump(temp, HeroMasterFile)  # write temp(which is a record) to the binary file
    HeroMasterFile.close()  # close file


# load file(name of file) --> returns a list of instances?
def load_file(file_name):
    # open file
    HeroMasterFile = open(file_name, "rb")  # open in read binary
    # start with empty array
    heroes = []
    # append record from file to EOL
    heroes.append(pickle.load(HeroMasterFile))
    # return the array
    return heroes


# display array (array)
def display_list(array):
    # loop for each array element
    for instance in array:
        # print current array element
        print(instance)


# main menu
def main():
    main_run = True
    while main_run:
        usr_inp = input_number(0, 2, """
0 - exit
1 - add hero
2 - display
> """)
        # if 0 exit
        if usr_inp == 0:
            main_run = False
        # elif 1 add a hero
        elif usr_inp == 1:
            add_hero()
        # elif 2 display hero (by reading the file)
        elif usr_inp == 2:
            display_list(load_file("Heroes.DAT"))
            # HeoroesList = load_file("Heroes.DAT")

main()

#def test_code():
