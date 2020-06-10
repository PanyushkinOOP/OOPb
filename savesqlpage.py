class savesqlpage:
    def __init__(self, store, dataxml, datasql):
        self.sto = store
        self.xml = dataxml
        self.sql = datasql
    
    def index(self):
        self.sql.write('new.sql', self.sto)
        s = '<a href=..>Back</a><br>'
        s += 'Save in new.sql'
        return s
    index.exposed=True
