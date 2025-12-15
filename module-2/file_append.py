# Melissa Favelli
# CSD205 Intro to Programming with Python
# July 6, 2025
# Module 5 Assignment


def main():
    # prompt for file name
    file_name_input = input("Enter a name for your file: ")
    file_name = file_name_input + "_data.txt"

    # prompt for name, address & phone number
    name = input("Enter your name: ")
    street_address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")

    # write the data to the file
    with open(file_name, "q") as file:
        file.write(name + "," + street_address + "," + phone_number + "\n")

    # read and display file contents
    print("\nThe file contents are as follows:")
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())

main()