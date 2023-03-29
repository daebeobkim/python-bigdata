import pandas as pd

sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])
print('시리즈 출력 :')
print('-'*15)
print(sr)
print('시리즈의 값 : {}'.format(sr.values))
print('시리즈의 인덱스 : {}'.format(sr.index))