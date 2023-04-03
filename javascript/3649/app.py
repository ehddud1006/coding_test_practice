import sys
input = sys.stdin.readline

NANO_METER = 10_000_000
answer = []

while True:
    try:
        widthHole = int(input()) * NANO_METER
        numberOfLegoPeices = int(input())
        legoPeices = []

        legoPeices = [int(input()) for _ in range(numberOfLegoPeices)]

        legoPeices.sort()

        lt, rt = 0, numberOfLegoPeices-1
        flag = True

        while lt <= rt:
            if widthHole == legoPeices[lt] + legoPeices[rt]:
                print('yes %d %d' %(legoPeices[lt], legoPeices[rt]))
                flag = False
                break
            elif widthHole > legoPeices[lt] + legoPeices[rt]:
                lt += 1
            else:
                rt -= 1

        if flag:
            print('danger')
    except:
        break
