

def read_file(file_path: str):
    """read_file expects the filepath for the BODB file,
    and returns a list of strings, where each string corresponds to a line in the file.
    
    This is a generator that reads a file line by line, yielding each line as a string.
    Utilize this function to read the BODB file line by line.  You can iterate over the lines
    by using a for loop, or by calling the next() function on the generator.
    
    This allows the function to read large files without loading the entire file into memory.

    Args:
        file_path (str): The absolute or relative path to the BODB file.
    """
    
    file = open(file_path, "r")
    for line in file:
        yield line
    file.close()
    