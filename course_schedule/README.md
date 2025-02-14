## Course Schedule

### Description
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return True if you can finish all courses. Otherwise, return False.

A function to determine if it is possible to finish all courses given the prerequisites.

Example
Input:
numCourses = 2, prerequisites = [[1,0]]
Output: True
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
Input:
numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
### File
- [course_schedule.py](course_schedule.py)
Run the code in VS Code by pressing F5 or by clicking the "Run" button in the top-right corner.
Verify the output:
Can finish all courses with 2 courses and prerequisites [[1, 0]]: True
Can finish all courses with 2 courses and prerequisites [[1, 0], [0, 1]]: False
Can finish all courses with 3 courses and prerequisites [[1, 0], [2, 1]]: True