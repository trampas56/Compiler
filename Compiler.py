

#Trampas Eleftherios AM : 4625

file= open('programmaCPY.cpy','r')

alfavito = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
noumera = ['0','1','2','3','4','5','6','7','8','9']

katastasi_start = 0
katastasi_noumero = 1
katastasi_gramma = 2  
katastasi_hashtag = 3
katastasi_sxolio = 4
katastasi_mikrotero = 5 
katastasi_megalitero = 6
katastasi_iso = 7
katastasi_thavmastiko = 8
katastasi_diairesh = 9
katastasi_kleinei_hashtag = 10

keno = 0
noumero = 1 
gramma = 2
sin = 3
plin = 4
diairesh = 5
epi = 6
mod = 7
iso = 8
mikrotero = 9
megalitero = 10
koma = 11
thavmastiko = 12
hashtag = 13
anoigei_parenthesh = 14
kleinei_parenthesh = 15
EOF = 16
anoigei_agkili = 17
kleinei_agkili = 18
anw_katw_telia = 19
allagh_grammhs = 20
mh_apodekto_symvolo = 21
    
token_identifier = 100
token_noumero = 101
token_mikrotero= 102
token_sin = 103
token_plin = 104
token_diairesh = 105
token_epi = 106
token_mod = 107
token_iso = 108
token_mikrotero_H_iso = 109
token_megalitero_H_iso = 110
token_koma = 111
token_diaforo = 112
token_megalitero = 113
token_anoigei_parenthesh = 114
token_kleinei_parenthesh = 115
token_eof = 116
token_anoigei_agkili = 117
token_kleinei_agkili = 118
token_anw_katw_telia = 119
token_anathesi= 120

token_main = 200
token_if = 201
token_elif = 202
token_else = 203
token_while = 204
token_int = 205
token_and = 206
token_or = 207
token_not = 208
token_print = 209
token_return = 210
token_input = 211
token_def = 212
token_hashtag_def = 213
token_hashtag_int = 214
token_global = 215

error_thavmastiko = 500
error_noumero_gramma = 501
error_einai_ektos_oriwn = 502
error_panw_apo_30_xaraktires = 503
error_slash = 504
error_anoigei_agkili = 505
error_kleinei_agkili = 506
error_hashtag = 507
error_mh_apodekto_symvolo = 508
error_eof = 509

pinakas = [
            #katastasi_start 0 
            [katastasi_start , katastasi_noumero , katastasi_gramma ,
             token_sin , token_plin , katastasi_diairesh ,  token_epi , 
             token_mod , katastasi_iso , katastasi_mikrotero , katastasi_megalitero , 
             token_koma , katastasi_thavmastiko , katastasi_hashtag , token_anoigei_parenthesh , 
             token_kleinei_parenthesh , token_eof , error_anoigei_agkili , error_kleinei_agkili , 
             token_anw_katw_telia , katastasi_start , error_mh_apodekto_symvolo],
            
            #katastasi_noumero 1 
            [token_noumero , katastasi_noumero , error_noumero_gramma , token_noumero , token_noumero , token_noumero , 
             token_noumero , token_noumero , token_noumero , token_noumero , token_noumero , token_noumero ,
             token_noumero , token_noumero , token_noumero , token_noumero , token_noumero , token_noumero ,
             token_noumero , token_noumero , token_noumero , error_mh_apodekto_symvolo], 
            
            #katastasi_gramma 2 
            [token_identifier , katastasi_gramma , katastasi_gramma , token_identifier , token_identifier , 
             token_identifier , token_identifier , token_identifier , token_identifier , token_identifier , 
             token_identifier , token_identifier , token_identifier , token_identifier , token_identifier , 
             token_identifier , token_identifier , token_identifier , token_identifier , token_identifier , 
             token_identifier , error_mh_apodekto_symvolo], 

            #katastasi_hashtag 3 
            [error_hashtag , error_hashtag , katastasi_gramma , error_hashtag , error_hashtag , error_hashtag ,
             error_hashtag , error_hashtag , error_hashtag , error_hashtag , error_hashtag , error_hashtag , 
             error_hashtag , katastasi_sxolio , error_hashtag , error_hashtag , error_hashtag ,  
             token_anoigei_agkili , token_kleinei_agkili , error_hashtag , error_hashtag , error_mh_apodekto_symvolo], 

            #katastasi_sxolio 4 
            [katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , 
             katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , 
             katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_kleinei_hashtag , katastasi_sxolio , 
             katastasi_sxolio , error_eof , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , 
             katastasi_sxolio],
            
            #katastasi_mikrotero 5 
            [token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , 
             token_mikrotero , token_mikrotero , token_mikrotero_H_iso , token_mikrotero , token_mikrotero , token_mikrotero ,
             token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero ,
             token_mikrotero, token_mikrotero , error_mh_apodekto_symvolo], 

            #katastasi_megalitero 6 
            [token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , 
             token_mikrotero , token_mikrotero , token_megalitero_H_iso , token_mikrotero , token_mikrotero , token_mikrotero ,
             token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero , token_mikrotero ,
             token_mikrotero, token_mikrotero , error_mh_apodekto_symvolo],

            #katastasi_iso 7 
            [token_anathesi , token_anathesi , token_anathesi , token_anathesi , token_anathesi , token_anathesi , 
             token_anathesi , token_anathesi , token_iso , token_anathesi , token_anathesi , token_anathesi , token_anathesi , 
             token_anathesi , token_anathesi , token_anathesi , token_anathesi , token_anathesi , token_anathesi , 
             token_anathesi , token_anathesi , error_mh_apodekto_symvolo],

            #katastasi_thavmastiko 8 
            [error_thavmastiko , error_thavmastiko , error_thavmastiko , error_thavmastiko , error_thavmastiko , error_thavmastiko , 
             error_thavmastiko , error_thavmastiko , token_diaforo , error_thavmastiko , error_thavmastiko , error_thavmastiko , error_thavmastiko , 
             error_thavmastiko , error_thavmastiko , error_thavmastiko , error_thavmastiko , error_thavmastiko , error_thavmastiko ,
             error_thavmastiko , error_thavmastiko , error_mh_apodekto_symvolo],

            #katastasi_diairesh 9 
            [error_slash , error_slash , error_slash , error_slash , error_slash , token_diairesh , error_slash , error_slash , error_slash ,
             error_slash , error_slash , error_slash , error_slash , error_slash , error_slash , error_slash , error_slash ,
             error_slash , error_slash , error_slash , error_slash , error_mh_apodekto_symvolo],

            #katastasi_kleinei_hashtag 10 
            [katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , 
             katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , 
             katastasi_sxolio , katastasi_start , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , katastasi_sxolio , 
             katastasi_sxolio , katastasi_sxolio , error_mh_apodekto_symvolo]
]


