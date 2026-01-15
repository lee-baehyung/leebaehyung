def solution(n, k):
    service_drinks = n // 10
    return (n * 12000) + ((k - service_drinks) * 2000)