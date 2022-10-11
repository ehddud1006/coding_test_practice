import sys
input = sys.stdin.readline
 
S = list(input().rstrip())
result = ['']*len(S)
 
 
def func(arr, start):
    if not arr:
        return
    _min = min(arr)
    idx = arr.index(_min)
    result[start+idx] = _min
    print("".join(result))
    func(arr[idx+1:], start+idx+1)
    func(arr[:idx], start)
 
 
func(S, 0)