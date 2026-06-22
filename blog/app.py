from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'sNVoalkbniosnbdLnaksnvisdnvikdsnvkidsnvk'
# ------------------------------

@app.route('/')
def home():
    return render_template('blog/home.html')


@app.route('/about')
def about():
    return render_template('blog/about.html')



@app.route('/contact', methods=["POST","GET"])
def contact():
    name = ''
    if request.method == "POST":
        name = request.form.get('name')
        if name != "":
            flash('gode', 'red')
        else:
            flash('bad', 'gray')

    return render_template('blog/contact.html')




# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)