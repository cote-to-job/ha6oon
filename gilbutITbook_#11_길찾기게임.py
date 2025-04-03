def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10000)
    
    # 노드 번호 추가
    nodes = [(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]
    
    # y 기준 내림차순, x 기준 오름차순 정렬
    nodes.sort(key=lambda x: (-x[1], x[0]))
    
    preorder_result = []
    postorder_result = []
    
    def build_tree(sub_nodes):
        if not sub_nodes:
            return
        
        root = sub_nodes[0]
        x, y, index = root
        preorder_result.append(index)
        
        # 왼쪽 서브트리: x가 root보다 작은 것
        left = [node for node in sub_nodes[1:] if node[0] < x]
        # 오른쪽 서브트리: x가 root보다 큰 것
        right = [node for node in sub_nodes[1:] if node[0] > x]
        
        build_tree(left)
        build_tree(right)
        
        postorder_result.append(index)
    
    build_tree(nodes)
    
    return [preorder_result, postorder_result]
