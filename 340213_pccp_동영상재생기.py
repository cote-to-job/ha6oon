# 구현 - 문자열 ~ 분,초 단위 계산 유의
def solution(video_len, pos, op_start, op_end, commands):
    for command in commands:
        # 광고 범위 내에 있으면 광고 끝으로 점프
        if transform(pos) >= transform(op_start) and transform(pos)<= transform(op_end):
            pos = op_end
        # 명령어 실행
        if command == 'next':
            pos = calculate(pos, 10)
            if transform(pos) > transform(video_len):
                pos = video_len
        else: # command == 'prev'
            pos = calculate(pos, -10)
            if transform(pos) < 0:
                pos = "00:00"
        if transform(pos) >= transform(op_start) and transform(pos)<= transform(op_end):
            pos = op_end
    return pos

def transform(now): # 문자열 시간 -> 초 계산후 리턴
    min = int(now[:2])
    sec = int(now[3:])
    return 60 * min + sec
def calculate(now, cal): # +- 계산 -> 문자열 리턴
    total_seconds = transform(now) + cal
    total_seconds = max(0, total_seconds)  # 0초 미만 방지
    min = total_seconds // 60
    sec = total_seconds % 60
    return f"{min:02d}:{sec:02d}" # 시간 문자열 형식 보정 - 분과 초 모두 두 자리수 형식