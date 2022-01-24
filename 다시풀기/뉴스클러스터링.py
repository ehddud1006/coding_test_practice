
from collections import Counter

str1 = "aa1+aa2"
str2 = "AAAA12"
alphabet="abcdefghijklmnopqrstuvwxyz"

def solution(str1, str2):
    answer = 0
    set1 = []
    set2 = []
    
    gyu = 0
    hap = 0
    # 대문자를 소문자로
    str1 = str1.lower()
    str2 = str2.lower()
    
    # #특수 문자 정리
    # for w in str1 :
    #     if w not in alphabet :
    #         str1=str1.replace(w,"")      
    
    # for w in str2 :
    #     if w not in alphabet :
    #         str2=str2.replace(w,"")   
            
    for i in range(len(str1)-1) :
        w = str1[i:i+2]
        if w.isalpha() :
            set1.append(str1[i:i+2])
    
    for i in range(len(str2)-1) :
        w = str2[i:i+2]
        if w.isalpha() :
            set2.append(str2[i:i+2])
        
    set1_count = Counter(set1)
    set2_count = Counter(set2)
    hap = sum((set2_count | set1_count).values())
    gyu = sum((set2_count & set1_count).values())

    print(gyu)
    print(hap)
    if gyu == 0 and hap == 0 :
        answer = 65536
        print(answer)
        return answer
    
    answer = int((gyu / hap) * 65536)  
    print(answer)
    
    print(f'str1: {str1}')
    print(f'str2: {str2}')
    print(f'set1: {set1}')
    print(f'set2: {set2}')
    print(f'set1_count: {set1_count}')
    print(f'set2_count: {set2_count}')
    print(f'set2_count & set1_count: {set2_count & set1_count}')
    print(f'set2_count | set1_count: {set2_count | set1_count}')
    print(f'(set2_count | set1_count).values() : {(set2_count | set1_count).values()}')
    
    # # str1: france
    # str2: french
    # set1: {'an', 'nc', 'fr', 'ce', 'ra'}
    # set2: {'re', 'nc', 'ch', 'fr', 'en'}
    # set1_count: Counter({'an': 1, 'nc': 1, 'fr': 1, 'ce': 1, 'ra': 1})
    # set2_count: Counter({'re': 1, 'nc': 1, 'ch': 1, 'fr': 1, 'en': 1})
    # set2_count & set1_count: Counter({'nc': 1, 'fr': 1})
    # set2_count | set1_count: Counter({'re': 1, 'nc': 1, 'ch': 1, 'fr': 1, 'en': 1, 'an': 1, 'ce': 1, 'ra': 1})
    # (set2_count | set1_count).values() : dict_values([1, 1, 1, 1, 1, 1, 1, 1])
    return answer

solution(str1,str2)

