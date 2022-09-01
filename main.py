import py_scripts.etl_pipeline as etl
import sqlite3
import py_scripts.utility as u


if __name__ == '__main__':
    con = sqlite3.connect('db.db')

    etl.preload(con)

    print('Пожалуйста, введите дату, за которую хотите получить отчет в формате dd-mm-yyyy')
    print('пример ожидаемого ввода:')
    print('01-03-2021')

    print('='*100)
    date_report = input()
    etl.create_etl_pipeline(con, date_report)
    etl.create_fraud_report(con, date_report)

   
    cursor = con.cursor()
    try:
        print('='*100)
        print('Отчет о мошеннических операциях в текущем месяце на ' + date_report)
        c = con.execute('select * from REP_FRAUD')
        names = list(map(lambda x: x[0], c.description))
        print(names)
        u.showTable(cursor, 'REP_FRAUD')
    except:
        print('Не удалось построить отчет')

