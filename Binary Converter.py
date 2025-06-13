def is_binary(string):
    if string == "":
        return (False)

    for i in range (len(string)):
        if string[i] != "1" and string[i] !="0":
            return(False)

    return (True)

def binary_to_denary(bin):
    total = 0
    for i in range (len(bin)):
        if bin[-(i+1)] == "1":
            total = total +(2**i)

    return total


def denary_to_binary(den):
    bin_number = ""
    binary_number_place = 1
    num_of_bin_places = 1

    while binary_number_place < den:
        binary_number_place = binary_number_place * 2
        num_of_bin_places = num_of_bin_places + 1

    if binary_number_place != den:
        binary_number_place = binary_number_place / 2
        num_of_bin_places = num_of_bin_places - 1

    while num_of_bin_places != 0:
        bin_number = str(bin_number)
        bin_number = bin_number + str(int((den // binary_number_place)))
        if den >= binary_number_place:
            den = den - binary_number_place
        if binary_number_place > 1:
            binary_number_place = binary_number_place / 2
        else:
            binary_number_place = binary_number_place - 1
        num_of_bin_places = num_of_bin_places - 1

    return bin_number



number_type = input("\nWould you like to Convert:\n1 - Binary to Denary \n2 - Denary to Binary\nType your choice here: ").lower()

if "binary to denary" in number_type:
    number_type = "1"
elif "denary to binary" in number_type:
    number_type = "2"
else:
    number_type = number_type
while True:
    if number_type == "1" or number_type == "2":
        break
    else:
        print("That isn't an option, try again.")
        number_type = input("\nWould you like to Convert:\n1 - Binary to Denary \n2 - Denary to Binary\nType your choice here: ").lower()

number_to_convert = ""

if number_type == "1":
    while not is_binary(number_to_convert) :
        number_to_convert = input("Enter binary number:     ")
        if not is_binary(number_to_convert):
            print("That isn't a binary number, try again")
    print(binary_to_denary(number_to_convert))



else:
    while True:
        try:
            number_to_convert = int(input("Enter your denary integer here:     "))
            break
        except ValueError:
            print("That isn't a denary integer, try again")
            number_to_convert = int(input("Enter your denary integer here:     "))
    print(denary_to_binary(number_to_convert))




print("Hooray")