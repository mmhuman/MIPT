import psycopg2
import sys

conn = None
cur = None

cnt_cols = ("id", "name", "cf_profile", "tc_profile", "country", "organization")
tm_cols = ("id", "name", "rating", "contest_cnt", "member_1", "member_2", "member_3", "country", "organization")
tma_cols = ("id", "name", "team_id")
cst_cols  = ("id", "title", "date", "description", "participants", "max_problems_solved")
cstres_cols  = ("id", "contest_id", "team_id", "place", "problems_solved", "team_name")


def safe_commit():
    try:
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("Error in commit occured")
        print(e)
        return 1
    return 0


def add_contestant():
    cnt = {}
    for col in cnt_cols:
        print("Type ", col, ", type '-' for default value")
        cnt[col] = input()
    query = "INSERT INTO contestants VALUES ("
    for key in cnt_cols:
        if str(cnt[key]) == "-":
            query += "DEFAULT, "
        else:
            query += "%(" + key + ")s, "
    query = query[:-2] + ")"
    try:
        cur.execute(query, cnt)
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Contestant added succesfully")


def get_contestant():
    print("Type contestant name (or part of it):")
    cnt_name = "%" + str(input()) + "%"
    query = "SELECT * FROM contestants WHERE name LIKE %s"
    try:
        cur.execute(query, (cnt_name,))
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() != 0:
        return
    if cur.rowcount > 0:
        print(cnt_cols, ":")
        for v in cur:
            print(v)
    else:
        print("No such contestant found")


def upd_contestant():
    cnt = {}
    print("*You shouldn't type '-' for id value,")
    print("by this field we trying to find corresponding contestant")
    for col in cnt_cols:
        print("Type ", col, ", type '-' if you don't want to change this column")
        cnt[col] = input()

    query = "UPDATE contestants SET (";
    for v in cnt_cols:
        if str(cnt[v]) != "-":
            query += str(v) + ", "
    query = query[:-2]
    query += ") = ("

    for key in cnt_cols:
        if str(cnt[key]) != "-":
            query += "%(" + key + ")s, "
    query = query[:-2]
    query += ") "

    query += "WHERE id = %(id)s"
    try:
        cur.execute(query, cnt)
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Contestant updated succesfully")


def del_contestant():
    print("Type contestant id:")
    cnt_id = input()
    query = "DELETE FROM contestants WHERE id = %s"
    try:
        cur.execute(query, (cnt_id,))
    except Exception as e:
        print(e)
        return
    if safe_commit() == 0:
        print("Contestant deleted succesfully")


def add_team():
    tm = {}
    for col in tm_cols:
        print("Type ", col, ", type '-' for default value")
        tm[col] = input()
    query = "INSERT INTO teams VALUES ("
    for key in tm_cols:
        if str(tm[key]) == "-":
            query += "DEFAULT, "
        else:
            query += "%(" + key + ")s, "
    query = query[:-2] + ")"
    try:
        cur.execute(query, tm)
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Team added succesfully")


def get_team():
    print("Type team name (or part of it):")
    tm_name = "%" + str(input()) + "%"
    query = "SELECT * FROM teams WHERE name LIKE %s"
    try:
        cur.execute(query, (tm_name,))
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() != 0:
        return
    if cur.rowcount > 0:
        print(tm_cols, ":")
        for v in cur:
            print(v)
    else:
        print("No such team found")


def upd_team():
    tm = {}
    print("*You shouldn't type '-' for id value,")
    print("by this field we trying to find corresponding team")
    for col in tm_cols:
        print("Type ", col, ", type '-' if you don't want to change this column")
        tm[col] = input()

    query = "UPDATE teams SET (";
    for v in tm_cols:
        if str(tm[v]) != "-":
            query += str(v) + ", "
    query = query[:-2]
    query += ") = ("

    for key in tm_cols:
        if str(tm[key]) != "-":
            query += "%(" + key + ")s, "
    query = query[:-2]
    query += ") "

    query += "WHERE id = %(id)s"

    try:
        cur.execute(query, tm)
        conn.commit()
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Team updated succesfully")


def add_team_alias():
    tma = {}
    for col in tma_cols:
        print("Type ", col, ", type '-' for default value")
        tma[col] = input()
    query = "INSERT INTO teams_aliases VALUES ("
    for key in tma_cols:
        if str(tma[key]) == "-":
            query += "DEFAULT, "
        else:
            query += "%(" + key + ")s, "
    query = query[:-2] + ")"
    try:
        cur.execute(query, tma)
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Team alias added succesfully")


def get_team_alias():
    print("Type team alias (or part of it):")
    tma_name = "%" + str(input()) + "%"
    query = "SELECT * FROM teams_aliases WHERE name LIKE %s"
    try:
        cur.execute(query, (tma_name,))
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() != 0:
        return
    if cur.rowcount > 0:
        print(tma_cols, ":")
        for v in cur:
            print(v)
    else:
        print("No such team alias found")


