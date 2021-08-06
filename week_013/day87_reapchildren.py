"""
You are given two lists of integers and an integer representing a process id to kill. 
One of the lists represents a list of process ids and the other represents a list of each 
of the processes’ corresponding (by index) parent ids. When a process is killed, all of its
 children should also be killed. Return a list of all the process ids that are killed as a 
 result of killing the requested process.

Ex: Given the following…

pid =  [2, 4, 3, 7]
ppid = [0, 2, 2, 3]
kill = 3
the tree of processes can be represented as follows:
           2
         /   \
        4     3
             /
            7
return [3, 7] as killing process 3 will also require killing its child (i.e. process 7).
"""
# Time O(n)
# Space O(n)
def reapchildren(pid, ppid, kill):
    ppid_relation = {}
    for p, pp in zip(pid,ppid):
        if pp not in ppid_relation:
            ppid_relation[pp] = [p]
        else:
            ppid_relation[pp].append(p)

    output = []
    recurse(ppid_relation, kill, output)

    return output

def recurse(ppid_relation, cur_pid, output):
    output.append(cur_pid)
    if cur_pid in ppid_relation:
        for child in ppid_relation[cur_pid]:
            recurse(ppid_relation, child, output)
    return
        
print(reapchildren([2, 4, 3, 7], [0,2,2,3],3))
print(reapchildren([2, 4, 3, 7], [0,2,2,3],2))
print(reapchildren([1, 3, 10, 5], [3, 0, 5, 3],5))
print(reapchildren([1, 2, 3], [0, 1, 1],2))