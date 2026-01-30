def solution(s):
    answer = 0
    words = s.split()
    last_num = 0
    
    for char in words:
        if char == "Z":
            answer -= last_num
        else:
            num = int(char)
            answer += num
            last_num = num
            
    return answer