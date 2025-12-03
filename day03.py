
FILE_PATH_SAMPLE = 'input/day03_sample.txt'
FILE_PATH = 'input/day03.txt'

def main(file_path):

    with open(file_path) as f:
        lines = f.readlines()
    result = 0

    for line in lines:
        line = line.strip()
        first_number = None
        line_split = list(line)
        for i in range(9, 0, -1):
            i_str = str(i)
            if i_str in line_split and line_split.index(i_str) != len(line) - 1:
                first_number = i_str
                break
        assert first_number is not None
        first_idx = line_split.index(first_number)

        line_split = line_split[first_idx + 1:]
        second_number = None
        for i in range(9, 0, -1):
            i_str = str(i)
            if i_str in line_split:
                second_number = i_str
                break
        assert second_number is not None
        new_number = int(first_number + second_number)
        result += new_number

    return result

def part2(file_path):

    with open(file_path) as f:
        lines = f.readlines()
    result = 0

    for line in lines:
        line = line.strip()
        line_split = list(line)
        number_list: list[str] = []
        for n in reversed(range(12)):
            x = helper(line_split, n)
            idx = line_split.index(x)
            line_split = line_split[idx + 1:]
            number_list.append(x)

        new_number = int("".join(number_list))
        result += new_number

    return result

def helper(line: list[str], n: int):
    for i in range(9, 0, -1):
        i_str = str(i)
        if i_str in line and line.index(i_str) < len(line) - n:
            return i_str
    assert False, "Unreachable"


if __name__ == "__main__":
    sample_part1 = main(FILE_PATH_SAMPLE)
    print("Sample Part 1:", sample_part1)
    assert sample_part1 == 357

    part1 = main(FILE_PATH)
    print("Part 1", part1)
    assert part1 == 17330

    sample_part2 = part2(FILE_PATH_SAMPLE)
    print("Sample Part 2:", sample_part2)
    assert sample_part2 == 3121910778619

    part2_result = part2(FILE_PATH)
    print("Part 2:", part2_result)
    assert part2_result == 171518260283767
