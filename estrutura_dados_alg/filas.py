inQueue = []
deQueue = []
for i in range(10):
    inq = f"[{i}] "
    inQueue.append(inq)
    print(inQueue)
for j in range(10):
    deq = inQueue.pop(0)
    deQueue.append(deq)
    print(inQueue)