
FILE_PATH_SAMPLE = 'input/day02_sample.txt'
FILE_PATH = 'input/day02.txt'

def main(file_path, part2 = False):

    with open(file_path) as f:
        lines = f.read()
    result = 0

    ranges = list(map(lambda r: list(map(lambda x: x, r.split("-"))), lines.split(",")))

    for [low, high] in ranges:
        x = low[:len(low)//2]
        if len(x) == 0:
            x = '0'
        xx = int(x + x)

        while xx <= int(high):
            if xx >= int(low) and xx <= int(high):
                
                result += xx
            
            x = str(int(x) + 1)
            xx = int(x + x)

    return result

def part2(file_path):

    with open(file_path) as f:
        lines = f.read()
    result = 0

    ranges = list(map(lambda r: list(map(lambda x: int(x), r.split("-"))), lines.split(",")))

    for [low, high] in ranges:
        for i in range(low, high + 1):
            i_str = str(i)
            i_len = len(i_str)
            for n in range(1, (i_len // 2) + 1):
                substrings = substringEvery(i_str, n)
                if len(set(substrings)) == 1:
                    result += i
                    break
    return result

def substringEvery(x, n):
    return [x[i:i+n] for i in range(0, len(x), n)]


if __name__ == "__main__":
    sample_part1 = main(FILE_PATH_SAMPLE)
    print("Sample Part 1:", sample_part1)
    assert sample_part1 == 1227775554

    part1 = main(FILE_PATH)
    print("Part 1", part1)
    assert part1 == 37314786486

    sample_part2 = part2(FILE_PATH_SAMPLE)
    print("Sample Part 2:", sample_part2)
    assert sample_part2 == 4174379265

    part2_result = part2(FILE_PATH)
    print("Part 2:", part2_result)
    assert part2_result == 47477053982
