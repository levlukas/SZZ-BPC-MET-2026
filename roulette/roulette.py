import os 
import json
import random

# globals
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SUBFOLDERS_DIR = os.path.join(ROOT_DIR, "..", "text")
FORBIDDEN = ["_otazky.md", "_zdroje a materialy.md", "otazky"]
RECORD_FILE = os.path.join(ROOT_DIR, "record.json")


def clear_screen() -> None:
    # ANSI clear + cursor home keeps the UI compact in modern terminals.
    print("\033[2J\033[H", end="")


def render_ui(last_pick: str | None, message: str | None) -> None:
    clear_screen()
    print("SZZ MET")
    print("=" * 40)
    if last_pick:
        print(f"Current: {last_pick}")
    else:
        print("Current: -")
    if message:
        print(f"Status : {message}")
    else:
        print("Status : -")
    print("=" * 40)

def questions_to_json() -> dict:
    questions = {}
    for root, dirs, files in os.walk(SUBFOLDERS_DIR):
        for md_file in [x for x in files if x.endswith(".md")]:
            if not any(forbidden in md_file for forbidden in FORBIDDEN):
                folder = os.path.basename(root)
                questions.setdefault(folder, []).append(md_file)
    return questions

def ui(record: dict) -> dict:
    last_pick = None
    message = None
    while True:
        render_ui(last_pick, message)
        init_input = input("| [R]un | [Q]uit |\n> ")
        if init_input in ["q", "Q"]:
            return record
        elif init_input in ["r", "R"]:
            available = {k: v for k, v in record.items() if v}
            if not available:
                render_ui(last_pick, "All questions done!")
                return record
            folder = random.choice(list(available.keys()))
            question = random.choice(available[folder])
            last_pick = f"[{folder}] {question}"
            message = "Choose done or skip"
            render_ui(last_pick, message)
            secondary_input = input("| Mark as [D]one | [S]kip |\n> ")
            if secondary_input in ["d", "D"]:
                record[folder].remove(question)
                if not record[folder]:
                    del record[folder]
                message = "Marked as done"
            else:
                message = "Skipped"

def main() -> None:
    # if necessary record questions
    if not os.path.isfile(RECORD_FILE):
        with open(RECORD_FILE, 'w') as fp:
            json.dump(questions_to_json(), fp)

    # load record json
    with open(RECORD_FILE) as f:
        record = json.load(f)

    # run ui
    ui(record)

    # save json
    with open(RECORD_FILE, 'w') as fp:
        json.dump(record, fp)   

# main call
main()
