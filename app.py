from flask  import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret-key-"

#---------------------------------------------------------
@app.route('/')
def home():
    return render_template("blog/home.html")


@app.route('/about')
def about():
    return render_template("blog/about.html")


@app.route('/contact', methods=['GET','POST'])
def contact():
    name = 'sgbaoingbpaerjbmperagpowg'
    if request.method == 'POST':
        name = request.form.get('fulname')
        if name == '':
            flash('اسم را وارد کن عزیزم &#10060', 'danger')
        else:
            flash('با موفقیت ثبت شد  <p>I will display &#9989;</p>', 'success')
    return render_template("blog/contact.html", name=name)


#----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)