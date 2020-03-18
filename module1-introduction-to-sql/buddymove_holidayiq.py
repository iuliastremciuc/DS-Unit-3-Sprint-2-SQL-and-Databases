import pandas
import psycopg2
df = pandas.read_csv('buddymove_holidayiq.csv')
print(df.head())
print(df.shape)
con = psycopg2.connect('buddymove_holidayiq.csv')
cur = con.cursor()
#('buddymove_holidayiq', con=psycopg2.Connection)
cur.execute('SELECT * FROM buddymove_holidayiq').fetchall()
print('CONN ', con)