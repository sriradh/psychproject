from flask import Flask, render_template, request, redirect

app = Flask(__name__)

my_list = ["Amma", "Appa", "Shravan", "Shriman"]

my_dict = {"AmmaId": "AmmaValue",
           "AppaId": "AppaValue",
           "ShravanId": "ShravanValue",
           "ShrimanId": "ShrimanValue"
           }

print(list(my_dict.keys()))
print(list(my_dict.values()))

for k, v in my_dict.items():
    print(k)
    print(v)


@app.route('/dynamiccheckboxusingdict', methods=['GET', 'POST'])
def dynamic_checkbox_using_dict():
    if request.method == "POST":
        print(request.form.getlist("mydynamiccheckboxusingdict"))
        return redirect("/")
    return render_template("dynamic_checkbox_using_dict.html", valuestobepopulated=my_dict)


@app.route('/dynamicdropdown', methods=['GET', 'POST'])
def dynamic_dropdown():
    if request.method == "POST":
        print(request.form["person"])
        return redirect("/")
    return render_template('dynamic_dropdown.html', tobepopulatedlist=my_list)


@app.route('/dynamiccheckbox', methods=['GET', 'POST'])
def dynamic_checkbox():
    if request.method == "POST":
        print(request.form.getlist("mydynamiccheckbox"))
        return redirect("/")
    return render_template("dynamic_checkbox.html", tobepopulatedlist=my_list)


@app.route('/dynamicradiobutton', methods=['GET', 'POST'])
def dynamic_radiobutton():
    if request.method == "POST":
        print(request.form["myDynamicRadio"])
        return redirect("/")
    return render_template("dynamic_radiobutton.html", tobepopulatedlist=my_list)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Done!"


@app.route('/dropdown', methods=['GET', 'POST'])
def dropdown():
    if request.method == "POST":
        print(request.form["cars"])
        return redirect("/radiobutton")
    return render_template("dropdown.html")


@app.route('/checkbox', methods=['GET', 'POST'])
def checkbox():
    if request.method == "POST":
        print(request.form.getlist("mycheckbox"))
        return redirect("/radiobutton")
    return render_template("checkbox.html")


@app.route('/radiobutton', methods=['GET', 'POST'])
def radiobutton():
    if request.method == "POST":
        print(request.form["myRadio"])
        return redirect("/checkbox")
    return render_template("radiobutton.html")


if __name__ == "__main__":
    app.run(debug=True, port=1234)

