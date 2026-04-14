import os
import sys
import urllib.request
import json

class NaverSearcher:
    # 1. 처음 클래스를 만들 때 아이디, 비번, 시작위치, 개수를 모두 정합니다.
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        
        # 기본값으로 초기화 (나중에 언제든 바꿀 수 있어요)
        self.start = 1
        self.display = 10

    # 2. 검색을 수행하는 함수
    def crawl_naver_news(self, key_word):
        # 검색어를 URL용 문자로 변환
        enc_text = urllib.parse.quote(key_word)
        
        # 주소 만들기 (클래스 멤버 변수인 self.start와 self.display를 사용합니다)
        url = "https://openapi.naver.com/v1/search/blog?query=" + enc_text
        new_url = url + f'&start={self.start}&display={self.display}'
        
        try:
            # API 호출 준비
            request = urllib.request.Request(new_url)
            request.add_header("X-Naver-Client-Id", self.client_id)
            request.add_header("X-Naver-Client-Secret", self.client_secret)
            
            # 응답 받기
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            
            if rescode == 200:
                response_body = response.read()
                py_data = json.loads(response_body.decode('utf-8'))
                return py_data
            else:
                print("에러 발생! 에러 코드:", rescode)
                return None

        except Exception as e:
            # 예외 발생 시 에러 내용과 URL 확인
            print("--- 예외 발생 상황 ---")
            print(f"에러 내용: {e}")
            print(f"문제가 된 URL: {new_url}")
            print("----------------------")
            return None

# --- 클래스 사용법 ---

# 1. 객체 생성
searcher = NaverSearcher("내_아이디", "내_비밀번호")

# 2. 기본값(1번부터 10개)으로 검색할 때
print("--- 기본 설정으로 검색 ---")
result1 = searcher.crawl_naver_news("캠핑")

# 3. 설정을 바꿔서(11번부터 5개) 검색하고 싶을 때
print("--- 설정을 변경해서 검색 ---")
searcher.start = 11      # 시작 위치 변경
searcher.display = 5     # 출력 개수 변경
result2 = searcher.crawl_naver_news("캠핑")