#!/bin/bash
# shebang

# Purpose: Creates folder with the name of the day and sets up the files

FOLDER=$1

# -p flag creates the folder if it doesn't exist
mkdir -p $FOLDER

touch $FOLDER/easy_code.py
touch $FOLDER/easy_problem.md
touch $FOLDER/example.txt
touch $FOLDER/hard_code.py
touch $FOLDER/hard_problem.md
touch $FOLDER/input.txt

# command to run: ./create-aoc.sh folder_name
# TODO: make alias for this command
# dayme() function in aliases.sh | dayme folder_name