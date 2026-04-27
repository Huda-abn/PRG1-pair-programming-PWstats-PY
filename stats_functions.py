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
    


def process_and_print_lines(input_filename, delimiter):
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            for line in file:
                elements = line.strip().split(delimiter)
                # element = [ first bit, second bit]

                length = len(elements[1])

                pass_length_count[str(length)] += 1
            # print(pass_length_count)

                    # if element_count == 20:
        with open( OUTPUT_FILE,"w", encoding="utf-8") as file:
                for i in range (len(pass_length_count)): 
                   file.write(f"chars: {i}, count: {pass_length_count[str(i)]}\n ")                    

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")


delete_existing_output_file(OUTPUT_FILE)
process_and_print_lines(INPUT_FILE, DELIMITER)


