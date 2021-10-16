from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')

@app.route('/agendar', methods=['GET', 'POST'] )    
def agendar():
        if request.method == 'GET':
           servico = request.form.get('contact')
        print ('servico')       

        return render_template('agenda.html')
                      
if __name__ == "__main__":
    app.run(debug = True)