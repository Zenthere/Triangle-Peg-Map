N = 3

def valid_coord(a,b,c,n):
    ret = True
    if a < 0 or b < 0 or c< 0 :
        ret = False
    if a > n or b > n or c >n:
        ret = False    
    s=a+b+c
    if s != n:
        ret = False
    # print("   check: ",a,",",b,",",c,",",n,",",ret)
    return ret

def add_edge(src,dst,jmp):
    if dst < src:
        tmp = src
        src = dst
        dst = tmp
    edge = {(src,dst,jmp): True}
    return edge

def make_edge(a,amod,b,bmod,c,cmod,n,nodes,edges):
    ad = a+amod
    am = a+amod//2
    bd = b+bmod
    bm = b+bmod//2
    cd = c+cmod
    cm = c+cmod//2
    if valid_coord(ad,bd,cd,n):
        src = nodes[(a ,b, c )][0]
        dst = nodes[(ad,bd,cd)][0]
        jmp = nodes[(am,bm,cm)][0]
        edges.update(add_edge(src,dst,jmp))
    return edges

def clean_board(n):
    nodes = {}
    index = 0
    for a in range(n,-1,-1):
        for b in range (n,-1,-1):
            for c in range (n,-1,-1):
                if valid_coord(a,b,c,n):
                    nodes.update({ (a,b,c): [index,True]})
                    index += 1
    return nodes

def build_edges(nodes, n):
    edges = {}
    for node in nodes.keys():
        a = node[0]
        b = node[1]
        c = node[2]
        edges = make_edge(a,  2, b, -2, c,  0, n, nodes, edges)
        edges = make_edge(a, -2, b,  2, c,  0, n, nodes, edges)
        edges = make_edge(a,  0, b,  2, c, -2, n, nodes, edges)
        edges = make_edge(a,  0, b, -2, c,  2, n, nodes, edges)
        edges = make_edge(a,  2, b,  0, c, -2, n, nodes, edges)
        edges = make_edge(a, -2, b,  0, c,  2, n, nodes, edges)
    return edges
    
def print_nodes(nodes):
    print("Current board")
    print("id:  a   b   c   hasPiece")
    for (node, index) in nodes.items():
        print (index[0],": ",node[0]," ",node[1]," ",node[2]," ", index[1])

def print_all_edges(edges):
    print("Any Jumpable edge")
    print("src   dst   jmp")
    for e in edges.keys():
        print(e[0], "   ",e[1], "   ",e[2])

def main(n):
    nodes = clean_board(n)
    nodes[(3,0,0)][1] = False
    print_nodes(nodes)

    print()
    edges = build_edges(nodes, n)
    print_all_edges(edges)

main(N)