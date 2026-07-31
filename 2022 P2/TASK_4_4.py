from flask import Flask, render_template
import sqlite3
app = Flask(__name__, template_folder = "TASK_4_4")



@app.route("/")
def home():
    con = sqlite3.connect("")
    cur = con.cursor()
    
    cur.execute('''SELECT Member.FamilyName, Member.GivenName, Book.Title
                FROM Member JOIN Book JOIN Loan
                ON Loan.MemberNumber = Member.MemberNumber AND Loan.BookID = Book.BookID
                WHERE Loan.Returned = "FALSE"''')
    result = cur.fetchall()

    con.close()
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)