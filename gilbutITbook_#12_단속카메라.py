#그리디 - 가장 빨리 빠져나가는 차량에 카메라 설치
def solution(routes):
    routes.sort(key=lambda x:x[1])
    answer = 0
    last_camera = -30001
    for route in routes:
        if route[0] > last_camera:
            answer += 1
            last_camera = route[1]
    return answer