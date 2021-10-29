ppl = 0
max_ppl = 0

for i in range(10):
    out, go = map(int, input().split())
    ppl += go - out
    if ppl > max_ppl:
        max_ppl = ppl
print(max_ppl)