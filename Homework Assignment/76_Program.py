# ================= LINKED LIST CYCLE DETECTION =================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Floyd’s Cycle Detection (Fast & Slow Pointer)
def detect_cycle_linkedlist(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create linked list example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Create cycle
head.next.next.next.next.next = head.next


print("Linked List Cycle:",
      detect_cycle_linkedlist(head))


# ================= GRAPH CYCLE DETECTION (DFS) =================

def dfs(node, graph, visited, parent):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, node):
                return True
        elif neighbor != parent:
            return True

    return False


def detect_cycle_graph(graph):
    visited = [False] * len(graph)

    for i in range(len(graph)):
        if not visited[i]:
            if dfs(i, graph, visited, -1):
                return True

    return False


# Graph example
graph = [
    [1],
    [0, 2],
    [1, 3],
    [2, 4],
    [3]
]

print("Graph Cycle:",
      detect_cycle_graph(graph))
