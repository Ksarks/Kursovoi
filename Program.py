from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QDate, QObject, QThread
import DB_working
import sys
import Main
import Login
import goal
import quot
import record
import setting
import message
import testi
import newcrit
import time
import rest

class restwindow(QtWidgets.QDialog):
    Pom = pyqtSignal(int)

    def __init__(self, pomidor):
        super(restwindow, self).__init__()
        self.ui = rest.Ui_Dialog()
        self.ui.setupUi(self)
        if pomidor == 15:
            self.ui.Less.setEnabled(False)
        if pomidor == 50:
            self.ui.More.setEnabled(False)
        self.ui.Less.clicked.connect(self.changing)
        self.ui.Midlle.clicked.connect(self.changing)
        self.ui.More.clicked.connect(self.changing)

    def changing(self):
        sender = self.sender()
        if sender == self.ui.Less:
            self.Pom.emit(-5)
        if sender == self.ui.More:
            self.Pom.emit(5)
        self.close()

class recalculating(QThread):
    messag = pyqtSignal(str)

    def init(self, id, worktype, description, shedultype, year, mounth, date, concentration,
                 starttime='8:00', endtime='23:00', sdvig=0, timetowork=0.5):

        self.id = id
        self.worktype = worktype
        self.description = description
        self.shedultipe = shedultype
        self.year = year
        self.mounth = mounth
        self.date = date
        self.DATA = str(str(self.year) + '-' + str(self.mounth) + '-' + str(self.date))
        self.starttime = starttime
        self.endtime = endtime
        self.concentration = concentration
        self.move = sdvig
        self.timetowork = timetowork + timetowork/5
        std = self.DATA + ' ' + self.starttime
        self.std = time.strptime(std, '%Y-%m-%d %H:%M')
        self.tm = time.mktime(self.std)
        self.DataBase = DB_working.DBwork()
        self.crit = self.DataBase.GetCrit(self.id)
        self.allin = []



    def matter(self, data, moved):
        forinput = (self.id, data)
        shed = self.DataBase.GetShedul(forinput)
        flag = True
        tstr = str(moved.get('StartIvent'))
        if len(tstr) == 7:
            tstr = tstr[:4]
        else:
            tstr = tstr[:5]
        tnd = str(moved.get('EndIvent'))
        if len(tnd) == 7:
            tnd = tnd[:4]
        else:
            tnd = tnd[:5]

        tstr = time.strptime('2000-' + tstr, '%Y-%H:%M')
        tstr = time.mktime(tstr)
        tnd = time.strptime('2000-' + tnd, '%Y-%H:%M')
        tnd = time.mktime(tnd)

        delta = tnd - tstr
        oldtimee = time.mktime(self.std)
        getedshedul = True
        for i in shed:
            getedshedul = False
            tmstrt = str(i.get('StartIvent'))
            if len(tmstrt) == 7:
                tmstrt = tmstrt[:4]
            else:
                tmstrt = tmstrt[:5]
            tmend = str(i.get('EndIvent'))
            if len(tmend) == 7:
                tmend = tmend[:4]
            else:
                tmend = tmend[:5]

            tmrt = time.strptime('2000-' + tmstrt, '%Y-%H:%M')
            tmrt = time.mktime(tmrt)
            tend = time.strptime('2000-' + tmend, '%Y-%H:%M')
            tend = time.mktime(tend)
            dlt = oldtimee - tmrt

            if delta >= dlt:
                oldtimee = time.gmtime(oldtimee)
                oldtimee = time.strftime('%H:%M', oldtimee)
                forinput = [(self.id, data, oldtimee, tmstrt, moved.get('Description'),
                     moved.get('Type'), moved.get('movable'), moved.get('concentration'))]
                self.DataBase.ShedulInput(forinput)
                flag = False
            oldtimee = tend

        if getedshedul:
            forinput = [(self.id, data, moved.get('StartIvent'), moved.get('EndIvent'), moved.get('Description'),
                         moved.get('Type'), moved.get('movable'), moved.get('concentration'))]
            self.DataBase.ShedulInput(forinput)
            flag = False

        return flag

    def inpt(self, date, stime, etime):
        self.allin.append(
            (self.id, date, stime, etime, self.description, self.worktype, self.move,
             self.concentration))
        tstrt = time.strptime('2000-' + stime, '%Y-%H:%M')
        tstrt = time.mktime(tstrt)
        tnd = time.strptime('2000-' + etime, '%Y-%H:%M')
        tnd = time.mktime(tnd)
        return tnd - tstrt

    def reinput(self, oldrecord, data):
        deleteddata = (self.id, data, oldrecord.get('StartIvent'))
        self.DataBase.DeleteShedul(deleteddata)
        self.allin.append((self.id, data, oldrecord.get('StartIvent'), oldrecord.get('EndIvent'), self.description,
                           self.worktype, self.move, self.concentration))

    def newshedul(self):

        date = time.mktime(self.std)
        date += 24*60*60
        date = time.strftime('%Y-%m-%d', time.localtime(date))

        for i in self.neededchange:
            while True:
                flag = self.matter(date, i[0])
                if flag:
                    date = time.strptime(date, '%Y-%m-%d')
                    date = time.mktime(date)
                    date += 24 * 60 * 60
                    date = time.strftime('%Y-%m-%d', time.localtime(date))
                else:
                    break

    def shedput(self, data):
        forinput = (self.id, data)
        shed = self.DataBase.GetShedul(forinput)
        getedshedul = True
        weight = 0
        for k in self.crit:
            if k.get('idtypes') == self.worktype:
                weight = k.get('weight')
        for i in shed:
            tmstrt = str(i.get('StartIvent'))
            if len(tmstrt) == 7:
                tmstrt = tmstrt[:4]
            else:
                tmstrt = tmstrt[:5]
            tmend = str(i.get('EndIvent'))
            if len(tmend) == 7:
                tmend = tmend[:4]
            else:
                tmend = tmend[:5]

            if ((self.starttime > tmstrt and tmend < self.starttime) or (
                        self.endtime > tmstrt and tmend < self.endtime) or (
                        self.endtime > tmend and tmstrt < self.starttime)) and not i.get('movable'):
                getedshedul = False
                for k in self.crit:
                    if k.get('idtypes') == i.get('Type'):
                        if weight > k.get('weight'):
                            self.allin.append((self.id, data, self.starttime, self.endtime, self.description,
                                               self.worktype, self.move, self.concentration))

        if getedshedul:
            self.allin.append((self.id, data, self.starttime, self.endtime, self.description,
                               self.worktype, self.move, self.concentration))


    def run(self):
        if self.shedultipe == 0:
            self.shedput(self.DATA)
            self.DataBase.ShedulInput(self.allin)

        if self.shedultipe == 1:
            dateforcircle = time.mktime(time.strptime(self.DATA, '%Y-%m-%d'))
            endcircle = '2099-12-30'
            endcircle = time.mktime(time.strptime(endcircle, '%Y-%m-%d'))
            while dateforcircle < endcircle:
                dateforcircle = time.localtime(dateforcircle)
                dateforcircle = time.strftime('%Y-%m-%d', dateforcircle)
                self.shedput(dateforcircle)
                dateforcircle = time.strptime(dateforcircle, '%Y-%m-%d')
                dateforcircle = time.mktime(dateforcircle)
                dateforcircle += 7 * 24 * 60 * 60
            self.DataBase.ShedulInput(self.allin)

        if self.shedultipe == 2:
            dateforcircle = time.mktime(time.strptime(self.DATA, '%Y-%m-%d'))
            endcircle = '2099-12-30'
            endcircle = time.mktime(time.strptime(endcircle, '%Y-%m-%d'))
            while dateforcircle < endcircle:
                dateforcircle = time.localtime(dateforcircle)
                dateforcircle = time.strftime('%Y-%m-%d', dateforcircle)
                self.shedput(dateforcircle)
                dateforcircle = time.strptime(dateforcircle, '%Y-%m-%d')
                dateforcircle = time.mktime(dateforcircle)
                dateforcircle += 14 * 24 * 60 * 60
            self.DataBase.ShedulInput(self.allin)

        if self.shedultipe == 3:
            dateforcircle = time.mktime(time.strptime(self.DATA, '%Y-%m-%d'))
            endcircle = '2099-12-30'
            endcircle = time.mktime(time.strptime(endcircle, '%Y-%m-%d'))
            while dateforcircle < endcircle:
                dateforcircle = time.localtime(dateforcircle)
                dateforcircle = time.strftime('%Y-%m-%d', dateforcircle)
                self.shedput(dateforcircle)
                dateforcircle = time.strptime(dateforcircle, '%Y-%m-%d')
                months = dateforcircle.tm_mon + 1
                years = dateforcircle.tm_year
                if months > 12:
                    months = 1
                    years += 1
                dateforcircle = str(str(years) + '-' + str(months) + '-' + str(dateforcircle.tm_mday))
                dateforcircle = time.strptime(dateforcircle, '%Y-%m-%d')
                dateforcircle = time.mktime(dateforcircle)
            self.DataBase.ShedulInput(self.allin)

        if self.shedultipe == 4:
            dateforcircle = time.mktime(time.strptime(self.DATA, '%Y-%m-%d'))
            endcircle = '2030-12-30'
            endcircle = time.mktime(time.strptime(endcircle, '%Y-%m-%d'))

            while dateforcircle < endcircle:
                dateforcircle = time.localtime(dateforcircle)
                if dateforcircle.tm_wday == 5:
                    dateforcircle = time.mktime(dateforcircle)
                    dateforcircle += 2 * 24 * 60 * 60
                    dateforcircle = time.localtime(dateforcircle)
                if dateforcircle.tm_wday == 6:
                    dateforcircle = time.mktime(dateforcircle)
                    dateforcircle += 24 * 60 * 60
                    dateforcircle = time.localtime(dateforcircle)
                dateforcircle = time.strftime('%Y-%m-%d', dateforcircle)
                self.shedput(dateforcircle)
                dateforcircle = time.strptime(dateforcircle, '%Y-%m-%d')
                dateforcircle = time.mktime(dateforcircle)
                dateforcircle += 24 * 60 * 60
            self.DataBase.ShedulInput(self.allin)

        if self.shedultipe == 5:
            dateforcircle = time.mktime(time.strptime(self.DATA, '%Y-%m-%d'))
            endcircle = '2030-12-30'
            endcircle = time.mktime(time.strptime(endcircle, '%Y-%m-%d'))
            while dateforcircle < endcircle:
                dateforcircle = time.localtime(dateforcircle)
                if dateforcircle.tm_wday != 6 and dateforcircle.tm_wday != 5:
                    day = dateforcircle.tm_wday
                    dateforcircle = time.mktime(dateforcircle)
                    dateforcircle += (5-day) * 24 * 60 * 60
                    dateforcircle = time.localtime(dateforcircle)
                dateforcircle = time.strftime('%Y-%m-%d', dateforcircle)
                self.shedput(dateforcircle)
                dateforcircle = time.strptime(dateforcircle, '%Y-%m-%d')
                dateforcircle = time.mktime(dateforcircle)
                dateforcircle += 24 * 60 * 60
            self.DataBase.ShedulInput(self.allin)

        if self.shedultipe == 6:
            self.neededchange = []
            dateforcircle = time.time()
            dit = time.gmtime(dateforcircle)
            timeonday = (self.timetowork/((self.std.tm_year-dit.tm_year-1)*365 + (self.std.tm_yday-dit.tm_yday+365)*60*60))*60*60
            dfc = time.mktime(time.strptime(self.DATA, '%Y-%m-%d'))
            tnd = 0
            while dateforcircle < dfc and self.timetowork > 0:
                flag = True
                lunchBreak = True

                oldtime = self.starttime
                oldtime = time.strptime('2000-' + oldtime, '%Y-%H:%M')
                oldtime = time.mktime(oldtime)
                dateforcircle = time.localtime(dateforcircle)
                dateforcircle = time.strftime('%Y-%m-%d', dateforcircle)
                data = (self.id, dateforcircle)
                shed = self.DataBase.GetShedul(data)
                tnd += timeonday
                for i in shed:
                    flag = False
                    tmstrt = str(i.get('StartIvent'))
                    if len(tmstrt) == 7:
                        tmstrt = tmstrt[:4]
                    else:
                        tmstrt = tmstrt[:5]
                    tmend = str(i.get('EndIvent'))
                    if len(tmend) == 7:
                        tmend = tmend[:4]
                    else:
                        tmend = tmend[:5]
                    tmrt = time.strptime('2000-' + tmstrt, '%Y-%H:%M')
                    tmrt = time.mktime(tmrt)
                    tend = time.strptime('2000-' + tmend, '%Y-%H:%M')
                    tend = time.mktime(tend)
                    delta = tmrt - oldtime
                    if delta > (60*60):
                        tnd -= delta
                        if tnd < 0:
                            oldtime -= tnd
                            tnd = 0
                        if tmstrt > '12:00' and lunchBreak:
                            lunchBreak = False
                            oldtime = time.localtime(oldtime + 60*60)
                        else:
                            oldtime = time.localtime(oldtime)
                        oldtime = time.strftime('%H:%M', oldtime)
                        self.timetowork -= self.inpt(dateforcircle, oldtime, tmstrt)
                    oldtime = tend
                    if tnd == 0:
                        break


                if flag and tnd > 0:
                    delta = 4*60*60
                    n = tnd
                    if tnd > delta:
                        tnd -= self.inpt(dateforcircle, self.starttime, '12:00')
                        if tnd > 0:
                            tnd -= self.inpt(dateforcircle, '13:00', '18:00')
                            if tnd > 0:
                                tnd -= self.inpt(dateforcircle, '19:00', self.endtime)
                    elif tnd > 20*60:
                        k = time.strptime('2000-' + self.starttime, '%Y-%H:%M')
                        k = time.mktime(k)
                        k += tnd
                        k = time.localtime(k)
                        k = time.strftime('%H:%M', k)
                        tnd -= self.inpt(dateforcircle, self.starttime, k)
                    self.timetowork += tnd - n

                self.starttime = '8:00'
                dateforcircle = time.strptime(dateforcircle, '%Y-%m-%d')
                dateforcircle = time.mktime(dateforcircle)
                dateforcircle += 24*60*60
            #Перенос элементов по рангу

            if self.timetowork > 0:
                weight = 0
                for k in self.crit:
                    if k.get('idtypes') == self.worktype:
                        weight = k.get('weight')
                dateforcircle = time.time()
                dfc = time.mktime(time.strptime(self.DATA, '%Y-%m-%d'))

                while dateforcircle < dfc and self.timetowork > 0:
                    dateforcircle = time.localtime(dateforcircle)
                    dateforcircle = time.strftime('%Y-%m-%d', dateforcircle)
                    data = (self.id, dateforcircle)
                    shed = self.DataBase.GetShedul(data)
                    for i in shed:
                        if not i.get('movable'):
                            for k in self.crit:
                                if k.get('idtypes') == i.get('Type'):
                                    if weight > k.get('weight'):
                                        #Обработка обращения - удаление и запись нового события
                                        self.neededchange.append((i, dateforcircle))
                                        tmstrt = str(i.get('StartIvent'))
                                        if len(tmstrt) == 7:
                                            tmstrt = tmstrt[:4]
                                        else:
                                            tmstrt = tmstrt[:5]
                                        tmend = str(i.get('EndIvent'))
                                        if len(tmend) == 7:
                                            tmend = tmend[:4]
                                        else:
                                            tmend = tmend[:5]

                                        tmrt = time.strptime('2000-' + tmstrt, '%Y-%H:%M')
                                        tmrt = time.mktime(tmrt)
                                        tend = time.strptime('2000-' + tmend, '%Y-%H:%M')
                                        tend = time.mktime(tend)

                                        self.timetowork -= tend - tmrt
                        if self.timetowork < 0:
                            break

                    dateforcircle = time.strptime(dateforcircle, '%Y-%m-%d')
                    dateforcircle = time.mktime(dateforcircle)
                    dateforcircle += 24 * 60 * 60

            for i in self.neededchange:
                self.reinput(i[0], i[1])
            self.DataBase.ShedulInput(self.allin)
            self.newshedul()

