from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download   import download
from config import CONFIG
import os
CONFIG={'local_data_dir_wdc':'iugonet/wdc_kyoto/geomag/','remote_data_dir_wdc':'http://wdc-data.iugonet.org/data/'}
def ae(trange,level,res):
    """
    trange= (Optional) Time range of interest  (2 element array), if
    this is not set, the default is to prompt the user. Note
    that if the input time range is not a full month, a full
    month's data is loaded.
    fomat is trange=["yyyy-mm-dd"] ex:trange=["2012-04-05","2012-04-15"]
    level = The level of the data, the default is 'final' for geomag data.
    For AE and Dst index, the default is ['final', 'provsional'].
    resolution(res) = Time resolution of the data: 'min' or 'hour',
    default set to 'min' for AE index and geomag data.
    """
    out_files = []
    dir_wdc=[]
    prefix=[]
    if(level=='all' or level=='final'):
        dir_wdc.extend([res+'/index/ae/',res+'/index/au/',res+'/index/al/',res+'/index/ao/'])
        prefix.extend(['ae.','au.','al.','ao.'])
    if(level=='all' or level[0:4]=='prov'):
        if(res=='min'):
                #before1996
            dir_wdc.extend([res+'/index/a.e/',res+'/index/a.u/',res+'/index/a.l/',res+'/index/a.o/'])
            prefix.extend(['ae.','au.','al.','ao.'])
                #after1995
            dir_wdc.extend([res+'/index/pvae/']*5)
            prefix.extend(['ae','au','al','ao','ax'])
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc[i],suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix=prefix[i], directory=dir_2[0])
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])
        if local_files is not None:
                for file in local_files:
                    out_files.append(file)
    out_files = sorted(out_files)
    return out_files
def dst(trange,level):
    """
    trange= (Optional) Time range of interest  (2 element array), if
          this is not set, the default is to prompt the user. Note
          that if the input time range is not a full month, a full
          month's data is loaded.
          fomat is trange=["yyyy-mm-dd"] ex:trange=["2012-04-05","2012-04-15"]

    level = The level of the data, the default is 'final' for geomag data.
          For AE and Dst index, the default is ['final', 'provsional'].
    """
    out_files = []
    dir_wdc=[]
    prefix=[]
    res='hour'
    if(level=='all' or level=='final'):
        dir_wdc.append(res+'/index/dst/')
        prefix.append("dst")
    if(level=='all' or level[0:4]=='prov'):
        dir_wdc.append(res+'/index/pvdst/')
        prefix.append("dst")
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc[i],suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix=prefix[i], directory=dir_2[0])
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])
        if local_files is not None:
                for file in local_files:
                    out_files.append(file)
    out_files = sorted(out_files)
    return out_files
def aym(trange,res='min'):
    #resにはminかhourしか入らないようにエラーメッセージ出したほうがいいかも（minデータしかない？？）
    #levelもつけておいて無視の方がエラー少なくなるかも,level=Falseを初期値で与える？
    """
    ;trange= (Optional) Time range of interest  (2 element array), if
    ;     this is not set, the default is to prompt the user. Note
    ;      that if the input time range is not a full month, a full
    ;      month's data is loaded.
    ;      fomat is trange=["yyyy-mm-dd"] ex:trange=["2012-04-05","2012-04-15"]
    ;resolution(res) = Time resolution of the data: 'min' or 'hour',
    ;default set to 'min' for AE index and geomag data.
    """
    out_files=[]
    dir_wdc=res+'/index/asy/'
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc,suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix='asy', directory=dir_2[0],suffix='.wdc')
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])
        if local_files is not None:
            for file in local_files:
                out_files.append(file)
    out_files = sorted(out_files)
    return out_files
def sym(trange,res='min'):
    """
    ;trange= (Optional) Time range of interest  (2 element array), if
    ;this is not set, the default is to prompt the user. Note
    ;that if the input time range is not a full month, a full
    ;month's data is loaded.
    ;fomat is trange=["yyyy-mm-dd"] ex:trange=["2012-04-05","2012-04-15"]
    ;resolution(res) = Time resolution of the data: 'min' or 'hour',
    ;default set to 'min' for AE index and geomag data.
    """
    out_files = []
    dir_wdc=res+'/index/asy/'
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc,suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix='asy', directory=dir_2[0],suffix='.wdc')
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])
        if local_files is not None:
            for file in local_files:
                out_files.append(file)
    out_files = sorted(out_files)
    return out_files
