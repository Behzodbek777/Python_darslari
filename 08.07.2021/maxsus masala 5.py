EnUz = {
    "i" : "men",
    "you" : ["siz","sen"],
    "he": "u"
}
suz =input("inglizcha so'z kiriting:")
suz =suz.lower()
if suz in EnUz:
    print(EnUz[suz])
else:
    print("bunday so'z yo'q")