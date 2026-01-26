# Melissa Favelli
# CSD325 Advanced Python
# Assignment 1.3
# 12/8/25



def beer_bottles(bottles):
# while loop as long as the number of bottles is greater than 1
    while bottles > 1:
        print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.")
        print("Take one down and pass it around, " + str(bottles - 1) + " bottles of beer on the wall.")
        print() # blank line to separate the verses

        bottles = bottles -1 # reduce bottle count by 1 each time

# when only one bottle is left, change lyrics to singular version
    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take it down, pass it around, no more bottles of beer on the wall.")
        print()

def main():
    # ask user how many beer bottles to start with
    user_input = input("How many beer bottles are on the wall?")

    starting_bottles = int(user_input)

    # check that the number is positive
    if starting_bottles <= 0:
        print("You need at least 1 bottle to sing the song...")
        return # exit the program

    beer_bottles(starting_bottles)

    print("I suggest buying more beer.")
    
    
main()