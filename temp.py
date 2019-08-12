from __future__ import print_function
import string
from collections import OrderedDict
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy



class Mili(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.Step1()
        self.Step2()
        self.Step3()
        self.Step4()
        self.finWord()


    def Step1(self):
        print('--Step#1')
        self.A = [["S3/Y3", "S2/Y1"],
                 ["S4/Y1", "S4/Y3"],
                 ["S4/Y1", "S2/Y2"],
                 ["S2/Y2", "S2/Y3"]]
        self.SaveA = copy.deepcopy(self.A)
        self.NewA = []
        for S in range(4):
            print("\n")
            for X in range(2):
                print(self.A[S][X], end=' ')
                self.NewA.append(self.A[S][X])
        print("\n")

        for j in range(len(self.NewA)):
            kol = 0
            for S in range(4):
                for X in range(2):
                    if self.A[S][X] == self.NewA[j]:
                        kol += 1
                        if kol > 1:
                            self.A[S][X] = ' '
    def Step2(self):
        print('\n--Step#2\n')
        self.ForSb = []
        self.num = 1
        self.S1()
        self.S2()
        self.S3()
        self.S4()
        self.Sb()

        Y1 = self.Y('Y1')
        Y2 = self.Y('Y2')
        Y3 = self.Y('Y3')
        print('Y1 =',Y1,'\nY2 =',Y2,'\nY3 =',Y3, '\n')
    def Step3(self):
        print('\n--Step#3\n')
        self.X1WithKeys = {}
        self.X2WithKeys = {}
        self.forFin = []
        first = ''
        second = ''
        forSWith = [self.WithS1, self.WithS2, self.WithS3, self.WithS4]
        for S in range(4):
            for X in range(2):
                if X == 0:
                    first = self.SaveA[S][X]
                else:
                    second = self.SaveA[S][X]
            self.X1(first, forSWith[S])
            self.X2(second, forSWith[S])
        #print(self.X1WithKeys)
        #print(self.X2WithKeys)
    def Step4(self):
        print('\n--Step#4\n')
        self.createFinTable(self.X1WithKeys,0)
        self.createFinTable(self.X2WithKeys,1)

        print(self.finTable)

    def S1(self):
        S1 = self.S('S1')
        S1.sort()
        self.ForSb = self.ForSb + S1
        self.WithS1 = []
        for j in range(len(S1)):
            self.WithS1.append("S'" + str(self.num))
            self.num += 1
        print("S1 =",S1, "=", self.WithS1)
    def S2(self):
        S2 = self.S('S2')
        S2.sort()
        self.ForSb = self.ForSb + S2
        self.WithS2 = []
        for j in range(len(S2)):
            self.WithS2.append("S'" + str(self.num))
            self.num += 1
        print("S2 =",S2, "=", self.WithS2)
    def S3(self):
        S3 = self.S('S3')
        S3.sort()
        self.ForSb = self.ForSb + S3
        self.WithS3 = []
        for j in range(len(S3)):
            self.WithS3.append("S'" + str(self.num))
            self.num += 1
        print("S3 =",S3, "=", self.WithS3)
    def S4(self):
        S4 = self.S('S4')
        S4.sort()
        self.ForSb = self.ForSb + S4
        self.WithS4 = []
        for j in range(len(S4)):
            self.WithS4.append("S'" + str(self.num))
            self.num += 1
        print("S4 =",S4, "=", self.WithS4)
    def S(self,numS):
        i = 0
        tempS = []
        for S in range(4):
            for X in range(2):
                if numS in self.A[S][X]:
                    tempS.append(self.A[S][X])
        return tempS
    def Sb(self):
        self.Sb = []
        for j in range(self.num-1):
            self.Sb.append("S'" + str(j+1))
            self.num += 1
        print("Sb = S1 U S2 U S3 U S4 =",self.Sb)
        self.finTable = []
        for S in range(len(self.Sb)):
            self.finTable.append([])
            for X in range(2):
                self.finTable[S].append('o')
    def Y(self, Y):
        finY = []
        for j in range(len(self.ForSb)):
            if Y in self.ForSb[j]:
                finY.append(self.Sb[j])
        return finY

    def X1(self, SforX1, WithS):
        for i in range(len(self.ForSb)):
            if self.ForSb[i] == SforX1:
                print("X1 from ", WithS, "--->", self.Sb[i])
                self.forFin.append(self.Sb[i])
                self.X1WithKeys[str(WithS)] = self.Sb[i]
    def X2(self, SforX2, WithS):
        for i in range(len(self.ForSb)):
            if self.ForSb[i] == SforX2:
                print("X2 from ", WithS, "--->", self.Sb[i])
                self.forFin.append(self.Sb[i])
                self.X2WithKeys[str(WithS)] = self.Sb[i]

    def createFinTable(self,XWK,X):
        for key in XWK:
            for S in range(len(self.Sb)):
                if str(self.Sb[S]) in str(key):
                    self.finTable[S][X] = XWK[key]


    def finWord(self):
        print('\n')
        #self.Word = ['X1','X2','X2','X1','X1','X2']
        self.Word = [0,1,1,0,0,1]
        Slist = []
        Ylist = []
        s = 0
        for x in range(len(self.Word)):
            fin = self.SaveA[s][self.Word[x]]
            print('Sigma(S',s+1,' / X',self.Word[x]+1, ') =', fin[:2])
            Slist.append('S'+str(s+1))
            print('Lambda(S',s+1,' / X',self.Word[x]+1, ') =', fin[3:])
            Ylist.append(fin[3:])

            s = int(fin[1:2])-1
        print(Slist)
        print(Ylist)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Mili()
    window.setWindowTitle("OOP-style window creation")
    window.resize(700, 400)
    #window.show()
    sys.exit(app.exec_())

