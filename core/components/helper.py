import time
import datetime


class Helper:

    @staticmethod
    def between_dates(date, start_date, end_date):
        date = time.strptime(date, "%d %b %Y")
        start = time.strptime(start_date, "%d %b %Y")
        end = time.strptime(end_date, "%d %b %Y")
        return  start < date and date < end

    @staticmethod
    def change_date_format(date):
        return datetime.datetime.strptime(date, "%d %b %Y")\
            .strftime("%d/%m/%Y")