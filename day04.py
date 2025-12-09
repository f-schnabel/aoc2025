FILE_PATH_SAMPLE = "input/day04_sample.txt"
FILE_PATH = "input/day04.txt"


def main(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    result = 0

    grid = list(map((lambda x: list(x.strip())), lines))
    for y, line in enumerate(grid):
        for x, element in enumerate(line):
            if element == ".":
                continue
            if is_accessible(grid, x, y):
                result += 1

    return result


def is_accessible(grid, x, y):
    adjacent = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            xx = x + dx
            yy = y + dy
            if (
                (dx == 0 and dy == 0)
                or xx < 0
                or xx >= len(grid[y])
                or yy < 0
                or yy >= len(grid)
                or grid[yy][xx] == "."
            ):
                continue
            adjacent += 1
    return adjacent < 4


def part2(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    result = 0

    grid = list(map((lambda x: list(x.strip())), lines))

    queue = [(x, y) for y in range(len(grid)) for x in range(len(grid[y]))]

    while len(queue) > 0:
        x, y = queue.pop()
        if grid[y][x] == ".":
            continue
        if is_accessible(grid, x, y):
            result += 1
            grid[y][x] = "."
            queue.extend(
                [
                    (x + dx, y + dy)
                    for dx in [-1, 0, 1]
                    for dy in [-1, 0, 1]
                    if not (
                        (dx == 0 and dy == 0)
                        or x + dx < 0
                        or x + dx >= len(grid[y])
                        or y + dy < 0
                        or y + dy >= len(grid)
                        or grid[y + dy][x + dx] == "."
                    )
                ]
            )
    return result


if __name__ == "__main__":
    sample_part1 = main(FILE_PATH_SAMPLE)
    print("Sample Part 1:", sample_part1)
    assert sample_part1 == 13

    part1 = main(FILE_PATH)
    print("Part 1", part1)
    assert part1 == 1551

    sample_part2 = part2(FILE_PATH_SAMPLE)
    print("Sample Part 2:", sample_part2)
    assert sample_part2 == 43

    part2_result = part2(FILE_PATH)
    print("Part 2:", part2_result)
    assert part2_result == 9784
