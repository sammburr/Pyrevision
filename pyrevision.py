import random
import os

topics_path = os.getenv('APPDATA') + '\\pyrevision\\topics.csv'

def get_values(l):
    return l.split(',')

def print_topic(v):
    if len(v) > 2:
        print('Module: ' + v[0] + '\n' + 'Topic:  ' + v[1])
    else:
        print('Invalid module of values: ' + v)

lines = []
with open(topics_path) as f:
    lines = f.readlines()

header = lines[0]
lines = lines[1:]
random.shuffle(lines)

if len(lines) > 0:
    lowest_score = 9999
    for line in lines:
        values = get_values(line)
        if int(values[2]) < lowest_score:
            lowest_score = int(values[2])
    i = 0
    for line in lines:
        values = get_values(line)
        score = int(values[2])
        if score == lowest_score:
            print_topic(values)
            values[2] = str(score + 1) + '\n'
            lines[i] = ','.join(values)
            break
        i = i+1

    with open(topics_path, 'w') as f:
        f.write(header)
        f.write(''.join(lines))
    
else:
    print('No topics in topics.csv!')

