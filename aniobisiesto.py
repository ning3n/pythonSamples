def is_leap(year):
    leap = False

    a = 1992%4
    b = 1992%100
    c = 1992%400

    if (year%4 == 0) and (year%100 == 0) and (year%400 == 0):
        leap = True
    
    return a,b,c


    #return leap

year = int(input())
print(is_leap(year))