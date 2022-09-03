class Node:
    def __init__(self, data):
        self.data = data
        self.front = None
        self.back = None
        self.is_deleted = False


def solution(n, k, cmd):
    def move_up(num):
        nonlocal selected_index
        for _ in range(num):
            selected_index = nodes[selected_index].front.data

    def move_down(num):
        nonlocal selected_index
        for _ in range(num):
            selected_index = nodes[selected_index].back.data

    def delete():
        nonlocal selected_index
        prev_node = nodes[selected_index].front
        next_node = nodes[selected_index].back
        delete_history.append(selected_index)
        prev_node.back = next_node
        next_node.front = prev_node
        nodes[selected_index].is_deleted = True
        if next_node.data != -1:
            selected_index = next_node.data
        else:
            selected_index = prev_node.data

    def rollback():
        nonlocal selected_index
        data = delete_history.pop()
        node = nodes[data]
        node.is_deleted = False

        prev_node = node.front
        next_node = node.back
        prev_node.back = node
        next_node.front = node

    first_node = Node(-1)
    nodes = [first_node]

    for i in range(1, n + 1):
        node = Node(i)
        node.front = nodes[-1]
        nodes[-1].back = node
        nodes.append(node)

    last_node = Node(-1)
    nodes[-1].back = last_node
    last_node.front = nodes[-1]
    nodes.append(last_node)

    selected_index = k + 1
    delete_history = []

    for c in cmd:
        temp = c.split()
        if temp[0] == "U":
            move_up(int(temp[1]))
        elif temp[0] == "D":
            move_down(int(temp[1]))
        elif temp[0] == "C":
            delete()
        elif temp[0] == "Z":
            rollback()

    answer = ""
    for i in range(1, n + 1):
        if nodes[i].is_deleted:
            answer += "X"
        else:
            answer += "O"

    return answer
