class sellspage:
    def __init__(self, store):
        self.__sto = store

    def index(self):
        s = '<a href=..>%s</a><a href=addform>%s</a>' % (u'назад', u' добавить')
        s += '<table><th bgcolor=gray></th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th>' % (
            u'изделие',u'дата',u'фамилия',u'имя',u'отчество')
        r = 1
        bg = ''
        for c in self.__sto.getSellCodes():
            s += '<tr%s><td>%d</td>' % (bg, r)
            s += '<td>%s</td>' % self.__sto.getSellProductName(c)
            s += '<td>%s</td>' % self.__sto.getSellDate(c)
            s += '<td>%s</td>' % self.__sto.getSellSurname(c)
            s += '<td>%s</td>' % self.__sto.getSellName(c)
            s += '<td>%s</td>' % self.__sto.getSellSecname(c)
            s += '<td><a href=editform?code=%s>%s</a></td>' % (c, u'редактировать')
            s += '<td><a href=delr?code=%s>%s</a></td></tr>' % (c, u'удалить')
            r += 1
            if bg:
                bg = ''
            else:
                bg = ' bgcolor=silver'
        s += '</table>'
        return s

    index.exposed = True

    def productsCombo(self, code=0):
        s = '<select name=product>'
        for c in self.__sto.getProductCodes():
            if (code in self.__sto.getSellCodes()) and (c == self.__sto.getSellProductCode(code)):
                v = ' selected'
            else:
                v = ''
            s += '<option%s value=%s>%s</option>' % (v, str(c), self.__sto.getProductName(c))
        s += '</select>'
        return s

    def sellform(self, code=0, add=True):
        product, date, surname, name, secname = '', '', '', '', ''
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s' % code
        if code in self.__sto.getSellCodes():
            date = self.__sto.getSellDate(code)
            surname = self.__sto.getSellSurname(code)
            name = self.__sto.getSellName(code)
            secname = self.__sto.getSellSecname(code)

        s = '''
             <form action=%s method=post>
             <table>
                <tr><td>%s</td><td>%s</td></tr>
                <tr><td>%s</td><td><input type=text name=date value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=surname value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=name value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=secname value=%s></td></tr>
                <tr><td><input type=submit></td><td></td></tr>
            </table>
            </form>''' % (a, u'изделие', self.productsCombo(code), u'дата', date, u'фамилия', surname, 'имя', name, u'отчество', secname)
        return s

    def addaction(self, product, date, surname, name, secname):
        code = self.__sto.getSellNewCode()
        self.__sto.newSell(code)
        self.__sto.setSellProduct(int(code), int(product))
        self.__sto.setSellDate(int(code), date)
        self.__sto.setSellSurname(int(code), surname)
        self.__sto.setSellName(int(code), name)
        self.__sto.setSellSecname(int(code), secname)
        return 'продажа добавлена<br><a href=index>назад</a>'

    addaction.exposed = True

    def addform(self):
        s = u'Добавить новую продажу<br>'
        s += self.sellform(0)
        return s

    addform.exposed = True

    def editform(self, code):
        s = u'Редактировать продажу<br>'
        s += self.sellform(int(code), False)
        return s

    editform.exposed = True

    def editaction(self,code, product, date, surname, name, secname):
        self.__sto.setSellProduct(int(code), int(product))
        self.__sto.setSellDate(int(code), date)
        self.__sto.setSellSurname(int(code), surname)
        self.__sto.setSellName(int(code), name)
        self.__sto.setSellSecname(int(code), secname)
        return 'продажа изменена<br><a href=index>назад</a>'

    editaction.exposed = True

    def delr(self, code):
        self.__sto.removeSell(int(code))
        return 'продажа удалена<br><a href=index>назад</a>'

    delr.exposed = True
