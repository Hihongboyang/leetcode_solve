class Solution:
    """
    深度优先算法实现的查找算法
    """
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        self.visited = [False] * len(graph)  # 设置记录的列表，记录每条路径是否访问过
        return self.helper(graph, start, target)

    def helper(self, graph: List[List[int]], start:int , target: int):
        for i in range(len(graph)):
            # 访问过的不再遍历
            if self.visited[i]:
                continue
            
            # 开始，结束都符合，找到路径
            if graph[i][0] == start and graph[i][1] == target:
                return True  

            self.visited[i] = True

            # 目标路径符合，寻找开始路径
            if graph[i][1] == target and self.helper(graph, start, graph[i][0]):
                return True

            self.visited[i] = False

        return False

