import logging

from loaders import load_input_to_list
import re
from pathlib import Path
from runners import run
from aoc_logger import logger


numbers: dict[str, int] = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}


def find_end_digits_in_line(line: str) -> int:
    """
    Combine the first and last digit in a line to form a two-digit number.
    """
    digits = re.findall(r'(\d)', line)
    return int(digits[0])*10 + int(digits[-1])


def to_int(number):
    if number in numbers:
        return numbers[number]
    else:
        return int(number)


def find_end_digits_in_line_including_words(line: str) -> int:
    digits = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    a = to_int(digits[0])
    b = to_int(digits[-1])
    logger.debug(f'From line: {line.rstrip()} found {a} and {b}')
    return 10 * to_int(a) + to_int(b)


def part1(filepath: Path) -> int:
    lines = load_input_to_list(filepath)
    result = sum(map(find_end_digits_in_line, lines))
    return result


def part2(filepath: Path) -> int:
    lines = load_input_to_list(filepath)
    result = sum(map(find_end_digits_in_line_including_words, lines))
    return result


if __name__ == '__main__':
    file = Path(__file__).parent.joinpath('input.txt')
    run(part1, file, 2023, 1, 1, 55017)
    run(part2, file, 2023, 1, 2, 53539)