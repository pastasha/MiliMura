from __future__ import print_function
from PyQt5.QtWidgets import *
import copy
import mydesign
import sys



class Mili(QMainWindow, mydesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_btn.clicked.connect(self.start_func)

    def start_func(self):
        self.Step1()
        self.Step2()
        self.Step3()
        self.Step4()
        self.FinWord()
        self.Mura()
    def clear_func(self):
        self.fS1X1.clear()
        self.fS1X2.clear()
        self.fS2X1.clear()
        self.fS2X2.clear()
        self.fS3X1.clear()
        self.fS3X2.clear()
        self.fS4X1.clear()
        self.fS4X2.clear()
        self.fS5X1.clear()
        self.fS5X2.clear()
        self.fS6X1.clear()
        self.fS6X2.clear()
        self.fS7X1.clear()
        self.fS7X2.clear()
        self.fS8X1.clear()
        self.fS8X2.clear()
        self.label.clear()
        self.fS9X1.clear()
        self.fS9X2.clear()
        self.fS10X1.clear()
        self.fS10X2.clear()
        self.label_3.clear()


    def Step1(self):
        print('--Step#1')

        self.A = [[self.S1X1_3.toPlainText(), self.S1X2_3.toPlainText()],
                  [self.S2X1_3.toPlainText(), self.S2X2_3.toPlainText()],
                  [self.S3X1_3.toPlainText(), self.S3X2_3.toPlainText()],
                  [self.S4X1_3.toPlainText(), self.S4X2_3.toPlainText()]]
        '''
        self.A = [["S1/Y3", "S2/Y1"],
                  ["S4/Y1", "S2/Y3"],
                  ["S1/Y1", "S1/Y2"],
                  ["S2/Y2", "S2/Y3"]]
        '''
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
        self.Sb1()

        Y1 = self.Y('Y1')
        self.Y1_2.setText('Y1 = '+str(Y1))
        Y2 = self.Y('Y2')
        self.Y2_2.setText('Y2 = '+str(Y2))
        Y3 = self.Y('Y3')
        self.Y3_2.setText('Y3 = '+str(Y3))
        print('Y1 =',Y1,'\nY2 =',Y2,'\nY3 =',Y3, '\n')
    def Step3(self):
        print('\n--Step#3\n')
        self.X1WithKeys = {}
        self.X2WithKeys = {}
        self.forFin = []
        self.forVisual = []
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
        self.n1X1.setText(self.forVisual[0])
        self.n1X2.setText(self.forVisual[1])
        self.n2X1.setText(self.forVisual[2])
        self.n2X2.setText(self.forVisual[3])
        self.n3X1.setText(self.forVisual[4])
        self.n3X2.setText(self.forVisual[5])
        self.n4X1.setText(self.forVisual[6])
        self.n4X2.setText(self.forVisual[7])
    def Step4(self):
        print('\n--Step#4\n')
        self.createFinTable(self.X1WithKeys,0)
        self.createFinTable(self.X2WithKeys,1)

        if len(self.Sb) == 8:
            self.fS1X1.show()
            self.fS1X2.show()
            self.fS2X1.show()
            self.fS2X2.show()
            self.fS3X1.show()
            self.fS3X2.show()
            self.fS4X1.show()
            self.fS4X2.show()
            self.fS5X1.show()
            self.fS5X2.show()
            self.fS6X1.show()
            self.fS6X2.show()
            self.fS7X1.show()
            self.fS7X2.show()
            self.fS8X1.show()
            self.fS8X2.show()
            self.fS1X1.setText(self.finTable[0][0])
            self.fS1X2.setText(self.finTable[0][1])
            self.fS2X1.setText(self.finTable[1][0])
            self.fS2X2.setText(self.finTable[1][1])
            self.fS3X1.setText(self.finTable[2][0])
            self.fS3X2.setText(self.finTable[2][1])
            self.fS4X1.setText(self.finTable[3][0])
            self.fS4X2.setText(self.finTable[3][1])
            self.fS5X1.setText(self.finTable[4][0])
            self.fS5X2.setText(self.finTable[4][1])
            self.fS6X1.setText(self.finTable[5][0])
            self.fS6X2.setText(self.finTable[5][1])
            self.fS7X1.setText(self.finTable[6][0])
            self.fS7X2.setText(self.finTable[6][1])
            self.fS8X1.setText(self.finTable[7][0])
            self.fS8X2.setText(self.finTable[7][1])
            self.fS9X1.hide()
            self.fS9X2.hide()
            self.label_2.hide()
            self.fS10X1.hide()
            self.fS10X2.hide()
            self.label_3.hide()
            self.label_50.show()
            self.label_51.show()
            self.label_52.show()
            self.label_53.show()
            self.label_54.show()
            self.label_55.show()
            self.label_56.show()
            self.label.show()
        elif len(self.Sb) == 7:
            self.fS1X1.show()
            self.fS1X2.show()
            self.fS2X1.show()
            self.fS2X2.show()
            self.fS3X1.show()
            self.fS3X2.show()
            self.fS4X1.show()
            self.fS4X2.show()
            self.fS5X1.show()
            self.fS5X2.show()
            self.fS6X1.show()
            self.fS6X2.show()
            self.fS7X1.show()
            self.fS7X2.show()
            self.fS1X1.setText(self.finTable[0][0])
            self.fS1X2.setText(self.finTable[0][1])
            self.fS2X1.setText(self.finTable[1][0])
            self.fS2X2.setText(self.finTable[1][1])
            self.fS3X1.setText(self.finTable[2][0])
            self.fS3X2.setText(self.finTable[2][1])
            self.fS4X1.setText(self.finTable[3][0])
            self.fS4X2.setText(self.finTable[3][1])
            self.fS5X1.setText(self.finTable[4][0])
            self.fS5X2.setText(self.finTable[4][1])
            self.fS6X1.setText(self.finTable[5][0])
            self.fS6X2.setText(self.finTable[5][1])
            self.fS7X1.setText(self.finTable[6][0])
            self.fS7X2.setText(self.finTable[6][1])
            self.fS8X1.hide()
            self.fS8X2.hide()
            self.label.hide()
            self.label_50.show()
            self.label_51.show()
            self.label_52.show()
            self.label_53.show()
            self.label_54.show()
            self.label_55.show()
            self.label_56.show()
        elif len(self.Sb) == 6:
            self.fS1X1.show()
            self.fS1X2.show()
            self.fS2X1.show()
            self.fS2X2.show()
            self.fS3X1.show()
            self.fS3X2.show()
            self.fS4X1.show()
            self.fS4X2.show()
            self.fS5X1.show()
            self.fS5X2.show()
            self.fS6X1.show()
            self.fS6X2.show()
            self.fS1X1.setText(self.finTable[0][0])
            self.fS1X2.setText(self.finTable[0][1])
            self.fS2X1.setText(self.finTable[1][0])
            self.fS2X2.setText(self.finTable[1][1])
            self.fS3X1.setText(self.finTable[2][0])
            self.fS3X2.setText(self.finTable[2][1])
            self.fS4X1.setText(self.finTable[3][0])
            self.fS4X2.setText(self.finTable[3][1])
            self.fS5X1.setText(self.finTable[4][0])
            self.fS5X2.setText(self.finTable[4][1])
            self.fS6X1.setText(self.finTable[5][0])
            self.fS6X2.setText(self.finTable[5][1])
            self.fS7X1.hide()
            self.fS7X2.hide()
            self.label_56.hide()
            self.fS8X1.hide()
            self.fS8X2.hide()
            self.label.hide()
            self.label_50.show()
            self.label_51.show()
            self.label_52.show()
            self.label_53.show()
            self.label_54.show()
            self.label_55.show()
        elif len(self.Sb) == 5:
            self.fS1X1.show()
            self.fS1X2.show()
            self.fS2X1.show()
            self.fS2X2.show()
            self.fS3X1.show()
            self.fS3X2.show()
            self.fS4X1.show()
            self.fS4X2.show()
            self.fS5X1.show()
            self.fS5X2.show()
            self.fS1X1.setText(self.finTable[0][0])
            self.fS1X2.setText(self.finTable[0][1])
            self.fS2X1.setText(self.finTable[1][0])
            self.fS2X2.setText(self.finTable[1][1])
            self.fS3X1.setText(self.finTable[2][0])
            self.fS3X2.setText(self.finTable[2][1])
            self.fS4X1.setText(self.finTable[3][0])
            self.fS4X2.setText(self.finTable[3][1])
            self.fS5X1.setText(self.finTable[4][0])
            self.fS5X2.setText(self.finTable[4][1])
            self.fS6X1.hide()
            self.fS6X2.hide()
            self.label_55.hide()
            self.fS7X1.hide()
            self.fS7X2.hide()
            self.label_56.hide()
            self.fS8X1.hide()
            self.fS8X2.hide()
            self.label.hide()
            self.label_50.show()
            self.label_51.show()
            self.label_52.show()
            self.label_53.show()
            self.label_54.show()
        elif len(self.Sb) == 4:
            self.fS1X1.show()
            self.fS1X2.show()
            self.fS2X1.show()
            self.fS2X2.show()
            self.fS3X1.show()
            self.fS3X2.show()
            self.fS4X1.show()
            self.fS4X2.show()
            self.fS1X1.setText(self.finTable[0][0])
            self.fS1X2.setText(self.finTable[0][1])
            self.fS2X1.setText(self.finTable[1][0])
            self.fS2X2.setText(self.finTable[1][1])
            self.fS3X1.setText(self.finTable[2][0])
            self.fS3X2.setText(self.finTable[2][1])
            self.fS4X1.setText(self.finTable[3][0])
            self.fS4X2.setText(self.finTable[3][1])
            self.fS5X1.hide()
            self.fS5X2.hide()
            self.label_54.hide()
            self.fS6X1.hide()
            self.fS6X2.hide()
            self.label_55.hide()
            self.fS7X1.hide()
            self.fS7X2.hide()
            self.label_56.hide()
            self.fS8X1.hide()
            self.fS8X2.hide()
            self.label.hide()
            self.label_50.show()
            self.label_51.show()
            self.label_52.show()
            self.label_53.show()
        elif len(self.Sb) == 3:
            self.fS1X1.show()
            self.fS1X2.show()
            self.fS2X1.show()
            self.fS2X2.show()
            self.fS3X1.show()
            self.fS3X2.show()
            self.fS1X1.setText(self.finTable[0][0])
            self.fS1X2.setText(self.finTable[0][1])
            self.fS2X1.setText(self.finTable[1][0])
            self.fS2X2.setText(self.finTable[1][1])
            self.fS3X1.setText(self.finTable[2][0])
            self.fS3X2.setText(self.finTable[2][1])
            self.fS4X1.hide()
            self.fS4X2.hide()
            self.label_53.hide()
            self.fS5X1.hide()
            self.fS5X2.hide()
            self.label_54.hide()
            self.fS6X1.hide()
            self.fS6X2.hide()
            self.label_55.hide()
            self.fS7X1.hide()
            self.fS7X2.hide()
            self.label_56.hide()
            self.fS8X1.hide()
            self.fS8X2.hide()
            self.label.hide()
            self.label_50.show()
            self.label_51.show()
            self.label_52.show()
        elif len(self.Sb) == 2:
            self.fS1X1.show()
            self.fS1X2.show()
            self.fS2X1.show()
            self.fS2X2.show()
            self.fS1X1.setText(self.finTable[0][0])
            self.fS1X2.setText(self.finTable[0][1])
            self.fS2X1.setText(self.finTable[1][0])
            self.fS2X2.setText(self.finTable[1][1])
            self.fS3X1.hide()
            self.fS3X2.hide()
            self.label_52.hide()
            self.fS4X1.hide()
            self.fS4X2.hide()
            self.label_53.hide()
            self.fS5X1.hide()
            self.fS5X2.hide()
            self.label_54.hide()
            self.fS6X1.hide()
            self.fS6X2.hide()
            self.label_55.hide()
            self.fS7X1.hide()
            self.fS7X2.hide()
            self.label_56.hide()
            self.fS8X1.hide()
            self.fS8X2.hide()
            self.label.hide()
            self.label_50.show()
            self.label_51.show()
        elif len(self.Sb) == 1:
            self.fS1X1.show()
            self.fS1X2.show()
            self.fS1X1.setText(self.finTable[0][0])
            self.fS1X2.setText(self.finTable[0][1])
            self.fS2X1.hide()
            self.fS2X2.hide()
            self.label_51.hide()
            self.fS3X1.hide()
            self.fS3X2.hide()
            self.label_52.hide()
            self.fS4X1.hide()
            self.fS4X2.hide()
            self.label_53.hide()
            self.fS5X1.hide()
            self.fS5X2.hide()
            self.label_54.hide()
            self.fS6X1.hide()
            self.fS6X2.hide()
            self.label_55.hide()
            self.fS7X1.hide()
            self.fS7X2.hide()
            self.label_56.hide()
            self.fS8X1.hide()
            self.fS8X2.hide()
            self.label.hide()
            self.label_50.show()
        print(self.finTable)
    def FinWord(self):
        print('\n')
        #self.Word = ['X1','X2','X2','X1','X1','X2']

        self.Word = []
        self.WordOriginal = [self.w1.toPlainText(),self.w2.toPlainText(),self.w3.toPlainText(),self.w4.toPlainText(),self.w5.toPlainText(),self.w6.toPlainText()]
        for x in range(len(self.WordOriginal)):
            if str(self.WordOriginal[x]) == '1':
                self.Word.append(0)
            else:
                self.Word.append(1)
        print(self.Word)
        Slist = []
        Ylist = []
        s = 0
        tt = ''
        for x in range(len(self.Word)):
            fin = self.SaveA[s][int(self.Word[x])]
            #print('Sigma(S',str(s+1),' / X',str(self.Word[x]+1), ') =', fin[:2])
            #tt = tt+('Sigma(S'+ str(s+1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[:2] + '\n')
            Slist.append('S'+str(s+1))
            #print('Lambda(S',s+1,' / X',self.Word[x]+1, ') =', fin[3:])
            #tt = tt + ('Lambda(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[3:] + '\n')
            Ylist.append(fin[3:])
            if x == 0:
                self.sig1.setText(str('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[:2] + '\n'))
                self.lam1.setText('Lambda(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[3:] + '\n')
            elif x == 1:
                self.sig2.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[:2] + '\n')
                self.lam2.setText('Lambda(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[3:] + '\n')
            elif x == 2:
                self.sig3.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[:2] + '\n')
                self.lam3.setText('Lambda(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[3:] + '\n')
            elif x == 3:
                self.sig4.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[:2] + '\n')
                self.lam4.setText('Lambda(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[3:] + '\n')
            elif x == 4:
                self.sig5.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[:2] + '\n')
                self.lam5.setText('Lambda(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[3:] + '\n')
            elif x == 5:
                self.sig6.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[:2] + '\n')
                self.lam6.setText('Lambda(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin[3:] + '\n')
            s = int(fin[1])-1

        mylist0 = ''
        for el in self.Word:
            mylist0 = mylist0 + 'X' +str(el+1) + '  '
        self.forXX.setText(mylist0)
        print(Slist)
        mylist = ''
        for el in Slist:
            mylist = mylist + el+ '  '
        self.forSS.setText(mylist)
        mylist1 = ''
        for el in Ylist:
            mylist1 = mylist1 + el + '  '
        print(Ylist)
        self.forYY.setText(mylist1)
    def Mura(self):
        print('\n')
        # self.Word = ['X1','X2','X2','X1','X1','X2']

        self.Word = []
        self.WordOriginal = [self.w1.toPlainText(), self.w2.toPlainText(), self.w3.toPlainText(), self.w4.toPlainText(),
                             self.w5.toPlainText(), self.w6.toPlainText()]
        for x in range(len(self.WordOriginal)):
            if str(self.WordOriginal[x]) == '1':
                self.Word.append(0)
            else:
                self.Word.append(1)
        Slist = []
        Ylist = []
        s = 0
        print(self.forYlist)
        for x in range(len(self.Word)):
            fin = self.finTable[s][int(self.Word[x])]
            Slist.append('S' + str(s + 1))
            if x == 0:
                print(self.Word[x] + 1)
                print(type(str(self.Word[x] + 1)))
                y = self.forYlist[int(fin[2:])-1]
                y = y[3:]
                Ylist.append(y)
                self.sig1_2.setText(str('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin + '\n'))
                self.lam1_2.setText('Lambda(' + fin + ') =' + y + '\n')
            elif x == 1:
                y = self.forYlist[int(fin[2:])-1]
                y = y[3:]
                Ylist.append(y)
                self.sig2_2.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin + '\n')
                self.lam2_2.setText('Lambda(' + fin + ') =' + y + '\n')
            elif x == 2:
                y = self.forYlist[int(fin[2:])-1]
                y = y[3:]
                Ylist.append(y)
                self.sig3_2.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin + '\n')
                self.lam3_2.setText('Lambda(' + fin + ') =' + y + '\n')
            elif x == 3:
                y = self.forYlist[int(fin[2:])-1]
                y = y[3:]
                Ylist.append(y)
                self.sig4_2.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin + '\n')
                self.lam4_2.setText('Lambda(' + fin + ') =' + y + '\n')
            elif x == 4:
                Ylist.append(y)
                y = self.forYlist[int(fin[2:])-1]
                y = y[3:]
                self.sig5_2.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin + '\n')
                self.lam5_2.setText('Lambda(' + fin + ') =' + y + '\n')
            elif x == 5:
                y = self.forYlist[int(fin[2:])-1]
                y = y[3:]
                Ylist.append(y)
                self.sig6_2.setText('Sigma(S' + str(s + 1) + ' / X' + str(self.Word[x] + 1) + ') =' + fin + '\n')
                self.lam6_2.setText('Lambda(' + fin + ') =' + y + '\n')

            s = int(fin[2:]) - 1

        mylist0 = ''
        for el in self.Word:
            mylist0 = mylist0 + 'X' + str(el+1) + '  '
        self.forXX_2.setText(mylist0)
        print(Slist)
        mylist = ''
        for el in Slist:
            mylist = mylist + el + '  '
        self.forSS_2.setText(mylist)
        mylist1 = ''
        for el in Ylist:
            mylist1 = mylist1 + el + '  '
        print(Ylist)
        self.forYY_2.setText(mylist1)



    def S1(self):
        S1 = self.S('S1')
        S1.sort()
        self.forYlist = []
        self.ForSb = self.ForSb + S1
        self.WithS1 = []
        for j in range(len(S1)):
            self.WithS1.append("S'" + str(self.num))
            self.num += 1
        self.S1_3.setText("S1 ="+str(S1)+"="+str(self.WithS1))
        for el in S1:
            self.forYlist.append(el)
        print("S1 =",S1, "=", self.WithS1)
    def S2(self):
        S2 = self.S('S2')
        S2.sort()
        self.ForSb = self.ForSb + S2
        self.WithS2 = []
        for j in range(len(S2)):
            self.WithS2.append("S'" + str(self.num))
            self.num += 1
        self.S2_2.setText("S2 =" + str(S2) + "=" + str(self.WithS2))
        for el in S2:
            self.forYlist.append(el)
        print("S2 =",S2, "=", self.WithS2)
    def S3(self):
        S3 = self.S('S3')
        S3.sort()
        self.ForSb = self.ForSb + S3
        self.WithS3 = []
        for j in range(len(S3)):
            self.WithS3.append("S'" + str(self.num))
            self.num += 1
        self.S3_2.setText("S3 =" + str(S3) + "=" + str(self.WithS3))
        for el in S3:
            self.forYlist.append(el)
        print("S3 =",S3, "=", self.WithS3)
    def S4(self):
        S4 = self.S('S4')
        S4.sort()
        self.ForSb = self.ForSb + S4
        self.WithS4 = []
        for j in range(len(S4)):
            self.WithS4.append("S'" + str(self.num))
            self.num += 1
        self.S4_2.setText("S4 =" + str(S4) + "=" + str(self.WithS4))
        for el in S4:
            self.forYlist.append(el)
        print("S4 =",S4, "=", self.WithS4)
    def S(self,numS):
        i = 0
        tempS = []
        for S in range(4):
            for X in range(2):
                if numS in self.A[S][X]:
                    tempS.append(self.A[S][X])
        return tempS
    def Sb1(self):
        self.Sb = []
        for j in range(self.num-1):
            self.Sb.append("S'" + str(j+1))
            self.num += 1
        self.Sb_2.setText("Sb = S1 U S2 U S3 U S4 =\n"+str(self.Sb))
        print("Sb = S1 U S2 U S3 U S4 =",self.Sb)
        self.finTable = []
        for S in range(len(self.Sb)):
            self.finTable.append([])
            for X in range(2):
                self.finTable[S].append('o')


        for i in range(len(self.Sb)):
            u = 0
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
                self.forVisual.append("X1 from "+str(WithS)+"--->"+str(self.Sb[i]))
                self.forFin.append(self.Sb[i])
                self.X1WithKeys[str(WithS)] = self.Sb[i]
    def X2(self, SforX2, WithS):
        for i in range(len(self.ForSb)):
            if self.ForSb[i] == SforX2:
                print("X2 from ", WithS, "--->", self.Sb[i])
                self.forVisual.append("X2 from " + str(WithS) + "--->" + str(self.Sb[i]))
                self.forFin.append(self.Sb[i])
                self.X2WithKeys[str(WithS)] = self.Sb[i]

    def createFinTable(self,XWK,X):
        for key in XWK:
            for S in range(len(self.Sb)):
                if str(self.Sb[S]) in str(key):
                    self.finTable[S][X] = XWK[key]



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mili()
    window.resize(1200,895)
    window.show()
    sys.exit(app.exec_())

