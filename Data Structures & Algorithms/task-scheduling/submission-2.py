class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max heap and queue method
        h = [tasks.count(task) * -1 for task in list(set(tasks))]
        queue = []
        heapq.heapify(h)
        time = 0 
        while len(h) > 0 or len(queue) > 0:
            print(h)
            print(queue)
            time += 1
            if len(h) > 0: 
                task_cnt = heapq.heappop(h)
                task_cnt += 1
                if task_cnt < 0:
                    queue.append((task_cnt, time + n)) # enqueue next time to do task
            
            if len(queue) > 0 and queue[0][1] == time: 
                task = queue.pop(0)[0]
                heapq.heappush(h, task)
        return time
                


        # ind_dict = {}
        # for i, task in enumerate(tasks):
        #     print(ind_dict)
        #     if task not in ind_dict: # new task
        #         if 'empty' in ind_dict:
        #             ind_dict[task] = ind_dict['empty']
        #             ind_dict['empty'] = i
        #         else:
        #             ind_dict[task] = i
        #     elif i == ind_dict[task] + n + 1: # repeated task in correct pos
        #         ind_dict[task] = i
        #     else: # repeated task in wrong pos
        #         tasks[i] = None
        #         if 'empty' not in ind_dict:
        #             ind_dict['empty'] = i
        #         else:
        #             ind_dict['empty'] = min(ind_dict['empty'], i)
        #         ind_dict[task] = ind_dict[task] + n + 1
        # return max(ind_dict.values()) + 1

