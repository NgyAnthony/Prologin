def seedLCG(initVal):
    global rand
    rand = initVal

def lcg():
    a = 1337
    c = 404
    m = 1000
    global rand
    rand = (a*rand + c) % m
    return rand / m

seedLCG(42)

for i in range(333):
    print (lcg())