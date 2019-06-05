from flask import Flask, request, render_template
import wikipedia
app= Flask(__name__)


@app.route("/login", methods =['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        Search=request.form.get('Search')
        summary=wikipedia.summary(Search)
        return summary
       
    

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)