class timer(QThread):
    output = pyqtSignal(str, int)
    def inicilize(self, timevalue=1, usetimer=0, circlenuber=0):
        self.value = timevalue * 60
        self.uses = usetimer
        self.circle = circlenuber

    def run(self):
        while True:
            if self.uses:

                QThread.sleep(self.value)
                self.output.emit('work', self.circle)
                if self.circle == 3:
                    self.circle = 0
                    QThread.sleep(int((self.value+300)/2))
                    self.output.emit('rest', self.circle)
                else:
                    QThread.sleep(int(self.value/5))
                    self.circle += 1
                    self.output.emit('rest', self.circle)
            else:
                QThread.sleep(int(self.value))
                self.output.emit('timepass', 0)

class newcritmess(QtWidgets.QDialog):
    list = pyqtSignal(str)
    def __init__(self, ID):
        super(newcritmess, self).__init__()
        self.ID = ID
        self.ui = newcrit.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged[str].connect(self.onChang)
        self.ui.buttonBox.accepted.connect(self.acceptin)

    def onChang(self, text):
        self.line = text

    def acceptin(self):
        self.list.emit(self.line)
        self.close()

#Сообщение об ошибке или предупреждение с единственной кнопкой ОК
class messagewindow(QtWidgets.QDialog):
    hash = pyqtSignal(int)
    def __init__(self, line):
        super(messagewindow, self).__init__()
        self.ui = message.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(line)
        self.ui.buttonBox.accepted.connect(self.ok)

    def ok(self):
        self.hash.emit(1)
        self.close()

