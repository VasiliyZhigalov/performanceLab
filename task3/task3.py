import json
import sys


def find_value(tests, values):
    #Рекурсия
    for test in tests:
        for value in values:
            if value['id'] == test['id']:
                test['value'] = value['value']
                break
        if test.get('values'):
            find_value(test['values'], values)
    return tests


if __name__ == "__main__":
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    values = open(values_file, 'r')
    v = json.loads(values.read())['values']
    tests = open(tests_file, 'r')
    t = json.loads(tests.read())['tests']
    report = {'tests': find_value(t, v)}
    with open(report_file, 'w') as report_f:
        json.dump(report, report_f)
