class Solution:
    class UnionFind:
        def __init__(self) :
            self.parent = list(range(26))

        def find(self,index) :
            if index == self.parent[index] :
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def union(self,index1,index2) :
            self.parent[self.find(index1)] = self.find(index2)


    def equationsPossible(self, equations: [str]) -> bool:
        uf = self.UnionFind()
        for eq in equations :
            if eq[1] == "=" :
                index1 = ord(eq[0]) - ord("a")
                index2 = ord(eq[3]) - ord("a")
                uf.union(index1,index2)
        for eq in equations :
            if eq[1] == "!":
                index1 = ord(eq[0]) - ord("a")
                index2 = ord(eq[3]) - ord("a")
                if uf.find(index1) == uf.find(index2) :
                    return False
        return True


if __name__ == "__main__" :
    solution = Solution()
    equations = ["a==b","b!=c","c==a","c==d"]
    result = solution.equationsPossible(equations)
    print(result)