import time
import datetime


class Helper:

    @staticmethod
    def between_dates(date, start_date, end_date):
        try:
            start_date = time.strptime(start_date, "%d %b %Y")
            end_date = time.strptime(end_date, "%d %b %Y")
            date = time.strptime(date, "%d %b %Y")

            if start_date > end_date:
                return False

            return date > start_date and date < end_date
        except Exception:
            return False

    @staticmethod
    def change_date_format(date):
        return datetime.datetime.strptime(date, "%d %b %Y")\
            .strftime("%d/%m/%Y")