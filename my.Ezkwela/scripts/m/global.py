
import pg, string

class DBHandler:
    """ 
        The class for DB Handling. Utilizes 
        Usage: db = new DBHandler()
    """

    def __init__(self):
        self.dbname = "postgres"
        self.username = "postgres"
        self.password = "password"

        self.db = pg.connect(self.dbname, 'localhost', 5432, None, None, self.username, self.password)
    
    def close():
        pg.close(self.db)



class Hash:

    
    def __init__(self):
        
