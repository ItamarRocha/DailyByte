"""
This question is asked by Facebook. You are given a two dimensional matrix,friends, that represents 
relationships between coworkers in an office. If friends[i][j] = 1 then coworker i is friends with 
coworker j and coworker j is friends with coworker i. Similarly if friends[i][j] = 0 then coworker i
is not friends with coworker j and coworker j is not friend with coworker i. Friendships in the office
are transitive (i.e. if coworker one is friends with coworker two and coworker two is friends with coworker
three, coworker one is also friends with coworker three). Given the friendships in the office defined by
friends, return the total number of distinct friends groups in the office.

Note: Each coworker is friends with themselves (i.e.matrix[i][j] = 1 for all values where i = j)

Ex: Given the following matrix friends…

friends = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
], return 2.
The 0th and 1st coworkers are friends with one another (first friend group).
The 2nd coworker is friends with themself (second friend group).
"""
# Time O(n²)
# Space O(n)
def finding_friends(friends):
    seen = set()
    count = 0

    for i in range(len(friends)):
        if i not in seen:
            queue=[i]
            traverse_friends(queue, friends, seen)
            count += 1
    
    return count

def traverse_friends(queue, friends, seen):
    while queue:
        i = queue.pop(0)
        seen.add(i)
        for j in range(len(friends)):
            if friends[i][j] == 1 and j not in seen:
                queue.append(j)

    return

print(finding_friends([
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]))