def get_token(myGramma):

    counter = grammh

    if ( myGramma == ' ' or myGramma == '\t'):
        myGramma_tk = keno
    elif ( myGramma in alfavito):
        myGramma_tk = gramma
    elif ( myGramma in noumera):
        myGramma_tk = noumero
    elif ( myGramma == '+'):
        myGramma_tk = sin
    elif ( myGramma == '-'):
        myGramma_tk = plin
    elif ( myGramma == '/'):
        myGramma_tk = diairesh
    elif ( myGramma == '*'):
        myGramma_tk = epi
    elif ( myGramma == '%'):
        myGramma_tk = mod
    elif ( myGramma == '='):
        myGramma_tk = iso
    elif ( myGramma == '<'):
        myGramma_tk = mikrotero
    elif ( myGramma == '>'):
        myGramma_tk = megalitero
    elif ( myGramma == ','):
        myGramma_tk = koma
    elif ( myGramma == '!'):
        myGramma_tk = thavmastiko
    elif ( myGramma == '#'):
        myGramma_tk = hashtag
    elif ( myGramma == '('):
        myGramma_tk = anoigei_parenthesh
    elif ( myGramma == ')'):
        myGramma_tk = kleinei_parenthesh
    elif ( myGramma == ''):  
        myGramma_tk = EOF
    elif ( myGramma == '{'):
        myGramma_tk = anoigei_agkili
    elif ( myGramma == '}'):
        myGramma_tk = kleinei_agkili
    elif ( myGramma == ':'):
        myGramma_tk = anw_katw_telia
    elif ( myGramma == '\n'):
        counter = counter + 1
        myGramma_tk = allagh_grammhs
    else:
        myGramma_tk = mh_apodekto_symvolo
    
    return myGramma_tk

def desmevmena_tokens(prod_wrd, twrini_katastasi):
    if prod_wrd == 'main':
        twrini_katastasi = token_main
    elif prod_wrd == 'if':
        twrini_katastasi = token_if
    elif prod_wrd == 'elif':
        twrini_katastasi = token_elif
    elif prod_wrd == 'else':
        twrini_katastasi = token_else
    elif prod_wrd == 'while':
        twrini_katastasi = token_while
    elif prod_wrd == 'int':
        twrini_katastasi = token_int
    elif prod_wrd == 'and':
        twrini_katastasi = token_and
    elif prod_wrd == 'or':
        twrini_katastasi = token_or
    elif prod_wrd == 'not':
        twrini_katastasi = token_not
    elif prod_wrd == 'print':
        twrini_katastasi = token_print
    elif prod_wrd == 'return':
        twrini_katastasi = token_return
    elif prod_wrd == 'input':
        twrini_katastasi = token_input
    elif prod_wrd == 'def':
        twrini_katastasi = token_def
    elif prod_wrd == '#def':
        twrini_katastasi = token_hashtag_def
    elif prod_wrd == '#int':
        twrini_katastasi = token_hashtag_int
    elif prod_wrd == 'global':
        twrini_katastasi = token_global

    return twrini_katastasi

def print_error_message(error_code):
    if error_code == error_mh_apodekto_symvolo:
        print("mh apodekto symbolo")
    elif error_code == error_noumero_gramma:
        print("gramma meta apo kapoio psifio")
    elif error_code == error_einai_ektos_oriwn:
        print("ektos diastimatos [-32767,32767]")
    elif error_code == error_eof:
        print("ta sxolia den eklisan")
    elif error_code == error_panw_apo_30_xaraktires:
        print("panw apo 30 charaktires")
    elif error_code == error_slash:
        print("ena / mono tou")
    elif error_code == error_anoigei_agkili:
        print("ena { mono tou")
    elif error_code == error_kleinei_agkili:
        print("ena } mono tou")
    elif error_code == error_hashtag:
        print("ena # mono tou")
    elif error_code == error_thavmastiko:
        print("! mono tou")

