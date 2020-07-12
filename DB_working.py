import pymysql
import conect #Отдельный файл с подключением базы
import Loger

class DBwork():
#Открываем соединение с базой данных, да предыдущий импорт только для одной функции, а кто говорил, что будет легко?
    def __init__(self):
        self.connection = conect.getConnection()
        self.DBloger = Loger.loger("Database")

    #loger function
    def log(self, error, source):
        self.DBloger.error('Eror in ' + source + ' : ' + str(error))

    def GetShedul(self, data):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT StartIvent, EndIvent, Description, Type, movable, concentration FROM shedul WHERE (userID = %s AND Date = %s)"
            cursor.execute(sql, data)
            self.connection.commit()
            return cursor.fetchall()
        except Exception as error:
            self.log(error, 'GetShedul')

    def GetPomodoro(self, ID):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT pomodoro FROM setting WHERE userID = %s"
            cursor.execute(sql, ID)
            self.connection.commit()
            return cursor.fetchall()
        except Exception as error:
            self.log(error, 'GetPomodoro')

    def GetCrit(self, ID):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT idtypes, name, weight FROM types WHERE userID = %s"
            cursor.execute(sql, ID)
            self.connection.commit()
            return cursor.fetchall()
        except Exception as error:
            self.log(error, 'Get Criterior')

    def identity(self, line):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT idLogin FROM login WHERE Logins = %s"
            cursor.execute(sql, line)
            proof = cursor.fetchall()
            self.connection.commit()
            if (len(proof)!= 0):
                return True
            else:
                return False
        except Exception as error:
            self.log(error, 'Identity')
            return False

    def getID(self, line):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT idLogin FROM login WHERE Logins = %s"
            cursor.execute(sql, line)
            id = cursor.fetchall()
            self.connection.commit()
            return id[0].get('idLogin')
        except Exception as error:
            self.log(error, 'getID')
            return False

    def id_input(self, data):
        try:
            # Вносим данные в таблицу с данными магазина Лабиринт
            cursor = self.connection.cursor()
            data = (data)
            sql = "INSERT INTO login (Logins) VALUES (%s)"
            cursor.execute(sql, data)
            self.connection.commit()

        except Exception as error:
            self.log(error, 'id_input')

    def CritInput(self, data):
        try:
            # Вносим данные в таблицу с данными магазина Лабиринт
            cursor = self.connection.cursor()
            sql = "INSERT INTO types (userid, name, weight) VALUES (%s, %s, %s)"
            cursor.executemany(sql, data)
            self.connection.commit()

        except Exception as error:
            self.log(error, 'Criterior Input')

    def pomodoroinput(self, id):
        try:
            # Вносим данные в таблицу с данными магазина Лабиринт
            cursor = self.connection.cursor()

            pomodoro = [id, 25]
            sql = "INSERT INTO setting(userID, pomodoro) VALUES (%s, %s)"
            cursor.execute(sql, pomodoro)
            self.connection.commit()

        except Exception as error:
            self.log(error, 'Pomodoro Input')

    def ShedulInput(self, data):

        try:
            # Вносим данные в таблицу с данными магазина Лабиринт
            cursor = self.connection.cursor()
            sql = "INSERT INTO shedul (userID, Date, StartIvent, EndIvent, Description, Type, movable, concentration) "\
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.executemany(sql, data)
            self.connection.commit()

        except Exception as error:
            self.log(error, 'Shedul Input')

    def DeleteShedul(self, data):

        try:
            # Вносим данные в таблицу с данными магазина Лабиринт
            cursor = self.connection.cursor()
            sql = "DELETE FROM shedul where (UserId = %s and Date = %s and StartIvent = %s)"
            cursor.execute(sql, data)
            self.connection.commit()

        except Exception as error:
            self.log(error, 'Delete Shedul')

    def Deleting(self, data):

        try:
            # Вносим данные в таблицу с данными магазина Лабиринт
            cursor = self.connection.cursor()
            sql = "DELETE FROM shedul where (UserId = %s and Description = %s)"
            cursor.execute(sql, data)
            self.connection.commit()

        except Exception as error:
            self.log(error, 'Deleting')

    def ChangingSetting(self, data):
        try:
            # Вносим данные в таблицу с данными магазина Лабиринт
            cursor = self.connection.cursor()
            sql = "UPDATE setting SET pomodoro = %s WHERE userID = %s"
            cursor.execute(sql, data)
            self.connection.commit()

        except Exception as error:
            self.log(error, 'Changing Setting')

    def ChangingCriterior (self, data):
        try:
            # Вносим данные в таблицу с данными магазина Лабиринт
            cursor = self.connection.cursor()
            sql = "UPDATE types SET weight = %s WHERE (userid = %s and name = %s)"
            cursor.executemany(sql, data)
            self.connection.commit()

        except Exception as error:
            self.log(error, 'Changing Criteriors')
    #Close the console database
    def ConClose(self):
        # Закрываем соединение с базой данных
        self.connection.close()
