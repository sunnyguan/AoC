import re

def p(k):
    b = re.findall(r'(\d+)-(\d+) ([a-z]): ((.*?)\3){1}', k)
    if b:
        c = re.findall(fr': ((.*?){b[0][2]}){{{b[0][0]}}}', k)
        d = re.findall(fr': ((.*?){b[0][2]}){{{int(b[0][1])+1}}}', k)
        return 1 if c and not d else 0
    return 0

with open('day2.in', 'r') as f:
    s = f.read().split("\n")
    print(sum([p(a) for a in s]))