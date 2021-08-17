import csv
import json
from CSV.class_object import Object
from CSV.class_object import Comma
from CSV.class_object import Object03
from CSV.class_object import Contribute


class Csv_Home:
    def read_csv_01(self, path_file):  # read csv file has '|'
        with open(path_file, 'r') as csvfile:
            sample = csvfile.read()
            deduced_dialect = csv.Sniffer().sniff(sample)
        with open(path_file, 'r') as file_new:
            csv_read = csv.reader(file_new, deduced_dialect)
            next(csv_read, None)
            for line in csv_read:
                info = Object(line[0], line[1], line[2])
                print(info)

    def read_csv_02(self, path_file, delimiter):
        with open(path_file, 'r') as file:
            csv_read = csv.reader(file, delimiter)
            next(csv_read, None)
            for line in csv_read:
                info_02 = Comma(line[0], line[1], line[2])
                print(info_02)

    def read_json_03(self, path_file):
        with open(path_file, 'r') as file:
            read_03 = json.load(file)
            for i in read_03:
                a = dict(i)
                object = Object03(a['keyword'])
                print(object)

    def read_csv_04(self, path_file):
        with open(path_file, 'r') as file:
            csv_read = csv.reader(file)
            next(csv_read, None)
            for line in csv_read:
                info_04 = Contribute(line[0], line[1], line[2])
                print(info_04)


if __name__ == "__main__":
    csv_object = Csv_Home()
    csv_object.read_csv_01('data_01.csv')
    csv_object.read_csv_02('data_02.csv', ';')
    csv_object.read_json_03('data_03.json')
    csv_object.read_csv_04('data_04.csv')
