import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    class UnionFind:
        def __init__(self, n):
            self.parent = [i for i in range(n)]

        def find(self, x):
            if x == len(self.parent):
                return -1
            if self.parent[x] == x:
                return self.parent[x]

            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    
    n, m = map(int, input().split())
    uf = UnionFind(n)

    for _ in range(m):
        tag, num = input().split()
        num = int(num)
        if tag == "?":
            par = uf.find(num - 1)
            if par != -1:
                print(par + 1)
            else:
                print(-1)
        else:
            uf.parent[num-1] = uf.find(num)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()