grammh = 1
def Lektikos():
    global grammh
    prod_wrd = ''
    twrini_katastasi = katastasi_start
    
    counter = grammh
    apotelesmaLekt = []
    while( twrini_katastasi >= 0 and twrini_katastasi <= 10):
        
        myGramma = file.read(1)

        myGramma_tk = get_token(myGramma)     
        
        twrini_katastasi = pinakas[ twrini_katastasi ][ myGramma_tk ]    

        if ( len(prod_wrd) < 30):
            if ( twrini_katastasi != katastasi_start and twrini_katastasi != katastasi_sxolio and twrini_katastasi != katastasi_kleinei_hashtag):
                prod_wrd += myGramma
            else:
                prod_wrd=''
        else:
            twrini_katastasi = error_panw_apo_30_xaraktires

    if(twrini_katastasi == token_identifier or twrini_katastasi == token_noumero or twrini_katastasi == token_mikrotero or twrini_katastasi == token_megalitero or twrini_katastasi == token_anathesi):
        if (myGramma == '\n'):
                counter -= 1
        file.seek(file.tell()-1,0)  
        prod_wrd = prod_wrd[:-1]    

    if(twrini_katastasi==token_identifier):
        twrini_katastasi = desmevmena_tokens(prod_wrd, twrini_katastasi)

    if (twrini_katastasi == token_noumero):
        if (int(prod_wrd) > 32767):
            twrini_katastasi = error_einai_ektos_oriwn
            
    print_error_message(twrini_katastasi)

    apotelesmaLekt.append(twrini_katastasi)
    apotelesmaLekt.append(prod_wrd)
    apotelesmaLekt.append(counter)
    grammh=counter

    return apotelesmaLekt

'''
while(1):
    apotelesmaLekt = Lektikos() 
    if (apotelesmaLekt[0] == token_eof):
            break
    print(apotelesmaLekt)
'''




global lista_tetradwn		
lista_tetradwn = []
metritis_tetradas = 1	

def nextQuad():
	global metritis_tetradas
	
	return metritis_tetradas

def genQuad(prwto, deutero, trito, tetarto):
	global metritis_tetradas
	global lista_tetradwn
	lista = []

	metritis_tetradas = nextQuad()		
	lista += [metritis_tetradas] + [prwto] + [deutero] + [trito] + [tetarto]		
	
	metritis_tetradas +=1	
	lista_tetradwn += [lista] 	
	return lista

lista_T_i = []
T_i = 1
def newTemp():
	global T_i
	global lista_T_i
	
	T_arithmos = 'T_' + str(T_i)
	T_i += 1
	
	
	lista_T_i.append(T_arithmos)
	##print(lista_T_i)
	
	return T_arithmos

def emptyList():
	kenh_lista = []	
	
	return kenh_lista

def makeList(x):
	listThis = [x]
	
	return listThis

def merge(lista1, lista2):
	lista=[]
	lista += lista1 + lista2

	return lista

def backPatch(lista, z):
	global lista_tetradwn
	
	for i in range(len(lista)):
		for j in range(len(lista_tetradwn)):
			if(lista[i]==lista_tetradwn[j][0] and lista_tetradwn[j][4]=='_'):
				lista_tetradwn[j][4] = z
				break;	
	return	
    


lista_scopes = []

class Argument():
	def __init__(self):
		self.onoma = ''		
		self.type = 'Int'
class Entity():

	def __init__(self):
		self.onoma = ''			
		self.type = ''			

		self.variable = self.Variable()
		self.subprogram = self.SubProgram()
		self.parameter = self.Parameter()
		self.tempVar = self.TempVar()
		
	class Variable: 
		def __init__(self):
			self.type = 'Int'          
			self.offset = 0				
	class SubProgram: 
		def __init__(self):
						
			self.startQuad = 0			
			self.frameLength = 0		
			self.argumentList = []			
			
	class Parameter: 
		def __init__(self):
			self.mode = 'CV'				
			self.offset = 0				
	class TempVar: 
		def __init__(self):
					
			self.offset = 0				
class Scope():
	def __init__(self):
		self.onoma = ''						
		self.entityList = []		
		self.nestingLevel = 0				


def new_argument(object): 
	global lista_scopes

	lista_scopes[-1].entityList[-1].subprogram.argumentList.append(object) 
	
def new_entity(object):  
	global lista_scopes

	lista_scopes[-1].entityList.append(object)  

def new_scope(onoma): 
	global lista_scopes

	epomeno_scope = Scope()   
	epomeno_scope.onoma = onoma

	if( not lista_scopes ): 
		epomeno_scope.nestingLevel = 0

	else:
		epomeno_scope.nestingLevel = lista_scopes[-1].nestingLevel + 1

	lista_scopes.append(epomeno_scope)

def delete_scope(): 
	global lista_scopes

	freeScope = lista_scopes.pop()
	del freeScope

def compute_offset():
	global lista_scopes

	counter=0
	if(lista_scopes[-1].entityList is not []): 
		for ent in (lista_scopes[-1].entityList): 
			if(ent.type == 'VAR' or ent.type == 'TEMP' or ent.type=='PARAM'):  
				counter +=1  
	
	offset = 12+(counter*4) 
	
	return offset
	
def add_parameters():  
	global lista_scopes

	for arg in lista_scopes[-2].entityList[-1].subprogram.argumentList:
		ent = Entity() 
		ent.onoma = arg.onoma
		ent.type = 'PARAM'
		ent.parameter.mode = 'CV'
		ent.parameter.offset = compute_offset()
		new_entity(ent)

