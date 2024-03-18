# VALIDADOR MARC 21
# CDI - ESENFC

from pymarc import MARCReader
import csv
import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename


def validaMarc():
    relatorio = []
    relatores = ['abr','acp','act','adi','adp','aft','anl','anm','ann','ant','ape','apl','app','aqt','arc','ard','arr','art','asg','asn','ato','att','auc','aud','aui','aus','aut','bdd','bjd','bkd','bkp','blw','bnd','bpd','brd','brl','bsl','cas','ccp','chr','clb','cli','cll','clr','clt','cmm','cmp','cmt','cnd','cng','cns','coe','col','com','con','cor','cos','cot','cou','cov','cpc','cpe','cph','cpl','cpt','cre','crp','crr','crt','csl','csp','cst','ctb','cte','ctg','ctr','cts','ctt','cur','cwt','dbp','dfd','dfe','dft','dgc','dgg','dgs','dis','dln','dnc','dnr','dpc','dpt','drm','drt','dsr','dst','dtc','dte','dtm','dto','dub','edc','edm','edt','egr','elg','elt','eng','enj','etr','evp','exp','fac','fds','fld','flm','fmd','fmk','fmo','fmp','fnd','fpy','frg','gis','grt','his','hnr','hst','ill','ilu','ins','inv','isb','itr','ive','ivr','jud','jug','lbr','lbt','ldr','led','lee','lel','len','let','lgd','lie','lil','lit','lsa','lse','lso','ltg','lyr','mcp','mdc','med','mfp','mfr','mod','mon','mrb','mrk','msd','mte','mtk','mus','nrt','opn','org','orm','osp','oth','own','pad','pan','pat','pbd','pbl','pdr','pfr','pht','plt','pma','pmn','pop','ppm','ppt','pra','prc','prd','pre','prf','prg','prm','prn','pro','prp','prs','prt','prv','pta','pte','ptf','pth','ptt','pup','rbr','rcd','rce','rcp','rdd','red','ren','res','rev','rpc','rps','rpt','rpy','rse','rsg','rsp','rsr','rst','rth','rtm','sad','sce','scl','scr','sds','sec','sgd','sgn','sht','sll','sng','spk','spn','spy','srv','std','stg','stl','stm','stn','str','tcd','tch','ths','tld','tlp','trc','trl','tyd','tyg','uvp','vac','vdg','voc','wac','wal','wam','wat','wdc','wde','win','wit','wpr','wst']
    listamarc = {'010':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b','z','8']},
                 '016':{'rep':[True],'ind1':['\\','7'],'ind2':['\\'],'subcampo':['a','z','2','8']},
                 '017':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b']},
                 '020':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','c','z']},
                 '022':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','y','z']},
                 '024':{'rep':[True],'ind1':['0','2','7'],'ind2':['\\'],'subcampo':['a','c','d','z','2']},
                 '034':{'rep':[True],'ind1':['0','1','2'],'ind2':['\\','0','1'],'subcampo':['a','b','c','d','e','f','g','h','j','k','m','n','p','s','t']},
                 '035':{'rep':[False],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','z']},
                 '040':{'rep':[False],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b','c','d']},
                 '041':{'rep':[False],'ind1':['0','1'],'ind2':['\\','7'],'subcampo':['a','b','d','e','f','g','h']},
                 '044':{'rep':[False],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '080':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','x','2','z']},
                 '084':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','2']},
                 '100':{'rep':[False],'ind1':['0','1','2'],'ind2':['\\'],'subcampo':['a','b','c','d','4']},
                 '110':{'rep':[False],'ind1':['0','1','2'],'ind2':['\\'],'subcampo':['a','b','g','4']},
                 '111':{'rep':[False],'ind1':['0','1','2'],'ind2':['\\'],'subcampo':['a','c','d','n','4']},
                 '130':{'rep':[False],'ind1':['0','1','2','3','4','5','6','7','8','9'],'ind2':['\\'],'subcampo':['a','d','f','g','k','l','m','n','o','p','r','s']},
                 '210':{'rep':[True],'ind1':['0','1'],'ind2':['\\','0'],'subcampo':['a','b','2']},
                 '222':{'rep':[True],'ind1':['\\'],'ind2':['0','1','2','3','4','5','6','7','8','9'],'subcampo':['a','b']},
                 '240':{'rep':[False],'ind1':['0','1'],'ind2':['0','1','2','3','4','5','6','7','8','9'],'subcampo':['a','d','f','g','h','k','l','m','n','o','p','r','s']},
                 '242':{'rep':[True],'ind1':['0','1'],'ind2':['0','1','2','3','4','5','6','7','8','9'],'subcampo':['a','b','c','h','n','p','y']},
                 '245':{'rep':[False],'ind1':['0','1'],'ind2':['0','1','2','3','4','5','6','7','8','9'],'subcampo':['a','b','c','h','n','p']},
                 '246':{'rep':[False],'ind1':['0','1','2','3'],'ind2':['\\','0','1','2','3','4','5','6','7','8'],'subcampo':['a','b','f','g','h','i','n','p']},
                 '247':{'rep':[False],'ind1':['0','1'],'ind2':['0','1'],'subcampo':['a','b','c','h','n','p','f','g','x']},
                 '250':{'rep':[False],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b']},
                 '255':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b','c','d','e']},
                 '256':{'rep':[False],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '260':{'rep':[True],'ind1':['\\','2','3'],'ind2':['\\'],'subcampo':['a','b','c','e','f','g']},
                 '300':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b','c','e']},
                 '310':{'rep':[False],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b']},
                 '321':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b']},
                 '336':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','2']},
                 '337':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','2']},
                 '362':{'rep':[False],'ind1':['0','1'],'ind2':['\\'],'subcampo':['a','z']},
                 '490':{'rep':[True],'ind1':['0','1'],'ind2':['\\'],'subcampo':['a','v','x']},
                 '500':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '501':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '502':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '504':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '505':{'rep':[True],'ind1':['0','1','2','8'],'ind2':['\\','0'],'subcampo':['a']},
                 '506':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '508':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '510':{'rep':[True],'ind1':['0','1','2','3','4'],'ind2':['\\'],'subcampo':['a','b','c','x']},
                 '515':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '516':{'rep':[True],'ind1':['\\','8'],'ind2':['\\'],'subcampo':['a']},
                 '520':{'rep':[True],'ind1':['\\','0','1','2','3'],'ind2':['\\'],'subcampo':['a']},
                 '521':{'rep':[True],'ind1':['\\','0','1','2','3','4','8'],'ind2':['\\'],'subcampo':['a','b']},
                 '525':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '530':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','u']},
                 '533':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b','c','d','e','f','m','n']},
                 '534':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b','c','e','f','k','l','m','n','p','t','x','z']},
                 '538':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','i','u']},
                 '546':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','b']},
                 '550':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '555':{'rep':[True],'ind1':['\\','0','1'],'ind2':['\\'],'subcampo':['a']},
                 '580':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a']},
                 '585':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','5']},
                 '586':{'rep':[True],'ind1':['\\','8'],'ind2':['\\'],'subcampo':['a']},
                 '600':{'rep':[True],'ind1':['0','1','3'],'ind2':['0','1','2','3','4','5','6','7'],'subcampo':['a','b','c','d','t','v','x','y','z','2']},
                 '610':{'rep':[True],'ind1':['0','1','2'],'ind2':['0','1','2','3','4','5','6','7'],'subcampo':['a','b','v','x','y','z','2']},
                 '611':{'rep':[True],'ind1':['0','1','2'],'ind2':['0','1','2','3','4','5','6','7'],'subcampo':['a','c','d','n','v','x','y','z','2']},
                 '630':{'rep':[False],'ind1':['0','1','2','3','4','5','6','7','8','9'],'ind2':['0','1','2','3','4','5','6','7'],'subcampo':['a','d','f','g','h','k','l','m','n','o','p','r','s','v','x','y','z','2']},
                 '650':{'rep':[True],'ind1':['\\','0','1','2'],'ind2':['0','1','2','3','4','5','6','7'],'subcampo':['a','v','x','y','z','2']},
                 '651':{'rep':[True],'ind1':['\\'],'ind2':['0','1','2','3','4','5','6','7'],'subcampo':['a','v','x','y','z','2']},
                 '655':{'rep':[True],'ind1':['\\','0'],'ind2':['0','1','2','3','4','5','6','7'],'subcampo':['a','x','y','z']},
                 '700':{'rep':[True],'ind1':['0','1','2'],'ind2':['\\','2'],'subcampo':['a','b','c','d','4']},
                 '710':{'rep':[True],'ind1':['0','1','2'],'ind2':['\\','2'],'subcampo':['a','b','g','4']},
                 '711':{'rep':[False],'ind1':['0','1','2'],'ind2':['\\','2'],'subcampo':['a','c','d','n','4']},
                 '730':{'rep':[True],'ind1':['0','1','2','3','4','5','6','7','8','9'],'ind2':['\\','2'],'subcampo':['a','d','f','g','k','l','m','n','o','p','r','s']},
                 '740':{'rep':[True],'ind1':['0','1','2','3','4','5','6','7','8','9'],'ind2':['\\','2'],'subcampo':['a','h','n','p']},
                 '752':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['d']},
                 '754':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','c','d','x','z','2']},
                 '765':{'rep':[True],'ind1':['0','1'],'ind2':['\\','8'],'subcampo':['a','b','c','d','g','h','i','k','l','m','n','o','r','s','t','u','v','w','x','y','z','4','6','7','8']},
                 '767':{'rep':[True],'ind1':['0','1'],'ind2':['\\','8'],'subcampo':['t']},
                 '770':{'rep':[True],'ind1':['0','1'],'ind2':['\\','8'],'subcampo':['t','w']},
                 '772':{'rep':[True],'ind1':['0','1'],'ind2':['\\','8'],'subcampo':['t','w']},
                 '773':{'rep':[True],'ind1':['0','1'],'ind2':['\\','8'],'subcampo':['a','t','d','g','x','b','z',]},
                 '776':{'rep':[True],'ind1':['0','1'],'ind2':['\\','8'],'subcampo':['t','w']},
                 '777':{'rep':[True],'ind1':['0','1'],'ind2':['\\','8'],'subcampo':['t']},
                 '780':{'rep':[True],'ind1':['0','1'],'ind2':['0','1','2','3','4','5','6','7'],'subcampo':['t']},
                 '785':{'rep':[True],'ind1':['0','1'],'ind2':['0','1','2','3','4','5','6','7','8'],'subcampo':['t','x']},
                 '830':{'rep':[True],'ind1':['\\'],'ind2':['0','1','2','3','4','5','6','7','8','9'],'subcampo':['a','d','f','g','h','k','l','m','n','o','p','r','s','t','v','x','3']},
                 '856':{'rep':[True],'ind1':['\\','0','1','2','3','4','7'],'ind2':['\\','0','1','2','8'],'subcampo':['a','b','c','d','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','2','3']},
                 '907':{'rep':[True],'ind1':['0'],'ind2':['0'],'subcampo':['f','g','i','j']},
                 '945':{'rep':[True],'ind1':['\\'],'ind2':['\\'],'subcampo':['a','c','i','g','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']}
                 }
    
    

    filem = askopenfilename(filetypes =[('MARC Binário', '*.mrc')])
    with open(filem, 'rb') as fh:
        reader = MARCReader(fh)
        for record in reader:
            bibprinc = record['998']['a']
            biblio = record['908']['a']
            biblioId = biblio[1:]
            #Verifica se contém a sigla inválida "esenf" no campo biblioteca.
            if "esenf" in record['998'].value():
                relatorio.append([biblioId,bibprinc,'998',"esenf","Verificar o código da biblioteca."])
            if record.leader[7] == 'b' and (bibprinc == "enfa" or bibprinc == "enfb"):
                relatorio.append([biblioId,bibprinc,'Leader',"b","Verificar o nível bibliográfico da parte componente."])
            #Identifica erros em monografias da biblioteca proprietária "enfa" e "enfb".
            if record.leader[7] == 'm' and (bibprinc == "enfa" or bibprinc == "enfb"):

                recordlist = []
                for field in record:
                    campo1 = str(field)
                    camp = campo1[1:4]
                    in1 = campo1[6]
                    in2= campo1[7]
                    if camp == '001' or camp == '005' or camp == '008' or camp == '998' or camp == '908':
                        continue
                    if campo1[1:4] == '945':
                        nrexem = campo1.find('$y')
                        if nrexem >= 0:
                            exemplar = campo1[nrexem + 3:nrexem + 12]
                    if camp not in listamarc:
                        relatorio.append([biblioId,bibprinc,campo1[1:4],'',"Verificar se o campo é válido."])
                        continue
                    if camp in recordlist and listamarc[camp]['rep'] == False:
                        relatorio.append([biblioId,bibprinc,campo1[1:4],'',"Verificar se o campo é repetível."])
                    else:
                        recordlist.append(camp)
                    if in1 not in listamarc[camp]['ind1']:
                        relatorio.append([biblioId,bibprinc,campo1[1:4] + ' ' + in1 + in2,'',"Verificar se o 1.º indicador é válido."])
                    if in2 not in listamarc[camp]['ind2']:
                        relatorio.append([biblioId,bibprinc,campo1[1:4] + ' ' + in1 + in2,'',"Verificar se o 2.º indicador é válido."])
                    for subfield in field:
                        if subfield[0] not in listamarc[camp]['subcampo']:
                            relatorio.append([biblioId,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1], "Verificar se o subcampo é válido."])
                        if campo1[1:4] == '945':
                            if re.search('^\s', subfield[1]) is not None and subfield[0] == 'l':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar o preenchimento do local do exemplar."])
                            if '$lenf' not in campo1:
                                continue
                            if re.search('\s$', subfield[1]) is not None and subfield[0] == 's':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar o preenchimento do subcampo Estado do exemplar."])
                            if re.search('^\s', subfield[1]) is not None and subfield[0] == 'o':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar o preenchimento do subcampo Código 2 do exemplar."])
                            if re.search('^\s', subfield[1]) is not None and subfield[0] == 'q':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar o preenchimento do subcampo Mensagem do exemplar."])
                            if re.search('^\s', subfield[1]) is not None and subfield[0] == 'r':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar o preenchimento do subcampo Mensagem OPAC do exemplar."])
                            if re.search('\s$', subfield[1]) is not None and subfield[0] == 'a':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo cota não termina com um espaço."])
                            if re.search('^\s', subfield[1]) is not None and subfield[0] == 'a':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo cota não inicia com um espaço."])
                            if re.search('\s$', subfield[1]) is not None and subfield[0] == 'n':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo n.º do registo/nota não termina com um espaço."])
                            if re.search('^\s', subfield[1]) is not None and subfield[0] == 'n':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo n.º do registo/nota não inicia com um espaço."])
                            if re.search('\s$', subfield[1]) is not None and subfield[0] == 'i':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo código de barras não termina com um espaço."])
                            if re.search('^\s', subfield[1]) is not None and subfield[0] == 'i':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo código de barras não inicia com um espaço."])
                            if re.search('\s$', subfield[1]) is not None and subfield[0] == 'm':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo mensagem não termina com um espaço."])
                            if re.search('^\s', subfield[1]) is not None and subfield[0] == 'm':
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo mensagem não inicia com um espaço."])
                            if re.search('\s$', subfield[1]) is not None and (subfield[0] == 'g' or subfield[0] == 'h' or subfield[0] == 'c'):
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo não termina com um espaço."])
                            if re.search('^\s', subfield[1]) is not None and (subfield[0] == 'g' or subfield[0] == 'h' or subfield[0] == 'c'):
                                relatorio.append([biblioId + "/" + exemplar,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo não inicia com um espaço."])
                      
                        else:
                            if re.search('\s$', subfield[1]) is not None: 
                                relatorio.append([biblioId,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo não termina com um espaço."])
                            if re.search('^\s', subfield[1]) is not None:
                                relatorio.append([biblioId,bibprinc,campo1[1:4] + ' ' + in1 + in2 + " |" + subfield[0],subfield[1],"Verificar se o subcampo não inicia com um espaço."])
                for field in record.get_fields():
                    campo = str(field)
                    if campo[1:4] == '998':
                        continue   
                    if "  " in campo[6:] and campo[1:4] != '945':
                        relatorio.append([biblioId,bibprinc,campo[1:4],campo,"Verificar espaçamento duplo."])
                    if "  " in campo[6:] and campo[1:4] == '945':
                        if "$lenfa" in campo:
                            relatorio.append([biblioId,bibprinc,campo[1:4],campo,"Verificar espaçamento duplo."])
                        if "$lenfb" in campo:
                            relatorio.append([biblioId,bibprinc,campo[1:4],campo,"Verificar espaçamento duplo."])
                    if ",," in campo[6:]:
                            relatorio.append([biblioId,bibprinc,campo[1:4],campo,"Verificar vírgula."])
                    if " , " in campo[6:]:
                        relatorio.append([biblioId,bibprinc,campo[1:4],campo,"Verificar espaço antes da vírgula."])
                    if campo[1:4] == '250' and (re.search('\$a\d\{u00AA\}\s', campo) is not None or re.search('\$a\d\d\{u00AA\}\s', campo) is not None):
                        relatorio.append([biblioId,bibprinc,campo[1:4],campo,"Verificar abreviatura ordinal."])
                if record['260'] is not None:
                    string=record['260'].value()
                    if not(string[-1] == '.' or string[-1] == '-' or string[-1] == ']' or string[-1] == ')'):
                        relatorio.append([biblioId,bibprinc,'260',record['260'].value(),"Verificar se o campo termina com pontuação válida."])
                if record['250'] is not None:
                    string=record['250'].value()
                    if not(string[-1] == '.'):
                        relatorio.append([biblioId,bibprinc,'250',record['250'].value(),"Verificar se o campo termina com pontuação válida."])
                if record['100'] is not None:
                    string=record['100'].value()
                    if (not(string[-1] == '.') and not(string[-1] == '-')) or (string[-2:] == '-.'):
                        relatorio.append([biblioId,bibprinc,'100',record['100'].value(),"Verificar se o campo termina com pontuação válida."])
                if record['110'] is not None:
                    string=record['110'].value()
                    if not(string[-1] == '.'):
                        relatorio.append([biblioId,bibprinc,'110',record['110'].value(),"Verificar se o campo termina com pontuação válida."])
                if record['111'] is not None:
                    string=record['111'].value()
                    if not(string[-1] == '.'):
                        relatorio.append([biblioId,bibprinc,'111',record['111'].value(),"Verificar se o campo termina com pontuação válida."])
                if record['130'] is not None:
                    string=record['130'].value()
                    if not(string[-1] == '.'):
                        relatorio.append([biblioId,bibprinc,'130',record['130'].value(),"Verificar se o campo termina com pontuação válida."])
                if record['245'] is not None:
                    string=record['245'].value()
                    if not(string[-1] == '.'):
                        relatorio.append([biblioId,bibprinc,'245',record['245'].value(),"Verificar se o campo termina com pontuação válida."])
                if record['245'] is not None and "= " in record['245'].value() and record['246'] is None:
                    relatorio.append([biblioId,bibprinc,'245',record['245'].value(),"Verificar se o campo 246 está preenchido."])
                if record['245'] is not None and "= " in record['245'].value() and record['246'] is not None:
                    indica2=record['246'].indicator2
                    if indica2 != '1':
                        relatorio.append([biblioId,bibprinc,'245',record['245'].value(),"Verificar o segundo indicador do campo 246."])
                if record['300'] is not None and record['490'] is not None:
                    string=record['300'].value()
                    if not(string[-1] == '.'):
                        relatorio.append([biblioId,bibprinc,'300',record['300'].value(),"Verificar se o campo termina com pontuação válida."])
                if record['300'] is not None and record['490'] is None and "cm." in record['300'].value():
                    string=record['300'].value()
                    if string[-3:] == 'cm.':
                        relatorio.append([biblioId,bibprinc,'300',record['300']['c']," Verificar abreviatura \"cm\"."])
                if record['440'] is not None:
                    relatorio.append([biblioId,bibprinc,'440',record['440'].value(),"Campo obsoleto. Ver campo 490."])
                if record['490'] is not None:
                    string=record['490'].value()
                    if string[-1] == '.':
                        relatorio.append([biblioId,bibprinc,'490',record['490'].value(),"Verificar se o campo termina com pontuação válida."])
                if record:
                    for notas in record.get_fields('500', '501', '502','504','506','507','508','515', '518','520','521','525','530','534','538','545','546','550','561','580','583','586'):
                        novo = str(notas)
                        if novo[-1] != '.':
                            relatorio.append([biblioId,bibprinc,novo[1:4],novo[1:],"Verificar se o campo termina com pontuação válida."])
                        if "\\$a<" in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],novo[1:],"Verificar caracteres inválidos, ex. \"<\", \">\", \"{\""])
                if record:
                    for notas in record.get_fields('650'):
                        novo = str(notas)
                        if '$2' in novo:
                            if '.$2' not in novo:
                                relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find('$2')-4:novo.find('$2')+3] + ' ...',"Verificar a pontuação precedente do subcampo 2."])
                        if '.$x' in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find('.$x')-4:novo.find('.$x')+3] + ' ...',"Verificar a pontuação precedente do subcampo."])
                        if ' $x' in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find(' $x')-4:novo.find(' $x')+3] + ' ...',"Verificar o espaço precedente do subcampo."])
                        if '.$v' in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find('.$v')-4:novo.find('.$v')+3] + ' ...',"Verificar a pontuação precedente do subcampo."])
                        if ' $v' in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find('.$v')-4:novo.find('.$v')+3] + ' ...',"Verificar o espaço precedente do subcampo."])
                        if '.$y' in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find('.$y')-4:novo.find('.$y')+3] + ' ...',"Verificar a pontuação precedente do subcampo."])
                        if ' $y' in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find('.$y')-4:novo.find('.$y')+3] + ' ...',"Verificar o espaço precedente do subcampo."])
                        if '.$z' in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find('.$z')-4:novo.find('.$z')+3] + ' ...',"Verificar a pontuação precedente do subcampo."])
                        if ' $z' in novo:
                            relatorio.append([biblioId,bibprinc,novo[1:4],'... ' + novo[novo.find('.$z')-4:novo.find('.$z')+3] + ' ...',"Verificar o espaço precedente do subcampo."])
                if record:
                    lista=[]
                    for notas in record.get_fields('650', '610','611','630','651','655'):
                        novo = str(notas)
                        if '$x' in novo and '$a' in novo:
                            prelator = novo.find("$x") + 2
                            if '.$z' in novo:
                                fimrelator = novo.find(".$z" )
                            elif '.$2' in novo:  
                                fimrelator = novo.find(".$2" )
                            else:
                                fimrelator = novo.find("$2" )
                            relatorx = novo[prelator:fimrelator]
                            lista.append(relatorx.lower())
                            arelator = novo.find("$a") + 2
                            afimrelator = novo.find("$x")
                            arelatorx = novo[arelator:afimrelator]
                            lista.append(arelatorx.lower())
                    if len(lista) > 3 and (lista[0] == lista[3] and lista[1] == lista[2]):
                        relatorio.append([biblioId,bibprinc,'650',[lista],"Verificar se o campo 650 está repetido."])
                    if len(lista) > 6 and (lista[4] == lista[7] and lista[5] == lista[6]):
                        relatorio.append([biblioId,bibprinc,'650',[lista],"Verificar se o campo 650 está repetido."]) 
                if record:
                    for notasb in record.get_fields('700', '710', '711'):
                        novob = str(notasb)
                        subfield = '$'
                        if novob[-1] == '.' or novob[-1] == '-':
                            if novob.count(subfield) == 1 and '$a' in novob:
                                continue
                            else:
                                relatorio.append([biblioId,bibprinc,novob[1:4],novob[1:],"Verificar se o campo termina com pontuação válida."])
                if record:
                    for notasc in record.get_fields('700', '710', '711'):
                        novoc = str(notasc)
                        if '$4' in novoc:
                            prelator = novoc.find("$4") + 2
                            fimrelator = prelator + 3
                            relator = novoc[prelator:fimrelator]
                            if relator not in relatores:
                                relatorio.append([biblioId,bibprinc,novoc[1:4],novoc[1:],"Verificar o código de função."])                                         
                        if '$4' in novoc and ',$4' not in novoc:
                            relatorio.append([biblioId,bibprinc,novoc[1:4],novoc[1:],"Adicionar vírgula \",\" antes do subcampo 4"])
                if record:
                    for notasg in record.get_fields('773'):
                        novog = str(notasg)
                        if '$x' in novog and '$xISSN' not in novog:
                            relatorio.append([biblioId,bibprinc,'773x',novog[1:],"Verificar o subcampo |x do campo 773."])
                        if '$dISSN' in novog or '$dVol.' in novog or '$dN\{u00BA\}' in novog:
                            relatorio.append([biblioId,bibprinc,'773d',novog[1:],"Verificar o subcampo |d do campo 773."])
                        if ('$x' in novog and '$g' not in novog) or ('$t' in novog and '$g' not in novog):
                            relatorio.append([biblioId,bibprinc,'773g',novog[1:],"Verificar se o subcampo |g do campo 773 está preenchido."])
                        if '$gISSN' in novog:
                            relatorio.append([biblioId,bibprinc,'773g',novog[1:],"Verificar o subcampo |g do campo 773."])
                        if '.- ' in novog:
                            relatorio.append([biblioId,bibprinc,'773g',novog[1:],"Verificar a pontuação do campo 773."])
                        
                if record['830'] is not None:
                    string=record['830'].value()
                    if string[-1] != '.':
                        relatorio.append([biblioId,bibprinc,'830',string,"Verificar se o campo termina com pontuação válida."])                         
                if record['260'] is not None:
                    stringc=record['260']['a']
                    stringb=record['260']['b']
                    stringd=record['260']['c']
                    stringe=record['260']['e']
                    stringf=record['260']['f']
                    if record['260']['e'] is not None and record['260']['f'] is not None:
                        if stringe[0] == '(' and stringf[-1] != ')':
                            relatorio.append([biblioId,bibprinc,'260ef',record['260'].value(),"Verificar a pontuação do campo ou o parêntese curvo."])
                    if record['260']['e'] is not None and record['260']['f'] is None:
                        if stringe[0] == '(' and stringe[-1] != ')':
                            relatorio.append([biblioId,bibprinc,'260e',record['260'].value(),"Verificar a pontuação do campo ou o parêntese curvo."])
                    if (stringc[0] != '[' and stringc[0].islower()) or (stringc[0] == '[' and stringc[1].islower()):
                        relatorio.append([biblioId,bibprinc,'260a',record['260']['a'],"Verificar se o campo inicia com maiúsculas."])
                    if '[s.n' in stringc or '[S.n' in stringc or 's. n' in stringc:
                        relatorio.append([biblioId,bibprinc,'260a',record['260']['a'],"Verificar a abreviatura do campo ou o parêntese reto"])
                    if record['260']['a'] is not None:
                        if '[' in stringc and ']' not in stringc:
                            relatorio.append([biblioId,bibprinc,'260a',record['260']['a'],"Verificar o parêntese reto."])
                    if record['260']['b'] is not None:
                        if '[' in stringb and ']' not in stringb:
                            relatorio.append([biblioId,bibprinc,'260b',record['260']['b'],"Verificar o parêntese reto."])
                    if record['260']['c'] is not None:
                        if ']' in stringd and '[' not in stringd:
                            relatorio.append([biblioId,bibprinc,'260c',record['260']['c'],"Verificar o parêntese reto."])


            if (len(relatorio) > 1000000):
                break

        for i in range(len(relatorio)):
            relatorio[i].append("Verificar")    
        table.build_table_data(coldata=cdata, rowdata=relatorio)
        table.load_table_data()

