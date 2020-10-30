import csv
# import pandas as pd


def csv_create(id, info_1):
    a = id
    cur = info_1.cursor()
    query = "select * from sql_flask_excel_table where id = '" + str(a) + "'"

    ##############(method-1)#############

    # df = pd.read_sql_query(query, con=mydb)
    # file_name = 'csv_data.csv'
    # df.to_csv(file_name, index=False)
    # return send_file(file_name, as_attachment=True)

    ###############(method-2)##############

    cur.execute(query)

    s = cur.fetchall()

    total_list = []
    for i in s:

        all_dict = {'id': i[0], 'name_info': i[1], 'mail': i[2], 'contact': i[3], 'address': i[4]}
        total_list.append(all_dict)

    list_columns = ['id', 'name_info', 'mail', 'contact', 'address']
    csv_path = 'C:/Users/Hemanth Y/Desktop/csv_file.csv'

    try:
        with open(csv_path, 'w') as csv_data:
            writer = csv.DictWriter(csv_data, fieldnames=list_columns)
            writer.writeheader()

            for data in total_list:
                writer.writerow(data)
    except IOError:
        print("I/O error")

    return csv_path