def upd_team_alias():
    tma = {}
    print("*You shouldn't type '-' for id value,")
    print("by this field we trying to find corresponding team alias")
    for col in tma_cols:
        print("Type ", col, ", type '-' if you don't want to change this column")
        tma[col] = input()

    query = "UPDATE teams_aliases SET (";
    for v in tma_cols:
        if str(tma[v]) != "-":
            query += str(v) + ", "
    query = query[:-2]
    query += ") = ("

    for key in tma_cols:
        if str(tma[key]) != "-":
            query += "%(" + key + ")s, "
    query = query[:-2]
    query += ") "

    query += "WHERE id = %(id)s"

    try:
        cur.execute(query, tma)
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Team alias updated succesfully")


def del_team_alias():
    print("Type team alias id:")
    tma_id = input()
    query = "DELETE FROM teams_aliases WHERE id = %s"
    try:
        cur.execute(query, (tma_id,))
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Team alias deleted succesfully")


def add_contest():
    cst = {}
    for col in cst_cols:
        print("Type ", col, ", type '-' for default value")
        cst[col] = input()
    query = "INSERT INTO contests VALUES ("
    for key in cst_cols:
        if str(cst[key]) == "-":
            query += "DEFAULT, "
        else:
            query += "%(" + key + ")s, "
    query = query[:-2] + ")"
    try:
        cur.execute(query, cst)
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Contest added succesfully")


def get_contest():
    print("Type contest title (or part of it):")
    cst_title = "%" + str(input()) + "%"
    query = "SELECT * FROM contests WHERE title LIKE %s"
    try:
        cur.execute(query, (cst_title,))
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() != 0:
        return
    if cur.rowcount > 0:
        print(cst_cols, ":")
        for v in cur:
            print(v)
    else:
        print("No such contest found")


def get_contest_by_id(cst_id = -1):
    if cst_id == -1:
        print("Type constest id:")
        try:
            cst_id = int(input())
        except Exception as e:
            print(e)
            return
    cst = {}
    try:
        query = "SELECT * FROM contests WHERE id = %s"
        cur.execute(query, (cst_id,))
    except Exception as e:
        print(e)
        return {}
    if safe_commit() != 0:
        return {}
    try:
        cst_tuple = cur.fetchone()
        for n in range(len(cst_cols)):
            cst[cst_cols[n]] = cst_tuple[n]
    except Exception as e:
        print(e)
        return {}
    return cst


def upd_contest_rating(plus, cst_id = -1):
    cst = get_contest_by_id()
    if len(cst) == 0:
        print("Wrong contest id")
        return
    results = {}
    try:
        query = "SELECT * FROM contests_results WHERE contest_id = %s"
        cur.execute(query, (cst["id"],))
    except Exception as e:
        print("Error occured in selection from contests results")
        print(e)
        return
    safe_commit()
    try:
        for v in cur:
            results[v[2]] = {}
            n = 0
            for col in cstres_cols:
                results[v[2]][col] = v[n]
                n += 1
    except Exception as e:
        print("Error occured in selection from contests results")
        print(e)
        return

    try:
        if plus == 1:
            query = """
                    UPDATE teams
                    SET contest_cnt = contest_cnt + 1,
                        rating = (rating * contest_cnt + %s) / (contest_cnt + 1)
                    WHERE id = %s
                    """
        else:
            query = """
                    UPDATE teams
                    SET contest_cnt = contest_cnt - 1,
                        rating = (rating * contest_cnt - %s) / GREATEST(1, contest_cnt - 1)
                    WHERE id = %s
                    """

        for team_id, res in results.items():
            place = int(res["place"])
            n = int(cst["participants"])
            solved = int(res["problems_solved"])
            max_solved = int(cst["max_problems_solved"])
            rating = 200.0 * ((n - place + 1) / n) * (solved / max_solved)
            cur.execute(query, (rating, res["team_id"]))
    except Exception as e:
        print("Error occured in updating teams rating")
        print(e)
        return
    if safe_commit() == 0:
        if plus == 1:
            print("Results of constest added to team ratings succesfully")
        else:
            print("Results of constest deleted from team ratings succesfully")


