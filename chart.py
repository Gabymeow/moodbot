import matplotlib
import matplotlib.pyplot as plt
from sqlighter import sqlighter
import numpy as np
import os
import matplotlib.ticker as ticker
import time

BASE_DIR = str(os.path.dirname(os.path.abspath(__file__)))
#save paht = json_file = os.path.exists(BASE_DIR+f'{myuser_id}.png')
db = sqlighter('db.db')
matplotlib.use('Agg') 


def save(myuser_id):
    #time.sleep(2)
    db = sqlighter('db.db')
    data = db.get_data(myuser_id)[0]
     
    x = ('Счастливый', 'Несчастный', 'Веселый', 'Расстроенный', 'Злой', 'Грустный', 'Бодрый', 'Энергичный', 'Вялый')
    z1 = data[2:11]
    width = 0.8

    fig, ax = plt.subplots()
    fig.set_figwidth(12)
    plt.bar(x, z1, width)
    plt.title('График твоего настроения')
    ax.tick_params(labelleft = False)
    plt.savefig(f'{BASE_DIR}/img/{myuser_id}.png')
    print(f'{BASE_DIR}/img/{myuser_id}.png')
    plt.close('all')
    del fig