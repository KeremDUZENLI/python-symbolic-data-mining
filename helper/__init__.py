import os
import sys
import webbrowser


def create_column_labels(item):
    label = ""
    while True:
        label = chr(ord('a') + (item % 26)) + label
        item = item // 26 - 1
        if item < 0:
            break
    return label.upper()


def open_pdf(file_path):
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.dirname(__file__))

    full_path = os.path.join(base, file_path) if not os.path.isabs(file_path) else file_path
    platform = sys.platform
    
    if not os.path.exists(full_path):
        print(f"PDF NOT FOUND: {full_path}")
        return

    if platform.startswith('win'):
        os.startfile(full_path)
    elif platform == 'darwin':
        os.system(f'open "{full_path}"')
    else:
        os.system(f'xdg-open "{full_path}"')


def open_url(url):
    webbrowser.open_new(url)


def welcome_message():
    lines = [
        "--------------------------------------------------",
        "SYMBOLIC DATA MINING",
        "Instructor: Dr. László Szathmáry",
        "Developer : Kerem Düzenli | PhD Candidate, University of Debrecen",
        "--------------------------------------------------",
        "Features:",
        "- Frequent itemset mining (Apriori, Apriori-Close, Apriori-Rare, Eclat)",
        "- Association rule generation (confidence-based)",
        "- CLI & GUI (draw or generate datasets visually)",
        "- Laszlo.rcf default dataset + random dataset generator",
        "- Clear, aligned output with support/confidence thresholds",
        "--------------------------------------------------",
        "Educational use only | Licensed under CC BY-NC 4.0",
        "Project Repository : https://github.com/KeremDUZENLI/python-symbolic-data-mining",
        "Support My Projects: https://revolut.me/krmdznl",
        "--------------------------------------------------",
    ]
    
    return lines
