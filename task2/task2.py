import sys


def _position_of_dot_to_circle(radius, pos_circle, pos_dot):
    k = (pos_circle[0] - pos_dot[0]) ** 2 + (pos_circle[1] - pos_dot[1]) ** 2
    if k < radius ** 2:
        return 1
    elif k > radius ** 2:
        return 2
    else:
        return 0


def _dots_position(circle_file, dots_file):
    # парсим точки
    dots_f = open(dots_file, 'r')
    dot_lines = dots_f.readlines()
    dots = [list(map(float, line.strip().split())) for line in dot_lines]
    # парсим окружность
    circle_f = open(circle_file, 'r')
    circle_lines = circle_f.readlines()
    pos_circle = list(map(float, circle_lines[0].strip().split()))
    radius = float(circle_lines[1].strip())
    for dot in dots:
        res = _position_of_dot_to_circle(radius, pos_circle, dot)
        print(res)


if __name__ == "__main__":
    circle_file = sys.argv[1]
    dots_file = sys.argv[2]
    _dots_position(circle_file, dots_file)
