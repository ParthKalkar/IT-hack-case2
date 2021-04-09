import psycopg2
import random
from faker import Faker
import random

con = psycopg2.connect(database="Happines_index", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")

cur = con.cursor()
cur.execute("DROP TABLE user_info")
cur.execute("""CREATE TABLE IF NOT EXISTS user_info (
	id serial primary key not NULL,
	first_name VARCHAR (255) not NULL,
	last_name VARCHAR (255) not NULL,
	age INT not NULL,
	gender VARCHAR (255) not NULL,
	address VARCHAR (255) NOT NUll,
	workplace VARCHAR (255) NOT NUll,
	position VARCHAR (255) NOT NUll,
	bpm INT not NULL,
	blood_pressure VARCHAR(100) not NULL,
	steps_per_day INT not NULL,
	visits_sport_clubs INT not NULL,
	visits_art_clubs INT not NULL,
	interaction_with_friends INT not NULL,
	salary INT not NULL,
	relationship VARCHAR (255) not NULL,
	performance INT not NULL
);""")
fake = Faker()

positions = ["Employee"] * 50 + ["Manager"] * 25 + ["Supervisor"] * 12 + ["Chief manager"] * 8 + ["CEO"] * 5
# print(fake.name().split())
for i in range(4000):
    fname = fake.name().split()[0]
    lname = fake.name().split()[1]
    age = random.randint(10, 60)
    gender = random.choice(['M', 'F'])
    address = fake.address()
    workplace = f'company{random.randint(1, 20)}'
    position = random.choice(positions)
    salary = random.randint(12000, 70000)
    relation = random.choice(['Single', 'Married', 'In a relationship'])
    for j in range(10):
        cur.execute(
            f"INSERT INTO user_info (first_name, last_name, age, gender, address, workplace, position , bpm , blood_pressure , steps_per_day , visits_sport_clubs ,"
            f" visits_art_clubs, interaction_with_friends , salary , relationship, performance  )  VALUES "
            f"('{fname}', '{lname}', {age}, '{gender}', '{address}', "
            f"'{workplace}', '{position}', {random.randint(70, 200)}, '{random.randint(80, 140)}/{random.randint(70, 90)}', "
            f"{random.randint(200, 20000)}, {random.randint(0, 3)}, {random.randint(0, 3)}, {random.randint(1, 10)}, {salary}, "
            f"'{relation}', {random.randint(1, 100)})")
con.commit()
con.close()
