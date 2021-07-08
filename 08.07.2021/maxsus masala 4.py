person1 = {
    "name" : "John",
    "father" : "Bill",
    "motehr" : "Anna",
    "married" : 0
}
person2 = {
    "name" : "Kate",
    "father" : "Pet",
    "motehr" : "Maria",
    "married" : 0
}
year1 = int(input("person1 was married:"))
year2 = int(input("person2 was married:"))
if year1==year2:
    person3 = {
        "name": "Bruce",
        "father": "John",
        "motehr": "Kate",
        "married": 0
    }
    person2.update({"married": True})
    person1.update({"married": True})
    print(f"{person1}")
    print(f"{person2}")
    print(f"farzand ->{person3}")
else:
    print("Tey were not married together")
