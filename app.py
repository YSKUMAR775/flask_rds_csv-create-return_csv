from flask import Flask, send_file
from module import mysql_connect, create_csv


app = Flask(__name__)


@app.route('/get_csv/<int:id>', methods=['Get'])
def fun_main(id):

    info_1 = mysql_connect.fun_connect()
    info_2 = create_csv.csv_create(id, info_1)

    return send_file(info_2, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
