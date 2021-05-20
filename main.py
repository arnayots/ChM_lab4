import math
import sys

a = 0.25 * (-3 - math.sqrt(13))
b = 0.25 * (-3 + math.sqrt(13))
p = 4
eps = 0.5 * 1E-4

debug = True
debug = False
maxIter = 1000

fname = "log.txt"
f = open(fname, "w")

def f1(x):
    return 2*x

def f2(x):
    return 2* x**2 + 5*x - 0.5

def get_h(n):
    return (b - a) / n

def get_equal_pts(n):
    if n < 2:
        raise Exception("in get_equal_pts(n) n < 2")
    tmp = list([])
    h = get_h(n)
    for i in range(0, n + 1):
        tmp.append(a + i * h)
    if debug:
        print(tmp)
    return tmp

def Simpsone(func, n: int):
    h = get_h(n)
    points = get_equal_pts(n)
    sum_1 = 0
    for i in range(0, round(n/2)):
        sum_1 += func(points[2*i - 1])
    sum_2 = 0
    for i in range(0, round(n/2) - 1):
        sum_2 += func(points[2*i])
    res = (func(points[0]) + 4 * sum_1 + 2 * sum_2 + func(points[n])) * h / 3
    return res

def runge_mistake(cur_integr, prev_integr):
    return abs(prev_integr - cur_integr) / (2**p - 1)

def calc(func):
    n = 2
    prev_integr = Simpsone(func, n)
    n = 2*n - 1
    cur_integr = Simpsone(func, n)
    iter = 0
    f.write("Starting calc" + "\n")
    if debug:
        print("Starting calc")
    r_mist = runge_mistake(cur_integr, prev_integr)
    f.write(str(iter) + " n = " + str(n) + " : prev_iter = " + str(prev_integr) + " cur_iter = " + str(cur_integr) + " diff = " + str(r_mist) + "\n")
    if debug:
        print(str(iter) + " : prev_iter = " + str(prev_integr) + " cur_iter = " + str(cur_integr) + "diff = " + str(r_mist))
    while (r_mist >= eps and iter < maxIter):
        prev_integr = cur_integr
        n = 2 * n - 1
        cur_integr = Simpsone(func, n)
        iter += 1
        f.write(str(iter) + " n = " + str(n) + " : prev_iter = " + str(prev_integr) + " cur_iter = " + str(cur_integr) + " diff = " + str(r_mist) + "\n")
        if debug:
            print(str(iter) + " : prev_iter = " + str(prev_integr) + " cur_iter = " + str(cur_integr) + "diff = " + str(r_mist))
        r_mist = runge_mistake(cur_integr, prev_integr)
    if iter == maxIter:
        raise Exception("Error: too many iterations")
    f.write("steps: " + str(iter) + " n: " + str(n) + " h: " + str(get_h(n)) + "\n")
    return cur_integr

if __name__ == '__main__':
    print("Calculating...")
    f.write("Function f1(x) = 2*x\n")
    interg1 = calc(lambda x: f1(x))
    f.write("For function " + "f1(x) = 2*x" + " integral in range [" + str(a) + " , " + str(b) + "] is \n")
    f.write("integral = " + str(interg1) + "\n")
    f.write("\nFunction f2(x) = 2*x^2 + 5*x - 0.5\n")
    interg2 = calc(lambda x: f2(x))
    f.write("For function " + "f2(x) = 2*x^2 + 5*x - 0.5" + " integral in range [" + str(a) + " , " + str(b) + "] is \n")
    f.write("integral = " + str(interg2) + "\n")
    area = interg1 - interg2
    f.write("\narea = " + str(area) + "\n")
    f.close()
    print("OK")
    sys.exit(0)
