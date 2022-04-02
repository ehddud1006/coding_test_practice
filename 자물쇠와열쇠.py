def turn_right_key(_key):
    key_size = len(_key)
    temp_key = [[0] * key_size for i in range(0, key_size)]
 
    reverse_i = key_size - 1
    for i in range(key_size):
        for j in range(key_size):
            temp_key[j][reverse_i] = _key[i][j]
        reverse_i -= 1
 
    return temp_key
 
 
def is_unlock(bg_size, _lock, _key, start_x, start_y, c_start, c_end):
    bg = [[0] * bg_size for i in range(0, bg_size)]
 
    # 1. put key in background
    for i in range(0, len(_key)):
        for j in range(0, len(_key)):
            bg[start_y + i][start_x + j] += _key[i][j]
 
    # 2. put lock in background
    for i in range(c_start, c_end):
        for j in range(c_start, c_end):
            bg[i][j] += _lock[i - c_start][j - c_start]
            # lock + key == 1이 안닌 경우 False
            if bg[i][j] != 1:
                return False
 
    return True
 
 
def unlock(_lock, _key):
    lock_size = len(_lock)
    c_start = len(_key) - 1 # center 좌표
    c_end = c_start + lock_size
    bg_size = lock_size + (2 * c_start) # 처음부터 1개 겹쳐서 비교하기 위해
 
    for x in range(0, 4):
        for i in range(0, c_end):
            for j in range(0, c_end):
                if is_unlock(bg_size, _lock, _key, i, j, c_start, c_end) is True:
                    return True
        # key를 90도 돌린다.
        _key = turn_right_key(_key)
 
    return False
 
 
if __name__ == "__main__":
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
 
    print(unlock(lock, key))