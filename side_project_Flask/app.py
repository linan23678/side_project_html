from flask import Flask , render_template, request

app = Flask(__name__)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =='GET':
        return render_template('register.html')
    else:
        ## 1.接收用戶透過GET方式發送過來的數據
        print(request.form)
        ## 2.給用戶在返還結果

        return '註冊成功'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        ## 1.接收用戶透過GET方式發送過來的數據
        username = request.form.get('user')
        password = request.form.get('pwd')
        print(request.form)
        print(username, password)
        ## 2.給用戶在返還結果
        return '登入成功'

if __name__ == '__main__':
    app.run()