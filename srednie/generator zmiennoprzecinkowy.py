def frange(start, stop=None, step=None):
    # if stop and step argument is None set start=0.0 and step = 1.0
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    print("start= ", start, "stop= ", stop, "step= ", step)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

for i in frange(1.12,-0.14,-0.14):
    print(i)