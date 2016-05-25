from databin.parsers.util import ParseException
from databin.parsers.simple import parse_dsv, parse_tsv, parse_ssv, pandas_parser
from databin.parsers.psql import parse_psql

PARSERS = [
    ('Auto Detect', "pandas_table", pandas_parser),
    ('Excel copy & paste', 'excel', parse_tsv),
    ('PostgreSQL Shell', 'psql', parse_psql),
    ('MySQL Shell', 'mysql', parse_psql),
    ('Comma-Separated Values', 'csv', parse_dsv),
    ('Tab-Separated Values', 'tsv', parse_tsv),
    ('Space-Separated Values', 'ssv', parse_ssv)
]


def parse(format, data):
    for name, key, func in PARSERS:
        if key == format:
            return func(data)
    raise ParseException()


def get_parsers():
    for name, key, func in PARSERS:
        yield (key, name)
