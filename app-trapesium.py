from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("trapesium.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        trapesium = request.form["trapesium"]
        trapesium2 = request.form["trapesium2"]
        trapesium3 = request.form["trapesium3"]
        trapesium4 = request.form["trapesium4"]
        sum = float(trapesium)
        sum2= float(trapesium2)
        sum3 = float(trapesium3)
        sum4 = float(trapesium4)
        result = 0.5 * (sum + sum2) * sum3
        result2 = sum + sum2 + sum3 + sum4
        return render_template("trapesium.html", sum=result, sum2=result2, sum3=sum2, sum4=sum3)
    else:
        return render_template("trapesium.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
