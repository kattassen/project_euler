class Node:
    def __init__(self, value, 
                 nxt_l=0, prv_l=0, 
                 nxt_r=0, prv_r=0):
        self.value = value
        self.nxt_r = nxt_r
        self.prv_r = prv_r
        self.nxt_l = nxt_l
        self.prv_l = prv_l

    def remove(self):
        if not self.prv_l == 0:
            self.prv_l.nxt_r = 0
        if not self.prv_r == 0:
            self.prv_r.nxt_l = 0
        if not self.nxt_l == 0:
            self.nxt_l.prv_l = 0
        if not self.nxt_r == 0:
            self.nxt_r.prv_l = 0
        self.value = 0
        

node_list = []
paths = 0
total = 0

def euler18():
    global paths
    global node_list
    global total
    # Add raw string
    triangle15 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

    triangle = triangle15.split("\n")

    for i, row in enumerate(triangle):
        # Add a new row
        node_list.append([])
        for j, col in enumerate(row.split(" ")):
            prv_r = 0
            prv_l = 0
            # Add a node previous pointers
            if not i == 0:
                if not j == 0:
                    # Find upper left node if not left edge
                    prv_l = node_list[i-1][j-1]
                if not j == i:
                    # Find upper right node if not right edge
                    prv_r = node_list[i-1][j]

            # Add the node
            node_list[i].append(Node(int(col), prv_r=prv_r, prv_l=prv_l))

            # Add reference to this node from parent
            if not prv_l == 0:
                prv_l.nxt_r = node_list[i][j]
            if not prv_r == 0:
                prv_r.nxt_l = node_list[i][j]

    traverse_tree(node_list[0][0], 0)

    print paths
    print total


def traverse_tree(node, tot_sum):
    global paths
    global total
    tot_sum += node.value
    if node.nxt_l == 0 and node.nxt_r == 0:
        # We are at the bottom
        paths += 1
        if tot_sum > total:
            total = tot_sum
        return

    if not node.nxt_l == 0:
        traverse_tree(node.nxt_l, tot_sum)

    if not node.nxt_r == 0:
        traverse_tree(node.nxt_r, tot_sum)    


def main():
    euler18()

if __name__ == "__main__":
    main()
