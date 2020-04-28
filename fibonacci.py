def fibonacci(n):
        a = 0
        b, f = 1, 1
        for i in range(0, n):
                f = a + b
                a = b
                b = f
        
        return f

print(fibonacci(5))


fp = 0
def recursive_fibonacci(n):
        global fp

        if (n <= 1):
                fp = 1
                return 1

        t = recursive_fibonacci(n - 1)
        f = t + fp
        fp = t
        
        return f

print(recursive_fibonacci(5))