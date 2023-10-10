import numpy as np
import pandas as pd
book = pd.read_csv("C:/Users/11/Desktop/book.csv")
new_coulums = ['count','도서명','저자명','장르','출판사','NUN']
book.columns = new_coulums

def longshort():
    data = [(book['도서명'][i], len(book['도서명'][i])) for i in range(100)]

    min_value = data[0][1]
    max_value = data[0][1]

    for i in range(1, len(data)):
        if data[i][1] < min_value:
            min_value = data[i][1]
        elif data[i][1] > max_value:
            max_value = data[i][1]

    min_books = [item[0] for item in data if item[1] == min_value]
    max_books = [item[0] for item in data if item[1] == max_value]

    print("가장 짧은 제목:", min_books)
    print("가장 긴 제목:", max_books)

def all():
    lns = len(book['저자명'].unique())
    print("총 저자의 수%d" %lns)

def everything():
    most_common_authors = book['저자명'].value_counts()

    top_authors = most_common_authors[most_common_authors == most_common_authors.max()].index.tolist()

    for author in top_authors:
        books_by_author = book[book['저자명'] == author]['도서명'].tolist()
        print(f"저자 '{author}'가 쓴 책들: {', '.join(books_by_author)}")

def five():
    count = book['출판사'].value_counts().sort_values(ascending=False)
    print("최대 책을 출판한 5개 출판사\n%s\n%s\n%s\n%s\n%s" %(count.index[0],count.index[1],count.index[2],count.index[3],count.index[4]))

def alltime():
    역사 = book[book['장르'] == '역사']['출판사'].value_counts().sort_values(ascending=False)
    철학 = book[book['장르'] == '철학사상']['출판사'].value_counts().sort_values(ascending=False)
    print("역사분야",역사.head(5))
    print("철학사상분야",철학.head(5))
while True:
    menu = input("숫자를 선택하시오 : 1, 2, 3, 4, 5\n끝내려면 6\n")
    if menu =='1':
        longshort()
    elif menu =='2':
        all()
    elif menu =='3':
        everything()
    elif menu =='4':
        five()
    elif menu =='5':
        alltime()
    elif menu =='6':
        break