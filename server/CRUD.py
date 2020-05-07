import pymysql
# Configuration
def connect():
    # Connection instance to be used with other functions
    return pymysql.connect(host="unraid.bishoyabdelmalik.com",
                           port=42069,
                           user="lizard",
                           password="ashrab_shai",
                           db="PMS",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
class CRUD(dict):
    """ CRUD class to be inherited by component classes. Do not instantiate!"""
    def __init__(self, table: str):
        self._dict = {}
        self.table = table
        self.unique_id = None

    def _type_check(self,value):
        # Type check for SQL queries
        if type(value) == str:
            return f'"{value}"'
        # TODO: check datetime type
        return str(value)
    
    def create(self) -> None:
        # Insert a populated class in the corresponding table
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = (
                    f"INSERT INTO {self.table} (" +
                    (', '.join(f"{key}" for key in self.keys())) +
                    ") VALUES(" +
                    (', '.join(("NULL" if value is None or value is "" else self._type_check(value)) for value in self.values())) +
                    ")"
                )
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close()
            
    def retreive(self, unique_id: int) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} WHERE id={unique_id}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchone()
                if result is not None:
                    self.update(result)
        finally:
            self.unique_id = unique_id
            connection.close()
    def retreiveMostRecent(self) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table} ORDER BY `id` DESC"
                print(query)
                cursor.execute(query)
                result = cursor.fetchone()
                if result is not None:
                    self.update(result)
        finally:
            connection.close()
    def retreiveAll(self) -> None:
        # Populate the class preexsiting values
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM {self.table}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
        finally:
            connection.close()
            return result
    def deleteRemote(self) -> None:
        # Delete the remote and local record
        if self.unique_id is None:
            return
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"DELETE FROM {self.table} WHERE id={self.unique_id}"
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close()    
    def delete(self) -> None:
        # Delete the remote and local record
        if self.unique_id is None:
            return
        connection = connect()
        try:
            with connection.cursor() as cursor:
                query = f"DELETE FROM {self.table} WHERE id={self.unique_id}"
                print(query)
                cursor.execute(query)
            connection.commit()
        finally:
            self.clear()
            connection.close()
