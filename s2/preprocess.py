def preprocess(para_list):
    x = para_list
    keywords = ["disclaimer","ndtv","look here","also read","swirlster","buy","shopping","post","here:"]

    list1=[]
    for i in x:
        if(i.lower().find(keywords[0]) != -1):
            continue
        elif(i.lower().find(keywords[1]) != -1):
            continue
        elif(i.lower().find(keywords[2]) != -1):
            continue
        elif(i.lower().find(keywords[3]) != -1):
            continue
        elif(i.lower().find(keywords[4]) != -1):
            continue
        elif(i.lower().find(keywords[5]) != -1):
            continue
        elif(i.lower().find(keywords[6]) != -1):
            continue
        elif(i.lower().find(keywords[7]) != -1):
            continue
        elif(i.lower().find(keywords[8]) != -1):
            continue
        else:
            list1.append(i)
    return list1        

