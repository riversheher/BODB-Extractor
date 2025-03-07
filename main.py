
import extractor
import internal.load

import sys

from models.Database.utils import init_tables
from models.Database.utils import reset_tables

def test():
    
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <filepath>')
        exit(0)
        
    config = internal.load.load_config()
    print("config loaded: \n")
    print(config)
    system = extractor.extractor(config)
    system.connect()  
        
    if sys.argv[1] == 'reset':
        print(f'Resetting tables')
        reset_tables(system.conn)
        
        error = init_tables(system.conn)
        if error is not None:
         print(f"Error initializing tables: {error}")
    else:
        # Test 100 lines test file
        system.extract(sys.argv[1])
    
    ## Disconnect from the database
    system.disconnect()
    
test()

    