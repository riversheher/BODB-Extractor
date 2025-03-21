import extractor
import internal.load
import sys


# from models.Database.utils import init_tables  # POSTGRES
# from models.Database.utils import reset_tables  # POSTGRES

def test():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <filepath>')
        exit(0)

    #config = internal.load.load_config()
    #print("config loaded: \n")
    #print(config)
    #system = extractor.extractor(config)
    system = extractor.extractor()
    # system.connect()  # POSTGRES

    if sys.argv[1] == 'reset':
        print(f'Resetting tables')
        # reset_tables(system.conn)  # POSTGRES

        # error = init_tables(system.conn)  # POSTGRES
        # if error is not None:
        #     print(f"Error initializing tables: {error}")  # POSTGRES
    else:
        # Test 100 lines test file
        system.extract(sys.argv[1])

    # Disconnect from the database
    # system.disconnect()  # POSTGRES


test()

    