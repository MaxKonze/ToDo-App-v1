from datetime import datetime


# a function to help sorting a list by date
def datum_als_datetime(datum_str):
    return datetime.strptime(datum_str[0], "%d.%m.%Y")
