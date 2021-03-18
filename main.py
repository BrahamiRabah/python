class Todo:
      """
      Todo represents a task with a name, description, point value, and completed.
      A new Todo should have a `completed` field that defaults to `False`.
      All other attributes must be provided.

      >>> todo = Todo(name='Get Lunch', description='Need to eat.', points=0)
      >>> print(todo)
      Get Lunch (Incomplete - 0 points): Need to eat.
      >>> todo.completed = True
      >>> print(todo)
      Get Lunch (Complete - 0 points): Need to eat.
      >>> todo2 = Todo(name='Test', description='Another todo', points=1, completed=True)
      """
        def __init__(self, name, description, points, completed=false):
            self.name= name
            self.description= description
            self.points= points
            self.completed= completed
        def __repr__(self):
            if completed:
                return (f"{self.name}(complete - {self.points} points): {self.description}")
            else:
                return (f"{self.name}(incomplete - {self.points} points): {self.description}")

  class TodoList:
      """
      TodoList wraps a list of Todo objects and implements some functionality that
      utilize the information from the entire collection.

      >>> todo = Todo(name='Get Lunch', description='Need to eat', points=0, completed=True)
      >>> todo2 = Todo(name='Submit Talk Proposal', description='Write and submit talk for PyCon', points=3)
      >>> todo_list = TodoList([todo, todo2])
      >>> todo_list.average_points()
      1.5
      >>> todo_list.completed()
      [Get Lunch (Complete - 0 points): Need to eat]
      >>> todo_list.incomplete()
      [Submit Talk Proposal (Incomplete - 3 points): Write and submit talk for PyCon]
      """
         def __init__(self, list):
             self.list= list
         def completed(self):
            i=0
            while i <len(self.list) :
                if self.list[i].completed == True:
                    return (f"{self.name}(complete - {self.points} points): {self.description}")
         def incompleted(self):
            i=0
            while i <len(self.list) :
                if self.list[i].completed == False:
                    return (f"{self.name}(incomplete - {self.points} points): {self.description}")
                i+= 1
         def average_points(self):
            i=0
            sum=0
            while i <len(self.list) :
                sum+= self.list[i].points
                i+= 1
            return sum / 2
