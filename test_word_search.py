from word_search import word_search, get_lines
from unittest import TestCase


class TestWordSearch(TestCase):

    def test_find_horizontal(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
        }
        assert result == expected

    def test_find_horizontal_reversed(self):
        new_data = self.data().copy()
        new_data.insert(0, ["KIRK"])
        result = word_search(new_data)
        expected = {
            'KIRK': [(4, 7), (3, 7), (2, 7), (1, 7)],
        }
        assert result == expected

    def test_find_vertical(self):
        new_data = self.data().copy()
        new_data.insert(0, ["BONES"])
        result = word_search(new_data)
        expected = {
            'BONES': [(0, 6), (0, 7), (0, 8), (0, 9), (0, 10)],
        }
        assert result == expected

    def test_find_vertical_reversed(self):
        new_data = self.data().copy()
        new_data.insert(0, ["KHAN"])
        result = word_search(new_data)
        expected = {
            'KHAN': [(5, 9), (5, 8), (5, 7), (5, 6)],
        }
        assert result == expected

    def test_find_diagonal(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SPOCK"])
        result = word_search(new_data)
        expected = {
            'SPOCK': [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)],
        }
        assert result == expected

    def test_find_diagonal_reversed(self):
        new_data = self.data().copy()
        new_data.insert(0, ["UHURA"])
        result = word_search(new_data)
        expected = {
            'UHURA': [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
        }
        assert result == expected

    def test_find_other_diagonal_reversed(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SULU"])
        result = word_search(new_data)
        expected = {
            'SULU': [(3, 3), (2, 2), (1, 1), (0, 0)],
        }
        assert result == expected

    def test_find_all(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY", "KIRK", "BONES", "KHAN", "SPOCK", "UHURA", "SULU"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
            'KIRK': [(4, 7), (3, 7), (2, 7), (1, 7)],
            'BONES': [(0, 6), (0, 7), (0, 8), (0, 9), (0, 10)],
            'KHAN': [(5, 9), (5, 8), (5, 7), (5, 6)],
            'SPOCK': [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)],
            'UHURA': [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
            'SULU': [(3, 3), (2, 2), (1, 1), (0, 0)],
        }
        assert result == expected

    def test_read_file_and_find_names(self):
        lines = get_lines('test_data.txt')
        new_data = self.data().copy()
        new_data.insert(0, ['BONES', 'KHAN', 'KIRK', 'SCOTTY', 'SPOCK', 'SULU', 'UHURA'])
        self.assertCountEqual(lines, new_data)

    def test_find_when_only_one_name_in_the_list(self):
        new_data = [
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'R', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'E', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'K', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'I', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'R'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ]
        new_data.insert(0, ["SCOTTY", "KIRK", "BONES", "KHAN", "SPOCK", "UHURA", 'RIKER'])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [],
            'KIRK': [],
            'BONES': [],
            'KHAN': [],
            'SPOCK': [],
            'UHURA': [],
            'RIKER': [(6, 5), (5, 4), (4, 3), (3, 2), (2, 1)]
        }
        assert result == expected

    def test_no_names_present(self):
        new_data = [
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'R', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'E', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'K', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'I', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'R'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ]
        new_data.insert(0, ["SCOTTY", "KIRK", "BONES", "KHAN", "SPOCK", "UHURA"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [],
            'KIRK': [],
            'BONES': [],
            'KHAN': [],
            'SPOCK': [],
            'UHURA': [],
        }
        assert result == expected

    def test_alternative_data(self):
        names = [
            "CAT",
            "DOG",
            "ELF",
            "GLORFINDEL",
            "HOUSE",
        ]
        data = [
            ["J", "T", "V", "E", "X", "X", "J", "U", "S", "X", "H", "P", "T", "M", "P"],
            ["Q", "W", "S", "M", "N", "B", "E", "O", "G", "Z", "H", "T", "K", "U", "G"],
            ["W", "J", "D", "T", "A", "Z", "H", "K", "W", "I", "X", "Z", "H", "U", "M"],
            ["H", "H", "M", "T", "G", "Y", "C", "Q", "P", "G", "V", "R", "Q", "S", "H"],
            ["E", "Z", "L", "Y", "Y", "O", "R", "R", "L", "R", "R", "S", "D", "W", "T"],
            ["Z", "Y", "P", "X", "J", "K", "D", "O", "T", "E", "Y", "Y", "O", "V", "T"],
            ["I", "E", "A", "M", "J", "T", "R", "I", "N", "N", "N", "O", "M", "Z", "M"],
            ["A", "O", "X", "R", "U", "F", "L", "Y", "R", "M", "L", "B", "I", "A", "T"],
            ["L", "M", "X", "B", "I", "U", "O", "L", "K", "Z", "Q", "P", "E", "P", "K"],
            ["P", "L", "D", "N", "E", "S", "U", "O", "H", "A", "J", "Q", "E", "G", "T"],
            ["H", "Y", "D", "C", "F", "E", "Y", "J", "Q", "N", "G", "P", "P", "F", "S"],
            ["N", "E", "K", "T", "S", "C", "O", "V", "E", "A", "F", "Z", "L", "T", "E"],
            ["L", "E", "E", "A", "A", "D", "M", "A", "M", "G", "X", "E", "U", "L", "S"],
            ["Q", "I", "U", "C", "X", "M", "V", "G", "V", "B", "E", "O", "F", "E", "F"],
            ["I", "I", "V", "R", "W", "J", "C", "Y", "F", "E", "J", "I", "R", "X", "X"],
        ]
        data.insert(0, names)
        result = word_search(data)
        expected = {
            'CAT': [(3, 13), (3, 12), (3, 11)],
            'DOG': [(6, 5), (5, 4), (4, 3)],
            'ELF': [(11, 12), (12, 11), (13, 10)],
            'GLORFINDEL': [(9, 3), (8, 4), (7, 5), (6, 6), (5, 7), (4, 8), (3, 9), (2, 10), (1, 11), (0, 12)],
            'HOUSE': [(8, 9), (7, 9), (6, 9), (5, 9), (4, 9)]
        }
        self.assertEqual(result, expected)

    def data(self):
        return [
            ["U", "M", "K", "H", "U", "L", "K", "I", "N", "V", "J", "O", "C", "W", "E"],
            ["L", "L", "S", "H", "K", "Z", "Z", "W", "Z", "C", "G", "J", "U", "Y", "G"],
            ["H", "S", "U", "P", "J", "P", "R", "J", "D", "H", "S", "B", "X", "T", "G"],
            ["B", "R", "J", "S", "O", "E", "Q", "E", "T", "I", "K", "K", "G", "L", "E"],
            ["A", "Y", "O", "A", "G", "C", "I", "R", "D", "Q", "H", "R", "T", "C", "D"],
            ["S", "C", "O", "T", "T", "Y", "K", "Z", "R", "E", "P", "P", "X", "P", "F"],
            ["B", "L", "Q", "S", "L", "N", "E", "E", "E", "V", "U", "L", "F", "M", "Z"],
            ["O", "K", "R", "I", "K", "A", "M", "M", "R", "M", "F", "B", "A", "P", "P"],
            ["N", "U", "I", "I", "Y", "H", "Q", "M", "E", "M", "Q", "R", "Y", "F", "S"],
            ["E", "Y", "Z", "Y", "G", "K", "Q", "J", "P", "C", "Q", "W", "Y", "A", "K"],
            ["S", "J", "F", "Z", "M", "Q", "I", "B", "D", "B", "E", "M", "K", "W", "D"],
            ["T", "G", "L", "B", "H", "C", "B", "E", "C", "H", "T", "O", "Y", "I", "K"],
            ["O", "J", "Y", "E", "U", "L", "N", "C", "C", "L", "Y", "B", "Z", "U", "H"],
            ["W", "Z", "M", "I", "S", "U", "K", "U", "R", "B", "I", "D", "U", "X", "S"],
            ["K", "Y", "L", "B", "Q", "Q", "P", "M", "D", "F", "C", "K", "E", "A", "B"],
        ]
