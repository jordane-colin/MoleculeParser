#!/usr/bin/env python3

import argparse
import re
import logger
from collections import defaultdict
from typing import Dict

# We want to get all atoms (can be Mg or just M),
# all brackets [({ and the number of atoms (digits)
REGEX = re.compile(r'[A-Z][a-z]?|[()\[\]{}]|\d+')
OPEN_LIST = ['[', '{', '(']
CLOSE_LIST = [']', '}', ')']
logger = logger.get_logger()


def parse_molecule(formula: str) -> Dict[str, int]:
    def _handle_errors(formula):
        # Check to verify if all brackets are balanced and presents
        if not formula:
            logger.warning('Formula is empty')
            raise ValueError('Formula is empty')
        if not _check_brackets(formula):
            logger.error('Opening or closing brackets are missing')
            raise ValueError('Opening or closing brackets are missing []{}()')

    # Check to verify if a given list of brackets is opened
    # and closed with balanced order
    # Balanced : Mg(OH)2
    # Unbalanced: Mg[(OH])2
    def _check_brackets(formula: str):
        stack = []
        for i in formula:
            if i in OPEN_LIST:
                stack.append(i)
            elif i in CLOSE_LIST:
                pos = CLOSE_LIST.index(i)
                if (len(stack) > 0) \
                        and (OPEN_LIST[pos] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

    # Parts example : ['Mg', '(', 'O', 'H', ')', '2']
    parts = REGEX.findall(formula)

    # Retrieve the multiplier to be apply on atoms
    def get_multiplier(i: int) -> int:
        cursor = i + 1
        return int(parts[cursor]) \
            if cursor < len(parts) and parts[cursor].isdigit() else 1

    # Move the cursor to sub atoms if needed
    def cursor(i: int) -> int:
        cursor = i + 1
        if cursor < len(parts) and parts[cursor].isdigit():
            return 1 if (int(parts[cursor])) else 0
        return 0

    # Parse all the formula, character by character.
    # If it an alphabetic character, we store it in molecule_list with
    # its multiplier (default 1).
    # Else if its an opening bracket,
    # we recursively parse the sub molecule to get
    # alphabetic character
    # and merge them in molecule_list with its number.
    # Finally, if it's a closing bracket,
    # we can get the multiplier right after the bracket,
    # iterate on the molecule_list to apply it.
    def parse(i: int):
        molecule_list = defaultdict(int)

        while i < len(parts):
            character = parts[i]
            if character.isalpha():
                molecule_list[character] += get_multiplier(i)
                i += 1 + cursor(i)
            elif character in OPEN_LIST:
                i, sub_molecule = parse(i + 1)
                for atom_number in {*sub_molecule, *molecule_list}:
                    total_molecule_and_sub_number = \
                        molecule_list[atom_number] + sub_molecule[atom_number]
                    molecule_list[atom_number] = total_molecule_and_sub_number
            elif character in CLOSE_LIST:
                for molecule, atom_number in molecule_list.items():
                    molecule_list[molecule] = atom_number * get_multiplier(i)
                i += 1 + cursor(i)
                break

        return i, molecule_list

    _handle_errors(formula)

    # We start from the beginning of the formula
    logger.info('Start parsing the formula %s', formula)
    _, r = parse(0)

    return dict(r)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('formula')
    args = parser.parse_args()

    print(parse_molecule(args.formula))


if __name__ == '__main__':
    main()
