import csv
to_write = {}

def write():
    with open("data.csv", "r") as f:
        csvfile = csv.DictReader(f)


        for row in csvfile:
            elective = row["Specialization"].split(";")
            value = "{};{}".format(row['Name'], row['Roll no'])


            if elective[0] in to_write:
                data = to_write[elective[0]]
                data.append(value)
                to_write[elective[0]] = data
            else:
                data = []
                data.append(value)
                to_write[elective[0]] = data

            if elective[1] in to_write:
                data = to_write[elective[1]]
                data.append(value)
                to_write[elective[1]] = data
            else:
                data = []
                data.append(value)
                to_write[elective[1]] = data

    for key in to_write.keys():
        fname = "{}.txt".format(key)
        data = to_write[key]
        with open(fname, "w") as f:
            f.write("&".join(data))

def extract(stream):
    fname = "{}.txt".format(stream)

    content = ""
    with open(fname) as f:
        content = f.read()

    details = content.split("&")
    
    return details