def print_Symbol_table():

	global lista_scopes, pinakas_symvolwn

    
	for sco in reversed(lista_scopes):
		pinakas_symvolwn.write("scope: "+"onoma:"+sco.onoma+" nestingLevel:"+str(sco.nestingLevel))
		pinakas_symvolwn.write("\n\tENTITIES:\n")
		for ent in sco.entityList:
			if(ent.type == 'VAR'):
					pinakas_symvolwn.write("\tENTITY: "+" onoma:"+ent.onoma+"\t variable-type:"+ent.variable.type+"\t type:"+ent.type+"\t offset:"+str(ent.variable.offset))
			elif(ent.type == 'TEMP'):
					pinakas_symvolwn.write("\tENTITY: "+" onoma:"+ent.onoma+"\t temp-type:"+ent.tempVar.type+"\t type:"+ent.type+"\t offset:"+str(ent.tempVar.offset))
			elif(ent.type == 'SUBPR'):
				pinakas_symvolwn.write("\tENTITY: "+" onoma:"+ent.onoma+"\t function-type:"+ent.subprogram.type+"\t type:"+ent.type+"\t startQuad:"+str(ent.subprogram.startQuad)+"\t frameLength:"+str(ent.subprogram.frameLength))
				pinakas_symvolwn.write("\t\tARGUMENTS:")
				for arg in ent.subprogram.argumentList:
					pinakas_symvolwn.write("\t\tARGUMENT: "+" onoma:"+arg.onoma+"\t type:"+arg.type+"\t parMode:"+arg.parMode)
			elif(ent.type == 'PARAM'):
				pinakas_symvolwn.write("\tENTITY: "+" onoma:"+ent.onoma+"\t mode:"+ent.parameter.mode+"\t type:"+ent.type+"\t offset:"+str(ent.parameter.offset))
			pinakas_symvolwn.write("\n")
		pinakas_symvolwn.write("\n\n")
	pinakas_symvolwn.write("--------------------------------------------------------------------------------------------------------------------------------")
	pinakas_symvolwn.write("\n\n\n\n\n")








assembly_arxeio = open('assembly.asm','w') 
assembly_arxeio.write(' \n\n') 

def gnlvcode():  
	global lista_scopes
	global assembly_arxeio

def loadvr(v,r): 
		global lista_scopes
		global assembly_arxeio

def storerv(r,v):  
	global lista_scopes
	global assembly_arxeio
      

def telikos():  

	global lista_scopes
	global lista_tetradwn
	global assembly_arxeio

	for i in range(len(lista_tetradwn)): 

		assembly_arxeio.write('L' + str(lista_tetradwn[i][0]) + ': \n') 

		if (lista_tetradwn[i][1] == 'jump'): 
			assembly_arxeio.write('b L'+str(lista_tetradwn[i][4])+'\n')
		elif (lista_tetradwn[i][1] == '=='): 
			loadvr(lista_tetradwn[i][2],1) 
			loadvr(lista_tetradwn[i][3],2) 
			assembly_arxeio.write('beq,t1,t2,L'+str(lista_tetradwn[i][4])+'\n')
		elif (lista_tetradwn[i][1] == '!='): 
			loadvr(lista_tetradwn[i][2],1)
			loadvr(lista_tetradwn[i][3],2)
			assembly_arxeio.write('bne,t1,t2,L'+str(lista_tetradwn[i][4])+'\n')
		elif (lista_tetradwn[i][1] == '>'):
			loadvr(lista_tetradwn[i][2],1)
			loadvr(lista_tetradwn[i][3],2)
			assembly_arxeio.write('bgt,t1,t2,L'+str(lista_tetradwn[i][4])+'\n')
		elif (lista_tetradwn[i][1] == '<'): 
			loadvr(lista_tetradwn[i][2],1)
			loadvr(lista_tetradwn[i][3],2)
			assembly_arxeio.write('blt,t1,t2,L'+str(lista_tetradwn[i][4])+'\n')
		elif (lista_tetradwn[i][1] == '>='):	
			loadvr(lista_tetradwn[i][2],1)
			loadvr(lista_tetradwn[i][3],2)
			assembly_arxeio.write('bge,t1,t2,L'+str(lista_tetradwn[i][4])+'\n')
		elif (lista_tetradwn[i][1] == '<='):
			loadvr(lista_tetradwn[i][2],1)
			loadvr(lista_tetradwn[i][3],2)
			assembly_arxeio.write('ble,t1,t2,L'+str(lista_tetradwn[i][4])+'\n')	
		elif (lista_tetradwn[i][1] == ':='):
			loadvr(lista_tetradwn[i][2],1)
			storerv(1,lista_tetradwn[i][4])
		elif (lista_tetradwn[i][1] == '+'):
			loadvr(lista_tetradwn[i][2],1)
			loadvr(lista_tetradwn[i][3],2)
			assembly_arxeio.write('add,t1,t1,t2'+'\n')
			storerv(1,lista_tetradwn[i][4])
		elif ( lista_tetradwn[i][1] == 'begin_block' and lista_scopes[-1].nestingLevel!=0):  
			assembly_arxeio.write('sw ra,(sp)\n')
		elif ( lista_tetradwn[i][1] == 'end_block' and lista_scopes[-1].nestingLevel!=0):  
			assembly_arxeio.write('lw ra,(sp)\n')
			assembly_arxeio.write('jr ra\n')
		elif ( lista_tetradwn[i][1] == 'halt'):
			assembly_arxeio.write('li a0,0\n')
			assembly_arxeio.write('li a7,93\n')
			assembly_arxeio.write('ecall\n')

	lista_tetradwn = []







