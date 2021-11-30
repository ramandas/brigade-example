from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/count")
def index():
    
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    # hostname = os.uname

    # Render HTML with count variable
    return render_template("index.html", count=count)

@app.route("/getHost", methods = ['POST','GET'])
def gethostname():
    hostname = os.uname()
    return {"hostname" : hostname[1],
    "sysname" : hostname[0]
    }

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=3000, debug=True)
    # app.run()