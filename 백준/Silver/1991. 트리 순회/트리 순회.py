class Btree:
    def __init__(self,elem,left,right):
        self.data = elem
        self.left = left
        self.right = right
def VLR(n):
    if n is not None:
        print(n.data,end="")
        VLR(n.left)
        VLR(n.right)
def LVR(n):
    if n is not None:
        LVR(n.left)
        print(n.data,end="")
        LVR(n.right)
def LRV(n):
    if n is not None:
        LRV(n.left)
        LRV(n.right)
        print(n.data,end="")
d = int(input())
cnt = {}
for i in range(d):
    a,b,c = input().split()
    if b == ".":
        b = None
    if c == ".":
        c = None
    cnt[a] = Btree(a,b,c)
for i in cnt:
    node = cnt[i]
    if node.left is not None:
        node.left = cnt[node.left]
    if node.right is not None:
        node.right = cnt[node.right]
VLR(cnt['A'])
print()
LVR(cnt['A'])
print()
LRV(cnt['A'])