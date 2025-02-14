from collections import defaultdict, deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Determine if it is possible to finish all courses given the prerequisites.
    """
    # Build the graph
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Initialize the queue with courses that have no prerequisites
    queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
    completed_courses = 0

    while queue:
        course = queue.popleft()
        completed_courses += 1
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return completed_courses == numCourses

if __name__ == "__main__":
    test_cases = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
        (3, [[1, 0], [2, 1]])
    ]
    for numCourses, prerequisites in test_cases:
        print(f"Can finish all courses with {numCourses} courses and prerequisites {prerequisites}: {canFinish(numCourses, prerequisites)}")