shaxslar = [{
    "ism":"Behzod",
    "yosh" : 25
    },
    {
    "ism":"Laylo",
    "yosh" : 11
    },
    {
    "ism":"Ulug'bek",
    "yosh" : 30
    },
    {
    "ism":"Abdurauf",
    "yosh" : 22
    },
    {
    "ism":"Bobur",
    "yosh" : 12
    }
]
for shaxs in shaxslar:
    for yosh in shaxs:
        if shaxs["yosh"]>20:
            print(shaxs["ism"])
