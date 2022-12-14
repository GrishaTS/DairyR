import pandas as pd
import json
import os
from main import check_person
from main import cd
message = "message.json"


def parce(_id):
    try:
        excel_data = pd.read_excel(f'savedFiles/{_id}diary.xlsx')
        m = [(excel_data[f'Unnamed: {1 + 4 * i}'][5:],
              excel_data[f'Unnamed: {2 + 4 * i}'][5:],
              excel_data[f'Unnamed: {3 + 4 * i}'][5:]) for i in range(6) if f'Unnamed: {3 + 4 * i}' in excel_data]
        all1 = [tuple([[k if str(k) != 'nan' else "" for k in j] for j in i]) for i in m]
        for i in range(len(all1)):
            all1[i] = (all1[i][0],
                       all1[i][1],
                       list(map(lambda x: "ok" if str(x) != '\n' else '', all1[i][2])))
        m1 = [list(zip(*i)) for i in all1]
        for i in range(len(m1)):
            m1[i] = dict(list(map(lambda x: x[:-1],
                                  list(filter(lambda x: all(x), m1[i])))))
        s = {}
        for i in range(1, len(m1) + 1):
            s[str(i)] = m1[i - 1]

        with open(cd) as file:
            sfile = json.load(file)
            if str(_id) in sfile:
                sfile1 = sfile[str(_id)]
                sfile1["notice"] = 1
            else:
                sfile1 = {"notice": 1}
            for i in s.keys():
                sfile1[str(i)] = s[i]
            sfile[str(_id)] = sfile1
        for i in range(1, 8):
            if str(i) not in sfile[str(_id)]:
                sfile[str(_id)][f"{i}"] = {}
        with open(cd, "w", encoding='utf-8') as file:
            json.dump(sfile, file)
        os.remove(f"savedFiles/{_id}diary.xlsx")
        return
    except Exception as e:
        print(e)
        return "no"


def change_tz(_id, newtz):
    a = check_person(_id)
    with open(cd) as file:
        sfile = json.load(file)

        if str(_id) in sfile:
            sfile1 = sfile[str(_id)]

            if a[0]:
                sfile1["timez"] = newtz
                sfile[str(_id)] = sfile1

            else:
                sfile[str(_id)] = {"timez": newtz}

        else:
            sfile1 = {"timez": newtz}
            sfile[str(_id)] = sfile1
    with open(cd, "w", encoding='utf-8') as file:
        json.dump(sfile, file)
    return


def add_dtime(_id, dtime):
    with open(cd) as file:
        sfile = json.load(file)
        sfile1 = sfile[str(_id)]
        sfile1["dtime"] = dtime
        sfile[str(_id)] = sfile1
    with open(cd, "w") as file:
        json.dump(sfile, file)
    return


def day_dairy(_id, day):
    with open(cd) as file:
        sfile = json.load(file)
        sfile1 = sfile[str(_id)][str(day)]

    if sfile1 == {}:
        return f'{["??????????????????????", "??????????????", "??????????", "??????????????", "??????????????", "??????????????", "??????????????????????"][day - 1]}:\n' \
               f'?????? ????????????\n'
    daylessons = ""
    for i in sfile1.keys():
        daylessons += f'{i} - {sfile1[i]}\n'
    return f'{["??????????????????????", "??????????????", "??????????", "??????????????", "??????????????", "??????????????", "??????????????????????"][day - 1]}:' \
           f'\n{daylessons}'



