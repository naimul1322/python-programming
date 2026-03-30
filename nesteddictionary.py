# nested dictionary

student={
    "name":"rakul",
    "subject":{
        "phy":95,
        "math":85,
        "chem":88
    }
}

print(student["subject"])

print(len(student))

print(list(student.keys()))
print(student.values())

print(list(student.items()))