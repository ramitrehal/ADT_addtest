# import pyodbc 
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=server_name;'
#                       'Database=database_name;'
#                       'Trusted_Connection=yes;')
import cx_Oracle as oc

# dsn_tns = cx_Oracle.makedsn('qdciad1126.qdx.com', '1535', service_name='IDAATSTQ')
#  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.

# conn = cx_Oracle.connect(user=r'tst02idaauser', password=r'tst03user', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

# c = conn.cursor()
# c.execute('select * from idaa_specimen_stability where work_code="899"')

# #print (row[0], '-', row[1])

conn = oc.connect("tst02idaauser/idaauser2008@qdciad1126.qdx.com:1535/IDAATSTQ")

c = conn.cursor()
b = conn.cursor()
a = conn.cursor()
rt= 'select rt from idaa_specimen_stability where work_code in (6399,899)'
rf= 'select rf from idaa_specimen_stability where work_code in (6399,899)'
fz= 'select fz from idaa_specimen_stability where work_code in (6399,899)'
c.execute(rt)
b.execute(rf)
a.execute(fz)
res = c.fetchall()
rez = b.fetchall()
red = a.fetchall()
# for line in c:
#     print(line)
print(res)
print(rez)
print(red)

# c.close()
# conn.close()