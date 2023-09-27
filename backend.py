import sqlite3


def connect():
    conn= sqlite3.connect('D://personal_routine//routine.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS routine
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                earnings INTEGER,
                exercise TEXT,
                study TEXT,
                diet TEXT,
                expense INTEGER)''')
    conn.commit()
    conn.close()

connect()

def insert(date, earnings, exercise, study, diet, expense):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine (date, earnings, exercise, study, diet, expense) VALUES (?, ?, ?, ?, ?, ?)",
                (date, earnings, exercise, study, diet, expense))
    conn.commit()
    conn.close()



def view():
    conn= sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows= cur.fetchall()
    conn.commit()
    conn.close()
    return(rows)
    # print(rows)

def update(id, date, earnings, exercise, study, diet, expense):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("UPDATE routine SET date=?, earnings=?, exercise=?, study=?, diet=?, expense=? WHERE id=?",
                (date, earnings, exercise, study, diet, expense, id))
    conn.commit()
    conn.close()


def delete(id):
    conn= sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(date='', earnings='', exercise='', study='', diet='', expense=''):
    conn= sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR earnings=? OR exercise=? OR study=? OR diet=? OR expense=?" , (date , earnings , exercise , study , diet , expense))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return(rows)
    # print(rows)

# insert('4-05-23', 3000, 'yes', 'no', 'yes', 300)
# insert('8-06-23', 5820, 'yes', 'yes', 'no', 1500)
# insert('18-03-23', 7890, 'no', 'yes', 'yes', 2000)
# insert('25-03-23', 7890, 'no', 'no', 'yes', 2000)
# insert('21-03-23', 7890, 'yes', 'yes', 'no', 2000)
# search(earnings =300)
# delete(4)
# view()
