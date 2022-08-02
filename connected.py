'''
All code was assembled by myself, Samuel Sidzyik.
I pulled bits and pieces from various sources but this code is my own.

Establishes connection to Pet Database on Azure server
Framework for the connection pulled from Microsoft Azure's help file:
https://docs.microsoft.com/en-us/azure/postgresql/single-server/connect-python
example on bottom of what they supplied

other resources
https://www.postgresql.org/docs/current/datatype-binary.html
https://stackoverflow.com/questions/9293900/how-to-increment-integer-columns-value-by-1-in-sql
https://stackoverflow.com/questions/18345825/typeerror-int-object-does-not-support-indexing
https://stackoverflow.com/questions/6053897/how-to-assign-an-sql-value-to-this-python-variable#:~:text=My%20code%20for%20assigning%20the%20value%20of%20the,for%20adding%20data%20to%20the%20database%20on%20closure
https://www.geeksforgeeks.org/postgresql-create-sequence/#:~:text=To%20get%20the%20next%20value%20from%20the%20sequence,nexval%20%28%29%20function%20we%20get%20the%20incremented%20value.
https://www.programiz.com/python-programming/methods/built-in/memoryview#:~:text=The%20memoryview%20%28%29%20function%20returns%20a%20memory%20view,data%20is%20a%20memory%20array%20or%20a%20buffer.

'''
import psycopg2
import dotenv
import os
import random
import hashlib as hash

# Database Information
dotenv.load_dotenv(dotenv.find_dotenv())
host = "pmisev1.postgres.database.azure.com"
dbname = "PetFinal"
user = "owner"
password = os.getenv('database')
sslmode = "require"
# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)

#Data used (works but didn't finish adding to database)
breedsdict = {  'Mixed Breed under 15 lbs.':{'size':'XS','lifespan':15},
                'Mixed Breed under 30 lbs.':{'size':'S','lifespan':13},
                'Mixed Breed under 65 lbs.':{'size':'M','lifespan':11},
                'Mixed Breed under 110 lbs.':{'size':'L','lifespan':9},
                'Mixed Breed over 110 lbs.':{'size':'XL','lifespan':7},
                'Lab':{'size':'L','lifespan':11},
                'Shepherd':{'size':'M','lifespan':9},
                'Yippie':{'size':'XS','lifespan':15},
                'Monster':{'size':'XL','lifespan':7}}

#Data used (works but didn't finish adding to database)
claimdict = {   'XS':110,
                'S':125,
                'M':140,
                'L':180,
                'XL':210
}

#Clears database and recreates public schema (done)
def clearall():
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()
    
    #Create sequencing for policy number
    cursor.execute("DROP SCHEMA PUBLIC CASCADE")
    cursor.execute("CREATE SCHEMA PUBLIC")
    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Creates a sequencing rule for policy numbers (done)
