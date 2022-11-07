from flask import Flask, request, redirect, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        submit= request.form

        
        return render_template('todolists.html', submit=submit)



@app.route('/clear')
def clear(): 
    return redirect('/')


 


if __name__ == '__main__':
    app.run()