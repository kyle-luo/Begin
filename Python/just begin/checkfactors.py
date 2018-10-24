def checkfactor(x):
    if x == 1:
        print str(x) + "'s factor is"
        print 1
    elif x == 0:
        print 'Dude, every integer is a factor of 0.'
    elif x%2 == 0:
        factor = 1
        print str(x) + "'s factors are"
        while factor <= x / 2:
            if x % factor == 0:
                print factor
                factor += 1
            else:
                factor += 1
        print x
    else:
        print str(x) + "'s factors are"
        print 1
        print x

checkfactor(0)
checkfactor(1)
checkfactor(18)
checkfactor(135)
checkfactor(596)