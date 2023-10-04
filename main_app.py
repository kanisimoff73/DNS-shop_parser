from flask import Flask, render_template, send_file, make_response
from parser import create_excel

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route('/download')
def generate_excel():
    create_excel()
    excel_file = 'statistics.xlsx'
    print('Сбор данных прошёл успешно!')
    return make_response(send_file(
        excel_file,
        as_attachment=True,
        download_name=f'statistics.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    ))


if __name__ == "__main__":
    app.run(debug=True)
