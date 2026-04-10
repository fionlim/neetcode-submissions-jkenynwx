class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create directed graph
        # each unique char point to a set of chars we know comes after it
        dag = {v:set() for word in words for v in word}

        for i in range(len(words) - 1):
            s = words[i]
            t = words[i+1]

            # check for invalid order
            # if prefix is the same but len(s) > len(t)
            min_len = min(len(s), len(t))
            if s[:min_len] == t[:min_len] and len(s) > len(t):
                return ''
            for v in range(min_len):
                if s[v] != t[v]:
                    dag[s[v]].add(t[v])
                    break
        print(dag)
        # traverse dag
        visited = set() # visited to track nodes which have been processed
        path = set()
        self.cycle = False

        def dfs(v):
            path.add(v)
            print('path' + str(path))
            if len(dag[v]) == 0: # if no next nodes
                visited.add(v)
                return v
            elif dag[v] <= visited: # if all next nodes have been processed
                visited.add(v)
                return v 
            res = ''
            for t in dag[v]:
                if t in visited: # means t alr processed in a deeper dfs
                    continue
                if t in path: # t not processed but reappears in path, cycle present
                    self.cycle = True
                    return ''
                res = dfs(t) + res
            print('result:' + res)
            if res == '':
                return res
            res = res + v
            visited.add(v)
            return res
        order = ''
        for v in dag:
            path = set()
            if v in visited:
                continue
            res = dfs(v)
            if self.cycle:
                return ''
            print('result:' + res)
            order = order + res
        return order[::-1]
