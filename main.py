print("Hello")

file_one = "data/file_a.txt"
file_two = "data/file_b.txt"
final_merged_file = "data/merged_file.txt"
remove_empty_lines = True

# Preberemo obe datoteke v mapi data

# združimo obe datoteke in jih shranimo n+ v novo datoteko imenova skupni.txt

with open(file_one, "r") as file_a:
    file_a_data = file_a.readlines()

with open(file_two, "r") as file_b:
    file_b_data = file_b.readlines()

# merge files

merged_list = file_a_data + file_b_data

# remove new line characters
merged_list = [line.strip() for line in merged_list]

# remove empty lines
if remove_empty_lines:
    merged_list = [line for line in merged_list if line != ""]

with open(final_merged_file, "w") as merged_file:
    for line in merged_list:
        merged_file.write(line + "\n")
