cred = ['root', '']
import mysql.connector
from subprocess import Popen, PIPE

def get_databases():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    databases = mycursor.fetchall()
    return databases

def shell(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).stdout.read().decode('utf-8')
    return p

for i in get_databases():
    if i[0] == 'information_schema' or i[0] == 'mysql' or i[0] == 'performance_schema' or i[0] == 'sys':
        pass
    else:
        print(i[0])
        shell('mysqldump -u '+cred[0]+' -p"'+cred[1]+'" --databases ' + i[0] + ' > ' + i[0] + '.sql')


