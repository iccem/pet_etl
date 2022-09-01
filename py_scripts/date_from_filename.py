def get_date(filename):
    f = filename.split('_')
    f_ = f[-1].split('.')
    date_ = f_[0]
    temp_date = date_[4:] + '-' + date_[2:4] + '-' + date_[:2]
    return temp_date