def Syntaktikos(): 
    global grammh
    global apotelesmaLekt

    def startRule():

        new_scope('main')

        declarations()
        def_part()
        call_main_part()

    def def_part():
        global apotelesmaLekt

        while(apotelesmaLekt[0] == token_def):
            def_function()

    def def_function():
        global grammh
        global apotelesmaLekt
                
        if(apotelesmaLekt[0] == token_def):
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
            if(apotelesmaLekt[0] == token_identifier):
                onoma = apotelesmaLekt[1]
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]

                if(apotelesmaLekt[0] == token_anoigei_parenthesh):
                    apotelesmaLekt = Lektikos()
                    grammh = apotelesmaLekt[2]

                    ent = Entity()						
                    ent.type = 'SUBPR'					
                    ent.onoma = onoma					
                    ent.subprogram.type = 'Function'	
                    new_entity(ent)	

                    id_list(0)
                        
                    if(apotelesmaLekt[0] == token_kleinei_parenthesh):
                        apotelesmaLekt = Lektikos()
                        grammh = apotelesmaLekt[2]
                                                
                        if(apotelesmaLekt[0] == token_anw_katw_telia):
                            apotelesmaLekt = Lektikos()
                            grammh = apotelesmaLekt[2]
                                
                            if(apotelesmaLekt[0] == token_anoigei_agkili):
                                apotelesmaLekt = Lektikos()
                                grammh = apotelesmaLekt[2]

                                new_scope(onoma)
                                add_parameters()
                                                          
                                declarations()
                                while(apotelesmaLekt[0] == token_def):
                                    def_function()
                                globalnames()
                                genQuad('begin_block',onoma,'_','_')
                                statements()
                                genQuad('end_block',onoma,'_','_')

                                print_Symbol_table()
                                delete_scope()

                                                          
                                if(apotelesmaLekt[0] == token_kleinei_agkili):
                                    apotelesmaLekt = Lektikos()
                                    grammh = apotelesmaLekt[2]
                                else:
                                    print("den yparxei #}",grammh)
                                    exit(0)
                            else:
                                print("den yparxei #{",grammh)
                                exit(0)
                        else:
                            print("den yparxei : meta apo ()",grammh)
                            exit(0)
                    else:
                        print("den kleinei h deksia parenthesi",grammh)
                        exit(0)
                else:
                    print("den anoigei h aristeri parenthesi",grammh)
                    exit(0)
            else:
                print("den yparxei onoma function",grammh)
                exit(0)
        else:
            print("def den yparxei stin arxi",grammh)
            exit(0)

    def declarations():
        global apotelesmaLekt
            
        while(apotelesmaLekt[0] == token_hashtag_int):
            declaration_grammh()

    def declaration_grammh():
        global grammh
        global apotelesmaLekt
                
        if (apotelesmaLekt[0] == token_hashtag_int):
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2] 
            id_list(1)

    def globalnames():
        global apotelesmaLekt
            
        while(apotelesmaLekt[0] == token_global):
            globalnames_grammh()

    def globalnames_grammh():
        global grammh
        global apotelesmaLekt   
                
        if (apotelesmaLekt[0] == token_global):
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]    
            id_list(2)

    def id_list(flag):
        global grammh
        global apotelesmaLekt

        if(apotelesmaLekt[0] == token_identifier):
            onoma = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]

            if (flag == 1): 
                ent = Entity()							
                ent.type = 'VAR'						
                ent.onoma = onoma						
                ent.variable.offset = compute_offset()	
                new_entity(ent)							
            elif (flag == 0):  
                arg = Argument()		
                arg.onoma = onoma		
                arg.parMode = 'CV'		
                new_argument(arg)		
        
            while(apotelesmaLekt[0] == token_koma):
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]
                            
                if(apotelesmaLekt[0] == token_identifier):
                    onoma = apotelesmaLekt[1]
                    apotelesmaLekt = Lektikos()
                    grammh = apotelesmaLekt[2]

                    if (flag == 1):  
                        ent = Entity()							
                        ent.type = 'VAR'						
                        ent.onoma = onoma					
                        ent.variable.offset = compute_offset()	
                        new_entity(ent)							
                    elif (flag == 0):  
                        arg = Argument()		
                        arg.onoma = onoma		
                        arg.parMode = 'CV'		
                        new_argument(arg)		                            
                else:
                    print("den yparxei id meta apo koma", grammh)
                    exit(0)               
                
    def statement():
        global grammh
        global apotelesmaLekt

        if(apotelesmaLekt[0]==token_identifier or apotelesmaLekt[0]==token_print or apotelesmaLekt[0]==token_return):
            simple_statement()
        elif(apotelesmaLekt[0]==token_if or apotelesmaLekt[0]==token_while):
            structured_statement()
        else:
            print("lathos statement", grammh)
            exit(0)

    def statements():
        global apotelesmaLekt

        statement()
        while(apotelesmaLekt[0]==token_identifier or apotelesmaLekt[0]==token_print or apotelesmaLekt[0]==token_return or apotelesmaLekt[0]==token_if or apotelesmaLekt[0]==token_while):
            statement()

    def simple_statement():
        global apotelesmaLekt

        if(apotelesmaLekt[0]==token_identifier):
            assignment_stat()
        elif(apotelesmaLekt[0]==token_print):
            print_stat()
        elif(apotelesmaLekt[0]==token_return):
            return_stat()
        
    def structured_statement():
        global apotelesmaLekt

        if(apotelesmaLekt[0]==token_if):
            if_stat()
        elif(apotelesmaLekt[0]==token_while):
            while_stat()

    def assignment_stat():
        global grammh
        global apotelesmaLekt
                
        if(apotelesmaLekt[0] == token_identifier):
            identifier = apotelesmaLekt[1]

            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
            if(apotelesmaLekt[0] == token_anathesi):
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]
                                
                if(apotelesmaLekt[0] == token_int):
                    apotelesmaLekt = Lektikos()
                    grammh = apotelesmaLekt[2]
                                    
                    if(apotelesmaLekt[0] == token_anoigei_parenthesh):
                        apotelesmaLekt = Lektikos()
                        grammh = apotelesmaLekt[2]

                        if(apotelesmaLekt[0] == token_input):
                            apotelesmaLekt = Lektikos()
                            grammh = apotelesmaLekt[2]
                            genQuad('inp',identifier,'_','_')

                            if(apotelesmaLekt[0] == token_anoigei_parenthesh):
                                apotelesmaLekt = Lektikos()
                                grammh = apotelesmaLekt[2]
                                                
                                if(apotelesmaLekt[0] == token_kleinei_parenthesh):
                                    apotelesmaLekt = Lektikos()
                                    grammh = apotelesmaLekt[2]
                                
                                    if(apotelesmaLekt[0] == token_kleinei_parenthesh):
                                        apotelesmaLekt = Lektikos()
                                        grammh = apotelesmaLekt[2]
                                    else:
                                        print("den yparxei ) sto assignment_stat",grammh)
                                        exit(0)
                                else:
                                    print("den yparxei ) sto assignment_stat",grammh)
                                    exit(0)
                            else:
                                print("den yparxei ( sto assignment_stat",grammh)
                                exit(0)
                        else:
                            print("den yparxei input sto assignment_stat",grammh)
                            exit(0)
                    else:
                        print("den yparxei ( sto assignment_stat",grammh)
                        exit(0)         
                else:
                    Eplace = expression()
                    genQuad(':=', Eplace, '_', identifier)
            else:
                print("den yparxei = meta to id.", grammh)
                exit(0) 
        else:
            print("den uparxei id",grammh)
            exit(0)
    def print_stat():
        global grammh
        global apotelesmaLekt
                
        if(apotelesmaLekt[0] == token_print):
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]

            if(apotelesmaLekt[0] == token_anoigei_parenthesh):
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]
                                
                Eplace = expression()
                
                                
                if(apotelesmaLekt[0] == token_kleinei_parenthesh):
                    apotelesmaLekt = Lektikos()
                    grammh = apotelesmaLekt[2]
                    genQuad('out', Eplace, '_', '_')

                else:
                    print("den exei deksia parenthesi stin print_stat",grammh)
                    exit(0)
            else:
                print("den exei aristeri parenthesi stin print_stat", grammh)
                exit(0)
        else:
            print("den uparxei print",grammh)
            exit(0)

    def return_stat():
        global grammh
        global apotelesmaLekt
                
        if(apotelesmaLekt[0] == token_return):
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]

            Eplace = expression()
            genQuad('retv', Eplace, '_', '_')
        else:
            print("den uparxei return",grammh)
            exit(0)


    def if_stat():
        global grammh
        global apotelesmaLekt

        lista_out=emptyList()

        if(apotelesmaLekt[0] == token_if):
            apotelesmaLekt= Lektikos()
            grammh = apotelesmaLekt[2]

            C = condition()
            

            if(apotelesmaLekt[0] == token_anw_katw_telia):
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]
                             
                if(apotelesmaLekt[0] == token_anoigei_agkili):
                    apotelesmaLekt = Lektikos()
                    grammh = apotelesmaLekt[2]

                    backPatch(C[0], nextQuad())
                                    
                    statements()

                    lista_if = makeList(nextQuad())
                    genQuad('jump', '_', '_', '_')
                    lista_out = merge(lista_out, lista_if)
                    
                    if(apotelesmaLekt[0] == token_kleinei_agkili):
                        apotelesmaLekt = Lektikos()
                        grammh = apotelesmaLekt[2]
                        backPatch(C[1], nextQuad())
                    else:
                        print("den yparxei #} meta ta statements kapoias if",grammh)
                        exit(0)
                else:
                    backPatch(C[0], nextQuad())
                    statement()

                    lista_if = makeList(nextQuad())
                    genQuad('jump', '_', '_', '_')
                    lista_out = merge(lista_out, lista_if)
                    backPatch(C[1], nextQuad())

                while(apotelesmaLekt[0] == token_elif):
                    apotelesmaLekt= Lektikos()
                    grammh = apotelesmaLekt[2]

                    C = condition()

                    if(apotelesmaLekt[0] == token_anw_katw_telia):
                        apotelesmaLekt = Lektikos()
                        grammh = apotelesmaLekt[2]
                                         
                        if(apotelesmaLekt[0] == token_anoigei_agkili):
                            apotelesmaLekt = Lektikos()
                            grammh = apotelesmaLekt[2]

                            backPatch(C[0], nextQuad())
                                                
                            statements()

                            lista_if = makeList(nextQuad())
                            genQuad('jump', '_', '_', '_')
                            lista_out = merge(lista_out, lista_if)

                            if(apotelesmaLekt[0] == token_kleinei_agkili):
                                apotelesmaLekt = Lektikos()
                                grammh = apotelesmaLekt[2]

                                backPatch(C[1], nextQuad())

                            else:
                                print("den yparxei #} meta ta statements kapoias elif",grammh)
                                exit(0)
                        else:
                            backPatch(C[1], nextQuad())
                            statement()

                            lista_if = makeList(nextQuad())
                            genQuad('jump', '_', '_', '_')
                            lista_out = merge(lista_out, lista_if)
                            backPatch(C[1], nextQuad())
                    else:
                        print("den yparxei : meta to tou elif", grammh)
                        exit(0)

                if(apotelesmaLekt[0] == token_else):
                    apotelesmaLekt = Lektikos()
                    grammh = apotelesmaLekt[2]
                             
                    if(apotelesmaLekt[0] == token_anw_katw_telia):
                        apotelesmaLekt = Lektikos()
                        grammh = apotelesmaLekt[2]
                                    
                        if(apotelesmaLekt[0] == token_anoigei_agkili):
                            apotelesmaLekt = Lektikos()
                            grammh = apotelesmaLekt[2]
                                    
                            statements()

                            
                            
                            if(apotelesmaLekt[0] == token_kleinei_agkili):
                                apotelesmaLekt = Lektikos()
                                grammh = apotelesmaLekt[2]

                                backPatch(lista_out, nextQuad())

                            else:
                                print("den yparxei #} meta ta statements kapoias if",grammh)
                                exit(0)
                        else:
                            statement()
                            backPatch(lista_out, nextQuad())

                    else:
                        print("den yparxei : meta to else",grammh)
                        exit(0)
                else:
                    backPatch(lista_out, nextQuad())

            else:
                print("den yparxei : meta to if",grammh)
                exit(0)

        else:
            print("den uparxei if",grammh)
            exit(0)
                

    def while_stat():
        global grammh
        global apotelesmaLekt

        Cquad=nextQuad()
                
        if(apotelesmaLekt[0] == token_while):
            apotelesmaLekt= Lektikos()
            grammh = apotelesmaLekt[2]

            C = condition()

            if(apotelesmaLekt[0] == token_anw_katw_telia):
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]
                             
                if(apotelesmaLekt[0] == token_anoigei_agkili):
                    apotelesmaLekt = Lektikos()
                    grammh = apotelesmaLekt[2]

                    backPatch(C[0], nextQuad())
                                    
                    statements()

                    genQuad('jump', '_', '_', Cquad)

                    if(apotelesmaLekt[0] == token_kleinei_agkili):
                        apotelesmaLekt = Lektikos()
                        grammh = apotelesmaLekt[2]

                        backPatch(C[1], nextQuad())

                    else:
                        print("den yparxei #} meta ta statements kapoias while",grammh)
                        exit(0)
                else:
                    backPatch(C[0], nextQuad())
                    statement()

                    genQuad('jump', '_', '_', Cquad)
                    backPatch(C[1], nextQuad())

            else:
                print("den yparxei : meta to while",grammh)
                exit(0)

        else:
            print("den yparxei while",grammh)
            exit(0)

    def expression():
        global apotelesmaLekt
        global grammh   

        optional_sign()
        T1 = term()

        while(apotelesmaLekt[0]==token_sin or apotelesmaLekt[0]==token_plin):
            plusOrMinus = ADD_OP()
            T2 = term()

            w = newTemp()
            genQuad(plusOrMinus, T1, T2, w)
            T1 = w

        E = T1
        return E

    def term():
        global apotelesmaLekt
        global grammh

        F1 = factor()
                
        while(apotelesmaLekt[0]==token_epi or apotelesmaLekt[0]==token_diairesh or apotelesmaLekt[0]==token_mod):
            mul_h_div = MUL_OP()
            F2 = factor()

            w = newTemp()
            
            genQuad(mul_h_div, F1, F2, w)
            F1 = w

        T =F1
        return T
      
    def factor():
        global grammh
        global apotelesmaLekt
                
        if(apotelesmaLekt[0]==token_noumero):
            fact = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]

        elif(apotelesmaLekt[0]==token_anoigei_parenthesh):
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]

            Eplace = expression()
            fact = Eplace

            if(apotelesmaLekt[0] == token_kleinei_parenthesh):
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]
                                
            else:
                print("den yparxei dexia parenthesi ')' meta to expression stin factor ",grammh)
                exit(0)
        elif( apotelesmaLekt[0] == token_identifier):
            apotelesma_factor = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
            fact = idtail(apotelesma_factor)
                        
        else:
            print("prepei na exoume constant h expression h variable stin factor",grammh)
            exit(0)
               
        return fact
        
    def idtail(onoma):
        global grammh
        global apotelesmaLekt
                
        if(apotelesmaLekt[0] == token_anoigei_parenthesh ):
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]

            actual_par_list()
            w=newTemp()
            genQuad('par', w, 'RET', '_')
            genQuad('call', onoma, '_', '_')
            
                        
            if(apotelesmaLekt[0]==token_kleinei_parenthesh):
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]
                return w
            else:
                print("prepei na exoume ) stin idtail",grammh)
                exit(0)
        else:
            return onoma

    def actual_par_list():
        global grammh
        global apotelesmaLekt
                
        if (apotelesmaLekt[0]==token_noumero or apotelesmaLekt[0]==token_anoigei_parenthesh or apotelesmaLekt[0]==token_identifier):
                    
            thisExpression = expression()
            genQuad('par', thisExpression, 'CV', '_')
                    
            while(apotelesmaLekt[0] == token_koma):
                apotelesmaLekt  = Lektikos()
                grammh = apotelesmaLekt[2]
                        
                thisExpression = expression()
                genQuad('par', thisExpression, 'CV', '_')

                
                        

    def optional_sign():
        global apotelesmaLekt
                
        if(apotelesmaLekt[0] == token_sin or apotelesmaLekt[0] == token_plin):
                        
            ADD_OP()
        
    def ADD_OP():
        global grammh
        global apotelesmaLekt
                
        if(apotelesmaLekt[0]==token_sin):
            apotelesmaddOp = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
        elif(apotelesmaLekt[0]==token_plin):
            apotelesmaddOp = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
        return apotelesmaddOp


    def MUL_OP():
        global grammh
        global apotelesmaLekt
                
        if (apotelesmaLekt[0] == token_epi):
            apotelesmamulop = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
        elif (apotelesmaLekt[0] == token_diairesh):
            apotelesmamulop = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
            
        return apotelesmamulop

                
    def condition():
        global grammh
        global apotelesmaLekt

        condition_true = []
        condition_false = []
                
        bool_term_1 = bool_term()

        condition_true = bool_term_1[0]
        condition_false = bool_term_1[1]
                
        while(apotelesmaLekt[0]==token_or):
            apotelesmaLekt=Lektikos()
            grammh = apotelesmaLekt[2]

            backPatch(condition_false, nextQuad())
                        
            bool_term_2 = bool_term()

            condition_true = merge(condition_true, bool_term_2[0])
            condition_false = bool_term_2[1]

        return condition_true, condition_false
                
                
    def bool_term():
        global grammh
        global apotelesmaLekt

        bool_term_true = []
        bool_term_false = []

        bool_factor_1 = bool_factor()

        bool_term_true = bool_factor_1[0]
        bool_term_false = bool_factor_1[1]
                
        while(apotelesmaLekt[0]==token_and):
            apotelesmaLekt=Lektikos()
            grammh = apotelesmaLekt[2]

            backPatch(bool_term_true, nextQuad())

            bool_factor_2 = bool_factor()

            bool_term_false = merge(bool_term_false, bool_factor_2[1])
            bool_term_true = bool_factor_2[0]
        
        return bool_term_true, bool_term_false

                
    def bool_factor():
        global grammh
        global apotelesmaLekt

        bool_factor_true = []
        bool_factor_false = []
                
        if(apotelesmaLekt[0]==token_not):
            apotelesmaLekt=Lektikos()
            grammh = apotelesmaLekt[2]

            C = condition()
            bool_factor_true = C[1]
            bool_factor_false = C[0]
        else:

            Eplace1 = expression()
            relop = REL_OP()
            Eplace2 = expression()
            bool_factor_true=makeList(nextQuad())

            genQuad(relop, Eplace1, Eplace2, '_')
            bool_factor_false=makeList(nextQuad())
            genQuad('jump', '_', '_', '_')

        return bool_factor_true, bool_factor_false

    def REL_OP():
        global grammh
        global apotelesmaLekt
                
        if(apotelesmaLekt[0]==token_iso):
            relop = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
        elif(apotelesmaLekt[0]==token_mikrotero):
            relop = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
        elif(apotelesmaLekt[0]==token_mikrotero_H_iso):
            relop = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
        elif(apotelesmaLekt[0]==token_diaforo):
            relop = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
        elif(apotelesmaLekt[0]== token_megalitero):
            relop = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
        elif(apotelesmaLekt[0]==token_megalitero_H_iso):
            relop = apotelesmaLekt[1]
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
        else:
            print("den yparxei = h < h <= h <> h >= h > ",grammh)
            exit(0)

        return relop

    def call_main_part():
        global grammh
        global apotelesmaLekt

        if(apotelesmaLekt[0] == token_hashtag_def):
            apotelesmaLekt = Lektikos()
            grammh = apotelesmaLekt[2]
                        
            if(apotelesmaLekt[0] == token_main):
                apotelesmaLekt = Lektikos()
                grammh = apotelesmaLekt[2]

                declarations()
                genQuad('begin_block','main','_','_')
                statements()
                genQuad('halt','_','_','_')
                genQuad('end_block','main','_','_')

                print_Symbol_table()

                delete_scope()


            else:
                print("den yparxei main stin call_main_part",grammh)
                exit(0) 
        else:
            print("den yparxei #def stin call_main_part",grammh)
            exit(0)

    apotelesmaLekt= Lektikos()
    grammh = apotelesmaLekt[2]
    startRule() 

