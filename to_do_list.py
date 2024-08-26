from task import Task, Status
import sys

class Node:
    def __init__(self, task) -> None:
        self.task = task
        self.next = None
    


class ToDoList:
    def __init__(self) -> None:
        self.head = None
    
    def add_task(self, task):
        if not self.head:
            self.head = Node(task)
        else:
            new_task = Node(task=task)
            iterate_obj = self.head
            while iterate_obj.next:
                iterate_obj = iterate_obj.next
            
            iterate_obj.next = new_task

    def delete_task(self, task_num):
        
        # check if it is first
        if not self.head:
            return False
        if task_num == 1:
            self.head = self.head.next
        else:
            iterate_obj = self.head
            count = 1
            while iterate_obj.next:
                if count == task_num-1:
                    break
                iterate_obj = iterate_obj.next
            else:
                return False
            
            iterate_obj.next = iterate_obj.next.next
        return True
    def display_task(self):
        print("*********************************************************")
        
        if not self.head:
            print("Empty List")
        else:
            iterate_obj = self.head
            count = 1
            
            while iterate_obj:
                print(f"{count}. {iterate_obj.task}")
                count+=1
                iterate_obj = iterate_obj.next
        print("*********************************************************")
    def update_status(self, task_num, status):
        count = 1
        iterate_obj = self.head

        while iterate_obj:
            if count == task_num:
                iterate_obj.task.status = status
                break
            count+=1
            iterate_obj = iterate_obj.next
        else:
            print("Invalid task number")
        

if __name__ == "__main__":
    to_do_list = ToDoList()
    while True:
        try:
            to_do_list.display_task()
            choice = int(input("Please select the action\n" \
                               "1.Add task in todo list\n" \
                               "2.Delete task\n" \
                               "3.Update status \n" \
                               "To exit enter 0\n" \
                               "Enter your action by action number "))
        except ValueError:
            print("Please enter valied action")
        
        if choice ==0:
            sys.exit("Thanks!")
        elif choice == 1:
            task_name = input("Enter your task: ")
            task_dl =input("Enter task dead line in DD-Mmm-YYYY format EX: 01-Jan-2024: ")
            try:
                task = Task(task_name, task_dl)
                to_do_list.add_task(task=task)
                print("Task Added")
               
            except ValueError:
                print("Please enter date format as mentioned")
        elif choice == 2:
            to_do_list.display_task()
            try:
                del_num = int(input("Please enter task number you want to delete "))
                if to_do_list.delete_task(del_num):
                    print("Task Deleted successfully")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Invalid input please try again")
        elif choice == 3:
            to_do_list.display_task()
            try:
                task_num = int(input("Please enter task number you want to update the status "))
                status_list = list(Status)
                for x, y in enumerate(status_list):
                    print(f"{x+1}. {y.value}")
                status_num = int(input("Please enter status number you want"))
                to_do_list.update_status(task_num,status_list[status_num-1])
            except ValueError:
                print("Invalid input please try again")
        else:
            print("Out of options")

            


