from flask import render_template, Flask, request
 
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def getvalue():
    name=request.form['name']
    password=request.form['password'] 
  
    return render_template('info.php',n=name,password=password)

if __name__=='__main__':
    app.run(debug=True)