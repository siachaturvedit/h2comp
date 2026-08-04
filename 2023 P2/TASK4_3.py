from flask import Flask, render_template

app = Flask(__name__)

def get_colour(code):
    if str(code) == '000':
        return 'red'
    elif str(code) == '001':
        return 'white'
    elif str(code) == '010':
        return 'yellow'
    elif str(code) == '011':
        return 'blue'
    elif str(code) == '100':
        return 'black'
    elif str(code) == '110':
        return 'green'


@app.route("/")
def colour_table():
    colours = []
    with open("/Users/navyamahajan/Library/CloudStorage/OneDrive-Personal(2)/Desktop/Alevel_2023/decompressedimage.txt", "r") as f:
        allLines = f.readlines()
        for line in allLines:
            colours.append(get_colour(line.strip()))

    colours_2d = [colours[i:i+9] for i in range(0, len(colours), 9)]

    return render_template("TASK4_3.html", colours_2d=colours_2d)


if __name__=="__main__":
    app.run(debug=True)
    