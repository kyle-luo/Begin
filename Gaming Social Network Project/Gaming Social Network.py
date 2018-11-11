def computepay(h,r):
    if h <= 40:
        return h * r
    else:
        return 40 * r + (h - 40) * r * 1.5

hrs = float(input("Enter Hours:"))
rate = float(input('Enter Rate:'))
p = computepay(hrs, rate)
print("Pay",p)