from collections import Counter

txt = input()
counter = Counter(txt)

six_nine_count = counter.get('6', 0) + counter.get('9', 0)
counter['6/9'] = (six_nine_count + 1) // 2  # 대체 가능 숫자 처리

if '6' in counter:
    del counter['6']
if '9' in counter:
    del counter['9']

print(max(counter.values()))
