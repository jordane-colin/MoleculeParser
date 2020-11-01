#!/usr/bin/env python3

from main import parse_molecule

MOLECULES = (
    ('Water', 'H2O'),
    ('Magnesium hydroxide', 'Mg(OH)2'),
    ('Fremy\'s salt', 'K4[ON(SO3)2]2'),
    ('Sucrose', 'C12H22O11'),
)


def pprint(name, molecule):
    print(name, ':', molecule, '->', parse_molecule(molecule))


if __name__ == '__main__':

    for name, item in MOLECULES:
        pprint(name, item)
