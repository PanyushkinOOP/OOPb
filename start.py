import cherrypy
import sys
sys.path.insert(0, "./store")
from store import store
from dataxml import dataxml
from datasql import datasql
from materialspage import materialspage
from productspage import productspage
from sellspage import sellspage
from savexmlpage import savexmlpage
from savesqlpage import savesqlpage

class start:
    def __init__(self):
        self.__store=store()
        self.__dataxml=dataxml()
        self.__dataxml.read('new.xml',self.__store)
        self.__datasql=datasql()
        self.materialspage=materialspage(self.__store)
        self.productspage=productspage(self.__store)
        self.sellspage=sellspage(self.__store)
        self.savexml = savexmlpage(self.__store, self.__dataxml, self.__datasql)
        self.savesql = savesqlpage(self.__store, self.__dataxml, self.__datasql)
    def index(self):
        return """
               <a href=materialspage\>Материал</a><br>
               <a href=productspage\>Изделие</a><br>
               <a href=sellspage\>Продажа</a><br>
               <a href=savesql\>Save as SQL</a><br>
               <a href=savexml\>Save as XML</a><br>
        """
    index.exposed=True
root=start()
cherrypy.config.update({
        'log.screen': True,
})

cherrypy.tree.mount(root)
if __name__ == '__main__':
    cherrypy.engine.start()
    cherrypy.engine.block()

