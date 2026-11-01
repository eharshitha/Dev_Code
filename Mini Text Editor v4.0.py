
# ============================================================
# MINI TEXT EDITOR - VERSION 4.0
# ============================================================

# Imports
import json
import os
import re
import textwrap
from copy import deepcopy

# Variables
txt = {}
i = 0
active_file = "Text.json"

history = [{}]
redo_stack = []

wrap_enabled = False
last_find = ""
find_index = 0

commands = [
    "$view.txt$",
    "$exit$",
    "$delete.txt$",
    "$edit.txt$",
    "$clear.txt$",
    "$save.txt$",
    "$load.txt$",
    "$search.txt$",
    "$count.txt$",
    "$stats.txt$",
    "$upper.txt$",
    "$lower.txt$",
    "$replace.txt$",
    "$reverse.txt$",
    "$export.txt$",
    "$undo.txt$",
    "$redo.txt$",
    "$wrap.txt$",
    "$new.txt$",
    "$open.txt$",
    "$files.txt$",
    "$findnext.txt$",
    "$highlight.txt$"
]



# ============================================================
# DISPLAY MENU
# ============================================================

def show_menu():
    print("\n========== MINI TEXT EDITOR ==========")

    for number, command in enumerate(commands, start=1):
        print(f"{number:2}. {command}")

    print("======================================")
    print(f"Active file: {active_file}")
    print("======================================\n")


# ============================================================
# GENERAL FUNCTIONS
# ============================================================

def renumber():
    global txt, i

    txt = {
        f"Line {n}": value
        for n, value in enumerate(txt.values(), start=1)
    }

    i = len(txt)


def auto_save():
    try:
        with open(active_file, "w", encoding="utf-8") as file:
            json.dump(txt, file, indent=4)
    except OSError as error:
        print(f"Auto-save failed: {error}")


def commit_change():
    history.append(deepcopy(txt))
    redo_stack.clear()
    auto_save()


def read_line_number():
    try:
        return int(input("Line number: "))
    except ValueError:
        print("Please enter a valid number!")
        return None


def get_filename():
    name = input("File name: ").strip()

    if not name:
        print("Filename cannot be empty!")
        return None

    name = os.path.basename(name)

    if not name.endswith(".json"):
        name += ".json"

    return name


# ============================================================
# VIEW
# ============================================================

def view_txt(highlight=None):
    if not txt:
        print("The document is empty!")
        return

    for key, value in txt.items():

        if highlight:
            pattern = re.escape(highlight)

            value = re.sub(
                pattern,
                lambda match: "\033[93m" + match.group() + "\033[0m",
                value,
                flags=re.IGNORECASE
            )

        prefix = f"{key}: "

        if wrap_enabled:
            lines = textwrap.wrap(
                value,
                width=70,
                subsequent_indent=" " * len(prefix)
            )

            print(prefix + (lines[0] if lines else ""))

            for line in lines[1:]:
                print(line)

        else:
            print(prefix + value)


# ============================================================
# SAVE AND LOAD
# ============================================================

def save_txt():
    try:
        with open(active_file, "w", encoding="utf-8") as file:
            json.dump(txt, file, indent=4)

        print("Saved successfully!")

    except OSError as error:
        print(f"Save failed: {error}")


def load_txt():
    global txt, i, history, redo_stack

    if not os.path.exists(active_file):
        print("File not found!")
        return

    try:
        with open(active_file, "r", encoding="utf-8") as file:
            loaded = json.load(file)

        if not isinstance(loaded, dict):
            print("Invalid file format!")
            return

        if not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in loaded.items()
        ):
            print("Invalid text data!")
            return

        txt = loaded
        renumber()

        history = [deepcopy(txt)]
        redo_stack.clear()

        print("Loaded successfully!")

    except (OSError, json.JSONDecodeError) as error:
        print(f"Load failed: {error}")


# ============================================================
# MULTIPLE FILES
# ============================================================

def new_txt():
    global txt, i, active_file, history, redo_stack

    filename = get_filename()

    if filename is None:
        return

    if os.path.exists(filename):
        print("That file already exists! Use OPEN instead.")
        return

    active_file = filename
    txt = {}
    i = 0

    history = [{}]
    redo_stack.clear()

    auto_save()

    print(f"Created {active_file}!")


def open_txt():
    global active_file

    filename = get_filename()

    if filename is None:
        return

    if not os.path.exists(filename):
        print("File not found!")
        return

    active_file = filename
    load_txt()


def list_files():
    files = [
        name for name in os.listdir(".")
        if name.endswith(".json")
    ]

    if files:
        print("Available text files:")

        for filename in files:
            print(f"- {filename}")
    else:
        print("No JSON files found!")


# ============================================================
# SEARCH
# ============================================================

def search_txt():
    search = input("Search for: ").strip()

    if not search:
        print("Search cannot be empty!")
        return

    found = False

    for key, value in txt.items():
        if search.casefold() in value.casefold():
            print(f"{key}: {value}")
            found = True

    if not found:
        print("No results found!")


# ============================================================
# FIND NEXT
# ============================================================

def find_next():
    global last_find, find_index

    search = input("Search for: ").strip()

    if not search:
        print("Search cannot be empty!")
        return

    if search.casefold() != last_find.casefold():
        last_find = search
        find_index = 0

    matches = []

    for key, value in txt.items():
        for match in re.finditer(
            re.escape(last_find),
            value,
            re.IGNORECASE
        ):
            matches.append((key, match.start(), value))

    if not matches:
        print("No occurrences found!")
        return

    if find_index >= len(matches):
        find_index = 0
        print("Reached the end. Starting again!")

    key, position, value = matches[find_index]

    print(f"Found in {key}, character position {position + 1}:")
    print(value)

    find_index += 1


