fpath = "C:\\Users\\carlos.toledo\\Downloads\\cfc\\cf74"

f = open(fpath)

docs = {} 

ab = False
abkey = ""
abvalue = ""

for line in f:

    if(ab):
        if (line[:2] == "  "):
            abvalue += line[2:-2]
        else:
            ab = False
            docs[abkey] = abvalue
    else:
        if (line[:2] == "RN"):
            abkey = line[3:-2]
        
        elif (line[:2] == "AB"):
            abvalue = line[2:-2]
            ab = True

for key,value in docs.items():
    print("{}:{}".format(key,value))
