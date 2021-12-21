def iug_load_gmag_wdc_relpath(sname,trange,addmaster,*extra,level='all',res='min'):
    dir_wdc=[]
    prefix=[]
    suffix=[]
    relpathnames=[]
    
    #fileformat='yyMM'
    #dirformat='YYYY/'
    
    relpathnames=''
    
    if(sname.lower()=='dst'):
        res='hour'
        if(level=='all' or level=='final'):
            dir_wdc.append(res+'/index/dst/')
            prefix.append(sname)
            suffix.append('')
        if(level=='all' or level[0:4]=='prov'):
            dir_wdc.append(res+'/index/pvdst/')
            prefix.append(sname)
            suffix.append('')
    elif(sname.lower()=='ae'):
        if(level=='all' or level=='final'):
            dir_wdc.extend([res+'/index/ae/',res+'/index/au/',res+'/index/al/',res+'/index/ao/'])
            prefix.extend(['ae.','au.','al.','ao.'])
            suffix.extend(['']*4)
        if(level=='all' or level[0:4]=='prov'):
            if(res=='min'):
                #before1996
                dir_wdc.extend([res+'/index/a.e/',res+'/index/a.u/',res+'/index/a.l/',res+'/index/a.o/'])
                prefix.extend(['ae.','au.','al.','ao.'])
                suffix.extend(['']*4)
                #after1995
                dir_wdc.extend([res+'/index/pvae/']*5)
                prefix.extend(['ae','au','al','ao','ax'])
                suffix.extend(['']*5)
    elif(sname.lower()=='sym'or sname.lower=='asy'):
        dir_wdc.append(res+'/index/asy/')
        prefix.append('asy')
        suffix.append('.wdc')
    else:
        dir_wdc.append(res+'/'+sname.lower()+'/')
        prefix.append(sname.lower())
        if(res=='min'):
            suffix.append('.wdc')
        else:
            suffix.append('')
    for i in range(len(dir_wdc)):
        #have not made this func yet
        file_daily=file_dailynames([dir_wdc[i],prefix[i],suffix[i],dir_format=dirformat,file_format=fileformat,trange=trange,addmaster=addmaster)
        #
        relpathnames.append(file_daily)
    return(relpathnames)
