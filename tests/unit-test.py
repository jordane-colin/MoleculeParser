import unittest

from parser import parse_molecule

MOLECULES = (
    ('H2O', {'H': 2, 'O': 1}),
    ('Mg(OH)2', {'Mg': 1, 'O': 2, 'H': 2}),
    ('K4[ON(SO3)2]2', {'K': 4, 'O': 14, 'N': 2, 'S': 4}),
    ('C12H22O11', {'C': 12, 'H': 22, 'O': 11}),
)

NOT_BALANCED_MOLECULES = (
    'C12[{H22]}O11',
    'C12[{H22O11',
)

WRONG_MOLECULES = (
    ('C12$! O11', {'C': 12, 'O': 11}),
)

MISCALCULATED_MOLECULES = (
    ('K4[ON(SO3)2]2', {'K': 4, 'O': 12, 'N': 6, 'S': 4}),
    ('Mg(OH)2', {'Mg': 1}),
)


class TestParseMolecule(unittest.TestCase):

    def test_parse_wrong_molecule(self):
        for item, response in WRONG_MOLECULES:
            element = parse_molecule(item)
            self.assertDictEqual(element, response)

    def test_parse_molecule(self):
        for item, response in MOLECULES:
            element = parse_molecule(item)
            self.assertDictEqual(element, response)

    def test_not_balanced_formula(self):
        for item in NOT_BALANCED_MOLECULES:
            with self.assertRaises(ValueError):
                parse_molecule(item)

    def test_miscalculated_formula(self):
        for item, response in MISCALCULATED_MOLECULES:
            element = parse_molecule(item)
            self.assertNotEqual(element, response)


if __name__ == '__main__':
    unittest.main()
