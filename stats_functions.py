import os

INPUT_FILE = "./10000-common-passwords.csv"
OUTPUT_FILE = "./statistics.csv"
DELIMITER = ","


def delete_existing_output_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    

pass_length_count = {
     "0" : 0,
    "1" :  0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0,
    "10" : 0,
    "11" : 0,
    "12" : 0,
    "13" : 0,
    "14" : 0,
    "15" : 0,
    "16" : 0,
    "17" : 0,
    "18" : 0,
    "19" : 0,
    "20" : 0,
    "21" : 0
}

pass_first_letter = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0,
}   


def process_and_print_lines(input_filename, delimiter):
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            for line in file:
                elements = line.strip().split(delimiter)
                # element = [ first bit, second bit]

                length = len(elements[1])

                pass_length_count[str(length)] += 1
                #print(pass_length_count)
                for element in elements[1]:
                    first_letter = element[0]
                    first_letter = first_letter.lower()
                print (first_letter)
                print(pass_first_letter)

                # pass_first_letter[first_letter] += 1
        # with open("./letter_statistics.csv", "w", encoding = "utf-8") as file:
        #     for i in range (len(pass_first_letter)):
        #         file.write(f"letter {pass_first_letter[i]}, count : {pass_first_letter[str(i)]}\n")
        #             # if element_count == 20:
        with open( OUTPUT_FILE,"w", encoding="utf-8") as file:
                for i in range (len(pass_length_count)): 
                   file.write(f"chars: {i}, count: {pass_length_count[str(i)]}\n ")                    

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    
#     Number of passwords beginning with A? B? C? (A through Z analysis)
# Number of passwords starting with a number (0-9)


delete_existing_output_file(OUTPUT_FILE)
process_and_print_lines(INPUT_FILE, DELIMITER)


