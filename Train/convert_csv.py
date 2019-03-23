import csv


def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        external_id = line["External ID"]
        label_data = line["Label"]
        print(type(dict(label_data)))
        exit()
        for key in label_data.keys():
            print("%s:\t\t\t\t" % key, line[key])
        exit()


if __name__ == "__main__":
    with open("data.csv") as f_obj:
        csv_dict_reader(f_obj)