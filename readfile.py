# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    readfile.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: emaksimo <emaksimo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 16:53:15 by emaksimo          #+#    #+#              #
#    Updated: 2023/03/22 17:27:03 by emaksimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys

RED = "\033[1;31m"

RESET = "\033[0m"

file_path = sys.argv[1]

file_ext = os.path.splitext(file_path)[1]

file_kwargs = {}

try:
    if file_ext in [".txt", ".py"]:
        file_mode = "r"
    elif file_ext in [".csv", ".dat"]:
        file_mode = "r"
        file_kwargs = {"newline": ""}
    else:
        file_mode = "rb"
    with open(file_path, mode=file_mode, **file_kwargs) as file:
        file_contents = file.read()
    print(f"{RED}{file_contents}{RESET}")

except OSError as e:
    print(f"Error opening file: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if "file" in locals():
        file.close()
