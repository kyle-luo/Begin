opg = open('C:/Users/tsjlk/OneDrive/Desktop/ltx.htm')
page = []
for x in opg:
    string = str(x)
    page.append(string)

def count(word):
    ct = 0
    for x in page:
        a = x.count(word)
        ct += a
    print(ct)

def countnotin(x,y):
    list = []
    for b in page:
        a = str(b)
        words = a.split(' ')
        for c in words:
            if y not in c:
                if x in c:
                    list.append(c)
    print(list)

def inp(word):
    list = []
    count=0
    for x in page:
        if '<p>' in x:
            if word in x:
                list.append(x)
                count+=1
    print(list)

count('licensetraxx')
count('license')
count('track')

inp('track')
