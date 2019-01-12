import pandas as pd
import numpy as np
class main():
    """funtion for import grade from csv and choose data from multi dataframe"""
    def readfile(self):
     self.readCSV = pd.read_csv("1.csv",encoding = "utf8")
     self.Choosedata = self.readCSV[['subject','grade']]
     self.Choosedata = self.Choosedata.iloc[0:]
    def insertgrade(self):
     self.row = input("Select row you want to edit: ")
     self.column = input("Select column you want to edit:" )
     self.editgrade = input("Select grade you want to edit:")
     self.Choosedata.loc[self.row,self.column] = self.editgrade
     self.Choosedata.to_csv("1.csv")
     print(self.Choosedata)
    def editgrade(self):
     self.row1 = input("Select row you want to edit: ")
     self.column1 = input("Select column you want to edit:" )
     self.editgrade1 = input("Select grade you want to edit:")
     self.Choosedata.set_value('5', self.column1, self.editgrade1)
     self.Choosedata.to_csv("1.csv")
     print(self.row1)
    def calcularategrade(self):
     idx = 0
     rategrade = {'A': 4, 'B+': 3.5,'B': 3,'C+': 2.5,'C': 2,'D+': 1.5,'D': 1,'F': 0}
     self.Choosedata = self.Choosedata.replace({'grade':rategrade})
     # self.Choosedata.insert(loc=idx,column='หน่วยกิต',value=self.Choosedata.replace({'grade':rategrade})
     print(self.Choosedata)
demo = main()
demo.readfile()
#demo.editgrade()
demo.calcularategrade()










