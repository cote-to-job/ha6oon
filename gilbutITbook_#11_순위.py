def solution(n, results):
    # 선수 간의 승패 관계를 저장할 2차원 배열 생성
    # 0: 관계 없음, 1: i가 j를 이김, -1: i가 j에게 짐
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    # 입력된 결과를 바탕으로 초기 승패 기록
    for win, lose in results:
        graph[win][lose] = 1      # win 선수가 lose 선수를 이김
        graph[lose][win] = -1     # lose 선수는 win 선수에게 짐

    # 플로이드-워셜 알고리즘: 간접 승패 관계 전파
    for k in range(1, n + 1):           # 중간 선수 k
        for i in range(1, n + 1):       # 시작 선수 i
            for j in range(1, n + 1):   # 끝 선수 j
                # i가 k를 이기고, k가 j를 이기면 → i는 j도 이김
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1   # 반대 방향도 같이 갱신
                # i가 k에게 지고, k가 j에게 지면 → i는 j에게도 짐
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1    # 반대 방향도 같이 갱신

    answer = 0  # 정확한 순위를 알 수 있는 선수 수

    # 각 선수에 대해 순위를 알 수 있는지 확인
    for i in range(1, n + 1):
        known = 0  # i 선수의 승패가 확실한 다른 선수 수
        for j in range(1, n + 1):
            if i == j:
                continue
            if graph[i][j] != 0:  # 승패 관계가 있으면 +1
                known += 1
        # 자기 제외한 모든 선수와 승패가 확실하면 순위 확정
        if known == n - 1:
            answer += 1

    return answer
