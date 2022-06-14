school = {"course": "python", "duration": "6 month", "location": "Kakkanad", "Time": "10 Am", "Fee": 30000}

print(school["Fee"])

print(school["course"])

print(school["location"])



print("classroom" in school)

school["classroom"]="c4"

print(school)

print("students" in school)

school["students"]=25

print(school)

school["students"]=30

school["Time"]="11 AM"

print(school)

print(dir(dict))
