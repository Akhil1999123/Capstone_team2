def searchDB(self,fil):
    self.f="filename"
    sql="""
          select * from searchfiles  where filename like '%{0}""".formmat(fil)
    self.cur.execute(sql)
    row=self.cur.fetchone()
    if row==None:
        return 0
    else:
        return  row
def insertDB(self,filenmae):
    sql="""