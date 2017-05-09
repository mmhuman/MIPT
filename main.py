import psycopg2
import sys

conn = None
cur = None

cnt_cols = ("id", "name", "cf_profile", "tc_profile", "country", "organization")

def add_contestant():
    n = 0
    cnt = {}
    for col in cnt_cols:
        print("Type ", col, ", '-' for default value")
        cnt[n] = input()
        n += 1

    query = "INSERT INTO contestants VALUES ("
    for key, v in cnt.items():
        if str(v) == "-":
            query += "DEFAULT, "
        else:
            query += "'" + str(v) + "', "
    query = query[:-2]
    query += ")"
    try:
        cur.execute(query)
        conn.commit()
        print("Contestant added succesfully")
    except Exception as e:
        print("Error occured")
        print(e)


def get_contestant():
    print("name:")
    cnt_name = input()
    query = "SELECT * FROM contestants WHERE name LIKE '%" + str(cnt_name) + "%'"
    try:
        cur.execute(query)
        conn.commit()
    except Exception as e:
        print("Error occured")
        print(e)
        return

    print(cnt_cols, ":")
    for v in cur:
        print(v)


def upd_contestant():
    n = 0
    cnt = {}
    for col in cnt_cols:
        print("Type ", col, ", '-' if you don't want to change this column")
        cnt[n] = input()
        n += 1

    cnt_id = cnt[0]

    query = "UPDATE contestants SET (";
    n = 0
    for v in cnt_cols:
        print(cnt[n])
        if str(cnt[n]) != "-":
            query += str(v) + ", "
        n += 1
    query = query[:-2]
    query += ") = ("

    for key, v in cnt.items():
        if str(v) != "-":
            query += "'" + str(v) + "', "
    query = query[:-2]
    query += ") "

    query += "WHERE id = " + str(cnt_id)

    print(query)
    try:
        cur.execute(query)
        conn.commit()
        print("Contestant updated succesfully")
    except Exception as e:
        print("Error occured")
        print(e)


def del_contestant():
    print("id:")
    cnt_id = input()
    query = "DELETE FROM contestants WHERE id = " + str(cnt_id)

    try:
        cur.execute(query)
        conn.commit()
        print("Contestant deleted succesfully")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='test_user2',
            port='5432',
            password='-',
            host='localhost'
        )
        cur = conn.cursor()
    except Exception as err:
        if conn:
            conn.rollback()
        print(err)
        sys.exit()

    while 1:
        command = input()
        if command == "add_contestant" or command == "acnt":
            add_contestant()
        elif command == "get_contestant" or command == "gcnt":
            get_contestant()
        elif command == "upd_contestant" or command == "ucnt":
            upd_contestant()
        elif command == "exit" or command == "ex":
            break
        else:
            print("Wrong command")

    try:
       conn.close()
    except Exception as err:
        print(err)
    finally:
        sys.exit()
