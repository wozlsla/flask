from db_model.mongodb import conn_mongodb
from datetime import datetime


class BlogSession():
    blog_page = {'A': 'blog_A.html', 'B': 'blog_B.html'}
    session_count = 0

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):  # 접속 할 때마다 접속 정보 저장
        now = datetime.now()
        # time -> str,  https://strftime.org/
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")

        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'session_ip': session_ip,
            'user_email': user_email,
            'page': webpage_name,
            'access_time': now_time
        })

    @staticmethod
    def get_blog_page(blog_id=None):  # args 없어도 O. 사용하려면 넣기
        if blog_id == None:
            if BlogSession.session_count == 0:
                BlogSession.session_count = 1
                return 'index.html'
            else:
                BlogSession.session_count = 0
                return 'index_2.html'
        else:
            return BlogSession.blog_page[blog_id]
