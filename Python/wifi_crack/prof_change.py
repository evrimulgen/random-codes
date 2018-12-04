PROF_FILE = open("prof.xml", "r").readlines()

first_part = "".join(PROF_FILE).split("<keyMaterial>")[0]
second_part = "".join(PROF_FILE).split("</keyMaterial>")[1]
line = "".join(PROF_FILE).split("<keyMaterial>")[1].split("</keyMaterial>")[0]

new_pass = "yunanistan123234324"

PROF_FILE_WRT = open("prof.xml", "w")
PROF_FILE_WRT.write(first_part + "<keyMaterial>" + new_pass + "</keyMaterial>" + second_part)

