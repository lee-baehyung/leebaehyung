def solution(hp):
    general, hp = divmod(hp, 5)
    soldier, worker = divmod(hp, 3)
    
    return general + soldier + worker