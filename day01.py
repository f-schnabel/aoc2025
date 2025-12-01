
FILE_PATH_SAMPLE = 'input/day01_sample.txt'
FILE_PATH = 'input/day01.txt'

def main(file_path, part2 = False):

    with open(file_path) as f:
        lines = f.readlines()
    dial = 50
    result = 0

    for line in lines:
        direction, amount = line[0], int(line[1:])
        if direction == 'L':
            amount *= -1
            if dial == 0:
                dial = 100

        dial += amount

        rotations, dial = divmod(dial, 100)

        if part2:
            result += abs(rotations)
            if dial == 0 and direction == 'L':
                result += 1

        elif dial == 0:
            result += 1
    
    return result

if __name__ == "__main__":
    sample_part1 = main(FILE_PATH_SAMPLE)
    print("Sample Part 1:", sample_part1)
    assert sample_part1 == 3
    
    sample_part2 = main(FILE_PATH_SAMPLE, part2=True)
    print("Sample Part 2:", sample_part2)
    assert sample_part2 == 6

    part1 = main(FILE_PATH)
    print("Part 1", part1)
    assert part1 == 1084

    part2 = main(FILE_PATH, part2=True)
    print("Part 2:", part2)
    assert part2 == 6475
