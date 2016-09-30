import gc

def get():
    return gc.count_generation(0), gc.count_generation(1), gc.count_generation(2)

def show():
    print(get())

print("==========================")
print("Creating a big ol cycle")
class Node(object):
    def __init__(self):
        self.children = []

a = Node()
show()
for i in range(300):
    n = Node()
    a.children.append(n)
    n.children.append(a)
show()
print("Deleting the cycle")
del a
del n
show()
print("Creating more objects to trigger a normal collection")
a = [[]for i in range(700)]
show()
