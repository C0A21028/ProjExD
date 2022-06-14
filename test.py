print("hello world")

single = [2,4,6,8,10]
twice = list()

for i in single:
    twice.append(i*2)

print(twice)

scores = list()
while True:
    y = int(input("リストに入れる値"))
    if y < 0:
        break
    else:
        scores.append(y)