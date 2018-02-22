import pygame

import sqlite3 as lite
import sys

displaySize = (1000, 900)

#pygame.init()

#pygame.display.set_caption('Chess Networked V0.1')

#display = pygame.display.set_mode(displaySize)

running = True

def write(con, data, name):
    try:
        cur = con.cursor()

        cur.execute("INSERT INTO " + name + " VALUES " + str(data))

        con.commit()

    except lite.Error as e:

        if con:
            con.rollback()

        print("Error %s:" % e.args[0])

    finally:
        if con:
            con.close()

def make(con, data, name, overwrite=False):
    with con:
        cur = con.cursor()

        if overwrite:
            cur.execute('DROP TABLE IF EXISTS ' + name)
            cur.execute('CREATE TABLE ' + name + data)
        else:
            cur.execute('CREATE TABLE IF NOT EXISTS ' + name + data)

def read(con, name):
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM " + name)

        rows = cur.fetchall()

        return rows

make(lite.connect('test.db'), "(Id INT, Name STRING, Price INT)", 'NewCar')
write(lite.connect('test.db'), (1, 'THIS SHOULD WORK!!!', 10000000), 'NewCar')
write(lite.connect('test.db'), (10000, 'ANOTHER!!!',100000000000000000000000), 'NewCar')
print(str(read(lite.connect('test.db'), 'NewCar')))

#while running:
    #display.fill((0, 0, 0))

    #pygame.display.update()
