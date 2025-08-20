class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def create_set(self, value):
        self.parent[value] = value
        self.rank[value] = 0


    def find_value(self,value):

        current_value = value


