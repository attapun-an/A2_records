import pickle # library required to create binary files

class Hero:

    def __init__(self): # constructor
        # self.heroID = ""
        self.heroName = ""
        self.age = 0
        self.height = 0
        self.mass = 0
        self.level = 0 # goes from  0-5

# main menu
    # if 0 exit

    # elif 1 add a hero


    # elif 2 display hero (by reading the file)

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

# add hero ()
def add_hero():
    # create a new temp instance of the hero
    temp = Hero()
    # modify said instance
    temp.heroName = input("Input Hero Name: ")
    temp.age = input_number(18, 150, "Input Age: ")
    temp.height = input_number(0, 300, "Input Height (cm): ")
    temp.mass = input_number(0,200, "Input Mass (kg): ")
    temp.level = input_number(0, 5, "Input Level (0-5): ")








# input_number (max, min, message)  makes sure it's actually a number too and returns that


# modify hero()

# load the file

# display said file




