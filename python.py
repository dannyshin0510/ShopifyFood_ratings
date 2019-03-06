import mysql.connector

mydb= mysql.connector.connect(host="localhost", user="root", passwd="Flower3212!", database="amazonfoods")

cursor=mydb.cursor()
cursor.execute("SELECT key_benefits FROM apps WHERE Rating>=4")
result=cursor.fetchall()
x=0
match1=0
word="cloud"
for rows in result:
	if(str(result[x]).find(word)!= -1):
		match1+=1
	x+=1
print(match1)

cursor.execute("SELECT key_benefits FROM apps WHERE Rating<=4")
result=cursor.fetchall()
y=0
match2=0
word="cloud"
for rows in result:
	if(str(result[y]).find(word)!= -1):
		match2+=1
	y+=1
print(match2)

if(match2==0):
	print("100 percent good")
else:
	share=match1/(match1+match2)
	print (share)
