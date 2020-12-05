flist = {}


def fib(n):
    """
    calculates the fibbonaci number at nth value and returns it
    """
    fib.count = fib.count+1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if not n-1 in flist:
        flist[n-1] = fib(n-1)
    if not n-2 in flist:
        flist[n-2] = fib(n-2)
    return flist[n-1]+flist[n-2]


fib.count = 0
print(fib(int(input())))
print(fib.count)
