from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_ENDPOINT = 'https://your-api-endpoint.com'  # 실제 API 엔드포인트 URL로 대체하세요.

# 일반 사용자 기능
# 과제 1: 매장에서 판매 중인 도서 목록 가져오기
@app.route('/books', methods=['GET'])
def get_books():
    try:
        response = requests.get(f"{API_ENDPOINT}/books")
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 과제 2: ISBN에 따라 책을 구하세요
@app.route('/books/<isbn>', methods=['GET'])
def get_book_by_isbn(isbn):
    try:
        response = requests.get(f"{API_ENDPOINT}/books/{isbn}")
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 과제 3: 저자별 모든 책 가져오기
@app.route('/books/author/<author>', methods=['GET'])
def get_books_by_author(author):
    try:
        response = requests.get(f"{API_ENDPOINT}/books?author={author}")
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 과제 4: 제목에 따라 모든 책 가져오기
@app.route('/books/title/<title>', methods=['GET'])
def get_books_by_title(title):
    try:
        response = requests.get(f"{API_ENDPOINT}/books?title={title}")
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 과제 5: 책 리뷰 받기
@app.route('/reviews/<isbn>', methods=['GET'])
def get_reviews(isbn):
    try:
        response = requests.get(f"{API_ENDPOINT}/reviews/{isbn}")
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 과제 6: 신규 사용자 등록
@app.route('/register', methods=['POST'])
def register_user():
    try:
        response = requests.post(f"{API_ENDPOINT}/users", json=request.json)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 과제 7: 등록된 사용자로 로그인
@app.route('/login', methods=['POST'])
def login_user():
    try:
        response = requests.post(f"{API_ENDPOINT}/login", json=request.json)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 등록된 사용자 기능
# 과제 8: 책 리뷰 추가/수정
@app.route('/reviews/<isbn>', methods=['PUT'])
def add_or_update_review(isbn):
    try:
        response = requests.put(f"{API_ENDPOINT}/reviews/{isbn}", json=request.json)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 과제 9: 해당 사용자가 추가한 도서 리뷰 삭제
@app.route('/reviews/<isbn>', methods=['DELETE'])
def delete_review(isbn):
    try:
        response = requests.delete(f"{API_ENDPOINT}/reviews/{isbn}")
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

# 4가지 방법 예제
# 과제 10: 모든 책 가져오기 – 비동기 콜백 함수 사용
def get_all_books(callback):
    try:
        response = requests.get(f"{API_ENDPOINT}/books")
        callback(None, response.json())
    except requests.RequestException as e:
        callback(e, None)

# 과제 11: ISBN으로 검색 – Promises 사용
def get_book_by_isbn_promise(isbn):
    try:
        response = requests.get(f"{API_ENDPOINT}/books/{isbn}")
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

# 과제 12: 작성자로 검색
def get_books_by_author_async(author):
    try:
        response = requests.get(f"{API_ENDPOINT}/books?author={author}")
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

# 과제 13: 제목으로 검색
def get_books_by_title_async(title):
    try:
        response = requests.get(f"{API_ENDPOINT}/books?title={title}")
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(port=3000, debug=True)
