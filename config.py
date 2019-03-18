from simple import Scrapy
from simple import DataObject
from simple import ComparewithExcel
class MainClass:
 s = Scrapy()
 carddata = s.card_details_data()
 excel=ComparewithExcel()
 conNo=excel.extractvalues()
 for i in conNo:
  if (carddata['customId_ConsessionNo']!=i):
   dt=DataObject()
   dataobject=dt.dataobjectcreation(carddata)