def sequencecreate():
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()
    
    #Create sequencing for policy number
    cursor.execute("CREATE SEQUENCE policy_seq INCREMENT 2 START 10000;")

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Create Tables for database (done)
def tablescreate():
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()
    
    #Create sequencing for policy number
    cursor.execute("create table Address(address_id serial,country varchar(3),state varchar(2),city varchar(20),zip integer,address1 varchar,address2 varchar,address3 varchar, primary key(address_id));")
    cursor.execute("create table Size(breed_size varchar(3) unique,value_modifier float);")
    cursor.execute("create table Login(username varchar(30),account_type varchar(10),password bytea,salt bytea,primary key(username));")
    cursor.execute("create table Agent(agent_id serial,agent_name varchar(50) not null,address_id serial,username varchar(30),primary key(agent_id),foreign key(address_id) references Address(address_id),foreign key(username) references Login(username));")
    cursor.execute("create table Policy(policy_no serial, agent_id serial,primary key(policy_no),foreign key(agent_id) references Agent(agent_id));")
    cursor.execute("create table Customer(customer_id serial,policy_no serial,owner_fname varchar(20) not null,owner_lname varchar(25) not null,address_id serial,username varchar(30),primary key(customer_id),foreign key(policy_no) references Policy(policy_no),foreign key(username) references Login(username),foreign key(address_id) references Address(address_id));")
    cursor.execute("create table Breeds(breed_id serial,breed_name varchar(34) unique,breed_lifespan integer,breed_size varchar(3),primary key(breed_id),foreign key(breed_size) references Size(breed_size));")
    cursor.execute("create table Pets(pet_id serial,policy_no serial not null,pet_name varchar(50) not null,pet_age integer not null,pet_issue_age integer,breed_name varchar,pet_alive boolean,primary key(pet_id),foreign key(policy_no) references Policy(policy_no),foreign key(breed_name) references Breeds(breed_name));")

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Creates minimum data needed to use query database and add to tables (done)
def dataset():
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()
    pasw = b'\xb5\xaa\xe7\xa1x\x10/#\xa4\xfbu\x9e5n\x8a\x14\x9f)p\x1fJP8\x8fK\x1e\x16\xfe)\xd1\xc8\xd4'
    salt = b' z\xaa\xa1\x035\xea\x04\xc1W\xd2\xd2\x9e\xf6>\xcb\xf2\xc1\x0f\xd7\xf9D\xac\x10\x87\xa9@\xe3\x16\x83\xb1\xa5!V!\x81i\xd3\xd1^\x12\x0c\xe0\xa8\xd21\xe9r\x9cbbH\xb2\x82\xe7b\x19\xed\xbd\xc1\xd1\xed\x97P'
    #Create sequencing for policy number
    cursor.execute("INSERT INTO address (address_id) VALUES (0)")
    cursor.execute("INSERT INTO Login (username,account_type,password,salt) VALUES ('user1','Customer',%s,%s)",(pasw,salt))
    cursor.execute("INSERT INTO Login (username,account_type,password,salt) VALUES ('agent1','Agent',%s,%s)",(pasw,salt))
    cursor.execute("INSERT INTO Login (username,account_type,password,salt) VALUES ('actuary1','Actuary',%s,%s)",(pasw,salt))
    for i in range(6):
        cursor.execute("INSERT INTO agent (agent_id,agent_name,address_id) VALUES ({},'James',0)".format(i))
    cursor.execute("INSERT INTO Policy (policy_no,agent_id) VALUES (nextval('policy_seq'),0);")
    cursor.execute("INSERT INTO Size (breed_size,value_modifier) values ('XS' ,110);")
    cursor.execute("INSERT INTO Size (breed_size,value_modifier) values ('S' ,125);")
    cursor.execute("INSERT INTO Size (breed_size,value_modifier) values ('M' ,140);")
    cursor.execute("INSERT INTO Size (breed_size,value_modifier) values ('L' ,180);")
    cursor.execute("INSERT INTO Size (breed_size,value_modifier) values ('XL' ,210);")
    cursor.execute("INSERT INTO Breeds (breed_name,breed_lifespan,breed_size) VALUES ('Mixed Breed under 15 lbs.',15,'XS');")
    cursor.execute("INSERT INTO Breeds (breed_name,breed_lifespan,breed_size) VALUES ('Mixed Breed under 30 lbs.',13,'S');")
    cursor.execute("INSERT INTO Breeds (breed_name,breed_lifespan,breed_size) VALUES ('Mixed Breed under 65 lbs.',11,'M');")
    cursor.execute("INSERT INTO Breeds (breed_name,breed_lifespan,breed_size) VALUES ('Mixed Breed under 110 lbs.',9,'L');")
    cursor.execute("INSERT INTO Breeds (breed_name,breed_lifespan,breed_size) VALUES ('Mixed Breed over 110 lbs.',7,'XL');")
    cursor.execute("UPDATE Agent Set username = 'agent1' where agent_id = 3")
    cursor.execute("UPDATE Agent Set username = 'actuary1' where agent_id = 4")
    
    
    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Creates 50 customer complete with address, policy and 2-3 pets each (done)
