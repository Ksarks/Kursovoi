import pymysql.cursors  
 
# Функция возвращает connection.
def getConnection():
     
    # Вы можете изменить параметры соединения.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Takeshi',
                                 db='shedul',
                                 port=3306,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
