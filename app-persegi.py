from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("persegi.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        persegi = request.form["persegi"]
        sum = float(persegi) * 2
        sum2 = float(persegi) * 4
        return render_template("persegi.html", sum=sum, sum2=sum2)
    else:
        return render_template("persegi.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
