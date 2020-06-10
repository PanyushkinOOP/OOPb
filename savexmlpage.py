class savexmlpage:
    def __init__(self, store, dataxml, datasql):
        self.sto = store
        self.xml = dataxml
        self.sql = datasql
    
    def index(self):
        self.xml.write('new.xml', self.sto)
        s = '<a href=..>Back</a><br>'
        s += 'Save in new.xml'
        return s
    index.exposed=True