def population():
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()
    for i in range(50):
        city = random.choice(['Omaha','Lincoln','Grand Island','Bellevue','Ralston'])
        zip = random.randrange(61000,69000)
        add1 = str(random.randrange(10,11000)) + " " + random.choice(['Maple','Ipe','Oak','Pine','Cotton','Hawthorn','Cherry']) + " " + random.choice(['St.','Blvd','Ave.','Rd.','Cir.'])
        add2 = ''
        if random.randrange(1,10) == 5:
            add2 = random.choice(['Apt. 3A','Apt. 4d','Unit 11','PO Box 1123'])
        add3 = ''
        cursor.execute("INSERT INTO Address (country, state, city, zip, address1, address2, address3) VALUES (%s,%s,%s,%s,%s,%s,%s);", ("US","NE",city,zip,add1,add2,add3))
        cursor.execute('select max(address_id) from Address')
        add_id = cursor.fetchone()
        cursor.execute("select nextval('policy_seq');")
        policyno = cursor.fetchone()
        agent = random.choice([0,1,2,3,4,5])
        cursor.execute("INSERT INTO Policy (policy_no,agent_id) VALUES (%s,%s);",(policyno[0],agent))
        fname = random.choice(['Jesse','James','Ash','Brock','Misty','Dawn','Giovanni','Red','Gary','Bill'])
        lname = random.choice(['Mime','Izard','Laxx','Tini','Onyx','Bliss','Pincer','Alam','Muetoo'])
        cursor.execute("INSERT INTO Customer (policy_no, owner_fname, owner_lname, address_id) VALUES (%s,%s,%s,%s);",(policyno[0],fname,lname,add_id[0]))
        dognames = ['Stax','Pringle','Twizzler','Crush','Hershey','Twix','Crunch','Fruit Loop','Skippy']
        for i in range(random.randrange(2,4)):
            dog_name = random.choice(dognames)
            dognames.remove(dog_name)
            dog_age = random.randrange(1,9)
            dog_breed = random.choice(['Mixed Breed under 15 lbs.','Mixed Breed under 30 lbs.','Mixed Breed under 65 lbs.','Mixed Breed under 110 lbs.','Mixed Breed over 110 lbs.'])
            cursor.execute("INSERT INTO Pets (policy_no,pet_name,pet_age,pet_issue_age,breed_name,pet_alive) VALUES (%s,%s,%s,%s,%s,%s);", (policyno,dog_name,dog_age,dog_age,dog_breed,True))
    cursor.execute("INSERT INTO Customer (policy_no, owner_fname, owner_lname, address_id, username) VALUES (10100,'Fred','Flintstone','20','user1')")
    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Query to return necessary data to create Customer object (done)
def customerdata(username):
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()
    cursor.execute("SELECT policy_no,owner_fname,owner_lname FROM Customer where username = '{}';".format(username))
    temp = cursor.fetchone()
    policy = temp[0]
    fname = temp[1]
    lname = temp[2]
    dogs = []
    #Queries to Database
    cursor.execute("SELECT * FROM Pets where policy_no = {} and pet_alive = True".format(policy))
    dogs = cursor.fetchall()
    dognames = []
    premium = 0
    for i in dogs:
        dognames.append(i[2])
        lifespan = breedsdict[i[5]]['lifespan']
        lifeleft = lifespan - i[3]
        quote = claimdict[breedsdict[i[5]]['size']]/lifeleft
        premium += round(quote,2)
            
    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()
    return fname,lname,dognames,premium,policy

#Query to return necessary data to create Agent object (done)
def agentdata(username):
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    cursor.execute("SELECT agent_name,agent_id FROM Agent where username = '{}';".format(username))
    temp = cursor.fetchone()
    name = temp[0]
    aid = temp[1]

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()
    return name,aid

#Query to return necessary data to create Actuary object (done)
def actuarydata(username):
    name = 'Scotty'
    return name

#Query to return list of existing usernames (done)
def users():
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    cursor.execute("SELECT username from login ;")
    usernames = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return usernames

