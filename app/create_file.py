import sys
import os
from datetime import datetime


def create_file() -> None:
    command = sys.argv

    if "-d" in command:
        current_directory = command[command.index("-d") + 1]
        path = os.path.join(
            current_directory, command[command.index("-d") + 2]
        )
        os.makedirs(path, exist_ok=True)

    if "-f" in command:
        if "-d" in command:
            current_directory = command[command.index("-d") + 1]
            new_directory = command[command.index("-d") + 2]
            file_name = command[command.index("-f") + 1]
            file_path = os.path.join(
                current_directory, new_directory, file_name
            )
        else:
            file_path = command[command.index("-f") + 1]

        with open(file_path, "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S \n"))
            count_line = 0
            while True:
                enter_line = input("Enter content line: ")
                count_line += 1
                if enter_line == "stop":
                    break
                file.write(f"{count_line} {enter_line}\n")
            file.write("\n")


create_file()
