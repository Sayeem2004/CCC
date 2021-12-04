def main():
    fin = open("CCC Placement _ Availability (Responses) - Form Responses 1.csv","r");
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    split = [];
    for line in lines:
        temp = [];
        a = line;
        for i in range(4):
            c = a.find(",");
            temp.append(a[0:c]);
            a = a[c+1:];
        temp.append(a);
        split.append(temp);
    bd,id,ad = {'C':0,'M':0,'T':0,'W':0},{'C':0,'M':0,'T':0,'W':0},{'C':0,'M':0,'T':0,'W':0};
    for line in split:
        if line[3] == "Beginner":
            bd['C'] = bd['C']+1;
            if line[4].find("Monday") != -1: bd["M"] = bd["M"]+1;
            if line[4].find("Tuesday") != -1: bd["T"] = bd["T"]+1;
            if line[4].find("Wednesday") != -1: bd["W"] = bd["W"]+1;
        if line[3] == "Intermediate":
            id['C'] = id['C']+1;
            if line[4].find("Monday") != -1: id["M"] = id["M"]+1;
            if line[4].find("Tuesday") != -1: id["T"] = id["T"]+1;
            if line[4].find("Wednesday") != -1: id["W"] = id["W"]+1;
        if line[3] == "Advanced":
            ad['C'] = ad['C']+1;
            if line[4].find("Monday") != -1: ad["M"] = ad["M"]+1;
            if line[4].find("Tuesday") != -1: ad["T"] = ad["T"]+1;
            if line[4].find("Wednesday") != -1: ad["W"] = ad["W"]+1;
    print("Beginner: ","Count: "+str(bd["C"]),"Monday: "+str(bd["M"]),"Tuesday: "+str(bd["T"]),"Wednesday: "+str(bd["W"]));
    print("Intermediate: ","Count: "+str(id["C"]),"Monday: "+str(id["M"]),"Tuesday: "+str(id["T"]),"Wednesday: "+str(id["W"]));
    print("Advanced: ","Count: "+str(ad["C"]),"Monday: "+str(ad["M"]),"Tuesday: "+str(ad["T"]),"Wednesday: "+str(ad["W"]));

main();
