import fnmatch
import os


def strip_new_line_characters(file_data: list[str]) -> list[str]:
    return [line.strip() for line in file_data]


def remove_empty_lines_from_list(file_data: list[str]) -> list[str]:
    return [line for line in file_data if line != ""]


def writ_list_to_text_file(file_data: list[str], file_path: str) -> None:
    with open(file_path, "w") as file:
        for line in file_data:
            file.write(line + "\n")


def validate_folder_path(path: str) -> None:
    dir_name, file_name = os.path.split(path)
    if not os.path.exists(dir_name):
        print("Directory (dir_name) does not exist! Creating it.")
        os.makedirs(dir_name)
