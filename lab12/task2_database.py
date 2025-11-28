from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self):
        pass

    @abstractmethod
    def close(self):
        pass


class SQLiteDatabase(DatabaseInterface):
    def connect(self):
        print("Connecting to SQLite...")

    def execute_query(self):
        print("Executing SQLite query...")

    def close(self):
        print("Closing SQLite connection...")


class PostgreSQLDatabase(DatabaseInterface):
    def connect(self):
        print("Connecting to PostgreSQL...")

    def execute_query(self):
        print("Executing PostgreSQL query...")

    def close(self):
        print("Closing PostgreSQL connection...")


db1 = SQLiteDatabase()
db1.connect()
db1.execute_query()
db1.close()

db2 = PostgreSQLDatabase()
db2.connect()
db2.execute_query()
db2.close()