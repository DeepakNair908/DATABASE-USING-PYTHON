import sqlite3
conn=sqlite3.connect('MOVIES.db')
c=conn.cursor()

##### THE TABLE CREATION ########



#c.execute("""CREATE TABLE MOVIES (
 #           NAME text,
  #          ACTOR text,
   #         YEAR integer,
    #        DIRECTOR NAME text
     #      )""")

     
##### INSERTION INTO TABLE ######


     
#c.execute("INSERT INTO MOVIES VALUES('PULP FICTION','John Travolta',1994,'Quentin Tarantino')")
#c.execute("INSERT INTO MOVIES VALUES('Fight Club','Brad Pitt',1999,'David Fincher')")
#c.execute("INSERT INTO MOVIES VALUES('The Dark Knight','Christian Bale',2008,'Christopher Nolan')")


##### EXECUTING COMMANDS #######

     
c.execute("select * from MOVIES ")

print(c.fetchall())

c.execute("select * from MOVIES WHERE  ACTOR = 'Brad Pitt'")

print(c.fetchall())

conn.commit()

conn.close()

