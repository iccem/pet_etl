def showTable(cursor, tbl_name):
    cursor.execute('select * from ' + tbl_name)
    for row in cursor.fetchall():
        print(row)


def delete_tbl(cursor, tbl_name):
    cursor.execute(f'DROP TABLE if exists {tbl_name}')


def delete_view(cursor, tbl_name):
    cursor.execute(f'DROP VIEW if exists {tbl_name}')


def get_readable_date(report_dt):
    report_dt = report_dt.replace('-', '')
    readable_report_dt = report_dt[4:] + '-' + report_dt[2:4] + '-' + report_dt[:2]
    return readable_report_dt

