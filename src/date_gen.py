import datetime

class DateGenerator:
    def __init__(self, year: int):
        self.year = year
        self.start_date = datetime.date(year, 1, 1)
        self.end_date = datetime.date(year, 12, 31)

    def __iter__(self):
        current_date = self.start_date
        while current_date <= self.end_date:
            yield current_date.strftime("%Y-%m-%d")
            current_date += datetime.timedelta(days=1)
