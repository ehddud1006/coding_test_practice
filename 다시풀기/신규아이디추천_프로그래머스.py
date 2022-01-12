alphabet = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
special = "._-"

# new_id = "123_.def"

# 1단계
new_id = new_id.lower()
# print(f'1단계: {new_id}')

# 2단계
for i in new_id :
    if i in alphabet or i in number or i in special :
        continue
    else :
        new_id = new_id.replace(i,"")

# print(f'2단계: {new_id}')

# 3단계
while '..' in new_id :
    new_id = new_id.replace('..','.')
    
# print(f'3단계: {new_id}')    

# 4단계
if new_id[0] == "." :
    new_id = new_id[1:]
    if len(new_id)>0 and new_id[-1] == "." :
        new_id = new_id[:-1] 
elif new_id[-1] == "." :
    new_id = new_id[:-1] 
    
# print(f'4단계: {new_id}')     
            
if len(new_id)== 0 :
    new_id = "a"
    
# print(f'5단계: {new_id}')  

if len(new_id)>=16 :
    new_id = new_id[:15]
    if new_id[-1] == "." :
        new_id = new_id[:-1]         

# print(f'6단계: {new_id}')

while len(new_id)<=2 :
    new_id = new_id + new_id[-1]

# print(f'7단계: {new_id}')
    