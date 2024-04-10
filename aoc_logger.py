import logging
import sys
import coloredlogs


ANSWER = 21
CORRECT_ANSWER = 22
INCORRECT_ANSWER = 23


logging.addLevelName(CORRECT_ANSWER, 'CORRECT_ANSWER')
logging.addLevelName(INCORRECT_ANSWER, 'INCORRECT_ANSWER')
logging.addLevelName(ANSWER, 'ANSWER')


class AocLogger(logging.Logger):
    def answer(self, year, day, part, number, *args, **kwargs):
        msg = f"{year:04d} day {day} part {part} answer = {number}"
        self.log(ANSWER, msg, *args, **kwargs)

    def correct_answer(self, year, day, part, number, *args, **kwargs):
        msg = f"{year:04d} day {day} part {part} answer = {number} is correct"
        self.log(CORRECT_ANSWER, msg, *args, **kwargs)

    def incorrect_answer(self, year, day, part, number, correct, *args, **kwargs):
        msg = f"{year:04d} day {day} part {part} answer = {number} is incorrect. Should be {correct}."
        self.log(INCORRECT_ANSWER, msg, *args, **kwargs)


logging.basicConfig()
logging.setLoggerClass(AocLogger)
logger: AocLogger = logging.getLogger(__name__)
logger.setLevel(ANSWER)
coloredlogs.install(logger=logger)
logger.propagate = False

coloredFormatter = coloredlogs.ColoredFormatter(
    fmt='%(levelname)s %(message)s',
    level_styles=dict(
        answer=dict(color='yellow'),
        correct_answer=dict(color='green'),
        incorrect_answer=dict(color='red', bright=True),
    ),
    field_styles=dict(
        name=dict(color='white'),
        asctime=dict(color='white'),
        funcName=dict(color='white'),
        lineno=dict(color='white'),
    )
)

ch = logging.StreamHandler(stream=sys.stdout)
ch.setFormatter(coloredFormatter)
logger.addHandler(hdlr=ch)
logger.setLevel(level=ANSWER)