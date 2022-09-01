import py_scripts.init_and_load__ddl_dmldb as init
import py_scripts.utility as ut
import py_scripts.transactions as ld
import py_scripts.terminals as lt
import py_scripts.init_additionals_tbls as adt
import py_scripts.passport_blacklist as pbl
import py_scripts.rep_fraud as rf
import py_scripts.upload_file_to_archive as u
import py_scripts.init_rep_fraud as r


def preload(con):
    cursor = con.cursor()

    # Загрузка данных из файла ddl_dml.sql в базу данных
    init.create_db(cursor)


def create_etl_pipeline(con, date_report: str):
    cursor = con.cursor()

    # Создание в базе данных дополнительных таблиц отчетов
    adt.init_additional_tbls(cursor)
    date_report = date_report.replace('-', '')

    # Загрузка отчетов терминалов 
    path_terminals = r'terminals_' + date_report + '.xlsx'
    try:
        lt.load_terminals_report(con, path_terminals)
        u.upload(path_terminals)
    except (FileNotFoundError, IOError):
        print("Новый отчет по терминалам за интересующую вас дату не найден")
        ut.delete_tbl(cursor, 'STG_TERMINALS')
        ut.delete_view(cursor, 'STG_V_TERMINALS')
    
    # Загрузка отчетов транзакций
    path_transactions = r'transactions_' + date_report + '.txt'
    try:
        ld.load_transactions_report(con, path_transactions)
        u.upload(path_transactions)
    except (FileNotFoundError, IOError):
        print("Новый отчет по транзакциям за интересующую вас дату не найден")
        ut.delete_tbl(cursor, 'STG_TRANSACTIONS')
    
    # Загрузка отчетов паспортов
    path_pass = r'passport_blacklist_' + date_report + '.xlsx'
    try:
        pbl.load_passport_blacklist_report(con, path_pass)
        u.upload(path_pass)
    except (FileNotFoundError, IOError):
        print("Новый отчет по паспортам, занесенным в черный список, за интересующую вас дату не найден")
        ut.delete_tbl(cursor, 'STG_PASSPORT_BLACKLIST')


def create_fraud_report(con, date_report):
    r.init_rep_fraud_tbl(con)

    rf.if_fraud(con, date_report)