#Окно настройки (Помидор, новое дело, перераспределение рангов)
class settingwindow(QtWidgets.QDialog):
    def __init__(self, ID):
        self.ID = ID
        super(settingwindow, self).__init__()
        self.DataBase = DB_working.DBwork()
        self.crit = self.DataBase.GetCrit(self.ID)

        self.ui = setting.Ui_Dialog()
        self.ui.setupUi(self)
        pom = self.DataBase.GetPomodoro(self.ID)
        self.ui.Timer.setProperty("value", pom[0].get('pomodoro'))
        self.ui.Timer.valueChanged.connect(self.changingValue)
        self.ui.Priority.clicked.connect(self.ChangingPriority)
        self.ui.NewWork.clicked.connect(self.NewPriority)

    def changingValue(self):
        data = [self.ui.Timer.value(), self.ID]
        self.DataBase.ChangingSetting(data)

    def ChangingPriority(self):
        names = []
        for i in (self.crit):
            names.append(i.get('name'))
        self.TEST = testing(names)
        self.TEST.show()
        self.TEST.criteriors[list, list].connect(self.critInput)

    def critInput(self, criteriors, line):
        data = []
        for i in range(len(line)):
            k = (line[i], self.ID, criteriors[i])
            data.append(k)
        self.DataBase.ChangingCriterior(data)

    def NewPriority(self):
        self.new = newcritmess(self.ID)
        self.new.show()
        self.new.list[str].connect(self.jin)

    def jin(self, listin):
        self.listin = listin
        names = []
        for i in (self.crit):
            names.append(i.get('name'))
        names.append(self.listin)
        self.TEST = testing(names)
        self.TEST.show()
        self.TEST.criteriors[list, list].connect(self.newcritInput)

    def newcritInput(self, criteriors, line):
        for i in range(len(line)):
            if criteriors[i] == self.listin:
                data = [(self.ID, criteriors[i], line[i])]
                self.DataBase.CritInput(data)
        self.critInput(criteriors, line)

