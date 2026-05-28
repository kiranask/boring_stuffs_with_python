import json
with open("kiran.json", "r") as file:
    data = json.load(file)
print(data)
name =data["employee"]["name"]
skills = data["employee"]["skills"]
print(name)
print(skills)
location = data["employee"]["location"]
assert "Bangalore" ==  location["city"]