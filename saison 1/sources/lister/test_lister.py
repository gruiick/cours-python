import lister

def test_parse_args_empty_list():
    options = lister.parse_args([])
    assert options.show_modification_time is False
    
def test_parse_args_dash_l():
    options = lister.parse_args(["-l"])
    assert options.show_modification_time is True
    
    
def test_list_empty_entries():
    options = lister.Options()
    assert list(lister.list_entries([], options)) == []
    

def get_listing(entries, show_modification_time=False):
    options = lister.Options()
    options.show_modification_time = show_modification_time
    return list(lister.list_entries(entries, options))

def test_list_names():
    foo_txt = lister.Entry("foo.txt")
    entries = [foo_txt]
    assert get_listing(entries, show_modification_time=False) == ["foo.txt"]
    
def test_list_mtimes():
    foo_txt = lister.Entry("foo.txt")
    foo_txt.mtime = 1559404640
    entries = [foo_txt]
    assert get_listing(entries, show_modification_time=True)== ["foo.txt 1559404640"]
