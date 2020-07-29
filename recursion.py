# Recursion

def Func_R(a):
        if a == 0:
                return 0
        else:
                return Func_R(a - 1) + 1

# Func_R(3) => 3
# Recursion is LIFO - Last In Fisrt Out


def Func_R_Explained(b):
        print("Start: " + str(b))
        res = 0

        if b == 0:
                res = 0
        else:
                res = Func_R_Explained(b - 1) + 1

        print("End: " + str(b))
        return res

# Now you can see the Stack
# Start: 3
# Start: 2
# Start: 1
# Start: 0      -       Last In
# End: 0        -       First Out
# End: 1
# End: 2
# End: 3
# 3


def Func_R_Fail(c):
        print("Start: " + str(c))
        print("End: " + str(c))
        return Func_R_Fail(c - 1) + 1

# RecursionError: maximum recursion depth exceeded while calling a Python object
# You get this error when you call the function about a thousand times
# That will be the same as a While Loop without a reachable base case



# Sum

# Fail Implementation
def Recursive_Sum_Fail(n):
        if (n > 100):
                return n;
        else:
                return (n + Recursive_Sum_Fail(n - 1))


# you always need a reachable Base Case
# for instance, if the input is n = 99, you'll have an Stack Overflow Error
# and you get a crash, that's beacuse you have a case when the function never ends
# the Stack is Last In First Out queue and has all the tasks that will be excecuted


def Recursive_Sum(n):
        if (n <= 1):
                return n
        else:
                return (n + Recursive_Sum(n - 1))


# for example n = 3, here the output that we have is 6
# that's because the function will be executed 3 times
# the outputs of each call will be { (1) ; (2 + 1) ; (3 + 3) }



# Factorial

# Iterative Implementation
def Iterative_Factorial(fact):
        if (fact == 0 or fact == 1):
                return 1
        
        for i in range (fact-1, 1, -1):
                fact = fact * i

        return fact


# Recursive Implementation
def Recursive_Factorial(fnum):
        if (fnum == 0 or fnum == 1):
                return 1

        return fnum * Recursive_Factorial(fnum - 1)
