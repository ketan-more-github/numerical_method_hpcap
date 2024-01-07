import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

deck = ['1s',	'2s' ,'3s'	,'4s',	'5s',	'6s',	'7s',	'8s',	'9s',	'xs'	,'js',	'qs',	'ks',
        '1h',	'2h',	'3h'	,'4h',	'5h',	'6h'	,'7h',	'8h',	'9h',	'xs',	'js',	'qs',	'ks',
        '1d',	'2d',	'3d',	'4d',	'5d',	'6d',	'7d',	'8d	','9d',	'xs',	'js',	'qs',	'ks',
        '1c'	,'2c',	'3c',	'4c',	'5c',	'6c',	'7c',	'8c',	'9c',	'xs',	'js',	'qs',	'ks' 
]

# print(deck[12].startswith('k'))
# print(deck[25].startswith('k'))

cnt = 0
for i in range(1,1000):
    np.random.shuffle(deck)
    for j in range(0,52,1):
        for k in range(j+1 , 52 , 1):
            if(deck[j].startswith('k') and deck[k].startswith('k') ):
                cnt+=1
        break
probab = cnt/1000
print(probab)
