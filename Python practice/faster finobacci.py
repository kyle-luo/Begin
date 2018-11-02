#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    fibz = 0
    fibo = 1
    for step in range(0, n - 2):
        #fibpass = fibo
        #fibo += fibz
        #fibz = fibpass
        #step += 1
        fibo, fibz = fibo + fibz, fibo
    return fibo + fibz





print fibonacci(15)
# >>> 610
print fibonacci(36)
#>>> 14930352