
import extractor
import internal.load

from models.Database.utils import init_tables

def test():
    config = internal.load.load_config()
    print(config)
    system = extractor.extractor(config)
    system.connect()  
    ## TODO: Code for testing the extractor goes here (integration tests)
    error = init_tables(system.conn)
    if error is not None:
        print(f"Error initializing tables: {error}")
    else:
        print("Tables initialized")
    
    
    ## Disconnect from the database
    system.disconnect()
    
test()

    