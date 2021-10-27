from flask import Flask, render_template, request

# application instance Setup 
app = Flask(__name__)

# Routes
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':


        # HTML Form
        name = request.form['name']
        password = request.form['password']
        print(name, password)


        # Validation
        if len(results) == 0:
            print("Sorry, Incorrect Credentials Provided. Try Again")
        else:
            return render_template("logged_in.html")
        
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)