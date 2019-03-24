import json
import os

annotate_path = "annotate.txt"
json_path = "dataset\data.json"

with open(json_path, "r") as read_file:
    exists = os.path.isfile(annotate_path)
    if exists:
        os.remove(annotate_path)
    with open(annotate_path, "x") as write_file:
        data = json.load(read_file)
        for line in data:
            ext_id = line['External ID']
            label_data = line['Label']
            try:
                types = label_data.keys()
            except:
                continue
            for obj_type in types:
                obj_data = label_data[obj_type]
                for label in obj_data:
                    geometry = label['geometry']
                    xs = list(geometry[i]['x'] for i in range(len(geometry)))
                    ys = list(geometry[i]['y'] for i in range(len(geometry)))
                    xmin = min(xs)
                    xmax = max(xs)
                    ymin = min(ys)
                    ymax = max(ys)
                    converted = ",".join(list(map(str, ("dataset\\" + ext_id, xmin, ymin, xmax, ymax, obj_type)))) + "\n"
                    write_file.write(converted)
        #print(data[0])
