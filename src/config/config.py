from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:

    def ___init__(self) -> None:
        self.connection_string = 'mysql_pymysql://root:my-secret-pw@mysqldb/teste'
        self.session = None

    def __enter__(self):
        engine = create_engine(self.connection_string)
        session_maker = sessionmaker()
        self.session =  session_maker(bing=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()