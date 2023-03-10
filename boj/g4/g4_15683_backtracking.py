def change1Graph(x,y, dir):
    if dir == 0:
        for j in range(y, m):
            if graph[x][j] == 6:
                break
            graph[x][j] = '#'
    
    elif dir == 90:
        for i in range(x, n):
            if graph[i][y] == 6:
                break
            graph[i][y] = '#'
    
    elif dir == 180:
        for j in range(y, -1, -1):
            if graph[x][j] == 6:
                break
            graph[x][j] = '#'
            
    elif dir == 270:
        for i in range(x, -1, -1):
            if graph[i][y] == 6:
                break
            graph[i][y] = '#'
       
def change2Graph(x,y, dir):
    if dir == 0:
        change1Graph(x,y,0)
        change1Graph(x,y,180)
    elif dir == 90:
        change1Graph(x,y,90)
        change1Graph(x,y,270)
    elif dir == 180:
        change1Graph(x,y,0)
        change1Graph(x,y,180)
    elif dir == 270:
        change1Graph(x,y,90)
        change1Graph(x,y,270)

def change3Graph(x,y, dir):
    if dir == 0:
        change1Graph(x,y,0)
        change1Graph(x,y,270)
    elif dir == 90:
        change1Graph(x,y,90)
        change1Graph(x,y,0)
    elif dir == 180:
        change1Graph(x,y,180)
        change1Graph(x,y,90)
    elif dir == 270:
        change1Graph(x,y,270)
        change1Graph(x,y,180)  
       
def change4Graph(x,y, dir):
    if dir == 0:
        change1Graph(x,y,270)
        change1Graph(x,y,0)
        change1Graph(x,y,90)
    elif dir == 90:
        change1Graph(x,y,0)
        change1Graph(x,y,90)
        change1Graph(x,y,180)
    elif dir == 180:
        change1Graph(x,y,90)
        change1Graph(x,y,180)
        change1Graph(x,y,270)
    elif dir == 270:
        change1Graph(x,y,180)
        change1Graph(x,y,270)
        change1Graph(x,y,0)
        
def change5Graph(x,y, dir):
    change1Graph(x,y,0)
    change1Graph(x,y,90)
    change1Graph(x,y,180)
    change1Graph(x,y,270)
        
def changeGraph(x,y, value, dir):
    if value == 1:
        change1Graph(x,y,dir)
    elif value == 2:
        change2Graph(x,y,dir)
    elif value == 3:
        change3Graph(x,y,dir)
    elif value == 4:
        change4Graph(x,y,dir)
    elif value == 5:
        change5Graph(x,y,dir)
        
def getCount():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1

    return cnt

def getResult(cnt, start):

    if cnt == len(cctv):
        global min_cnt
        min_cnt = min(getCount(), min_cnt)
        return
    
    for i in range(start, len(cctv)):
        
        global graph
        temp_graph = [item[:] for item in graph]
        
        x, y, value = cctv[i]
       
        # ????????? ??????(0???)
        changeGraph(x,y, value, 0)
        getResult(cnt + 1, i+1)
        graph = [item[:] for item in temp_graph]
        
        # ????????? ??????(90???)
        changeGraph(x,y, value, 90)
        getResult(cnt + 1, i+1)
        graph = [item[:] for item in temp_graph]
        
        # ????????? ??????(180???)
        changeGraph(x,y, value, 180)
        getResult(cnt + 1, i+1)
        graph = [item[:] for item in temp_graph]
        
        # ????????? ??????(270???)
        changeGraph(x,y, value, 270)
        getResult(cnt + 1, i+1)
        graph = [item[:] for item in temp_graph]
                
# ??????
import sys, math
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# ??????1: cctv ?????? ?????????
cctv = []
for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append((i,j, graph[i][j]))

# ??????2: cctv ?????? 4?????? ?????? ???????????? ?????? ?????? ??????
min_cnt = math.inf
getResult(0, 0)

# ??????
print(min_cnt)