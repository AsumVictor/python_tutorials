
def main():
    a = int(input('Lower limit: '))
    b = int(input('Upper limit: '))
    n = int(input('Number of partition: '))
    pre_cal = ((b - a) / n)
    print(all_sum(r_sum(n, a, pre_cal), pre_cal))


def r_sum(n, a, pre_cal):
    sum: int = 0
    for i in range(1, n+1):
        r = a + (i - 0.5) * pre_cal
        sum += function_r(r)
    return sum


def function_r(r):
    return 4/((r**2 + 1))


def all_sum(sum, pre_cal):
    return pre_cal * sum


main()
