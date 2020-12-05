flist = {}


def fib(n):
    fib.count = fib.count+1
    flist[0] = 0
    flist[1] = 1
    if n > 1:
        i = 2
        while i <= n:
            flist[i] = flist[i-1]+flist[i-2]
            i = i+1
        return flist[n]
    else:
        if n < 0:
            print("not possible for -ve numbers")
            return
        else:
            return flist[n]


fib.count = 0
print(fib(int(input())))
print(fib.count)
