#!/usr/bin/env python3

import re
from collections import defaultdict
from typing import Dict

# We want to get all atoms (can be Mg or just M), all brackets [({ and the number of atoms (digits)
REGEX = re.compile(r'[A-Z][a-z]?|[()\[\]{}]|\d+')
OPEN_LIST = ['[', '{', '(']
CLOSE_LIST = [']', '}', ')']


def parse_molecule(formula: str) -> Dict[str, int]:
    parts = REGEX.findall(formula)

    # Check to verify if a given list of brackets is opened and closed with balanced order
    def _check_brackets(formula: str):
        stack = []
        for i in formula:
            if i in OPEN_LIST:
                stack.append(i)
            elif i in CLOSE_LIST:
                pos = CLOSE_LIST.index(i)
                if (len(stack) > 0) and (OPEN_LIST[pos] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

    # Retrieve the multiplier to be apply on atoms
    def get_multiplier(i: int) -> int:
        cursor = i + 1
        return int(parts[cursor]) if cursor < len(parts) and parts[cursor].isdigit() else 1

    # Move the cursor to sub atoms if needed
    def cursor(i: int) -> int:
        cursor = i + 1
        if cursor < len(parts) and parts[cursor].isdigit():
            return 1 if (int(parts[cursor])) else 0
        return 0

    # Parse the all formula, character by character. If it an alphabetic character, we stock it in molecule_list with
    # its multiplier (default 1).
    # Else if its an opening bracket, we recursively parse the sub molecule to get
    # alphabetic character and merge them in molecule_list with its number.
    # Finally, if its a closing bracket, we can the multiplier right after the bracket,
    # iterate on the molecule_list to apply it.
    def parse(i: int):
        molecule_list = defaultdict(int)

        while i < len(parts):
            if parts[i].isalpha():
                molecule_list[parts[i]] += get_multiplier(i)
                i += 1 + cursor(i)
            elif parts[i] in OPEN_LIST:
                i, sub_molecule = parse(i + 1)
                for atom_number in {*sub_molecule, *molecule_list}:
                    total_molecule_and_sub_number = molecule_list[atom_number] + sub_molecule[atom_number]
                    molecule_list[atom_number] = total_molecule_and_sub_number
            elif parts[i] in CLOSE_LIST:
                for molecule, atom_number in molecule_list.items():
                    molecule_list[molecule] = atom_number * get_multiplier(i)
                i += 1 + cursor(i)
                break

        return i, molecule_list

    # Check to verify if all brackets are balanced and presents
    if not _check_brackets(formula):
        raise ValueError("Opening or closing brackets are missing []{}()")

    # We start from the beginning of the formula
    _, r = parse(0)

    return dict(r)
