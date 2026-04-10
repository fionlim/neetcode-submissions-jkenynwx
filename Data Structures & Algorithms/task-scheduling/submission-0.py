class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ind_dict = {}
        for i, task in enumerate(tasks):
            print(ind_dict)
            if task not in ind_dict: # new task
                if 'empty' in ind_dict:
                    ind_dict[task] = ind_dict['empty']
                    ind_dict['empty'] = i
                else:
                    ind_dict[task] = i
            elif i == ind_dict[task] + n + 1: # repeated task in correct pos
                ind_dict[task] = i
            else: # repeated task in wrong pos
                tasks[i] = None
                if 'empty' not in ind_dict:
                    ind_dict['empty'] = i
                else:
                    ind_dict['empty'] = min(ind_dict['empty'], i)
                ind_dict[task] = ind_dict[task] + n + 1
        return max(ind_dict.values()) + 1