#Query to check entered password against what is in the login table (done)
def checkpass(username,password):
    user = [False,'pass']
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    cursor.execute("SELECT username from login ;")
    usernames = cursor.fetchall()
    if str(username) in str(usernames):

        cursor.execute("SELECT * from login where username = %s",(username,))
        user = cursor.fetchone()
        securepass = hash.pbkdf2_hmac('sha256',password.encode('utf-8'),bytes(user[3]),20000)
        if securepass != bytes(user[2]):
            user = [False,'pass']
    else:
        user = [False,'pass']
    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()
    return user[0],user[1]
    
#Query to create a policy given data provided by program (done)
def createpol(fname,lname,add1,add2,add3,city,state,zip,dog_name,dog_breed,dog_age,agent,user,pass1,salt):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()
    #Queries to Database
    cursor.execute("INSERT INTO Address (country, state, city, zip, address1, address2, address3) VALUES (%s,%s,%s,%s,%s,%s,%s);", ("US",state,city,zip,add1,add2,add3))
    cursor.execute('select max(address_id) from Address')
    add_id = cursor.fetchone()
    if user != "pass":
        cursor.execute("INSERT INTO Login (username,account_type, password, salt) VALUES (%s,'Customer',%s,%s);", (user,pass1,salt))
    cursor.execute("select nextval('policy_seq');")
    policyno = cursor.fetchone()
    cursor.execute("INSERT INTO Policy (policy_no,agent_id) VALUES (%s,%s);",(policyno[0],agent))
    cursor.execute("INSERT INTO Customer (policy_no, owner_fname, owner_lname, address_id, username) VALUES (%s,%s,%s,%s,%s);",(policyno[0],fname,lname,add_id[0],user))
    if dog_name != "pass":
        cursor.execute("INSERT INTO Pets (policy_no,pet_name,pet_age,pet_issue_age,breed_name,pet_alive) VALUES (%s,%s,%s,%s,%s,%s);", (policyno,dog_name,dog_age,dog_age,dog_breed,True))
    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Query to add dog to an existing policy (done)
def adddoggo(policy,dog_name,dog_breed,dog_age):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    cursor.execute("INSERT INTO Pets (policy_no,pet_name,pet_age,pet_issue_age,breed_name,pet_alive) VALUES (%s,%s,%s,%s,%s,%s);", (policy,dog_name,dog_age,dog_age,dog_breed,True))

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Removes dog from pet table (done)
def removedoggo(policyno, dogname):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    cursor.execute("DELETE from Pets where policy_no = %s and pet_name = %s;", (policyno,dogname))

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Unalives dog (done)
def claimdoggo(policyno, dogname):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    cursor.execute("UPDATE Pets SET pet_alive = False where policy_no = %s and pet_name = %s;", (policyno, dogname))

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

#Validates if policy number exists (done)
def polquery(policyno):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    cursor.execute("SELECT policy_no from Policy where policy_no = {};".format(int(policyno)))
    test = cursor.fetchone()
    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

    if policyno == test[0]:
        return True
    else:
        return False

#Returns list of dogs for a specific policy no (done)
def doglist(policyno):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    cursor.execute("SELECT pet_name from Pets where policy_no = %s ;",(policyno))
    list = cursor.fetchall()
    dogs = []
    for i in list:
        dogs.append(i[0])

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

    return dogs

#Returns list of policies attributed to an agent (done)
def querypollist(agentno):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    cursor.execute("SELECT policy_no from Policy where agent_id = {};".format(int(agentno)))
    list = cursor.fetchall()
    pols = []
    for i in list:
        pols.append(i[0])

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

    return pols

def getpremsquery(list):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    premium = 0
    for i in list:
        cursor.execute("SELECT breed_name, pet_issue_age from Pets where policy_no = {} and pet_alive = True;".format(int(i)))
        temp = cursor.fetchall()
        for j in temp:
            lifespan = breedsdict[j[0]]['lifespan']
            lifeleft = lifespan - j[1]
            if lifeleft < 1:
                pass
            else:
                quote = claimdict[breedsdict[j[0]]['size']]/lifeleft
                premium = premium+round(quote,2)

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

    return premium

