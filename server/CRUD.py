import pymysql
from server import connect

class CRUD(dict):
    """ CRUD class to be inherited by component classes. Do not instantiate!"""
    def __init__(self, table: str):
        self._dict = {}
        self.table = table
        self.unique_id = None

    def create(self) -> None:
        # Insert a populated class in the corresponding table
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = (
                    f"INSERT INTO {self.table} (" +
                    (', '.join(f"{key}" for key in self.keys())) +
                    ") VALUES(" +
                    (', '.join(f'"{value}"' for value in self.values())) +
                    ")"
                )
                print(query)
                cursor.execute(query)
            connection.commit()
        except Error as e:
            print(e)            # TODO: Add proper logging
        finally:
            connection.close()
            
    def retreive(self, unique_id: str) -> None: # TODO
        # Populate the class using a preexisting record
        pass

    def update_remote(self) -> None:
        # Update the DB record based on the local fields
        pass
        
    def delete(self) -> None:   # TODO
        # Delete the remote record
        pass
