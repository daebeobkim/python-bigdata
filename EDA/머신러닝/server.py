from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL 연결 설정
db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    db='customer',

    charset='utf8'
)




# 검색 기능 API
@app.route('/', methods=['POST'])
def search():
    # 안드로이드 스튜디오에서 전송된 검색어 받기
    search_word = request.form['search_word']

    # MySQL에서 검색어 검색
    cursor = db.cursor()
    query = """SELECT * 
    FROM food_table
    WHERE food_name LIKE %s
    ORDER BY 
        CASE 
            WHEN food_name LIKE %s THEN 0 
            WHEN food_name LIKE %s THEN 1 
            ELSE 2 
        END"""
    cursor.execute(query, ('%' + search_word + '%', search_word + '%', '%' + search_word + '%'))
    results = cursor.fetchall()
    cursor.close()


    # 검색 결과를 JSON 형태로 변환하여 안드로이드 스튜디오에 전송
    return jsonify(results)


if __name__ == '__main__':
    app.run()



