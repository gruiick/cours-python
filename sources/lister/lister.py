import sys
import os

def parse_args(args):
    options = Options()
    if "-l" in args:
        options.show_modification_time= True
    return options

class Options:
    def __init__(self):
        self.show_modification_time = False

class Entry:
    def __init__(self,name):
        self.name=name
        self.is_directory=False
        self.mtime=0
        
def get_entries():
    names = os.listdir(".")
    for name in names:
        entry = Entry(name)
        entry.mtime = os.stat(name).st_mtime
        yield entry

def list_entries(entries,options):
    for entry in entries:
        if options.show_modification_time :
            yield f"{entry.name} {entry.mtime}"
        else:
            yield entry.name
            
def main():
    options=parse_args(sys.argv)
    entries = get_entries()
    lines = list_entries(entries,options) 
    for line in lines:
        print(line)
        
if __name__=="__main__":
    main()