def site(trange,site,res):
    """
    trange= (Optional) Time range of interest  (2 element array), if
    this is not set, the default is to prompt the user. Note
    that if the input time range is not a full month, a full
    month's data is loaded.
    fomat is trange=["yyyy-mm-dd"] ex:trange=["2012-04-05","2012-04-15"]
    resolution(res) = Time resolution of the data: 'min' or 'hour',
    ;default set to 'min' for AE index and geomag data.
    site=Station ABB code or name of geomagnetic index.
    ;          Ex1) iug_load_gmag_wdc, site = 'kak', ...
    ;          Ex2) iug_load_gmag_wdc, site = ['dst', 'ae'], ...
    ;          If you skip this option, AE Dst SYM/ASY and KAK data are retrieved.
    vsnames='ABB AAA AAE ABG ABK ABN ACR ADA AED AGN AHM AIA AIF ALE ALH ALM ALU AMD AML AMN AMS AMT AMU ANC ANK ANN ANO APA API AQU ARC ARE ARK ARS ASC ASH ASK ASO ASP AVE AVI AWS AWY BAG BAL BBG BDE BDV BEL BEY BFE BFO BGA BGY BIN BJI BJN BKC BKK BLC BLT BMT BNA BNG BOC BOD BOP BOU BOX BRD BRS BRT BRW BSL BTI BTV BUZ BYR CAI CAO CAT CAX CBB CBI CCL CCP CCS CDN CDP CDS CEV CFI CHR CHT CKA CLA CLB CLF CLH CLI CLL CMB CMO CNB CNH COI COP CPA CPI CPS CPY CRC CSR CSS CSY CTA CTO CTX CUS CWE CZA CZT DAL DAR DAV DBN DIK DLN DLR DLT DOB DOU DRS DRV DUR DVS EAA EBR EGS EIC EKP ELI ELT ENB ENK EPN ESA ESK ETT EUA EUS EYR FAN FCC FCP FMM FRA FRD FRL FRN FSM FSP FSV FTN FUQ FUR FYU GCK GDH GEL GEN GIB GIM GIR GIT GJO GLM GLN GNA GRM GRW GTT GUA GUI GVD GWC GZH HAD HAN HBA HBK HBT HCR HEA HER HII HIS HKC HLL HLP HLS HLW HNA HON HRB HRI HRN HTY HUA HUS HVN HYB IBD INK IQA IRT ISC ISK ISL IVA IVI IZN JAI JOP JRV JUL KAK KAM KAR KDU KEM KGD KHB KHS KIR KIV KND KNG KNT KNY KNZ KOD KOR KOT KOU KRC KSA KSH KTG KTS KUM KUY KWJ KZA KZN LAA LAS LAU LDV LED LER LGR LIV LMD LMM LNN LNP LOB LOC LOV LOZ LPB LQA LRM LRV LSA LUA LUC LUK LVV LWI LYC LYN LZH LZV MAB MAN MAW MBC MBO MCL MCM MCP MCQ MDS MEA MEL MEV MFP MGD MGS MID MIR MIZ MJR MKL MLT MMB MMH MMK MNH MNK MNN MOG MOL MOS MRI MRN MUB MUT MWC MZL NAI NAL NAQ NCK NDA NEW NGK NGP NHO NKK NMP NMT NOK NOW NPF NPG NPH NPJ NPL NPM NRD NRW NSM NTS NUR NVL NVS NWP NWS NYI OAS ODE OKN ONW ORC OTT OUJ PAB PAF PAG PAI PBK PBQ PCU PEB PEG PET PHU PIL PIO PIU PLS PMG PND PNN POD POK POL POT PPT PRU PSM PST PTS PTU QGZ QIX QSB QUE QZH RAC RBD RDJ RES RIT ROB ROD RPC RSV RYB SAB SAH SAS SBA SCO SDH SED SEO SEY SFS SGG SHB SHL SHT SHU SIL SIM SIT SJG SKT SLU SMG SNA SNK SOD SOG SOR SOU SPA SPB SPL SPT SRE SRO SSH SSO STF STJ STO SUA SUB SVD SWI SYO SZT TAL TAM TAN TEH TEO TEV TFS THJ THL THU THY TIK TIP TIR TJO TKH TKT TLK TMB TMK TMP TNB TND TNG TOK TOL TOO TPA TRD TRO TRW TST TSU TTB TUC TUL TUM TUN UBA UGT UJJ UKH UMA UPS URC VAL VIC VLA VLJ VNA VOS VQS VSK VSS WAT WES WHN WHS WIA WIK WIL WIT WKE WLH WMQ WNG WNP WRH YAK YAU YCB YKC YSH YSS ZAR ZKW ZUY'
    """
    site2=site.split(" ")
    out_files = []
    dir_wdc=[]
    prefix=[]
    suffix=[]
    for i in range(len(site2)):
        dir_wdc.append(res+'/'+site2[i].lower()+'/')
        prefix.append(site2[i].lower())
        if(res=='min'):
            suffix.append('.wdc')
        else:
            suffix.append('')
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc[i],suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix=prefix[i], directory=dir_2[0],suffix=suffix[i])
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])
        if local_files is not None:
            for file in local_files:
                out_files.append(file)
    out_files = sorted(out_files)
    return out_files
