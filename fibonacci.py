# Fibonacci Sequence
def Fibonacci_Sequence(fib_numbers):
        a, b = 0, 1
        for i in range(0, fib_numbers):
                print(a)
                a, b = b, a + b

Fibonacci_Sequence(11)


# Fibonacci Usign Recursion
fp = 0
def Recursive_Fibonacci_Sequence(n):
        global fp

        if (n <= 1):
                fp = 1
                return 1

        t = Recursive_Fibonacci_Sequence(n - 1)
        f = t + fp
        fp = t
        print(fp)
        
        return f

print(Recursive_Fibonacci_Sequence(9))


# Fibonacci Generator also uses Recursion
def Fibonacci(fib_nums):
        a, b = 0, 1
        for j in xrange(0, fib_nums):
                yield "{}: {}".format(j+1, a)   # yield = generator
                a, b = b, a + b

# loop through the generator
for item in Fibonacci(11):
        print(item)



# Simplified examples:

# Iterative Implementation
def iterative_fibonacci(fnum):
        result = [0, 1]

        for i in range (2, fnum):
                a = result[i - 1]
                b = result[i - 2]

                result.append(a + b)
        
        return result[fnum]


# Recursive Implementation
def Recursive_Fibonacci(rnum):
        if (rnum < 2):
                return rnum

        return Recursive_Fibonacci(rnum - 1) + Recursive_Fibonacci(rnum - 2)