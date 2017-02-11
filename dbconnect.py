import pymysql

def connection():
	conn=pymysql.connect(host="localhost",user="root",passwd="dusty",db="projdb")
	c=conn.cursor()
	return c,conn
