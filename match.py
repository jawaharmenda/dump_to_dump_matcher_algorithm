def closematch(val):
    global matchresult
    try:
        if ' ' not in val:
            f_val=val.split('||')[0]
            f_val_city=val.split('||')[1]
            if f_val in l_count:
                l_val=[i for i,x in enumerate(l) if x==str(f_val)]
                l_val_city=[i for i,x in enumerate(l_1) if x==str(f_val_city)]
                l_val_final=list(set(l_val).intersection(l_val_city))
                best_match=difflib.get_close_matches(val,[df_restcount['clean_name_city'][k] for k in l_val_final],1)[0]
                matchresult=val+";"+best_match
            else:
                matchresult='no match'
        else:
            f_val=val.split()[0]
            f_val_city=val.split('||')[1]
            if f_val in l_count:
                l_val=[i for i,x in enumerate(l) if x==str(f_val)]
                l_val_city=[i for i,x in enumerate(l_1) if x==str(f_val_city)]
                l_val_final=list(set(l_val).intersection(l_val_city))
                best_match=difflib.get_close_matches(val,[df_restcount['clean_name_city'][k] for k in l_val_final],1)[0]
                matchresult=val+";"+best_match
            else:
                matchresult='no match'
    except:
        matchresult='no match'
    return matchresult