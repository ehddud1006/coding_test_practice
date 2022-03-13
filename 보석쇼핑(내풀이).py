

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
def solution(gems):
    
    # 중복을 제거하기 위해서 
    real_gems_count = len(set(gems))
    real_gems = set(gems)
    gem_count = {}
    lp = 0
    rp = 0
    
    len_gems_arr = len(gems)
    gugan_gili = len(gems)
    answer = [1,gugan_gili]
    while rp < len_gems_arr :
         
        if gems[rp] in gem_count :
            gem_count[gems[rp]] +=1 
        else :
            gem_count[gems[rp]] = 1 

        rp += 1
        
        while len(gem_count) == real_gems_count :
            if gem_count[gems[lp]]>1 :
                gem_count[gems[lp]] -= 1
                lp += 1
            elif rp-lp < gugan_gili :
                gugan_gili = rp - lp 
                answer = [lp+1,rp]
                break
            else :
                break 
                
    return answer

solution(gems)