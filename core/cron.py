

import os
import glob
from django.contrib.sessions.models import Session
from datetime import datetime

def delete_sessions():
    # dir_path = "/log"
    # if not os.path.isdir(dir_path):
    #     os.makedirs(dir_path)
    
    sessions = Session.objects.all()
    for session in sessions:
        print("===================================")
        print(f"현재시간: {datetime.now()}", end=", ")
        print(f"만료시간: {session.expire_date}")
        if datetime.now() > session.expire_date:
            session.delete()
            print("Delete completely expire_date!")
