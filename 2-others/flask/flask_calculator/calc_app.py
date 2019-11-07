from flask import Flask, render_template, request, url_for, jsonify
import os

calc_app = Flask(__name__)
calc_app._static_folder = os.path.abspath("templates/static/")

@calc_app.route("/", methods=['GET'])
def index():
    return render_template("layouts/index.html")

@calc_app.route("/calc", methods=['POST'])
def calculate():
    inp_dict = dict(request.form['calc_inp'])
    op1 = inp_dict["op1"]
    op2 = inp_dict["op2"]
    res = op1 + op2
    json_out = {"calc_result" : res}
    response_out = jsonify(json_out)
    return render_template("layouts/output.html", context = response_out)

if __name__ == "__main__":
    calc_app.run(debug=True)