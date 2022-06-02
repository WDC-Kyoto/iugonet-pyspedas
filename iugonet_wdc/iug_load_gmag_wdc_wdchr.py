def iug_load_gmag_wdc_wdchr(addmaster,downloadonly=False,no_download=False,trange,verbose=2,level ="final",datatype="gmag",site=['kak', 'dst']):
    from pyspedas.cluster.load_csa import load_csa
    from pyspedas.wdc.iug_load_gmag_wdc_relpath import iug_load_gmag_wdc_relpath
    from pyspedas.utilities.download import download 
    import numpy as np
    vns = ['gmag']
    """
    if(type(datatype)==str):
        datatype=load_csa(datatype,)
    else:
        print('DATATYPE kw must be of string type.')
        return
     
    ssl_check_validnameが分からないのでパス
    """
    vsnames='kak dst'
    vsnames_sample=vsnames.split(' ')
    vsnames_all ='dst ae sym asy ABB AAA AAE ABG ABK ABN ACR ADA AED AGN AHM AIA AIF ALE ALH ALM ALU AMD AML AMN AMS AMT AMU ANC ANK ANN ANO APA API AQU ARC ARE ARK ARS ASC ASH ASK ASO ASP AVE AVI AWS AWY BAG BAL BBG BDE BDV BEL BEY BFE BFO BGA BGY BIN BJI BJN BKC BKK BLC BLT BMT BNA BNG BOC BOD BOP BOU BOX BRD BRS BRT BRW BSL BTI BTV BUZ BYR CAI CAO CAT CAX CBB CBI CCL CCP CCS CDN CDP CDS CEV CFI CHR CHT CKA CLA CLB CLF CLH CLI CLL CMB CMO CNB CNH COI COP CPA CPI CPS CPY CRC CSR CSS CSY CTA CTO CTX CUS CWE CZA CZT DAL DAR DAV DBN DIK DLN DLR DLT DOB DOU DRS DRV DUR DVS EAA EBR EGS EIC EKP ELI ELT ENB ENK EPN ESA ESK ETT EUA EUS EYR FAN FCC FCP FMM FRA FRD FRL FRN FSM FSP FSV FTN FUQ FUR FYU GCK GDH GEL GEN GIB GIM GIR GIT GJO GLM GLN GNA GRM GRW GTT GUA GUI GVD GWC GZH HAD HAN HBA HBK HBT HCR HEA HER HII HIS HKC HLL HLP HLS HLW HNA HON HRB HRI HRN HTY HUA HUS HVN HYB IBD INK IQA IRT ISC ISK ISL IVA IVI IZN JAI JOP JRV JUL KAK KAM KAR KDU KEM KGD KHB KHS KIR KIV KND KNG KNT KNY KNZ KOD KOR KOT KOU KRC KSA KSH KTG KTS KUM KUY KWJ KZA KZN LAA LAS LAU LDV LED LER LGR LIV LMD LMM LNN LNP LOB LOC LOV LOZ LPB LQA LRM LRV LSA LUA LUC LUK LVV LWI LYC LYN LZH LZV MAB MAN MAW MBC MBO MCL MCM MCP MCQ MDS MEA MEL MEV MFP MGD MGS MID MIR MIZ MJR MKL MLT MMB MMH MMK MNH MNK MNN MOG MOL MOS MRI MRN MUB MUT MWC MZL NAI NAL NAQ NCK NDA NEW NGK NGP NHO NKK NMP NMT NOK NOW NPF NPG NPH NPJ NPL NPM NRD NRW NSM NTS NUR NVL NVS NWP NWS NYI OAS ODE OKN ONW ORC OTT OUJ PAB PAF PAG PAI PBK PBQ PCU PEB PEG PET PHU PIL PIO PIU PLS PMG PND PNN POD POK POL POT PPT PRU PSM PST PTS PTU QGZ QIX QSB QUE QZH RAC RBD RDJ RES RIT ROB ROD RPC RSV RYB SAB SAH SAS SBA SCO SDH SED SEO SEY SFS SGG SHB SHL SHT SHU SIL SIM SIT SJG SKT SLU SMG SNA SNK SOD SOG SOR SOU SPA SPB SPL SPT SRE SRO SSH SSO STF STJ STO SUA SUB SVD SWI SYO SZT TAL TAM TAN TEH TEO TEV TFS THJ THL THU THY TIK TIP TIR TJO TKH TKT TLK TMB TMK TMP TNB TND TNG TOK TOL TOO TPA TRD TRO TRW TST TSU TTB TUC TUL TUM TUN UBA UGT UJJ UKH UMA UPS URC VAL VIC VLA VLJ VNA VOS VQS VSK VSS WAT WES WHN WHS WIA WIK WIL WIT WKE WLH WMQ WNG WNP WRH YAK YAU YCB YKC YSH YSS ZAR ZKW ZUY'
    vsnames_all=vsnames_all.lower()
    vsnames_all=vsnames_all.split(" ")
    
    site_in=site
    """
    wdc_sites = ssl_check_valid_name(site_in, vsnames_all,/ignore_case, /include_all, /no_warning)
    """
    if (wdc_sites[0]==''):
        return
    
    nsites=len(wdc_sites)
    missing_value=9999
    
    for i in range (nsites):
        #ここはまだ途中
        relpathname=iug_load_gmag_wdc_relpath(sname=wdc_sites[0],res='hour', level=level,trange=trange, addmaster=addmaster)
        
        """
            source = file_retrieve(/struct)
            source.verbose = verbose
            source.local_data_dir = root_data_dir() + 'iugonet/wdc_kyoto/geomag/'
            source.remote_data_dir = 'http://wdc-data.iugonet.org/data/'
            if no_download=True:
                source.no_server = 1
            #file_retrieveが分からん。spd
        """
        
        """
        local_files =download(remote_file=relpathnames, remote_path=source.remote_data_dir, local_path=source.local_data_dir, _extra=source, /last_version)
        """
        print(local_files)
        if downloadonly==True:
            continue
            
        elemlist = ''
        elemnum = -1
        elemlength = 0

        basetime_start =np.nan
        basetime_end =np.nan
        basetime_resolution = 86400.
        data_resolution = 3600.
        
        for j in range(len(local_files)):
            file = local_files[j]
            
        
