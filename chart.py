import matplotlib.pyplot as plt
from sqlighter import sqlighter
import numpy as np
import os

BASE_DIR = str(os.path.dirname(os.path.abspath(__file__)))
db = sqlighter('db.db')

#def save(name='', fmt='png'):



def save(name, fmt, myuser_id):
    db = sqlighter('db.db')
    data = db.get_data(myuser_id)[0]
     
    x = ('Счастливый', 'Несчастный', 'Веселый', 'Расстроенный', 'Злой', 'Грустный', 'Бодрый', 'Энергичный', 'Вялый')
    z1 = data[2:11]

    # bar()
    fig = plt.figure()
    plt.bar(x, z1)
    plt.title('График твоего настроения')
    plt.grid(True)


    pwd = os.getcwd()
    iPath = BASE_DIR
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
    #plt.close()
"""
data = db.get_data(12149911)[0]
 
x = ('Счастливый', 'Несчастный', 'Веселый', 'Расстроенный', 'Злой', 'Грустный', 'Бодрый', 'Энергичный', 'Вялый')
z1 = data[2:11]

# bar()
fig = plt.figure()
plt.bar(x, z1)
plt.title('Simple bar chart')
plt.grid(True)   # линии вспомогательной сетки


# смотри преамбулу 3232322
#save(name='pic_2_2', fmt='png')
"""