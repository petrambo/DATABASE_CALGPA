import pandas as pd
import numpy as np

class main():
    """ funtion for import grade from csv and choose data from multi dataframe """
    def readfile(self):
     self.readCSV = pd.read_csv("w1_GPA.csv",encoding = "utf8")  # import file csv.
     self.Choosedata = self.readCSV[['ปีการศึกษา','ชื่อวิชา','หน่วยกิต','เกรด']] # Select only some active column
     self.Choosedata = self.Choosedata.iloc[0:37]
     self.Choosedata["หน่วยกิต"] = pd.to_numeric(self.Choosedata["หน่วยกิต"])


     """" this funtion for insert grade """
    def insertgrade(self):
     self.year = input("ปีการศึกษา: ")
     self.subject = input("ชื่อวิชา:" )
     self.credit = float(input("หน่วยกิต:"))
     self.grade = input("เกรด:")
     self.list= [self.year,self.subject,self.credit,self.grade]
     self.Choosedata.loc[len(self.Choosedata),:]=(self.list)     # insert list created

    """""funtion for edit grade"""
    def editgrade(self):
     self.col = input("ต้องการเเก้ไขสิ่งใด:")
     self.row = int(input("แถวที่เท่าไหร่:"))
     self.edit = input("เเก้ไขเป็น")
     if (self.col == 'หน่วยกิต'):
         float(self.edit)
         print("เเก้ไขเสร็จสิ้น")
     else:
         print("เเก้ไขเสร็จสิ้น")
     self.Choosedata.loc[self.Choosedata.index[self.row], self.col] = self.edit # edit list created
     print(self.Choosedata)


    """ funtion for calculate grade each term """
    def calcularategrade(self):
     rategrade = {'A': 4, 'B+': 3.5,'B': 3,'C+': 2.5,'C': 2,'D+': 1.5,'D': 1,'F': 0} # set value for convert grade to numaric
     self.Choosedata1 = self.Choosedata.replace({'เกรด':rategrade})
     self.Choose = self.Choosedata1[['เกรด']]
     self.Choosedata = pd.concat([self.Choosedata,self.Choose], axis=1) # include dataframe for continue calculate
     self.Choosedata.columns = ['ปีการศึกษา','ชื่อวิชา','หน่วยกิต','เกรด','น้ำหนักเฉลี่ย']     # rename duplicate column name
     self.Choosedata['นก*เกรด'] = self.Choosedata['หน่วยกิต'] * self.Choosedata['น้ำหนักเฉลี่ย']
     del self.Choosedata['น้ำหนักเฉลี่ย']         # Deleted columns that have not been calculated
     self.Choosedata['รวมหน่วยกิต'] = self.Choosedata.groupby(['ปีการศึกษา'])['หน่วยกิต'].transform('sum') # Total for further calculation
     self.Choosedata['รวมน้ำหนัก'] = self.Choosedata.groupby(['ปีการศึกษา'])['นก*เกรด'].transform('sum')
     self.Newdata = self.Choosedata.drop_duplicates(subset=['ปีการศึกษา'])   # Create new data for calcalate Semester grades
     del self.Newdata['ชื่อวิชา'] # Delete the calculated columns for the sort of dataframe.
     del self.Newdata['เกรด']
     del self.Newdata['นก*เกรด']
     self.Newdata['เกรดเฉลี่ยต่อเทอม'] = self.Newdata['รวมน้ำหนัก']/self.Newdata['รวมหน่วยกิต'] # Divided to find the average of the grade
     self.Newdata = self.Newdata.round(2)  # Gives results equal to 2 decimal places
     del self.Newdata['รวมน้ำหนัก']  # Delete the calculated columns for the sort of dataframe.
     del self.Newdata['รวมหน่วยกิต']
     del self.Newdata['หน่วยกิต']
     del self.Choosedata['รวมหน่วยกิต']
     del self.Choosedata['รวมน้ำหนัก']
     del self.Choosedata['นก*เกรด']
     self.Choosedata = pd.concat([self.Choosedata,self.Newdata], axis=1) # Combine old and new data into the same dataframe
     self.Choosedata.to_csv('w1_GPA.csv')# Export dataframe to CSV file
     self.__init__()

    """" Functions that are used to test and activate functions """
    def __init__(self):
     self.readfile()
     self.funtion = input("รายการที่ต้องการทำ? \n\n 1) ดูรายละเอียด \n\n 2) เพิ่มรายการ \n\n 3) เเก้ไข \n\n 4) ออกจากโปรเเกรม \n\n Please enter number  >>>>> ")
     if self.funtion == "1":
       print(self.Choosedata)
     elif self.funtion == "2":
      self.insertgrade()
     elif self.funtion == "3":
      self.editgrade()
     elif self.funtion == "4":
      print("จบการทำงาน")
      return
     else :
      print("out of range")
     print(self.Choosedata)
     self.funtion1 = input("ต้องการบันทึกหรือไม่ y/n ? \n\n >>>>>")
     if self.funtion1 == "y":
      self.calcularategrade()
     elif self.funtion1 =="n":
       self.__init__()


demo = main()