# ============================================================
# STATISTICS
# ============================================================

def count_txt():
    words = sum(len(value.split()) for value in txt.values())
    lines = len(txt)
    chars = sum(len(value) for value in txt.values())

    print(f"Total words      : {words}")
    print(f"Total lines      : {lines}")
    print(f"Total characters : {chars}")


def stats_txt():
    words = sum(len(value.split()) for value in txt.values())
    lines = len(txt)
    chars = sum(len(value) for value in txt.values())

    average = words / lines if lines else 0

    longest = max(
        txt.items(),
        key=lambda item: len(item[1]),
        default=None
    )

    print("\033[1m========== TEXT STATISTICS ==========\033[0m")
    print(f"Total words       : {words}")
    print(f"Total lines       : {lines}")
    print(f"Total characters  : {chars}")
    print(f"Average words/line: {average:.2f}")

    if longest:
        print(f"Longest line      : {longest[0]}")
        print(f"Longest length    : {len(longest[1])}")
    else:
        print("Longest line      : None")

    print("====================================")


# ============================================================
# UNDO AND REDO
# ============================================================

def undo_txt():
    global txt, i

    if len(history) <= 1:
        print("Nothing to undo!")
        return

    redo_stack.append(deepcopy(txt))
    history.pop()

    txt = deepcopy(history[-1])
    renumber()
    auto_save()

    print("Undo successful!")


def redo_txt():
    global txt, i

    if not redo_stack:
        print("Nothing to redo!")
        return

    txt = redo_stack.pop()
    history.append(deepcopy(txt))

    renumber()
    auto_save()

    print("Redo successful!")


# ============================================================
# EXPORT
# ============================================================

def export_txt():
    try:
        with open("Export.txt", "w", encoding="utf-8") as file:
            for key, value in txt.items():
                file.write(f"{key}: {value}\n")

        print("Exported to Export.txt!")

    except OSError as error:
        print(f"Export failed: {error}")


# ============================================================
# MAIN PROGRAM
# ============================================================

if os.path.exists(active_file):
    load_txt()

show_menu()

while True:

    txt_input = input("\033[1m>>\033[0m ")

    # ADD TEXT
    if txt_input not in commands:

        i += 1
        txt[f"Line {i}"] = txt_input

        commit_change()

    # VIEW
    elif txt_input == commands[0]:
        view_txt()

    # EXIT
    elif txt_input == commands[1]:
        save_txt()
        break

    # DELETE
    elif txt_input == commands[2]:

        view_txt()
        line_no = read_line_number()

        if line_no is not None:
            key = f"Line {line_no}"

            if key in txt:
                txt.pop(key)
                renumber()
                commit_change()
                view_txt()
            else:
                print("Line does not exist!")

    # EDIT
    elif txt_input == commands[3]:

        view_txt()
        line_no = read_line_number()

        if line_no is not None:
            key = f"Line {line_no}"

            if key in txt:
                edit_to = input("Edit to: ")
                txt[key] = edit_to
                commit_change()
                print("Edited successfully!")
            else:
                print("Line does not exist!")

    # CLEAR
    elif txt_input == commands[4]:

        if txt:
            txt.clear()
            i = 0
            commit_change()
            print("All lines cleared!")
        else:
            print("Already empty!")

    # SAVE
    elif txt_input == commands[5]:
        save_txt()

    # LOAD
    elif txt_input == commands[6]:
        load_txt()

    # SEARCH
    elif txt_input == commands[7]:
        search_txt()

    # COUNT
    elif txt_input == commands[8]:
        count_txt()

    # STATISTICS
    elif txt_input == commands[9]:
        stats_txt()

    # UPPERCASE
    elif txt_input == commands[10]:

        for key in txt:
            txt[key] = txt[key].upper()

        commit_change()
        print("Converted to uppercase!")

    # LOWERCASE
    elif txt_input == commands[11]:

        for key in txt:
            txt[key] = txt[key].lower()

        commit_change()
        print("Converted to lowercase!")

    # REPLACE
    elif txt_input == commands[12]:

        old = input("Find: ")

        if old:
            new = input("Replace with: ")

            for key in txt:
                txt[key] = txt[key].replace(old, new)

            commit_change()
            print("Replacement completed!")

        else:
            print("Search cannot be empty!")

    # REVERSE
    elif txt_input == commands[13]:

        for key in txt:
            txt[key] = txt[key][::-1]

        commit_change()
        print("All lines reversed!")

    # EXPORT
    elif txt_input == commands[14]:
        export_txt()

    # UNDO
    elif txt_input == commands[15]:
        undo_txt()

    # REDO
    elif txt_input == commands[16]:
        redo_txt()

    # WORD WRAPPING
    elif txt_input == commands[17]:

        wrap_enabled = not wrap_enabled

        print(
            "Word wrapping ON!"
            if wrap_enabled
            else "Word wrapping OFF!"
        )

    # NEW FILE
    elif txt_input == commands[18]:
        new_txt()

    # OPEN FILE
    elif txt_input == commands[19]:
        open_txt()

    # LIST FILES
    elif txt_input == commands[20]:
        list_files()

    # FIND NEXT
    elif txt_input == commands[21]:
        find_next()

    # HIGHLIGHT
    elif txt_input == commands[22]:

        term = input("Highlight text: ").strip()

        if term:
            view_txt(highlight=term)
        else:
            print("Search cannot be empty!")


print("Thank you for using Mini Text Editor!")
