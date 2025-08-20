from linklist import double_linklist, double_node


class lru_cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = {}
        self.current_size = 0
        self.most_recent = double_linklist()

    def insert_key_value_pair(self, key, value):
        if key not in self.cache:
            if self.current_size == self.max_size:
                self.evict_least_recent()
            else:
                self.current_size += 1
            self.cache[key] = double_node(key, value)
        else:
            self.replace_key(key,value)
        self.update_most_recent(self.cache[key])

    def evict_least_recent(self):
        key_to_remove = self.most_recent.tail.key
        self.most_recent.remove()
        del self.cache[key_to_remove]

    def update_most_recent(self, node):
        self.most_recent.insert(node)

    def replace_key(self, key,value):
        if key not in self.cache:
            raise Exception("Provided key is not in cache")
        self.cache[key].value = value

    def get_value_from_key(self, key):
        if key not in self.cache:
            return None
        self.update_most_recent(self.cache[key])
        return self.cache[key].value

    def get_most_recent(self):
        return self.most_recent.head.key