def main():

    app = tb.Window(themename="sandstone",minsize=(1600,860),maxsize=(1600,860))
 
    global rdata
    global table
    global cdata

    cdata = [
        {"text": "Registo Nº", "stretch": False,"anchor":W,"width":80},
        {"text":"Biblioteca","stretch": False,"anchor":W,"width":80},
        {"text": "Campo", "stretch": False,"anchor":W,"width":80},
        {"text": "Valor", "stretch": False,"anchor":W,"width":400},
        {"text": "Não conformidade", "stretch": False,"anchor":W,"width":200},
        {"text": "Estado", "stretch": False,"width":80},
    ]
    rdata = []

    table = Tableview(
        master=app,
        coldata=cdata,
        rowdata=rdata,
        paginated=TRUE,
        pagesize=50,
        autofit=FALSE,
        searchable=TRUE,
        bootstyle=PRIMARY,
        
        )
    table.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    def selresolv():
        rows=table.get_rows(selected=True)
        for x in rows:
            x.values[5]='Resolvido'
            x.refresh()
    def selaberto():
        rows=table.get_rows(selected=True)
        for x in rows:
            x.values[5]='Verificar'
            x.refresh()
       
    def saverel():
        table.export_all_records()
        table.purge_table_data()
    
    def openfile():  
        table.load_table_data()
        table.purge_table_data()
        file = askopenfilename(filetypes =[('CSV Files', '*.csv')])
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                rdata.append(row)
        table.build_table_data(coldata=cdata, rowdata=rdata)
        table.load_table_data()
        
        

    
    b3 = tb.Button(app, text="Criar relatório", bootstyle=SECONDARY, command=validaMarc)
    b3.pack(side=LEFT, padx=5, pady=10)
    
    b4 = tb.Button(app, text="Abrir relatório", bootstyle=SECONDARY, command=openfile)
    b4.pack(side=LEFT,padx=5, pady=10)
    
    b5 = tb.Button(app, text="Guardar", bootstyle=SECONDARY, command=saverel)
    b5.pack(side=LEFT, padx=5, pady=10)

    b1 = tb.Button(app, text="Resolvido", bootstyle=SUCCESS, command=selresolv)
    b1.pack(side=LEFT, padx=5, pady=10)

    b2 = tb.Button(app, text="Verificar", bootstyle=DEFAULT, command=selaberto)
    b2.pack(side=LEFT, padx=5, pady=10)
    

    app.mainloop()


if __name__ == "__main__":
    main()

