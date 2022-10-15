from web_through.main import login,tianbao
from setting import username,password
import sys
from app_through.NWPU import nwpuapp
if __name__ == '__main__':
    exec_state = False
    if (len(sys.argv) != 1):
        login(sys.argv[1], sys.argv[2])
        exec_state = tianbao(sys.argv[1])
    else:
        login(username, password)
        exec_state = tianbao(username)
    
    if(exec_state == False):
        print('网页登陆失败，尝试进行APP端登录')

        app = nwpuapp()
        app.getidToken()
        app.yqtb_one_sesstion()
