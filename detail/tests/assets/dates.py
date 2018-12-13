from django.utils.dateparse import parse_datetime, parse_date
from datetime import datetime, date


def _parse_date(date):
    parsed_date = parse_date(date)
    return parsed_date
