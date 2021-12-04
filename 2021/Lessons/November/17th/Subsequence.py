def largestcontiguoussum():
    v = [int(i) for i in input().split()];
    mx = -10000000000;
    sum = 0;
    for i in v:
        sum = max(sum+i,i);
        mx = max(sum,mx);
    print("Sum:",mx);
    return 0;
# def largestcontiguousproduct():
    # v = [int(i) for i in input().split()];
    # best = -100000000;
    # mx = 1;
    # mn = 1;
    # for i,x in enumerate(v):
        # temp1 = min(i,mn);
        # temp2 = max(i,mx);
    # print("Product:",mx);
    # return 0;
def pairsum():
    sum = int(input());
    v = [int(i) for i in input().split()];
    a = 0;
    b = len(v)-1;
    while (v[a]+v[b] != sum):
        if (v[a]+v[b] < sum):
            a+=1;
        if (v[a]+v[b] > sum):
            b-=1;
        if (a > b):
            print("No Sum Found");
            return 0;
    print(v[a],v[b]);
    return 0;
def tuplesum():
    sum = int(input());
    v = [int(i) for i in input().split()];
    imp = True;
    for i in v:
        s = sum - i;
        a = 0;
        b = len(v)-1;
        while (v[a]+v[b] != s):
            if (v[a]+v[b] < s):
                a+=1;
            if (v[a]+v[b] > s):
                b-=1;
            if (a > b):
                break;
        if (v[a]+v[b] == s):
            imp = False;
            break;
    if (imp):
        print("Impossible");
    else:
        print(v[a],v[b],sum-v[a]-v[b]);
    return 0;
# largestcontiguoussum();
# largestcontiguousproduct();
# pairsum();
# tuplesum();
