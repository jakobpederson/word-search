from argparse import ArgumentParser


def get_lines(file_name):
    lines = []
    with open('data' + '/' + file_name) as f:
        for line in f.readlines():
            lines.append(line.strip().split(','))
    return lines


def word_search(data):
    names = data[0]
    lines = data[1:]
    result = {}
    for name in names:
        first_letters = get_first_letters(name, lines)
        all_combos = get_all_combos(first_letters, name)
        result.update(get_name_coordinates(all_combos, lines, name))
    return result


def get_name_coordinates(all_combos, lines, name):
    result = {name: []}
    for coordinate in all_combos:
        if name in _get_word(coordinate, lines, name):
            result[name] = coordinate
        if name[::-1] in _get_word(coordinate, lines, name):
            coordinate.reverse()
            result[name] = coordinate
    return result


def get_all_combos(first_letters, name):
    result = []
    for letter in first_letters:
        result.extend(get_eight_viable_answers(letter, name))
    return result


def get_eight_viable_answers(letter, name):
    result = []
    result.append([(letter[0], letter[1] + i) for i in range(len(name))])
    result.append([(letter[0], letter[1] - i) for i in range(len(name))])
    result.append([(letter[0] + i, letter[1]) for i in range(len(name))])
    result.append([(letter[0] - i, letter[1]) for i in range(len(name))])
    result.append([(letter[0] + i, letter[1] + i) for i in range(len(name))])
    result.append([(letter[0] + i, letter[1] - i) for i in range(len(name))])
    result.append([(letter[0] - i, letter[1] + i) for i in range(len(name))])
    result.append([(letter[0] - i, letter[1] - i) for i in range(len(name))])
    return result


def get_first_letters(name, lines):
    first = []
    for y_coordinate, line in enumerate(lines):
        for x_coordinate, letter in enumerate(line):
            if letter == name[0]:
                first.append((x_coordinate, y_coordinate))
    return first


def _get_word(coords, lines, name):
    result = []
    if len(coords) == len(name):
        for coord in coords:
            try:
                result.append(lines[coord[1]][coord[0]])
            except IndexError:
                pass
        return ''.join(result)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--filename", required=True)
    args = parser.parse_args()
    lines = get_lines(args.filename)
    result = word_search(lines)
    for key, value in result.items():
        print("{}: {}".format(key, value))