def add_contest_results():
    cst = get_contest_by_id()
    cst_id = cst["id"]
    if len(cst) == 0:
        print("Wrong contest id")
        return
    print(  "You can type results,\n"\
            "or you can provide file with results ")

    print("Use input informatian by file? (yes/no)")
    input_type = str(input())
    results_teams = [""] * cst["participants"]
    results_problems_solved = [0] * cst["participants"]

    if input_type == "no" or input_type == "n":
        print(  "%d lines, in each line there should be:\n"\
                "$team_alias $solved_problems_amount\n", cst["participants"])

        for i in range(cst["participants"]):
            _in = input().split()
            results_teams[i] = _in[0]
            results_problems_solved[i] = _in[1]

    elif input_type == "yes" or input_type == "y":
        print(  "Results should be in the following format:\n"\
                "2 * $participants_amount lines, for each team there should be:\n"\
                "$team_alias\n"\
                "$solved_problems_amount\n"\
                "Teams have to be sorted from best to worse")
        print("Type path to file:")
        path = str(input())
        try:
            cst_file = open(path)
        except Exception as e:
            print("Error occured")
            print(e)

        n = 0
        for line in cst_file:    
            if n // 2 >= cst["participants"]:
                print("Error, too many teams")
                return
            if line[-1] == '\n':
                line = line[:-1]
            if n % 2 == 0:
                results_teams[n // 2] = line
            else:
                try:
                    results_problems_solved[n // 2] = int(line)
                except Exception as e:
                    print("Error occured")
                    print(e)
                    return
            n += 1

        if n // 2 != cst["participants"]:
            print("Error, only %d teams in file, (%d needed)", n // 2, cst["participants"])
            return

#    for i in range(cst["participants"]):
#        print(results_teams[i], ":", results_problems_solved[i])

    teams_ids = {}
    try:
        query = "SELECT team_id, name FROM teams_aliases WHERE name in %s"
        cur.execute(query, (tuple(results_teams),))
    except Exception as e:
        print("Error occured")
        print(e)

    if safe_commit() != 0:
        return

    try:
        n = 0
        for v in cur:
            teams_ids[v[1]] = v[0]
            n += 1
#        print(n)
        if n != cst["participants"]:
            print("Error not all teams names are valid")
            return
    except Exception as e:
        print("Error occured")
        print(e)

    try:
        query = "INSERT INTO contests_results "\
                "VALUES (DEFAULT, %(contest_id)s, %(team_id)s, %(place)s, "\
                "%(problems_solved)s, %(team_name)s)"
        for i in range(cst["participants"]):
            res = {}
            res["contest_id"] = cst_id
            res["team_id"] = teams_ids[results_teams[i]]
            res["place"] = i + 1
            res["problems_solved"] = results_problems_solved[i]
            res["team_name"] = results_teams[i]
            cur.execute(query, res)
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Results added succesfully")


def del_contest_results():
    cst = get_contest_by_id()
    cst_id = cst["id"]
    query = "DELETE FROM contests_results WHERE contest_id = %s"
    try:
        cur.execute(query, (cst_id,))
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print("Contest results deleted succesfully")


def get_contest_results():
    cst = get_contest_by_id()
    if len(cst) == 0:
        print("Wrong contest")
        return
    query = "SELECT * FROM contests_results WHERE contest_id = %s ORDER BY place"
    try:
        cur.execute(query, (cst["id"],))
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() != 0:
        return
    if cur.rowcount > 0:
        print(cstres_cols, ":")
        for v in cur:
            print(v)
    else:
        print("No such contest results found")


def get_teams_ordered_by_rating():
    try:
        print("Type page size:")
        page_size = int(input())
        print("Type page number:")
        page_num = int(input())
    except Exception as e:
        print("Error occured")
        print(e)
        return
    query = "SELECT * FROM teams ORDER BY rating DESC LIMIT %s OFFSET %s"
    try:
        cur.execute(query, (page_size, (page_num - 1) * page_size))
    except Exception as e:
        print("Error occured")
        print(e)
        return
    if safe_commit() == 0:
        print(tm_cols)
        for v in cur:
            print(v)


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
        elif command == "del_contestant" or command == "dcnt":
            del_contestant()
        elif command == "add_team" or command == "atm":
            add_team()
        elif command == "get_team" or command == "gtm":
            get_team()
        elif command == "upd_team" or command == "utm":
            upd_team()
        elif command == "del_team" or command == "dtm":
            del_team()
        elif command == "add_team_alias" or command == "atma":
            add_team_alias()
        elif command == "get_team_alias" or command == "gtma":
            get_team_alias()
        elif command == "upd_team_alias" or command == "utma":
            upd_team_alias()
        elif command == "del_team_alias" or command == "dtma":
            del_team_alias()
        elif command == "add_contest" or command == "acst":
            add_contest()
        elif command == "get_contest" or command == "gcst":
            get_contest()
        elif command == "del_contest" or command == "dcst":
            del_contestant()
        elif command == "add_contest_results" or command == "acstres":
            add_contest_results()
        elif command == "del_contest_results" or command == "dcstres":
            del_contest_results()
        elif command == "get_contest_results" or command == "gcstres":
            get_contest_results()
        elif command == "add_contest_rating" or command == "acstrtg":
            upd_contest_rating(1)
        elif command == "del_contest_rating" or command == "dcstrtg":
            upd_contest_rating(-1)
        elif command == "get_ratings" or command == "grtg":
            get_teams_ordered_by_rating()
        elif command == "exit" or command == "ex":
            break
        else:
            print("Wrong command")
        conn.rollback()

    try:
       conn.close()
    except Exception as err:
        print(err)
    finally:
        sys.exit()
