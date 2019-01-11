import pandas as pd
class main():
    """funtion for import grade from csv and choose data from multi dataframe"""
    def readfile(self):
     self.readCSV = pd.read_csv("1.csv",encoding = "utf8")
     self.Choosedata = self.readCSV[['ชื่อวิชา','เกรด']]
     self.Choosedata = self.Choosedata.iloc[0:37]
     print(self.Choosedata)
    def editgrade(self):
     self.row = input("Select row you want to edit: ")
     self.column = input("Select column you want to edit:" )
     self.editgrade = input("Select grade you want to edit:")
     self.Choosedata.loc[self.row,self.column] = self.editgrade
     self.Choosedata.to_csv("1.csv")
     print(self.Choosedata)
demo = main()
demo.readfile()
demo.editgrade()











