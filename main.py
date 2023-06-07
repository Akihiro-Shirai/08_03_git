def Max_1(x, y, z):
    m = x
    if y > m:
        m = y
    if z > m:
        m = z
    return m


def Min_1(x, y, z):
    n = x
    if y < n:
        n = y
    if z < n:
        n = z
    return n


def multi(a, b, c):
    s = Max_1(a, b, c)
    t = Min_1(a, b, c)
    u = s * t
    return u


def divide(a, b, c):
    s = Max_1(a, b, c)
    t = Min_1(a, b, c)
    u = s / t
    return u


def main():
    print("任意の数字を3つ入力してください。")
    x = int(input("1つ目の数字："))
    y = int(input("2つ目の数字："))
    z = int(input("3つ目の数字："))

    print("最大値と最小値の積は ", multi(x, y, z), " です。")
    print("最大値と最小値の商は ", divide(x, y, z), " です。")


main()
