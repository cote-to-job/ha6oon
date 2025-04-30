# 구현(시뮬레이션)
def solution(bandage, health, attacks):
    now_time = 1
    cnt = 0
    now_health = health
    
    for attack_time, attack_point in attacks:
        for _ in range(attack_time - now_time):
            print(now_time, now_health, cnt)
            now_health += bandage[1]
            cnt += 1
            if now_health > health:
                now_health = health
            if cnt == bandage[0]:
                now_health += bandage[2]
                if now_health > health:
                    now_health = health
                cnt = 0
        print(attack_time, -attack_point)  
        now_health -= attack_point
        if now_health <= 0:
            return -1
        cnt = 0  
        now_time = attack_time + 1  
            
    
    return now_health