class quotwindow(QtWidgets.QDialog):
    timing = pyqtSignal(int, bool)
    def __init__(self, flag):
        super(quotwindow, self).__init__()
        self.flag = flag
        self.ui = quot.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.tm)

    def tm(self):
        if self.flag:
            self.flag = False
        else:
            self.flag = True
        self.timing.emit(time.clock(), self.flag)
        self.close()

class recordwindow(QtWidgets.QDialog):
    def __init__(self, ID, dates):
        super(recordwindow, self).__init__()
        self.DataBase = DB_working.DBwork()
        self.id = ID
        self.ui = record.Ui_Dialog()
        self.ui.setupUi(self)
        self.crit = self.DataBase.GetCrit(ID)

        for i in range(len(self.crit)):
            # Наполняем список.
            self.ui.WorkCheck.addItem(self.crit[i].get('name'))

        self.ui.PeriodCheck.addItem('Без повторения')
        self.ui.PeriodCheck.addItem('Раз в неделю')
        self.ui.PeriodCheck.addItem('Раз в 14 дней')
        self.ui.PeriodCheck.addItem('Раз в месяц')
        self.ui.PeriodCheck.addItem('Будние дни')
        self.ui.PeriodCheck.addItem('Выходные')


        for i in range(2010, 2100):
            # Наполняем список.
            self.ui.year.addItem('%d' % i)

        for i in range(1, 32):
            # Наполняем список.
            self.ui.date.addItem('%d' % i)

        self.ui.mounth.addItem('Январь')
        self.ui.mounth.addItem('Февраль')
        self.ui.mounth.addItem('Март')
        self.ui.mounth.addItem('Апрель')
        self.ui.mounth.addItem('Май')
        self.ui.mounth.addItem('Июнь')
        self.ui.mounth.addItem('Июль')
        self.ui.mounth.addItem('Август')
        self.ui.mounth.addItem('Сентябрь')
        self.ui.mounth.addItem('Октябрь')
        self.ui.mounth.addItem('Ноябрь')
        self.ui.mounth.addItem('Декабрь')

        self.ui.year.setCurrentIndex(dates[0] - 2010)
        self.ui.mounth.setCurrentIndex(dates[1]-1)
        self.ui.date.setCurrentIndex(dates[2]-1)


        #Данные для записи
        self.worktipe = self.crit[0].get('idtypes')
        self.period = 0

        self.shr = 7    #start hour
        self.smin = 0   #start min
        self.ehr = 7    #end hour
        self.emin = 30  #end min

        self.year = dates[0]
        self.mounth = dates[1]
        self.date = dates[2]
        self.descript = ''
        self.chan = False
        self.concent = False

        self.ui.movable.stateChanged.connect(self.changing)
        self.ui.Concentrate.stateChanged.connect(self.changing)

        self.ui.starthour.valueChanged.connect(self.changingValue)
        self.ui.startminute.valueChanged.connect(self.changingValue)
        self.ui.endhour.valueChanged.connect(self.changingValue)
        self.ui.endminute.valueChanged.connect(self.changingValue)

        self.ui.year.currentIndexChanged.connect(self.datachange)
        self.ui.mounth.currentIndexChanged.connect(self.datachange)
        self.ui.date.currentIndexChanged.connect(self.datachange)

        self.ui.PeriodCheck.currentIndexChanged.connect(self.changingValue)
        self.ui.WorkCheck.currentIndexChanged.connect(self.workinput)
        self.ui.buttonBox.accepted.connect(self.calculating)
        self.ui.buttonBox.rejected.connect(self.close)

    def workinput(self):
        sender = self.sender()
        for i in self.crit:
            if i.get('name') == sender.currentText():
                self.worktipe = i.get('idtypes')
                break

    def txt(self, line):
        self.descript = line

    def datachange(self):
        sender = self.sender()
        if sender == self.ui.year:
            self.year = sender.currentText()
        if sender == self.ui.mounth:
            self.mounth = sender.currentIndex()+1
        if sender == self.ui.date:
            self.date = sender.currentIndex()+1

    def changing(self):
        sender = self.sender()
        if sender == self.ui.movable:
            if self.chan:
                self.chan = False
            else:
                self.chan = True
        else:
            if self.concent:
                self.concent = False
            else:
                self.concent = True

    def calculating(self):
        if self.smin == 0:
            timestart = str(str(self.shr) + ':' + '00')
        else:
            timestart = str(str(self.shr) + ':' + str(self.smin))
        if self.emin == 0:
            timend = str(str(self.ehr) + ':' + '00')
        else:
            timend = str(str(self.ehr) + ':' + str(self.emin))
        self.descript = self.ui.WorkEdit.toPlainText()
        self.calculation = recalculating()
        self.calculation.init(self.id, self.worktipe, self.descript, self.period, self.year, self.mounth, self.date, self.concent, timestart, timend, self.chan)
        self.calculation.messag.connect(self.out)
        self.calculation.run()

    def out(self, line):
        mess = messagewindow(line)
        mess.show()

    def changingValue(self):
        sender = self.sender()
        if sender == self.ui.starthour:
            self.shr = sender.text()
        if sender == self.ui.startminute:
            self.smin = sender.text()
        if sender == self.ui.endhour:
            self.ehr = sender.text()
        if sender == self.ui.endminute:
            self.emin = sender.text()
        if sender == self.ui.PeriodCheck:
            self.period = sender.currentIndex()

