import pygame

import sqlite3 as lite
import sys
import Render

displaySize = (1000, 900)

gameDB = lite.connect('ChessMaster.db')

pygame.init()

pygame.display.set_caption('Chess Networked V0.1')

display = pygame.display.set_mode(displaySize)

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

def delete(con, name):
    with con:
        cur = con.cursor()

        cur.execute('DROP TABLE IF EXISTS ' + name)

#----------------------------------------------------------START CODING HERE----------------------------------------------------------------------------------------------------------------------------------------------------------------

make(gameDB, '(posX INT, posY INT)', 'gamePos')
write(gameDB, (100, 100), 'gamePos')
write(gameDB, (200, 200), 'gamePos')

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                with gameDB:
                    cur = gameDB.cursor()
                    cur.execute('UPDATE game SET posX=' + str(read(gameDB, 'game')[0][0] + 5) + " WHERE posY=" + str(read(gameDB, 'gamePos')[0][1]))
            if event.key == pygame.K_a:
                with gameDB:
                    cur = gameDB.cursor()
                    cur.execute('UPDATE game SET posX=' + str(read(gameDB, 'game')[0][0] - 5) + " WHERE posY=" + str(read(gameDB, 'gamePos')[0][1]))
            if event.key == pygame.K_w:
                with gameDB:
                    cur = gameDB.cursor()
                    cur.execute('UPDATE game SET posY=' + str(read(gameDB, 'game')[0][1] - 5) + " WHERE posX=" + str(read(gameDB, 'gamePos')[0][0]))
            if event.key == pygame.K_s:
                with gameDB:
                    cur = gameDB.cursor()
                    cur.execute('UPDATE game SET posY=' + str(read(gameDB, 'game')[0][1] + 5) + " WHERE posX=" + str(read(gameDB, 'gamePos')[0][0]))
    display.fill((0, 0, 0))

    Render.renderRect((255, 255, 255), read(gameDB, 'gamePos')[0], (70, 70), display)
    Render.renderRect((0, 255, 255), read(gameDB, 'gamePos')[1], (70, 70), display)

    pygame.display.update()
pygame.quit()
quit()
