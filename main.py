"""
Tool for merging text files into one file

Usage:
python main.py --output-path=results\merged.txt --input-path=data\files* --remove-empty-lines 

Options
--input-path=<input_path>
--output-path=<output_path> Default: merged.txt
--remove-empty-lines
"""

print("Hello")

import fnmatch
import glob
import os
import sys

from file_helper import (
    remove_empty_lines_from_list,
    strip_new_line_characters,
    validate_folder_path,
    writ_list_to_text_file,
)

# - TODO: If not arguments provided


def parse_arguments_inout_path(arguments: list[str]) -> str:
    """Parse input path from arguments"""
    for argument in arguments:
        if argument.startswith("--input-path="):
            input_path = argument.split("--input-path=")[1]
            return input_path

    print("Argument --input-path= not provided. Please use it.")
    input("Enter input path: ")
    return path


def parse_arguments_output_path(arguments: list[str]) -> str:
    """Parse output path from arguments"""
    for argument in arguments:
        if argument.startswith("--output-path="):
            input_path = argument.split("--output-path=")[1]
            return input_path

    print(
        "Argument --output-path= not provided. Default value will be used (merged.txt)."
    )
    return "merged.txt"


def parse_arguments_remove_empty_lines(arguments: list[str]) -> bool:
    """Parse remove empty lines from arguments"""
    for argument in arguments:
        if argument == "--remove-empty-lines":
            return True
    return False


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


def split_input_path(input_path: str) -> tuple[str, str]:
    """splits input path into folder path and filter"""
    dir_name, file_name = os.path.split(input_path)
    if not os.path.exists(dir_name):
        print("Directory {dir_name} does not exist. Exiting ...")
        sys.exit(1)
    return dir_name, file_name


def main():
    # Parse arguments
    input_path = parse_arguments_inout_path(sys.argv)
    output_path = parse_arguments_output_path(sys.argv)
    validate_folder_path(output_path)
    remove_empty_lines = parse_arguments_remove_empty_lines(sys.argv)
    data_folder_name, filter_file_name = split_input_path(input_path)

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
    writ_list_to_text_file(file_path=output_path, file_data=merged_list)

    print("Done!")


print("Start ... ")
main()
