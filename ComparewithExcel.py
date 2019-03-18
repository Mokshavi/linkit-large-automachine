import pandas as pd
class ComparewithExcel:
    def extractvalues(self):
        df = pd.ExcelFile('C:\\Users\\murali\\PycharmProjects\\untitled\\Utilities\\ExcelTrack.xlsx').parse(
            'Sheet1')  # you could add index_col=0 if there's an index
        x = []
        x.append(df['consessionnum'])
        conNo = x[0].values
        return conNo

    def insertValues(self, carddata):
        df = pd.DataFrame(carddata)
        writer = pd.ExcelWriter('C:\\Users\\murali\\PycharmProjects\\untitled\\Utilities\\ExcelTrack.xlsx',
                                engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        value = writer.save()
        return value


