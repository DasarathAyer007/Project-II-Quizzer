from flask import Flask ,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
  return render_template('home.html')
   
@app.route('/login')
def login():
   return render_template('login.html')


@app.route('/<type>/<mode>')
def random_classic(type,mode):
   return render_template(f'quiz/{type}/{mode}.html')




if __name__=='__main__':
    app.run(debug=True)
