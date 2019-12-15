#!/usr/bin/python3

from collections import defaultdict, deque

def tc(v, e):
    c = e
    for k in v:
        c_next = set()
        for i in v:
            for j in v:
                if (i, j) in c or ((i, k) in c and (k, j) in c):
                    c_next.add((i, j))
        c = c_next
    return c


def load_from_file(file_name):
    v = set()
    e = set()
    with open(file_name, "r") as f:
        for line in f:
            a, b = line.strip().split(")")
            v.add(a)
            v.add(b)
            e.add((a, b))
    return v, e

def search(e, start, end):
    g = defaultdict(set)
    for a, b in e:
        g[a].add(b)
        g[b].add(a)
    visited = set()
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        last = path[-1]
        if last == end:
            return path
        if last not in visited:
            visited.add(last)
            for neighbor in g[last]:
                new_path = path.copy()
                new_path.append(neighbor)
                queue.append(new_path)

if __name__ == "__main__":
    v, e = load_from_file("input")
    c = tc(v, e)
    count = len(c)
    print(count)
    path = search(e, "YOU", "SAN")
    transfers = len(path) - 3
    print(transfers)