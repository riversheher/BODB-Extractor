import extractor
import internal.load
import sys
import os


# from models.Database.utils import init_tables  # POSTGRES
# from models.Database.utils import reset_tables  # POSTGRES

"""def test():
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

test()"""

# I WANT TO RUN THROUGH EVERY FILE IN SCRATCH PRESENT ON SHARCNET
def test():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <file_or_folder_path>')
        exit(0)

    system = extractor.extractor()

    input_path = sys.argv[1]

    if os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            file_path = os.path.join(input_path, filename)
            if os.path.isfile(file_path):
                print(f"Processing {file_path}...")
                system.extract(file_path)
    else:
        system.extract(input_path)

test()
    