new_id = "abcdefghijklmn.p"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBER ="0123456789"
SPECIAL = "-_."

#1단계
new_id = new_id.lower()
# print(new_id)

# 2단계
for word in new_id :
    if word in SPECIAL or word in NUMBER or word in ALPHABET :
        # print(f'if: {word}')
        continue
    else :
        new_id = new_id.replace(word,'')
        # print(f'else: {word}')
# print(new_id)

# 3단계
while '..' in new_id :
    new_id = new_id.replace('..','.')
    
# print(new_id)

# 4단계
if new_id[0] == '.' :
    new_id = new_id[1:]
    if len(new_id)>0 and new_id[-1] == '.' :
        new_id = new_id[:-1]
elif new_id[-1] == '.':
    new_id = new_id[:-1]
    
# new_id[:-2]라고 생각했는데 -1 로 해야 마지막글자 앞까지 자르는거니까
# -1로 해야한다.    

# print(new_id) 

# 5단계
if len(new_id) == 0 :
    new_id += 'a'

# print(new_id) 

# 6단계 
if len(new_id)>=16 :
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]       
 
# print(new_id) 
       
# 7단계 
if len(new_id)<=2 :
    plus = new_id[-1]
    while len(new_id)<3 :
             new_id = new_id + plus
             
# print(new_id) 
             





