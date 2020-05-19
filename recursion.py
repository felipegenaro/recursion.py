# Sum

# Fail Implementation
def Recursive_Sum(n):
        if (n > 100):
                return n;
        else:
                return (n + Recursive_Sum(n - 1))


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
