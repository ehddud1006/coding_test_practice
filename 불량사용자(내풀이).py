from itertools import permutations

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]

def check_permutation_id(prediction_id,banned_id):
    # banned_id 리스트의 길이를 기준으로 permutations을 하였기때문에
    # for문의 index를 banned_id 리스트길이로 선언합니다
    for i in range(len(banned_id)):
        # 만약 banned_id와 매칭되는 user_id의 길이가 서로 다르다면 
        # 제재 아이디 목록이 될 수 없으므로 return False 합니다
        if len(prediction_id[i]) != len(banned_id[i]) :
            return False
        # 길이가 같은경우에 * 라면 continue를 하고 
        # 문자열하나씩 비교했을때 하나라도 다르다면 False를 리턴합니다.
        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*' :
                continue
            elif banned_id[i][j] != prediction_id[i][j] :
                return False
    # 위 조건을 무사히 통과하였으면 True를 리턴합니다.
    return True

def solution(user_id, banned_id):
    answer = 0
    answer_set_list = []
    for prediction_id in permutations(user_id,len(banned_id)):
        if check_permutation_id(prediction_id,banned_id) :
            # set을 사용한 이유는 
            # {'frodo', 'abc123', 'crodo'}
            # {'frodo', 'frodoc', 'crodo'}
            # {'frodo', 'abc123', 'crodo'}
            # {'frodo', 'frodoc', 'crodo'}
            # 테스트 케이스 2번의 경우 permutations에서 
            # frodo , crodo
            # crodo , frodo 는 다른 경우이지만, 제재 아이디 목록에서는 
            # 하나의 경우로 수를 셉니다. 그러므로 그부분의 중복을 제거하기 위함입니다.
            if set(prediction_id) not in answer_set_list :
                answer_set_list.append(set(prediction_id))
    answer = len(answer_set_list)
    return answer

# solution(user_id,banned_id)