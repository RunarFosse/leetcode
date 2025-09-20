class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # Store tasks in a sorted set, sorted based on priority and itself
        self.priorities, self.users = {}, {}
        self.tasks = SortedSet([], key=lambda task: (self.priorities[task], task))

        # And add all the initial tasks
        for task in tasks:
            self.add(*task)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # Add the task to the task manager
        self.priorities[taskId] = priority
        self.users[taskId] = userId
        self.tasks.add(taskId)

    def edit(self, taskId: int, newPriority: int) -> None:
        # Get the userId of the tasks
        userId = self.users[taskId]

        # Remove the task from the task manager
        self.rmv(taskId)

        # And add it back with the new priority
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        # Remove the task from the manager
        self.tasks.remove(taskId)

    def execTop(self) -> int:
        # If there is no task, return -1
        if not self.tasks:
            return -1

        # Otherwise, get the highest priority task
        taskId = self.tasks.pop()

        # And return its user
        return self.users[taskId]


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()