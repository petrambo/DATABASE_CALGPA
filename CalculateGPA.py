import pandas as pd
import numpy as np
class main():
    """funtion for import grade from csv and choose data from multi dataframe"""
    def readfile(self):
     self.readCSV = pd.read_csv("w1_GPA.csv",encoding = "utf8")
     self.Choosedata = self.readCSV[['ปีการศึกษา','ชื่อวิชา','หน่วยกิต','เกรด']]
     self.Choosedata = self.Choosedata.iloc[0:]
     print(self.Choosedata)
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
     rategrade = {'A': 4, 'B+': 3.5,'B': 3,'C+': 2.5,'C': 2,'D+': 1.5,'D': 1,'F': 0} #set value for convert grade to numaric
     self.Choosedata1 = self.Choosedata.replace({'เกรด':rategrade})
     self.Choose = self.Choosedata1[['เกรด']]
     self.Choosedata = pd.concat([self.Choosedata,self.Choose], axis=1) #include dataframe for continue calculate
     self.Choosedata.columns = ['ปีการศึกษา','ชื่อวิชา','หน่วยกิต','เกรด','น้ำหนักเฉลี่ย']     #rename duplicate column name
     self.Choosedata['นก*เกรด'] = self.Choosedata['หน่วยกิต'] * self.Choosedata['น้ำหนักเฉลี่ย']
     del self.Choosedata['น้ำหนักเฉลี่ย']         #Deleted columns that have not been calculated
     self.Choosedata.to_csv("1.csv")
     print(self.Choosedata)
demo = main()
demo.readfile()
#demo.editgrade()
demo.calcularategrade()










