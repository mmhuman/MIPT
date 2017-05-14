import sys

n = 227

data = [0] * n

for i in range(n):
    _in = input().split(";")
    data[i] = {}
    data[i]["univer"] = str(_in[0])
    data[i]["num"] = int(_in[1])
    if i > 0:
        data[i - 1]["solved"] = int(_in[2])
    if i >= 179:
        data[i - 1]["solved"] = 0
    data[i]["mem_1"] = str(_in[3])
    data[i]["mem_2"] = str(_in[4])
    data[i]["mem_3"] = str(_in[5])

data[n - 1]["solved"] = 0

start_cnt_id = 13
start_tm_id = 9
start_tma_id = 4


"""
for i in range(n):
    print(data[i]["univer"] + " " + str(data[i]["num"]))
    print(data[i]["solved"])
"""


"""
tm_id = start_tm_id
for i in range(n):
    print("add_team_alias")
    print("-")
    print(data[i]["univer"] + " " + str(data[i]["num"]))
    print(tm_id)
    tm_id += 1

"""

"""
#add_teams:
cnt_id = start_cnt_id

for i in range(n):
    print("add_team")
    print("-")
    print(data[i]["univer"] + " " + str(data[i]["num"]))
    print("-")
    print("-")
    print(cnt_id)
    print(cnt_id + 1)
    print(cnt_id + 2)
    cnt_id += 3
    print("RU")
    print(data[i]["univer"])
"""

"""
add_contestants:

for i in range(n):
    print("add_contestant")
    print("-")
    print(data[i]["mem_1"])
    print("-")
    print("-")
    print("RU")
    print(data[i]["univer"])

    print("add_contestant")
    print("-")
    print(data[i]["mem_2"])
    print("-")
    print("-")
    print("RU")
    print(data[i]["univer"])

    print("add_contestant")
    print("-")
    print(data[i]["mem_3"])
    print("-")
    print("-")
    print("RU")
    print(data[i]["univer"])

"""