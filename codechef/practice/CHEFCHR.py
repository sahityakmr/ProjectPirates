t = int(input())
while t>0:
    str = input()
    l = len(str)
    chk = ['chef','chfe','cehf','cefh','cfhe','cfeh','hcef','hcfe','hecf','hefc','hfce','hfec','echf','ecfh','ehcf','ehfc','efch','efhc','fche','fceh','fhce','fhec','fech','fehc']
    count = 0
    for i in range (0,l-3):
        if str[i:i+4] in chk:
            count = count + 1
    if count == 0:
        print("normal")
    else:
        print("lovely",count)
    t = t-1
