from flask import Flask, render_template, request, session, flash

app=Flask(__name__)

click = None

@app.route("/")
def index():
    return render_template("index.html",res=0,click=None)

@app.route("/check", methods = ['POST','GET'])
def check():
    if request.method == "POST":
        plag = request.form.get('plag')
        print(plag) #call function here
        ret=0
        if ret==1:
            click="Clickbait"
        if ret==0:
            click="Not a Clickbait"
    return render_template("index.html",res=1,click=click)

if __name__ == "__main__":
    # webbrowser.open_new('http://127.0.0.1:5000/')
    app.run()