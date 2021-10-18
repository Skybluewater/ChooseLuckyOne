import argparse

from Main import DataImporting, Shuffle


def make_parser():
    parser = argparse.ArgumentParser(description="Search for the lucky one")
    parser.add_argument("-d", help="Input the substitute Json file", dest="JsonFilename")
    parser.add_argument("-r", action="store_true", help="Json file renew", dest="JsonFileRenew")
    return parser


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    if args.JsonFilename:
        DataImporting.Json.change_json_file_name(args.JsonFilename)
    if args.JsonFileRenew:
        Shuffle.Shuffle.excel_renew()
    Shuffle.Shuffle.read_from_json_as_dic()
    Shuffle.Shuffle.shuffle_dic()

# TODO: 增加QT Interface
