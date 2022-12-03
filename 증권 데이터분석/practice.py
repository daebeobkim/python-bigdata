import csv
function_list = ["book", "writer", "genre", "add", "end"]
def print_function():
    print("book : 도서 검색")
    print("writer : 저자 검색")
    print("genre : 장르 검색")
    print("add : 추가 입력")
    print("end : 종료")
    function = input("기능을 입력해 주세요! : ")
    print("=====================")
    return function

def book():
        search_book = input("찾고 싶은 도서의 이름을 입력해 주세요 : ")
        for i in range(len(book_list)):
            if search_book == book_list[i][1]:
                print("저자 : ", book_list[i][2])
                print("장르 : ", book_list[i][3])
                print("출판사 : ", book_list[i][4])
                print("=====================")
                break
        else:
            print("존재하지 않는 도서입니다!")
            print("=====================")
def writer():
        search_writer = input("찾고 싶은 저자를 입력해 주세요 : ")
        count=0
        for i in range(len(book_list)):
            if search_writer == book_list[i][2]:
                print("도서명 : ", book_list[i][1])
                print("장르 : ", book_list[i][3])
                print("출판사 : ", book_list[i][4])
                print("=====================")
                count+=1
            elif (i==len(book_list)-1 and search_writer!=book_list[i][2] and count==0):
                print("존재하지 않는 저자입니다!")
                print("=====================")
def genre():
    search_genre = input("찾고 싶은 장르를 입력해 주세요 : ")
    count=0
    for i in range(len(book_list)):
        if search_genre == book_list[i][3]:
            print("도서명 : ", book_list[i][1])
            print("저자 : ", book_list[i][2])
            print("출판사 : ", book_list[i][4])
            print("=====================")
            count+=1
        elif (i==len(book_list)-1 and search_genre!=book_list[i][3] and count==0):
            print("존재하지 않는 장르입니다!")
            print("=====================")
def add():
    with open("C:/Users/rlaeo/OneDrive/바탕 화면/book.csv","a", newline='') as file:
        lines = csv.writer(file)
        number = len(book_list)
        new_book = input("도서명을 입력해 주세요")
        new_writer = input("저자명을 입력해 주세요")
        new_genre = input("장르를 입력해 주세요")
        publisher = input("출판사를 입력해 주세요")
        new_list = [number, new_book, new_writer, new_genre, publisher]
        lines.writerow(new_list)
def main():
    while(True):
        with open("C:/Users/rlaeo/OneDrive/바탕 화면/book.csv","r") as file:
            lines = csv.reader(file)
            global book_list
            book_list = list(lines)
            function = print_function()
            if function == function_list[0]:
                book()
            elif function == function_list[1]:
                writer()
            elif function == function_list[2]:
                genre()
            elif function == function_list[3]:
                add()
            elif function == function_list[4]:
                break
main()