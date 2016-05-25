from StringIO import StringIO
import csv
import pandas

def parse_cell(cell):
    try:
        return cell.decode('utf-8')
    except:
        return cell


def parse_dsv(data, delimiter=','):
    databuf = StringIO(data.encode('utf-8'))
    rows = []
    for row in csv.reader(databuf, delimiter=delimiter):
        rows.append([parse_cell(c) for c in row])
    return False, rows


def parse_tsv(data):
    return parse_dsv(data, delimiter='\t')


def parse_ssv(data):
    return parse_dsv(data, delimiter=' ')


def pandas_parser(data):
    return False, pandas.read_table(StringIO(data), header=None, na_filter=False).values.tolist()