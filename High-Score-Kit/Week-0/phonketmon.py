# 해시로 풀기
def solution(nums):
    '''
    INPUT : 
    nums(list) : 폰켓몬의 번호가 적힌 리스트
    
    OUTPUT :
    answer(int) : n/2 중에서 가장 많은 종류의 폰켓몬을 선택한 종류의 갯수
    '''
    answer = 0
    dict_pocketmon = {}
    for i in nums:
        if i not in dict_pocketmon.keys():
            dict_pocketmon[i] = 1
        else:
            dict_pocketmon[i] += 1
    if len(dict_pocketmon.keys()) >= len(nums)/2:
        answer = len(nums)/2
        print(answer)    
    else:
        answer = len(dict_pocketmon.keys())
               
    return answer
   
# 그냥 풀기
def solution2(nums): 
    return len(nums)/2 if len(nums)/2 <= len(set(nums)) else len(set(nums))
