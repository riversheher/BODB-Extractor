
import extractor
import internal.load

def test():
    config = internal.load.load_config()
    print(config)
    system = extractor.extractor(config)
    system.connect()
    ## TODO: Code for testing the extractor goes here (integration tests)
    
    
    ## Disconnect from the database
    system.disconnect()
    
test()

    