class goalwindow(QtWidgets.QDialog):
    def __init__(self, ID, dates):
        super(goalwindow, self).__init__()
        self.DataBase = DB_working.DBwork()
        self.id = ID
        self.ui = goal.Ui_Dialog()
        self.ui.setupUi(self)
        self.crit = self.DataBase.GetCrit(ID)
        for i in range(len(self.crit)):
            # Наполняем список.
            self.ui.WorkTipe.addItem(self.crit[i].get('name'))

        for i in range(2010, 2100):
            # Наполняем список.
            self.ui.year.addItem('%d' % i)

        for i in range(1, 32):
            # Наполняем список.
            self.ui.data.addItem('%d' % i)

        self.ui.mounth.addItem('Январь')
        self.ui.mounth.addItem('Февраль')
        self.ui.mounth.addItem('Март')
        self.ui.mounth.addItem('Апрель')
        self.ui.mounth.addItem('Май')
        self.ui.mounth.addItem('Июнь')
        self.ui.mounth.addItem('Июль')
        self.ui.mounth.addItem('Август')
        self.ui.mounth.addItem('Сентябрь')
        self.ui.mounth.addItem('Октябрь')
        self.ui.mounth.addItem('Ноябрь')
        self.ui.mounth.addItem('Декабрь')

        self.ui.year.setCurrentIndex(dates[0] - 2010)
        self.ui.mounth.setCurrentIndex(dates[1])
        self.ui.data.setCurrentIndex(dates[2] - 1)

        self.year = dates[0]
        self.mounth = dates[1]
        self.date = dates[2]
        self.worktipe = self.crit[0].get('idtypes')
        self.concent = False
        self.worktime = '0,5'

        self.ui.year.currentIndexChanged.connect(self.datachange)
        self.ui.mounth.currentIndexChanged.connect(self.datachange)
        self.ui.data.currentIndexChanged.connect(self.datachange)
        self.ui.WorkLoad.valueChanged.connect(self.work)
        self.ui.WorkTipe.currentIndexChanged.connect(self.workinput)
        self.ui.Concentrate.stateChanged.connect(self.switch)
        self.ui.buttonBox.accepted.connect(self.calculating)
        self.ui.buttonBox.rejected.connect(self.close)

    def work(self):
        sender = self.sender()
        self.worktime = sender.text()

    def switch(self):
        if self.concent:
            self.concent = False
        else:
            self.concent = True

    def workinput(self):
        sender = self.sender()
        for i in range(len(self.crit)):
            if self.crit[i].get('name') == sender.currentText():
                self.worktipe = self.crit[i].get('idtypes')
                break

    def datachange(self):
        sender = self.sender()
        if sender == self.ui.year:
            self.year = sender.currentText()
        if sender == self.ui.mounth:
            self.mounth = sender.currentIndex() + 1
        if sender == self.ui.data:
            self.date = sender.currentIndex() + 1

    def calculating(self):
        self.descript = self.ui.WorkName.toPlainText()
        currenttime = time.time()
        DATA = str(str(self.year) + '-' + str(self.mounth) + '-' + str(self.date))
        goaltime = time.mktime(time.strptime(DATA, '%Y-%m-%d'))
        delta = (goaltime - currenttime) * (13/24)
        currenttime = time.strftime('%H:%M', time.localtime(currenttime))
        self.worktime = float(self.worktime.replace(',', '.'))
        hour = self.worktime*60*60
        if delta > hour:
            self.calculation = recalculating()
            self.calculation.init(self.id, self.worktipe, self.descript, 6, self.year, self.mounth, self.date,
                                  self.concent, timetowork=hour, starttime=currenttime)
            self.calculation.messag.connect(self.out)
            self.calculation.run()
        else:
            self.mesDialog = messagewindow("Данную задачу невозможно выполнить в указанный срок!\n")
            self.mesDialog.show()
    def out(self, line):
        mess = messagewindow(line)
        mess.show()

