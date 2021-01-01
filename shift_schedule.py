# shift_schedule.py
from datetime import datetime

S4896 = [1, 1, 2, 2, 3, 3]
S2448 = [1, 2, 3]
S2472 = [1, 2, 3, 4]


class ShiftSchedule:
    def __init__(self, start_date, shift_type):
        self.start_date = start_date
        self.shift_type = shift_type
