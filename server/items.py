from CRUD import CRUD
from CRUD import connect

class Deliverable(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'deliverables')
        self._dict = {
            'title': None,
            'description': None,
            'due_date': None
        }
    
class Task(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'tasks')
        self._dict = {
            'title': None,
            'description': None,
            'due_date': None,
            'expected_start_date': None,
            'expected_end_date': None,
            'expected_duration': None,
            'expected_effort': None,
            'actual_start_date': None,
            'actual_end_date': None,
            'actual_duration': None,
            'effort_completed': None,
            'actual_effort': None,
            'percent_complete': None,
            'deliverable_id': None,
        }
    def retreiveWithDeliverable(self, dunique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE deliverable_id={dunique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()

        finally:
            connection.close()
            return result
class Issue(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'issues')
        self._dict = {
            'title': None,
            'description': None,
            'priority': None,
            'severity': None,
            'date_raised': None,
            'date_assigned': None,
            'expected_completion_date': None,
            'actual_completion_date': None,
            'status': None,
            'status_description': None,
            'update_date': None,
        }
class ActionItem(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'action_items')
        self._dict = {
            'title': None,
            'description': None,
            'date_created': None,
            'date_assigned': None,
            'resource_assigned': None,
            'expected_completion_date': None,
            'actual_completion_date': None,
            'status': None,
            'status_description': None,
            'update_date': None,
            'issue_id': None,
        }
class Requirment(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'requirements')
        self._dict = {
            'title': None,
            'description': None,
            'deliverable_id': None,
        }
    def retreiveWithDeliverable(self, dunique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE deliverable_id={dunique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
        finally:
            connection.close()
            return result

class Resource(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'resources')
        self._dict = {
            'title': None,
            'action_items_id': None,
            'decision_id': None,
        }
class task_resource(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'task_resource')
        self._dict = {
            'task_id': None,
            'resource_id ': None,
        }  
    def retreiveWitTask(self, tunique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE `task_id`={tunique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    def retreiveWitResource(self, unique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE `resource_id`={unique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    def deleteRemoteResource(self, unique_id: int) -> None:
        # Delete the remote and local record
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"DELETE FROM {self.table} WHERE resource_id={unique_id}"
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close() 
    def deleteRemoteTask(self, unique_id: int) -> None:
        # Delete the remote and local record
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"DELETE FROM {self.table} WHERE task_id={unique_id}"
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close()     
class task_issue(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'task_issue')
        self._dict = {
            'task_id': None,
            'issue_id ': None,
        } 
    def retreiveWitTask(self, tunique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE `task_id`={tunique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    def retreiveWitIssue(self, unique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE `issue_id`={unique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    def deleteRemoteIssue(self, unique_id: int) -> None:
        # Delete the remote and local record
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"DELETE FROM {self.table} WHERE issue_id={unique_id}"
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close() 
    def deleteRemoteTask(self, unique_id: int) -> None:
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"DELETE FROM {self.table} WHERE task_id={unique_id}"
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close()     
class task_pred(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'task_pred')
        self._dict = {
            'task_id': None,
            'predecessor_id ': None,
        } 
    def retreiveWitTask(self, tunique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE `task_id`={tunique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    def deleteRemote(self, unique_id: int) -> None:
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"DELETE FROM {self.table} WHERE task_id={unique_id}"
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close() 
class task_succ(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'task_succ')
        self._dict = {
            'task_id': None,
            'predecessor_id ': None,
        } 
    def retreiveWitTask(self, tunique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE `task_id`={tunique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    def deleteRemote(self, unique_id: int) -> None:       
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"DELETE FROM {self.table} WHERE task_id={unique_id}"
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close() 