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