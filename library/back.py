import mysql.connector

host = "localhost"
user = "root"
password = "Iam@mysql123"


def get_connection():
    global host, user, password
    return mysql.connector.connect(host=host, user=user, passwd=password, port=3306)


def data():
    a = get_connection()
    b = a.cursor()
    b.execute("create database if not exists barry")
    b.execute("use barry")
    b.execute(
        "create table if not exists iris (ID BIGINT PRIMARY KEY, Book_name varchar(25), student_name varchar(25), student_class varchar(25), amount int )")
    b.execute("commit")
    b.close()


def add(ID, Book_name, student_name, student_class, amount):
    a = get_connection()
    b = a.cursor()
    b.execute("create database if not exists barry")
    b.execute("use barry")
    b.execute(
        "create table if not exists iris (ID BIGINT PRIMARY KEY, Book_name varchar(25), student_name varchar(25), student_class varchar(25), amount int )")
    b.execute("insert into iris values(%s,%s,%s,%s,%s)", (ID, Book_name, student_name, student_class, amount))
    b.execute("commit")
    b.close()


def display(student_name=""):
    print('in back disp', student_name)
    a = get_connection()
    print('type of a', type(a))
    b = a.cursor()
    print('a.cursor', b)
    b.execute("create database if not exists barry")
    b.execute("use barry")
    b.execute(
        "create table if not exists iris (ID BIGINT PRIMARY KEY, Book_name varchar(25), student_name varchar(25), student_class varchar(25), amount int )")
    b.execute("select * from iris where student_name = '" + student_name + "';")
    print('printing data', b)
    res = b.fetchone()
    for v in res:
        print(v)
    b.close()
    return res
