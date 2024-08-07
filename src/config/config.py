from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:

    def ___init__(self) -> None:
        self.__connection_string = 'mysql_pymysql://root:my-secret-pw@mysqldb/teste'
        self.session = None

        def __enter__(self):
            engine = create_engine(self.__connection_string)
            session_maker = sessionmaker()
            self.session =  session_maker(bing=engine)
            return self