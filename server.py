from flask import Flask, render_template, request
import core_predict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Prototype3.html")


@app.route('/', methods = ['POST'])
def getvalue():
    weight = request.form.get('weight')
    # testing ------------------------------------
    if weight == '':
        weight = 70
    print(weight)
    # --------------------------------------------
    params = core_predict.start(int(weight))
    return render_template("Prototype3.html", weight_py = weight, core_temp = params[0], skin_temp = params[1], max_HS = params[2], Stor_body = params[3], kcal_value = params[4], recovery = params[5], time_value = params[6], flags = params[7])


if __name__ == '__main__':
    app.run(debug = True)