class testing(QtWidgets.QDialog):
    criteriors = pyqtSignal(list, list)

    def __init__(self, line):
        super(testing, self).__init__()
        self.ui = testi.Ui_Dialog()
        self.ui.setupUi(self)
        self.line = line
        self.library = []
        self.dust = []
        for i in range(len(self.line)):
            self.library.append(0)
            self.dust.append(i)
        self.j = 1
        self.minimum = []
        self.maximum = []
        self.work()

    def work(self):
        self.ui.LeftButton.setText(self.line[self.dust[0]])
        self.ui.RightButton.setText(self.line[self.dust[self.j]])
        self.ui.LeftButton.clicked.connect(self.react)
        self.ui.RightButton.clicked.connect(self.res)

    def react(self):
        self.minimum.append(self.dust[self.j])
        self.jek()

    def res(self):
        self.maximum.append(self.dust[self.j])
        self.jek()

    def jek(self):
        flag = False
        if self.j < (len(self.dust)-1):
            self.j += 1
            self.ui.RightButton.setText(self.line[self.dust[self.j]])
        else:
            self.library[self.dust[0]] += len(self.minimum)
            for i in self.maximum:
                self.library[i] += len(self.minimum)+1
            flag = True
            i = 0
            while i < (len(self.library)-1):
                N = i
                for j in range(len(self.library)-N-1):
                    if self.library[N] == self.library[j+N+1]:
                        if flag:
                            flag = False
                            self.dust.clear()
                            self.minimum.clear()
                            self.maximum.clear()
                            self.dust = [i, j+i+1]
                            i = len(self.library)-1
                        else:
                            self.dust.append(j+N+1)
                i += 1
            self.j = 1
            self.ui.LeftButton.setText(self.line[self.dust[0]])
            self.ui.RightButton.setText(self.line[self.dust[self.j]])

        if flag:
            self.criteriors.emit(self.line, self.library)
            self.close()

