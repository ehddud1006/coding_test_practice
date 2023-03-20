n = int(input())
input = [input() for _ in range(n)]

answer = '1'*input.index('KBS1') + '4'*input.index('KBS1')
input.remove('KBS1')
input.insert(1, 'KBS1')
answer += '1'*input.index('KBS2') + '4'*(input.index('KBS2')-1)

print(answer)
