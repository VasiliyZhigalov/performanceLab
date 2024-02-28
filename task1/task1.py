import sys


def circle_arr(n, m):
    arr = list(range(1, n + 1))
    begin = arr[0]
    current_pos = 0
    path = ''
    while True:
        if current_pos + m - 1 < n:
            new_current_pos = current_pos + m - 1
            path_arr = arr[current_pos: new_current_pos + 1]
        else:
            new_current_pos = current_pos + m - n - 1
            path_arr = arr[current_pos:] + arr[:new_current_pos + 1]
        current_pos = new_current_pos
        path += str(path_arr[0])
        if begin == path_arr[-1]:
            break
    return int(path)


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    path = circle_arr(n, m)
    print(path)
