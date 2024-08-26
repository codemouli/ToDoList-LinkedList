import uuid
from datetime import datetime
from enum import Enum


class Status(Enum):
    YET_TO_DO = "Yet to do"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class Task:
    __slots__ = ["_id", "task", "dead_line", "__status"] 
    def __init__(self, task=None, dead_line=None):
        self._id = uuid.uuid4()
        self.task = task
        self.dead_line = datetime.strptime(dead_line, "%d-%b-%Y")
        self.__status = Status.YET_TO_DO

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, task_status):
        if task_status == Status.YET_TO_DO:
            self.__status = Status.YET_TO_DO
        elif task_status == Status.IN_PROGRESS:
            self.__status = Status.IN_PROGRESS
        elif task_status == Status.COMPLETED:
            self.__status = Status.COMPLETED
        else:
            raise ValueError
    
    
    
    def __str__(self):
        return f"{self.task}|{self.dead_line.strftime("%d-%b-%Y")}|{self.status.value}"
    