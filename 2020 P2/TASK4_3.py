from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def display():
    #open the file 'people.txt' to read the data
    data = []
    with open("people.txt", "r") as f:
        allLines = f.readlines()
        for line in allLines:
            full_name, dob, classtype = line.strip().split(",")
            data.append([full_name, dob, classtype])

    # data = [
    # ["John Tan","2000-06-01","Person"],
    # ["Jane Smith","2000-02-01","Person"],
    # ["William Lin","1980-03-10","Staff"],
    # ["Evan O'Reilly","2004-04-15","Student"],
    # ["Sally Jones","1995-06-19","Staff"],
    # ["Mike Green","2010-07-21","Student"],
    # ["Betty Wang","2003-12-25","Student"]]

    return render_template("index.html", data=data)


    
app.run(debug=True)