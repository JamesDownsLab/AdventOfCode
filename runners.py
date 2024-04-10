from pathlib import Path
from aoc_logger import logger


def run(f, filename: Path, year: int, day: int, part: int, answer: int | None = None):
    result = f(filename)
    if answer is None:
        logger.answer(year, day, part, result)
    elif result == answer:
        logger.correct_answer(year, day, part, result)
    else:
        logger.incorrect_answer(year, day, part, result, answer)