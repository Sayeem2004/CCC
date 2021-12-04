from collections import deque

implicit_graph = ['###############E##',
                  '# # #  #         #',
                  '#     ## ## # # ##',
                  '# # #     #   #  #',
                  '# # # # # # #   ##',
                  '###S##############'];

rows = len(implicit_graph);
columns = len(implicit_graph[0]);
for i,row in enumerate(implicit_graph):
    for j,item in enumerate(row):
        if (item == "S"):
            start_node = (i,j);
        if (item == "E"):
            end_node = (i,j);
visited = [[False] * columns for i in range(rows)];
distance = [[0] * columns for i in range(rows)];

def validate_node(r, c):
    if (r < 0 or r >= rows):
        return False;
    if (c < 0 or c >= columns):
        return False;
    if (implicit_graph[r][c] == "#"):
        return False;
    if (visited[r][c]):
        return False;
    return True;

visited[start_node[0]][start_node[1]] = True;
distance[start_node[0]][start_node[1]] = 0;

q = deque([start_node]);
while (q):
    r,c = q.popleft();
    for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if (validate_node(nr,nc)):
            q.append((nr,nc));
            visited[nr][nc] = True;
            distance[nr][nc] = distance[r][c]+1;
print(distance[end_node[0]][end_node[1]]);
