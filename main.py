print("Hello")

import fnmatch
import glob
import os

data_folder_name = "data"
filter_file_name = "file*"
final_merged_file = "results\merged_file.txt"
remove_empty_lines = True


def get_absolute_file_paths(folder_name: str, filter: str = "*") -> list[str]:
    absolute_paths = []
    for dirpath, _, filenames in os.walk(folder_name):
        for filename in filenames:
            if fnmatch.fnmatch(filename, filter):
                absolute_path = os.path.abspath(os.path.join(dirpath, filename))
                absolute_paths.append(absolute_path)
    return absolute_paths


def read_text_file_to_list(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        file_data = file.readlines()
    return file_data


def strip_new_line_characters(file_data: list[str]) -> list[str]:
    return [line.strip() for line in file_data]


def remove_empty_lines_from_list(file_data: list[str]) -> list[str]:
    return [line for line in file_data if line != ""]


def writ_list_to_text_file(file_data: list[str], file_path: str) -> None:
    with open(file_path, "w") as file:
        for line in file_data:
            file.write(line + "\n")


# Preberemo obe datoteke v mapi data

# združimo obe datoteke in jih shranimo n+ v novo datoteko imenova skupni.txt

all_files_paths = get_absolute_file_paths(data_folder_name, filter_file_name)
merged_list = []
for path in all_files_paths:
    file_data = read_text_file_to_list(path)
    merged_list += file_data
print(all_files_paths)

# remove new line characters

merged_list = strip_new_line_characters(merged_list)
print(merged_list)

# remove empty lines
if remove_empty_lines:
    merged_list = remove_empty_lines_from_list(merged_list)
print(merged_list)

# write to file
writ_list_to_text_file(merged_list, final_merged_file)
