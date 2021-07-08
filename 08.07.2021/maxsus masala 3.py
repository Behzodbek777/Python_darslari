shaxslar = [{
    "ism":"Behzod",
    "yosh" : 25,
    "otasining ismi":"Qodir",
    "jinsi":"erkak"
    },
    {
    "ism":"Laylo",
    "yosh" : 11,
    "otasining ismi":"Botir",
    "jinsi":"ayol"
    },
    {
    "ism":"Ulug'bek",
    "yosh" : 30,
    "otasining ismi":"Abdulla",
    "jinsi":"erkak"
    },
    {
    "ism":"Abdurauf",
    "yosh" : 22,
    "otasining ismi":"Sanjar",
    "jinsi":"erkak"
    },
    {
    "ism":"Bobur",
    "yosh" : 12,
    "otasining ismi":"Jo'ra",
    "jinsi":"erkak"
    },
{
    "ism":"Barno",
    "yosh" : 14,
    "otasining ismi":"Yorqin",
    "jinsi":"ayol"
    }
]
for shaxs in shaxslar:
    if shaxs["jinsi"]=="ayol":
        if shaxs["otasining ismi"][-1]=="a" or shaxs["otasining ismi"][-1]=="o" or  shaxs["otasining ismi"][-1]=="e" or  shaxs["otasining ismi"][-1]=="i":
            shaxs["otasining ismi"]=shaxs["otasining ismi"]+"yeva"
            print(shaxs)


        else:
            shaxs["otasining ismi"] = shaxs["otasining ismi"] + "ova"
        print(shaxs)
    elif shaxs["jinsi"]=="erkak":
        if shaxs["otasining ismi"][-1]=="a" or shaxs["otasining ismi"][-1]=="o" or  shaxs["otasining ismi"][-1]=="e" or  shaxs["otasining ismi"][-1]=="i":
            shaxs["otasining ismi"]=shaxs["otasining ismi"]+"yev"
            print(shaxs)
        else:
            shaxs["otasining ismi"] = shaxs["otasining ismi"] + "ov"
        print(shaxs)



