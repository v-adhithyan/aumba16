import csv

def profile(rollno):
    data = csv.DictReader(open("data.csv", "r"))

    content = {}
    for row in data:
        if row['Roll no'] == rollno:
            elective = row['Specialization'].split(";")
            content["elective_1"] =  elective[0]
            content["elective_2"] = elective[1]

            content["no_error"] = True
            content["name"] = row['Name']
            content["linkedin_image"] = row['Linkedin profile picture url']
            content["about_me"] = row['About yourselves']
            content["degree"] = "{} {}".format(row['UG Degree'], row['UG Branch'])
            content["college"] = row['UG College']
            content["summer_int"] = row['Summer internship company name']
            content["int_stream"] = row['Summer internship stream']


            if row['Do you have work experience ?'] == "No":
                content["prev_org"] = "No"
                content ["exp"] = "work"
                content["designation"] = "experience"
            else:
                content["prev_org"] = "{} {} {}".format("Worked", "in", row['Previous employer'])
                content["exp"] = "{} {} {}".format("for", row['Experience in years'], "year(s)")
                content["designation"] = "{} {}".format("as", row['Designation'])

            content["email"] = row['Email']
            content["linkedin_profile"] = row['Linkedin profile']
            break

    if len(content.keys()) == 0:
        content["no_error"] = False

    return content
