import argparse
from simpledbf import Dbf5


def dbf2csv(dbf_file_name, csv_file_name):
    """
    Converts a dbf to a csv file.

    Arguments:
    dbf_file_name: input
    csv_file_name: output
    """

    dbf = Dbf5(dbf_file_name, codec='latin_1')

    dbf.to_csv(f"{csv_file_name}")

    return


# executed only if run as a script:
# python format_conversion.py --input "dbf file name" --output  "csv file name"
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a dbf file to csv')
    parser.add_argument('--input', action='store', type=str)
    parser.add_argument('--output', action='store', type=str)
    args = parser.parse_args()
    dbf_file = args.input
    csv_file = args.output

    dbf2csv(dbf_file, csv_file)
