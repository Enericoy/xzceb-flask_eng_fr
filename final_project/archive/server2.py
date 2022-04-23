from flask import Flask, render_template, request

app = Flask("Test Flask")

@app.route("/")
def renderIndexPage():
    return render_template("index2.html")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)
if __name__=="__main__":
    app.run(debug=True) 
# When no port is specified, starts at default port 5000