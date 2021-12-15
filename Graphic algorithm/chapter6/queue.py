from collections import deque

graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
    return person[-1] == 'm'


def search_queue(in_queue):
    searched = []
    while in_queue:  # 如果队列不是空
        person = in_queue.popleft()
        if not person in searched:   # 先要检测
            if person_is_seller(person):
                print(f'{person} is a seller!')
                return True  # 找到了
            else:
                in_queue.extend(graph[person])
    return False


queue = deque()  # 创建一个队列
queue.extend(graph["you"])  # 和queue += graph["you"]等价
print(search_queue(queue))
