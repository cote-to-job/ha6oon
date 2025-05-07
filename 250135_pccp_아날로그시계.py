#초침이 시침/분침과 겹칠 때마다 알람 울림 -> 특정 시간 동안 알람이 울린 횟수 리턴

def solution(h1, m1, s1, h2, m2, s2):
    # 초를 기준으로 분/시 계산
    start = (h1 * 3600) + (m1 * 60) + s1
    end = (h2 * 3600) + (m2 * 60) + s2

    ans = 0
    
    # 시분초가 만나는 무조건 만나는 시간은 0시와 12시일 때임 
    if start == 0 or start == (60 * 60 * 12):
        ans += 1

    # 초마다 이동하는 각도로 표현하기
    # 시침 12시간에 360도 -> 1시간에 30도 -> 1초에 30/3600도 (1/120도)
    # 분침 60분에 360도 -> 1초에 360/3600도 (0.1도)
    # 초침 60초에 360도 -> 1초에 6도
    while start < end: # 시작시간이 끝시간을 넘지 않을 때까지 1초씩 움직이면서 겹치는지 확인함
        rad_h = (start / 120) % 360
        rad_m = (start / 10) % 360
        rad_s = (start * 6) % 360
        
        # 1초후의 각도와 현재의 각도가 cross 된다면 만나기 때문에 1초후의 각도도 계산해줌
        rad_h_next = ((start + 1) / 120) % 360
        rad_m_next = ((start + 1) / 10) % 360
        rad_s_next = ((start + 1) * 6) % 360
        
        # 만약 시/분/초침의 각도가 0도로 돌아오면 계속 돌아가야 하기 때문에 360도로 맞춰줌
        if rad_h_next == 0:
            rad_h_next = 360
        if rad_m_next == 0:
            rad_m_next = 360
        if rad_s_next == 0:
            rad_s_next = 360
        
        
        #초침이 시침/분침과 만나는 경우 생각하기
        #1. 1초 후에 시/분/초가 모두 같은 각도인 경우
        #2. 시침이 초침보다 각도가 큰 상태에서, 1초 후에 초침의 각도가 더 커지는 경우
        #3. 분침이 초침보다 각도가 큰 상태에서, 1초 후에 초침의 각도가 더 커지는 경우
        
        # 1. 
        if rad_h_next == rad_m_next == rad_s_next:
            ans += 1
            start += 1
            continue
        # 2. 
        if rad_s < rad_h and rad_s_next >= rad_h_next:
            ans += 1
        # 3. 
        if rad_s < rad_m and rad_s_next >= rad_m_next:
            ans += 1

        start += 1
    return ans