def queryincome():
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    premium = 0
    cursor.execute("SELECT breed_name, pet_issue_age from Pets where pet_alive = True;")
    temp = cursor.fetchall()
    for j in temp:
        lifespan = breedsdict[j[0]]['lifespan']
        lifeleft = lifespan - j[1]
        if lifeleft < 1:
            pass
        else:
            quote = claimdict[breedsdict[j[0]]['size']]/lifeleft
            premium = premium+round(quote,2)

    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()

    return premium

#Ages all living dogs 1 year (done pending rainbow bridge)
def agedogs(years):
    #Connect to Database
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()

    #Queries to Database
    for i in range(years):
        cursor.execute("UPDATE Pets SET pet_age = pet_age + 1 where pet_alive = True;")
    bois = rainbowbridge(cursor)
    #Close connection to Database
    conn.commit()
    cursor.close()
    conn.close()
    return bois

#Takes the best doggos to a farm to play
def rainbowbridge(cursor):
    #Queries to Database
    cursor.execute("UPDATE Pets SET pet_alive = False FROM Breeds where Pets.Breed_name = Breeds.Breed_name and pets.pet_alive = True and pets.pet_age >= 6 + breeds.breed_lifespan;")
    cursor.execute("SELECT pet_id from Pets where pet_alive = False;")
    bois = cursor.fetchall()
    
    return len(bois)

#--- --- ---SQL statements--- --- ---
"""
create table Address(
    address_id serial,
    country varchar(3),
    state varchar(2),
    city varchar(20),
    zip integer,
    address1 varchar,
    address2 varchar,
    address3 varchar
    primary key(address_id)
);
create table Size(
    breed_size varchar(3) unique,
    value_modifier float
);
create table Login(
    username varchar(30) unique,
    account_type varchar(10),
    password varchar,
    salt varchar,
    primary key(username)
);
create table Agent(
	agent_id serial,
	agent_name varchar(50) not null,
	address_id serial,
    username varchar(30),
	primary key(agent_id),
    foreign key(address_id) references Address(address_id),
    foreign key(username) references Login(username)
);
create table Policy(
    policy_no serial SET DEFAULT nextval('PolicySeq'::regclass);
    agent_id serial,
    primary key(policy_no),
    foreign key(agent_id) references Agent(agent_id)
);
create table Customer(
    customer_id serial,
	policy_no serial,
	owner_fname varchar(20) not null,
    owner_lname varchar(25) not null,
    address_id serial,
    username varchar(30),
	primary key(customer_id),
    foreign key(policy_no) references Policy(policy_no),
    foreign key(username) references Login(username),
    foreign key(address_id) references Address(address_id)
	);
create table Breeds(
	breed_id serial,
	breed_name varchar(20),
	breed_lifespan integer,
	breed_size varchar(3),
	primary key(breed_id),
    foreign key(breed_size) references Size(breed_size)
	);
create table Pets(
	pet_id serial,
	policy_no serial not null,
	pet_name varchar(50) not null,
	pet_age integer not null,
    pet_issue_age integer not null,
    breed_id,
    pet_alive boolean,
	primary key(pet_id),
	foreign key(policy_no) references Policy(policy_no),
    foreign key(funeral_kind) references CostSheet(funeral_kind)
	);
"""

#--- --- ---Code provided by Microsoft to establish a connection and make calls to database--- --- ---
'''
# def test_connect():

#     host = "server here.postgres.database.azure.com"
#     dbname = ""
#     user = ""
#     password = ""
#     sslmode = "require"
#     # Construct connection string

#     conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
#     conn = psycopg2.connect(conn_string) 
#     print("Connection established")
#     cursor = conn.cursor()
#     # Drop previous table of same name if one exists

#     cursor.execute("DROP TABLE IF EXISTS inventory;")
#     print("Finished dropping table (if existed)")
#     # Create a table

#     cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
#     print("Finished creating table")
#     # Insert some data into the table

#     cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
#     cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
#     cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
#     print("Inserted 3 rows of data")
#     # Clean up

#     conn.commit()
#     cursor.close()
#     conn.close()


# Auto Create Policies/Dogs with possible agent

# Get the Policy Cost
'''
