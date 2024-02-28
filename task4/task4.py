import sys


def count_step(nums):
    # Википедия: Медиана набора чисел — это число, сумма расстояний (или, если более строго, модулей)
    # от которого до всех чисел из набора минимальна.
    # Если набор упорядочить по возрастанию, то есть такое число,
    # что половина из элементов набора не меньше него, а другая половина не больше
    nums.sort()
    m = nums[len(nums) // 2]
    steps = 0
    for x in nums:
        steps += abs(x - m)
    print(steps)


if __name__ == '__main__':
    file = sys.argv[1]
    f = open(file, 'r')
    lines = f.readlines()
    nums = [int(l) for l in lines]
    count_step(nums)
