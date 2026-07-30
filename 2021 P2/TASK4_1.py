from flask import Flask, render_template
import sqlite3
app = Flask(__name__, template_folder = "Task4_4")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/round1/")
def round1():
    con = sqlite3.connect("/Users/navyamahajan/Library/CloudStorage/OneDrive-Personal(2)/Desktop/Alevel_2021/TASK4/Task4.db")
    cur = con.cursor()
    cur.execute('''SELECT competitor.name, scores.score 
                    FROM competitor JOIN scores ON competitor.id = scores.id
                    WHERE round = 1
                    ORDER BY scores.score DESC;''')
    result = cur.fetchall()
    con.close()
    return render_template("rounds.html", roundnum = 1, result=result)


@app.route("/round2/")
def round2():
    con = sqlite3.connect("/Users/navyamahajan/Library/CloudStorage/OneDrive-Personal(2)/Desktop/Alevel_2021/TASK4/Task4.db")
    cur = con.cursor()
    cur.execute('''SELECT competitor.name, scores.score 
                    FROM competitor JOIN scores ON competitor.id = scores.id
                    WHERE round = 2
                    ORDER BY scores.score DESC;''')
    result = cur.fetchall()
    con.close()
    return render_template("rounds.html", roundnum = 2, result=result)


@app.route("/round3/")
def round3():
    con = sqlite3.connect("/Users/navyamahajan/Library/CloudStorage/OneDrive-Personal(2)/Desktop/Alevel_2021/TASK4/Task4.db")
    cur = con.cursor()
    cur.execute('''SELECT competitor.name, scores.score 
                    FROM competitor JOIN scores ON competitor.id = scores.id
                    WHERE round = 3
                    ORDER BY scores.score DESC;''')
    result = cur.fetchall()
    con.close()
    return render_template("rounds.html", roundnum = 3, result=result)

@app.route("/mean/")
def mean():
    con = sqlite3.connect("/Users/navyamahajan/Library/CloudStorage/OneDrive-Personal(2)/Desktop/Alevel_2021/TASK4/Task4.db")
    cur = con.cursor()
    cur.execute('''SELECT competitor.name, round(AVG(scores.score),2)
                    FROM competitor JOIN scores 
                    ON competitor.id = scores.id
                    GROUP BY competitor.name
                    ORDER BY name ASC;''')
    result = cur.fetchall()
    con.close()
    return render_template("mean.html", result=result)


@app.route("/qualifiers/")
def qualifiers():
    con = sqlite3.connect("/Users/navyamahajan/Library/CloudStorage/OneDrive-Personal(2)/Desktop/Alevel_2021/TASK4/Task4.db")
    cur = con.cursor()
    cur.execute('''SELECT competitor.name as name, SUM(scores.score) as total, SUM(scores.score)>250 as qualified
                    FROM competitor JOIN scores 
                    ON competitor.id = scores.id 
                    GROUP BY name 
                    ORDER BY qualified DESC, total DESC;''')
    result = cur.fetchall()
    con.close()
    return render_template("qualifiers.html", result=result)


if __name__ == "__main__":
    app.run(debug = True)

