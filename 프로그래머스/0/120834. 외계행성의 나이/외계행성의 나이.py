def solution(age):
    alphabet = "abcdefghij"
    return "".join([alphabet[int(i)] for i in str(age)])