def create(endiamesosFile):
     for i in range(len(lista_tetradwn)):
          tetrada = lista_tetradwn[i]
          endiamesosFile.write(str(tetrada[0]))
          endiamesosFile.write(" :  ")
          endiamesosFile.write(str(tetrada[1]))
          endiamesosFile.write("  ")
          endiamesosFile.write(str(tetrada[2]))
          endiamesosFile.write("  ")
          endiamesosFile.write(str(tetrada[3]))
          endiamesosFile.write("  ")
          endiamesosFile.write(str(tetrada[4]))
          endiamesosFile.write("\n")




endiamesos = open('endiamesos.int', 'w')
pinakas_symvolwn = open('pinakas_symvolwn.sym', 'w')

Syntaktikos() 

print("compilation successfully completed")

create(endiamesos)
pinakas_symvolwn.close()
endiamesos.close()



'''
def print_lista_tetradwn():
	'Prints lista_tetradwn'
	for i in range(len(lista_tetradwn)):
		print (str(lista_tetradwn[i][0])+" "+str(lista_tetradwn[i][1])+" "+str(lista_tetradwn[i][2])+" "+str(lista_tetradwn[i][3])+" "+str(lista_tetradwn[i][4]))

print_lista_tetradwn()
'''



#Trampas Eleftherios AM : 4625