class logwindow(QtWidgets.QDialog):
    hash = pyqtSignal(str, str)

    def __init__(self):
        super(logwindow, self).__init__()
        self.ui = Login.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Login_2.clicked.connect(self.LogClick)
        self.ui.Registration.clicked.connect(self.RegClick)

    def LogClick(self):
        self.ui.Hash()
        self.otsend('Login')

    def RegClick(self):
        self.ui.Hash()
        self.otsend('Registration')

    def otsend(self, call):
        self.hash.emit(self.ui.hashline, call)
        self.close()

class mainwindow (QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.currentData = time.time()
        self.id = 0

        self.timethread = timer()
        # создадим объект для выполнения кода в другом потоке

        self.timethread.output.connect(self.circle)

        self.DataBase = DB_working.DBwork()
        self.timing = False
        self.delay = 0
        header = ['Время', 'Описание', 'Тип']
        self.ui.ShedulWidget.setHorizontalHeaderLabels(header)
        self.rows = 48
        self.colomns = 3
        self.ui.ShedulWidget.setRowCount(self.rows)
        self.ui.ShedulWidget.setColumnCount(self.colomns)
        self.ui.ShedulWidget.setColumnWidth(0, 50)
        self.ui.ShedulWidget.setColumnWidth(1, 230)
        self.ui.ShedulWidget.setColumnWidth(2, 100)
        self.ui.ShedulWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.times = []
        self.tm = time.strftime('%H:%M', time.localtime(self.currentData))

        for i in range(self.rows):
            if i % 2:
                out = QtWidgets.QTableWidgetItem(str(int(i / 20)) + str(int((i-1)/2) % 10) + ":30\n" + str(int((i + 1) / 20)) + str(int((i+1)/2) % 10) + ":00")
            else:
                self.times.append(str(int(i / 20)) + str(int(i/2) % 10) + ":00")
                self.times.append(str(int(i / 20)) + str(int(i/2) % 10) + ":30")
                out = QtWidgets.QTableWidgetItem(str(int(i / 20)) + str(int(i/2) % 10) + ":00\n" + str(int(i / 20)) + str(int(i/2) % 10) + ":30")
            self.ui.ShedulWidget.setItem(i, 0, out)
            self.ui.ShedulWidget.setRowHeight(i, 50)

        self.ui.ShedulWidget.cellClicked.connect(self.shedit)

        self.ChangingTable()
        self.ui.GoalB.clicked.connect(self.GoalClick)
        self.ui.RecordB.clicked.connect(self.RecordClick)
        self.ui.SettingB.clicked.connect(self.SettingClick)

        self.ui.deleteButton.clicked.connect(self.DeleteClick)


        self.ui.CalendarWidget.clicked.connect(self.ChangingTable)


    def shedit(self, row, colomn):
        self.des = self.ui.ShedulWidget.item(row, 1)

    def starttimer(self, circle):
        self.currentData = time.time()
        self.tm = time.strftime('%H:%M', time.localtime(self.currentData))
        date = time.strftime('%Y-%m-%d', time.localtime(self.currentData))

        userdata = (self.id, date)
        carrentShedul = self.DataBase.GetShedul(userdata)
        concent = True
        flag = True

        tie = time.localtime(self.currentData)
        delta = 0
        delay = 10
        for i in carrentShedul:
            SI = str(i.get('StartIvent'))
            if len(SI) == 7:
                SI = '0' + SI[:4]
            else:
                SI = SI[:5]
            EI = str(i.get('EndIvent'))
            if len(EI) == 7:
                EI = '0' + EI[:4]
            else:
                EI = EI[:5]

            if self.tm >= SI and self.tm <= EI:
                if i.get('concentration'):
                    concent = False
                    minus = time.strptime(EI, '%H:%M')
                    delta = (minus.tm_hour - tie.tm_hour)*60 + (minus.tm_min - tie.tm_min)

                elif flag:
                    flag = False
                    #minus = time.strptime(EI, '%H:%M')
                    delay = 5#(minus.tm_hour - tie.tm_hour)*60 + (minus.tm_min - tie.tm_min)


        if concent:
            self.timethread.inicilize(delay, 0, 0)
        else:
            pmr = self.DataBase.GetPomodoro(self.id)
            if delta < pmr[0].get('pomodoro'):
                if delta > 15:
                    pomidor = delta
                else:
                    pomidor = 15
            else:
                pomidor = pmr[0].get('pomodoro')
            self.timethread.inicilize(pomidor, 1, circle)
            mes = messagewindow('Запущен таймер работы')
            mes.show()


    def pomidorChange(self, chang):
        pom = self.DataBase.GetPomodoro(self.id)
        kin = pom[0].get('pomodoro')
        kin += chang
        data = (kin, self.id)
        self.DataBase.ChangingSetting(data)

    def circle(self, type, count):
        pom = self.DataBase.GetPomodoro(self.id)
        if type == 'work':
            self.rest = restwindow(pom[0].get('pomodoro'))
            self.rest.show()
            self.rest.Pom.connect(self.pomidorChange)
        if type == 'rest':
            self.starttimer(count)
        if type == 'timepass':
            self.starttimer(0)

    def ChangingTable(self):

        for i in range(self.rows):
            self.ui.ShedulWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(''))
            self.ui.ShedulWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(''))
            if self.tm >= (str(int(i / 20)) + str(int(i/2) % 10) + ":00"):
                self.ui.ShedulWidget.setCurrentCell(i, 1)

        dtuple = QDate.getDate(self.ui.CalendarWidget.selectedDate())

        datastring = str(str(dtuple[0]) + '-' + str(dtuple[1]) + '-' + str(dtuple[2]))
        self.crit = self.DataBase.GetCrit(self.id)

        data = (self.id, datastring)
        geted = self.DataBase.GetShedul(data)
        for i in geted:
            SI = str(i.get('StartIvent'))
            if len(SI) == 7:
                SI = '0' + SI[:4]
            else:
                SI = SI[:5]
            EI = str(i.get('EndIvent'))
            if len(EI) == 7:
                EI = '0' + EI[:4]
            else:
                EI = EI[:5]

            desc = i.get('Description')
            typ = i.get('Type')
            s = 0
            for k in self.times:
                if k >= SI and k < EI:
                    self.insertintable(s, desc, typ)
                s += 1

    def insertintable(self, set, description, type):
        Str = ''
        for k in self.crit:
            if k.get('idtypes') == type:
                Str = k.get('name')

        self.ui.ShedulWidget.setItem(set, 1, QtWidgets.QTableWidgetItem(description))
        self.ui.ShedulWidget.setItem(set, 2, QtWidgets.QTableWidgetItem(Str))

    def GoalClick(self):
        self.GoalDialog = goalwindow(self.id, QDate.getDate(self.ui.CalendarWidget.selectedDate()))
        self.GoalDialog.show()

    def RecordClick(self):
        self.RecordDialog = recordwindow(self.id, QDate.getDate(self.ui.CalendarWidget.selectedDate()))
        self.RecordDialog.show()

    def SettingClick(self):
        self.SetingDialog = settingwindow(self.id)
        self.SetingDialog.show()

    def login(self):
        self.loginDialog = logwindow()
        self.loginDialog.show()
        self.loginDialog.hash[str, str].connect(self.check)

    def check(self, hashline, info):
        self.DataBase = DB_working.DBwork()
        proof = self.DataBase.identity(hashline)
        if proof and info == 'Login':
            self.id = self.DataBase.getID(hashline)
            self.show()

            self.ChangingTable()
            self.starttimer(0)
            self.timethread.start()
        elif not proof and info == 'Registration':
            self.DataBase.id_input(hashline)
            self.id = self.DataBase.getID(hashline)
            criteriors = ['Работа', 'Учеба', 'Здоровье', 'Отдых', 'Саморазвитие', 'Работа по дому']
            self.TEST = testing(criteriors)
            self.TEST.show()
            self.TEST.criteriors[list, list].connect(self.critInput)
            self.starttimer(0)
            self.timethread.start()

        elif info == 'Login':
            win.err('Неверное имя пользователя или пароль')

        else:
            win.err('Пользователь с таким именем уже существует')

    def critInput(self, criteriors, line):
        data = []
        for i in range(len(line)):
            k = (self.id, criteriors[i], line[i])
            data.append(k)
        self.DataBase.CritInput(data)
        self.DataBase.pomodoroinput(self.id)
        self.show()

    def err(self, line):
        self.mesDialog = messagewindow(line)
        self.mesDialog.show()
        self.mesDialog.hash[int].connect(self.login)

    def DeleteClick(self):
        self.mesDialog = messagewindow('Удалить запись?')
        self.mesDialog.show()
        self.mesDialog.hash[int].connect(self.deleting)

    def deleting(self):
        dat = (self.id, self.des.text())
        self.DataBase.Deleting(dat)

app = QtWidgets.QApplication([])
win = mainwindow()
win.login()
sys.exit(app.exec())