import imp
import py_scripts.sql_scripts as scr
import py_scripts.utility as u

def _init_rep_fraud_tbl(cursor):
    script = scr.tbl_rep_fraud_init()
    cursor.execute(script)


def init_rep_fraud_tbl(con):
    cursor = con.cursor()
    try:
        u.delete_tbl(cursor, 'REP_FRAUD')
        _init_rep_fraud_tbl(cursor)
    except: 
        print('Table\'s already existed.')
