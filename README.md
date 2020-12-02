## My solutions for AoC 2020

Note: actual submissions are written in Java.

### Day 1

JavaScript: using `find` and `some` in JS, golfed from 124 to 85 bytes

`a=document.body.innerText.split("\n");k=2020;r=a.find(b=>a.some(c=>b- -c==k));r*(k-r)`

### Day 2

Python: cool regex matching solution

```
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
```
