from CRUD import CRUD

class Deliverable(CRUD):
    def __init__(self):
        CRUD.__init__(self, 'deliverables')
        self._dict = {
            'title': None,
            'description': None,
            'due_date': None
        }
