def is_correct(ws):
    stack = []
    for w in ws:
        if w == '(':
            stack.append(w)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def split(ws):
    count = 0
    for i in range(len(ws)):
        if ws[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return ws[:i+1], ws[i+1:]
                   
def solution(p):
    if not p:
        return ""
    u, v = split(p)
    if is_correct(u):
        return u + solution(v)
    else:
        new = "(" + solution(v) + ")"           
        re_u = u[1:-1]
        re_u_reversed = ''.join(['(' if uu == ')' else ')' for uu in re_u])
        return new + re_u_reversed
            
                   
    