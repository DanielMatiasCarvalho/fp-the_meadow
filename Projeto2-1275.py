"""
A simulação de ecossistemas decorre num prado rodeado por montanhas. 
No início, algumas das posições estão ocupadas por animais, 
que podem ser predadores ou presas, e as restantes estão vazias 
ou contêm obstáculos. Os animais podem-se movimentar, alimentar, reproduzir e 
morrer, com regras diferentes para predadores ou presas. 
A população do prado evolui ao longo de etapas de tempo discretas 
(gerações) de acordo com estas regras. A simulação consiste na construção 
de gerações sucessivas da população no prado.

Autor:Daniel Carvalho
Última atualização: 17/11/2021

"""
#2.1.1-Tipo Abstrato de Dados (TAD) de posições
"""
O TAD posicao é usado para representar uma posição 
(x, y) de um prado arbitrariamente grande, sendo x e y 
dois valores inteiros não negativos.

A representação interna utilizada neste TAD é lista.
"""
def cria_posicao(x,y):
    """
    cria_posicao(x,y) recebe os valores correspondentes às coordenadas de uma
    posição e devolve a posição correspondente.
    
    Após fazer, a validação dos dados de entrada, procede-se a criar
    a posição com a representação interna usada.
    
    cria_posicao: int × int → posicao
    """    
    if type(x)!=int or type(y)!=int or x<0 or y<0:
        raise ValueError ("cria_posicao: argumentos invalidos")
    return [x,y]

def cria_copia_posicao(arg):
    """
    cria_copia_posicao(pos) recebe uma posição e devolve 
    uma cópia nova da posição.
    
    Após verificar que o argumento de entrada é uma posição, procede a fazer
    a sua cópia.
    
    cria_copia_posicao: posicao → posicao
    """    
    if eh_posicao(arg)==False:
        raise ValueError ("cria_copia_posicao: argumento invalido")
    return arg.copy()

def obter_pos_x(pos):
    """
    obter_pos_x(pos) devolve a componente x da posição pos.
    
    obter_pos_x : posicao → int
    """    
    return pos[0]

def obter_pos_y(pos):
    """
    obter_pos_y(pos) devolve a componente y da posição pos.
    
    obter_pos_y : posicao → int
    """    
    return pos[1]

def eh_posicao(arg):
    """
    eh_posicao(arg) devolve True caso o seu argumento seja um TAD posicao e
    False caso contrário.
    
    Procede-se a validar todos os elementos, devolvendo True ou False
    se representa uma posição ou não.
    
    eh_posicao: universal → booleano
    """    
    if type(arg)!= list or len(arg)!=2 or type(arg[0])!=int \
       or type(arg[1])!=int or arg[0]<0 or arg[1]<0:
        return False
    else:
        return True

def posicoes_iguais(p1,p2):
    """
    posicoes_iguais(p1, p2) devolve True apenas se p1 e p2 
    são posições e são iguais.
    
    Primeiro,verifica se ambos os argumentos são posção, procedendo a comparar
    os seus elementos x e y.
    
    posicoes_iguais: posicao × posicao → booleano
    """    
    if eh_posicao(p1)==True and eh_posicao(p2)==True \
       and obter_pos_x(p1)==obter_pos_x(p2) \
       and obter_pos_y(p1)==obter_pos_y(p2):
        return True
    else:
        return False

def posicao_para_str(pos):
    """
    posicao_para_str(pos) devolve a cadeia de caracteres 
    ‘(x, y)’ que representa o seu argumento, sendo os 
    valores x e y as coordenadas de pos.
    
    Utiliza-se ".format()" de forma a colocar os elementos x e y de pos, nos
    lugares pretendidos na string.
    
    posicao_para_str : posicao → str
    """    
    return "({}, {})".format(pos[0],pos[1])

def obter_posicoes_adjacentes(pos):
    """
    obter_posicoes_adjacentes(pos) devolve um tuplo com as posições adjacentes 
    à posição pos, começando pela posição acima de pos e 
    seguindo no sentido horário.
    
    Divivdiu-se em quatro partes esta função, correspondendo às quatro hipóteses
    que fazem sentido neste TAD, visto que tanto o elemnto x como o elemento y
    necessitam de ser maior ou iguais a 0.
    
    obter_posicoes_adjacentes: posicao → tuplo
    """    
    if obter_pos_x(pos)==0 and obter_pos_y(pos)==0:
        #no caso de ambos os elementos serem 0, ou seja, que esta posição
        #se situe no canto superior esquerdo do prado        
        return (cria_posicao(obter_pos_x(pos)+1,obter_pos_y(pos)),\
                cria_posicao(obter_pos_x(pos),obter_pos_y(pos)+1)) 
    
    elif obter_pos_x(pos)==0:
        #no caso que o elemnto x seja 0, ou seja, que esta posição se situe
        #no limite esquerdo do prado        
        return (cria_posicao(obter_pos_x(pos),obter_pos_y(pos)-1),\
                cria_posicao(obter_pos_x(pos)+1,obter_pos_y(pos)),\
                cria_posicao(obter_pos_x(pos),obter_pos_y(pos)+1))
    
    elif obter_pos_y(pos)==0:
        #no caso que o elemnto y seja 0, ou seja, que esta posição se situe
        #no limite superior do prado          
        return (cria_posicao(obter_pos_x(pos)+1,obter_pos_y(pos)),\
                cria_posicao(obter_pos_x(pos),obter_pos_y(pos)+1),\
                cria_posicao(obter_pos_x(pos)-1,obter_pos_y(pos)))
    
    else:
        #caso restantes que fazem sentido neste TAD, mas nem sempre no prado
        return (cria_posicao(obter_pos_x(pos),obter_pos_y(pos)-1),\
                cria_posicao(obter_pos_x(pos)+1,obter_pos_y(pos)),\
                cria_posicao(obter_pos_x(pos),obter_pos_y(pos)+1),\
                cria_posicao(obter_pos_x(pos)-1,obter_pos_y(pos)))

def ordenar_posicoes(tuplo):
    """
    ordenar_posicoes(tuplo) devolve um tuplo contendo as mesmas posições 
    do tuplo fornecido como argumento, ordenadas de acordo com a 
    ordem de leitura do prado.
    
    De acordo com as regras do prado, lê-se primeiramente, as posições que
    possuem elemento y menor, pelo que se primeiro ordena desta forma.
    De seguida, como para mesmo elemento y, lê-se primeiro aqueles em que o
    elemento x é menor, ordena-se para as posições em que o seu elemento y
    é igual, do seu menor elemento x para o maior.
    
    ordenar_posicoes: tuplo → tuplo
    """    
    lista=sorted(tuplo, key= lambda posicao: obter_pos_y(posicao))
    #ordenação pelo elemento y
    comp=len(lista)-1
    alterado=True
    while alterado:
        #ordenação por borbulhamento
        alterado=False
        for i in range(comp):
            #ordena-se as posições em que elemento y é igual, do menor elemento
            #x ao maior            
            if obter_pos_y(lista[i])==obter_pos_y(lista[i+1]) and \
               obter_pos_x(lista[i])>obter_pos_x(lista[i+1]):
                lista[i],lista[i+1]=lista[i+1],lista[i]
                alterado=True
    return tuple(lista)
    
#2.1.2-Tipo Abstrato de Dados (TAD) de animais
"""
O TAD animal é usado para representar os animais do simulador de ecossistemas 
que habitam o prado, existindo de dois tipos: predadores e presas. Os predadores 
são caracterizados pela espécie, idade, frequência de reprodução, 
fome e frequência de alimentação. As presas são apenas caracterizadas pela 
espécie, idade e frequência de reprodução.

A representação interna deste tipo de dados é dicionário.
"""
def cria_animal(s,r,a):
    """
    cria_animal(s, r, a) recebe uma cadeia de caracteres s não vazia 
    correspondente à espécie do animal e dois valores inteiros 
    correspondentes à frequˆencia de reprodução r (maior do que 0) e 
    à frequˆencia de alimentação a (maior ou igual que 0); e 
    devolve o animal. Animais com frequência de alimentação maior que 0 são 
    considerados predadores, caso contrário sâo considerados presas.
    
    Após validar os dados de entrada, cria-se o animal, com a 
    representação interna escolhida. Neste caso, ao criar o animal, 
    foi acrescetado dois parâmetros, um de idade e um de fome.
    
    cria_animal: str × int × int → animal
    """    
    if type(s)!=str or len(s)<=0 or type(r)!=int or r<=0 or type(a)!=int or a<0:
        raise ValueError ("cria_animal: argumentos invalidos")
    else:
        return {"s":s,"r":r,"a":a,"i":0,"f":0}

def cria_copia_animal(animal):
    """
    cria_copia_animal(a) recebe um animal a (predador ou presa) e devolve uma
    nova cópia do animal.
    
    Após validar que o arg de entrada é uma animal, procede-se a 
    criar uma cópia.
    
    cria_copia_animal: animal → animal
    """    
    if eh_animal(animal)==False:
        raise ValueError ("cria_copia_animal: argumentos invalidos")
    else:
        return animal.copy()

def obter_especie(animal):
    """
    obter_especie(animal) devolve a cadeia de caracteres 
    correspondente à espécie do animal.
    
    obter_especie: animal → str
    """    
    return animal["s"]

def obter_freq_reproducao(animal):
    """
    obter_freq_reproducao(animal) devolve a frequência de reprodução do 
    animal a.
    
    obter_freq_reproducao: animal → int
    """    
    return animal["r"]

def obter_freq_alimentacao(animal):
    """
    obter freq alimentacao(animal) devolve a frequência de alimentação 
    do animal a (as presas devolvem sempre 0).
    
    obter_freq_alimentacao: animal → int
    """    
    return animal["a"]

def obter_idade(animal):
    """
    obter_idade(a) devolve a idade do animal a.
    
    obter_idade: animal → int
    """    
    return animal["i"]

def obter_fome(animal):
    """
    obter_fome(a) devolve a fome do animal a (as presas devolvem sempre 0).

    obter_fome: animal → int
    """    
    return animal["f"]

def aumenta_idade(animal):
    """
    aumenta_idade(a) modifica destrutivamente o animal a incrementando o 
    valor da sua idade em uma unidade, e devolve o próprio animal.
    
    aumenta_idade: animal → animal
    """    
    animal["i"]=animal["i"]+1
    return animal

def reset_idade(animal):
    """
    reset idade(a) modifica destrutivamente o animal a definindo o valor da sua
    idade igual a 0, e devolve o próprio animal.
    
    reset_idade: animal → animal
    """    
    animal["i"]=0
    return animal

def aumenta_fome(animal):
    """
    aumenta_fome(a) modifica destrutivamente o animal predador a incrementando 
    o valor da sua fome em uma unidade, e devolve o próprio animal. Esta
    operação não modifica os animais presa.
    
    aumenta_fome: animal → animal
    """    
    if eh_predador(animal)==True:
        animal["f"]=animal["f"]+1
        return animal #predador
    else:
        return animal #presa
    
def reset_fome(animal):
    """
    reset_fome(a) modifica destrutivamente o animal predador a definindo o 
    valor da sua fome igual a 0, e devolve o próprio animal. Esta operação não 
    modifica os animais presa.

    reset fome: animal → animal
    """    
    if eh_predador(animal)==True:
        animal["f"]==0
        return animal #predador
    else:
        return animal #presa

def eh_animal(arg):
    """
    eh_animal(arg) devolve True caso o seu argumento seja um TAD animal e
    False caso contrário.
    
    Após verificar se a o arg está de acordo com a representação interna do 
    animal, e se os seus elementos estão definidos corretamente, devolve True 
    or False dependendo do resultado.
    
    eh_animal: universal → booleano
    """    
    if type(arg)!=dict or len(arg)<5 or "s" not in arg or "r" not in arg\
       or "a" not in arg or "i" not in arg or "f" not in arg\
       or type(arg["s"])!=str or len(arg["s"])<=0 or type(arg["r"])!=int or \
       arg["r"]<=0 or type(arg["a"])!=int or arg["a"]<0 or type(arg["i"])!=int\
       or type(arg["f"])!=int or arg["i"]<0 or arg["f"]<0:
        return False
    else:
        return True

def eh_predador(arg):
    """
    eh_predador(arg) devolve True caso o seu argumento seja um TAD animal do
    tipo predador e False caso contrário.
    
    Esta função verfica se o arg é animal e se a sua frequência de alimentação
    é maior que 0.
    
    eh_predador : universal → booleano
    """    
    return eh_animal(arg)==True and obter_freq_alimentacao(arg)>0

def eh_presa(arg):
    """
    eh_predador(arg) devolve True caso o seu argumento seja um TAD animal do
    tipo predador e False caso contrário.
    
    Esta função verfica se o arg é animal e se a sua frequência de alimentação
    é 0.
    
    eh_presa : universal → booleano
    """      
    return eh_animal(arg)==True and obter_freq_alimentacao(arg)==0

def animais_iguais(a1,a2):
    """
    animais iguais(a1, a2) devolve True apenas se a1 e a2 são animais e são
    iguais
    
    animais_iguais: animal × animal → booleano
    """    
    return eh_animal(a1) and eh_animal(a2) and\
           obter_especie(a1)==obter_especie(a2) and \
           obter_freq_reproducao(a1)==obter_freq_reproducao(a2) and \
           obter_freq_alimentacao(a1)==obter_freq_alimentacao(a2) and \
           obter_idade(a1)==obter_idade(a2) and \
           obter_fome(a1)==obter_fome(a2)

def animal_para_char(animal):
    """
    animal_para_char(a) devolve a cadeia de caracteres dum único elemento 
    correspondente ao primeiro carácter da espécie do animal passada 
    por argumento, em maiúscula para animais predadores e em minúscula 
    para animais presa.
    
    animal_para_char : animal → str
    """    
    if eh_presa(animal)==True:
        return obter_especie(animal)[0].lower() #animais presa
    else:
        return chr(ord(obter_especie(animal)[0].lower())-32) #animais predadores
    
def animal_para_str(animal):
    """
    animal_para_str(a) devolve a cadeia de caracteres que representa o animal,
    por exemplo:
    >>> r1 = cria_animal(’rabbit’, 5, 0)
    >>> f1 = cria_animal(’fox’, 20, 10)
    >>> animal_para_str(r1)
    ’rabbit [0/5]’
    >>> animal_para_str(f1)
    ’fox [0/20;0/10]’
    
    animal_para_str : animal → str
    """    
    if eh_presa(animal)==True:
        #para presa é apenas necessário a freq. reprodução e a idade     
        return "{} [{}/{}]".format(obter_especie(animal),obter_idade(animal),\
                                   obter_freq_reproducao(animal))
    else:
        #no entanto, para os predadores, tmb é necessário a fome e a 
        #freq. alimentação   
        return "{} [{}/{};{}/{}]".format(obter_especie(animal),\
                                         obter_idade(animal),\
                                         obter_freq_reproducao(animal),\
                                         obter_fome(animal),\
                                         obter_freq_alimentacao(animal))

def eh_animal_fertil(animal):
    """
    eh_animal_fertil(a) devolve True caso o animal a tenha atingido a idade de 
    reprodução e False caso contrário.
    
    eh_animal_fertil: animal → booleano
    """    
    if obter_idade(animal)>=obter_freq_reproducao(animal):
        return True
    else:
        return False

def eh_animal_faminto(animal):
    """
    eh_animal_faminto(a) devolve True caso o animal a tenha atingindo um valor 
    de fome igual ou superior à sua frequência de alimentação e False caso 
    contrário. As presas devolvem sempre False.
    
    eh_animal_faminto: animal → booleano
    """    
    if eh_presa(animal):
        return False
    elif obter_fome(animal)>=obter_freq_alimentacao(animal):
        return True
    else:
        return False
    
def reproduz_animal(animal):
    """
    reproduz_animal(a) recebe um animal a devolvendo um novo animal da mesma
    espécie com idade e fome igual a 0, e modificando destrutivamente o 
    animal passado como argumento a alterando a sua idade para 0.
    
    reproduz_animal: animal → animal
    """    
    animal=reset_idade(animal) #Alterando a idade do animal passado para 0
    #Criação do animal "resultado" da reprodução
    return cria_animal(obter_especie(animal), obter_freq_reproducao(animal),\
                       obter_freq_alimentacao(animal))

#2.1.3-Tipo Abstrato de Dados (TAD) do prado
def cria_prado(d,r,a,p):
    """
    cria_prado(d, r, a, p) recebe uma posicão d correspondente à posição que
    ocupa a montanha do canto inferior direito do prado, um tuplo r de 0 ou
    mais posições correspondentes aos rochedos que não são as montanhas dos
    limites exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p 
    da mesma dimensão do tuplo a com as posições correspondentes ocupadas pelos
    animais; e devolve o prado que representa internamente o mapa e os animais
    presentes.
    
    cria_prado: posicao × tuplo × tuplo × tuplo → prado
    """
    if eh_posicao(d)==False or type(r)!=tuple or type(a)!=tuple or len(a)<1 or\
       type(p)!=tuple or len(a)!=len(p):
        #verifica se os tipos e comprimentos dos elementos de entrada estão
        #corretos
        raise ValueError ("cria_prado: argumentos invalidos")
    for ind in range(len(r)):
        #verifica se as posições dos rochedos estão bem definidas, 
        #se encontram dentro dos
        #limites dos prados (na zona delimitada pelas montanhas), e se
        #a sua posição coincide com alguma de um animal ou de um outro
        #rochedo definido
        if eh_posicao(r[ind])==False or r[ind] in p or\
           obter_pos_x(r[ind])==0 or\
           obter_pos_x(r[ind])>=obter_pos_x(d) or\
           obter_pos_y(r[ind])==0 or obter_pos_y(r[ind])>=obter_pos_y(d):
            raise ValueError ("cria_prado: argumentos invalidos")
        for verificacao in range(ind,len(r)-1):
            if posicoes_iguais(r[ind],r[verificacao+1])==True:
                raise ValueError ("cria_prado: argumentos invalidos")
        for verificacao2 in range(len(p)):
            if posicoes_iguais(r[ind],p[verificacao2])==True:
                raise ValueError ("cria_prado: argumentos invalidos")        
    
    for animais in a:
        #verificação se os elementos do tuplo são do tipo correto
        if eh_animal(animais)==False:
            raise ValueError ("cria_prado: argumentos invalidos")
    
    for ind in range(len(p)):
        #verifica se as posições dos aniamis estão bem definidas, se se 
        #encontram dentro dos limites do prado (zona delimitada pelas
        #montanhas), e se a posição de um animal coincide com uma de 
        #qualquer outro animal ou de um rochedo
        if eh_posicao(p[ind])==False or p[ind] in r or\
           obter_pos_x(p[ind])==0 or\
           obter_pos_x(p[ind])>=obter_pos_x(d) or\
           obter_pos_y(p[ind])==0 or \
           obter_pos_y(p[ind])>=obter_pos_y(d):           
            raise ValueError ("cria_prado: argumentos invalidos")
        for verificacao in range(ind,len(p)-1):
            if posicoes_iguais(p[ind],p[verificacao+1])==True:
                raise ValueError ("cria_prado: argumentos invalidos")
        for verificacao2 in range(len(r)):
            if posicoes_iguais(p[ind],r[verificacao2])==True:
                raise ValueError ("cria_prado: argumentos invalidos")
                                  
        
    return {"d":d,"r":r,"a":a,"p":p}

def cria_copia_prado(m):
    """
    cria_copia_prado(m) recebe um prado e devolve uma nova cópia do prado.
    
    cria_copia_prado: prado → prado
    """
    if eh_prado(m)==False:
        raise ValueError ("cria_copia_prado: argumentos invalidos")
    r1=()
    a1=()
    p1=()
    for rochedo in m["r"]: 
        #cópia individual de cada posição do rochedo 
        #(devido à definição interna de posições)
        r1+=(rochedo.copy(),)
    for animal in m["a"]:
        #cópia individual de cada animal 
        #(devido à definição interna de animal)        
        a1+=(animal.copy(),)
    for posicao in m["p"]:
        #cópia individual de cada posição do animal 
        #(devido à definição interna de posições)          
        p1+=(posicao.copy(),)    
    return {"d":m["d"].copy(),"r":r1,"a":a1,"p":p1}

def obter_tamanho_x(m):
    """
    obter_tamanho_x(m) devolve o valor inteiro que corresponde à dimensão Nx
    do prado
    
    obter_tamanho_x: prado → int
    """
    return obter_pos_x(m["d"])+1

def obter_tamanho_y(m):
    """
    obter_tamanho_y(m) devolve o valor inteiro que corresponde à dimensão Ny
    do prado.
    
    obter_tamanho_y: prado → int
    """
    return obter_pos_y(m["d"])+1

def obter_numero_predadores(m):
    """
    obter_numero_predadores(m) devolve o número de animais predadores no prado.
    
    obter_numero_predadores: prado → int
    """
    res=0
    for animais in m["a"]:
        if eh_predador(animais)==True:
            res+=1
    return res

def obter_numero_presas(m):
    """
    obter_numero_presas(m) devolve o número de animais presa no prado.
    
    obter_numero_presas: prado → int
    """
    res=0
    for animais in m["a"]:
        if eh_presa(animais)==True:
            res+=1
    return res

def obter_todos_animais(m):
    """
    Função auxiliar
    
    obter_todos_animais(m) devolve um tuplo de todos os animais existentes
    no prado.
    
    obter_todos_animais: prado → tuplo
    """
    return m["a"]

def obter_posicao_rochedos(m):
    """
    Função auxiliar
    
    obter_posicao_rochedos(m) devolve um tuplo das posições dos rochedos
    no prado.
    
    obter_posicao_rochedos: prado → tuplo
    """
    return m["r"]

def obter_posicao_animais(m):
    """
    obter_posicao_animais(m) devolve um tuplo contendo as posições do prado
    ocupadas por animais, ordenadas em ordem de leitura do prado.
    
    obter_posicao_animais: prado → tuplo posicoes
    """
    return ordenar_posicoes(m["p"])

def obter_animal(m,pos):
    """
    obter_animal(m, pos) devolve o animal do prado que se encontra 
    na posição pos.
    
    obter_animal: prado × posicao → animal
    """
    for i in range(len(m["p"])):
        if posicoes_iguais(pos, m["p"][i]):
            #o indice das posições dos animais no tuplo das posções dos aniamis,
            #corresponde ao animal do mesmo indice no tuplo dos aniamais
            return m["a"][i]

def eliminar_animal(m,p):
    """
    eliminar_animal(m, p) modifica destrutivamente o prado m eliminando o 
    animal da posição p deixando-a livre. Devolve o próprio prado.

    eliminar_animal: prado × posicao → prado
    """
    for i in range(len(m["p"])):
        if posicoes_iguais(p,m["p"][i]):
            if i==0: #se a posição for a primeira do tuplo
                m["p"]=m["p"][1:]
                m["a"]=m["a"][1:]
            elif i==len(m["p"])-1: #se a posição for a última do tuplo
                m["p"]=m["p"][:i]
                m["a"]=m["a"][:i]
            else:
                m["p"]=m["p"][:i]+m["p"][i+1:]
                m["a"]=m["a"][:i] + m["a"][i+1:]
            return m

def mover_animal(m,p1,p2):
    """
    mover_animal(m, p1, p2) modifica destrutivamente o prado m movimentando
    o animal da posição p1 para a nova posição p2, deixando livre a posição onde
    se encontrava. Devolve o próprio prado.
    
    mover_animal: prado × posicao × posicao → prado
    """
    for i in range(len(m["p"])):
        if posicoes_iguais(p1,m["p"][i]):
            if i==0:#se a posição for a primeira do tuplo
                m["p"]= (p2,) + m["p"][1:]
                
            elif i==len(m["p"])-1:#se a posição for a última do tuplo
                m["p"]=m["p"][:i]+(p2,)
                
            else:
                m["p"]=m["p"][:i]+ (p2,) + m["p"][i+1:]
            return m

def inserir_animal(m,a,p):
    """
    inserir_animal(m, a, p) modifica destrutivamente o prado m acrescentando
    na posição p do prado o animal a passado com argumento. Devolve o próprio
    prado.
    
    inserir_animal: prado × animal × posicao → prado
    """
    m["a"]=m["a"]+(a,)
    m["p"]=m["p"]+(p,)
    return m

def eh_prado(arg):
    """
    eh_prado(arg) devolve True caso o seu argumento seja um TAD prado e False
    caso contrário.
    
    eh_prado: universal → booleano
    """
    if  type(arg)!=dict or len(arg)!=4 or "d" not in arg or\
        "r" not in arg or "a" not in arg or "p" not in arg or\
        eh_posicao(arg["d"])==False or type(arg["r"])!=tuple or\
        type(arg["a"])!=tuple or len(arg["a"])<1 or type(arg["p"])!=tuple or\
        len(arg["a"])!=len(arg["p"]):
        #verificação do argumento de entrada e os seus componentes
            return False
        
    for ind in range(len(arg["r"])):
        #verifica se as posições dos rochedos estão bem definidas, 
        #se encontram dentro dos
        #limites dos prados (na zona delimitada pelas montanhas), e se
        #a sua posição coincide com alguma de um animal ou de um outro
        #rochedo definido        
        if eh_posicao(arg["r"][ind])==False or arg["r"][ind] in arg["p"] or\
            obter_pos_x(arg["r"][ind])==0 or\
            obter_pos_x(arg["r"][ind])>=obter_pos_x(arg["d"]) or\
            obter_pos_y(arg["r"][ind])==0 or\
            obter_pos_y(arg["r"][ind])>=obter_pos_y(arg["d"]):
            return False
        for verificacao in range(ind,len(arg["r"])-1):
            if posicoes_iguais(arg["r"][ind],arg["r"][verificacao+1])==True:
                return False
        for verificacao2 in range(len(arg["p"])):
            if posicoes_iguais(arg["r"][ind],arg["p"][verificacao2])==True:
                return False       
        
    for animais in arg["a"]:
        #verificação se os elementos do tuplo são do tipo correto
        if eh_animal(animais)==False:
            return False
        
    for ind in range(len(arg["p"])):
        #verifica se as posições dos aniamis estão bem definidas, se se 
        #encontram dentro dos limites do prado (zona delimitada pelas
        #montanhas), e se a posição de um animal coincide com uma de 
        #qualquer outro animal ou de um rochedo        
        if eh_posicao(arg["p"][ind])==False or arg["p"][ind] in arg["r"] or\
            obter_pos_x(arg["p"][ind])==0 or\
            obter_pos_x(arg["p"][ind])==obter_pos_x(arg["d"]) or\
            obter_pos_y(arg["p"][ind])==0 or \
            obter_pos_y(arg["p"][ind])==obter_pos_y(arg["d"]):           
            return False
        for verificacao in range(ind,len(arg["p"])-1):
            if posicoes_iguais(arg["p"][ind],arg["p"][verificacao+1])==True:
                return False
        for verificacao2 in range(len(arg["r"])):
            if posicoes_iguais(arg["p"][ind],arg["r"][verificacao2])==True:
                return False
    return True  
    
def eh_posicao_animal(m,p):
    """
    eh_posicao_animal(m, p) devolve True apenas no caso da posição p do prado
    estar ocupada por um animal.
    
    eh_posicao_animal: prado × posicao → booleano
    """
    for pos_animal in obter_posicao_animais(m):
        if posicoes_iguais(p,pos_animal):
            return True
    return False

def eh_posicao_obstaculo(m,p):
    """
    eh posicao obstaculo(m, p) devolve True apenas no caso da posição p do prado
    corresponder a uma montanha ou rochedo.
    
    eh_posicao_obstaculo: prado × posicao 7→ booleano
    """
    if obter_pos_x(p)==obter_tamanho_x(m)-1 or\
       obter_pos_y(p)==obter_tamanho_y(m)-1 or obter_pos_x(p)==0 or\
       obter_pos_y(p)==0:
        #verificação se é uma montanha
        return True
    
    for rochedos in m["r"]:
        #verificação se é rochedo
        if posicoes_iguais(p,rochedos):
            return True
    
    return False

def eh_posicao_livre(m,p):
    """
    eh_posicao_livre(m, p) devolve True apenas no caso da posição p do prado
    corresponder a um espaço livre (sem animais, nem obstáculos).
    
    eh_posicao_livre: prado × posicao → booleano
    """
    if obter_pos_x(p)>=obter_tamanho_x(m) and\
       obter_pos_y(p)>=obter_tamanho_y(m):
        return False
    if eh_posicao_obstaculo(m,p)==False and eh_posicao_animal(m,p)==False:
        return True
    else:
        return False
    
def prados_iguais(p1,p2):
    """
    prados_iguais(p1, p2) devolve True apenas se p1 e p2 forem prados e forem
    iguais.
    
    É válido se ambos os argumentos são prados, se as suas dimensões
    coincidem, se possuem os mesmos animais nas mesmas quantidades e posições e
    se as posições dos rochedos são iguais.
    
    prados_iguais: prado × prado → booleano
    """
    return eh_prado(p1) and eh_prado(p2) and\
           obter_tamanho_x(p1)==obter_tamanho_x(p2) and\
           obter_tamanho_y(p1)==obter_tamanho_y(p2) and\
           obter_numero_predadores(p1)==obter_numero_predadores(p2) and\
           obter_numero_presas(p1)==obter_numero_presas(p2) and\
           obter_posicao_animais(p1)==obter_posicao_animais(p2) and\
           obter_todos_animais(p1)==obter_todos_animais(p2) and\
           obter_posicao_rochedos(p1)==obter_posicao_rochedos(p2)

def prado_para_str(m):
    """
    prado_para_str(m) devolve uma cadeia de caracteres que representa o prado
    como por exemplo:
    
    >>> dim = cria_posicao(11, 4)
    >>> obs = (cria_posicao(4,2), cria_posicao(5,2))
    >>> an1 = tuple(cria_animal(’rabbit’, 5, 0) for i in range(3))
    >>> an2 = (cria_animal(’lynx’, 20, 15),)
    >>> pos = tuple(cria_posicao(p[0],p[1]) \
                            for p in ((5,1),(7,2),(10,1),(6,1)))
    >>> prado = cria_prado(dim, obs, an1+an2, pos)
    >>> print(prado_para_str(prado))
    +----------+
    |....rL...r|
    |...@@.r...|
    |..........|
    +----------+
    
    prado_para_str : prado → str
    """
    res="+" + "-"*(obter_tamanho_x(m)-2) + "+\n"
    #primeira linha
    for y in range(1,obter_tamanho_y(m)-1):
        #todas as linhas excepto a primeira e a última
        res+="|"
        for x in range(1,obter_tamanho_x(m)-1):
            #todas as colunas excepto a primeira e a última
            if eh_posicao_livre(m,cria_posicao(x,y))==True:
                res+="."
            else:
                if eh_posicao_obstaculo(m,cria_posicao(x,y))==True:
                    #rochedos
                    res+="@"
                else:#animal na posição correspondente
                    res+="{}".format(\
                        animal_para_char(obter_animal(m,cria_posicao(x,y))))
        res+="|\n" #final da linha
    res+="+" + "-"*(obter_tamanho_x(m)-2) + "+" #última linha
    return res

def obter_valor_numerico(m,p):
    """
    obter_valor_numerico(m, p) devolve o valor numérico da posição p 
    correspondente à ordem de leitura no prado m.
    
    obter_valor_numerico: prado × posicao → int
    """
    return (obter_tamanho_x(m)*(obter_pos_y(p))+obter_pos_x(p))

def obter_movimento(m,pos):
    """
    obter_movimento(m, pos) devolve a posição seguinte do animal na posição 
    pos dentro do prado m de acordo com as regras de movimento dos animais 
    no prado.
    
    obter_movimento: prado × posicao → posicao
    """
    posicoes_possiveis=obter_posicoes_adjacentes(pos)
    presas=[]
    livres=[]
    for posicao1 in posicoes_possiveis:
        if eh_posicao_animal(m,posicao1) and eh_presa(obter_animal(m,posicao1)):
            #verifica se existe presas adjacentemente
            presas+=[posicao1]
    for posicao2 in posicoes_possiveis:
        if eh_posicao_livre(m,posicao2):
            #verifica todas as posições livres adjacentes 
            livres+=[posicao2]
    if eh_predador(obter_animal(m,pos)) and len(presas)>0:
        #se for predador e existir presas adjacentes
        p=len(presas)
        return presas[obter_valor_numerico(m,pos)%p]
    elif len(livres)>0: #qualquer animal com posições livres adjacentes
        p=len(livres)
        return livres[obter_valor_numerico(m,pos)%p]
    else: #não se move
        return pos
    
        

#2.2.1-criação de uma geração
def geracao(prado):
    """
    geracao(m) é a função auxiliar que modifica o prado m fornecido 
    como argumento de acordo com a evolução correspondente a uma geração 
    completa, e devolve o próprio prado. Isto é, seguindo a ordem de leitura 
    do prado, cada animal (vivo) realiza o seu turno de ação de acordo com 
    as regras descritas.
    
    geracao: prado → prado 
    """
    pos_animais=obter_posicao_animais(prado)
    #posições dos animais ordenadas pela ordem de leitura do prado
    lista_comidos=[]
    #lista daqueles que foram comidos
    for posicao in pos_animais:
        verificacao=False
        for pos in lista_comidos:
            if posicoes_iguais(pos,posicao):
                verificacao=True
                break
        #verifica se foi comido ou não para executar o resto do código
        if not verificacao:
            animal=obter_animal(prado,posicao)
            #animal de que está a tratar
            movimento=obter_movimento(prado,posicao)
            #movimento que vai executar
            if eh_presa(animal):
                animal=aumenta_idade(animal)
                if not posicoes_iguais(posicao,movimento):
                    #verifica se o animal se pode mover
                    prado=mover_animal(prado,posicao,movimento)
                    if eh_animal_fertil(animal):
                        #após mover, verifica se é fértil o animal
                        # se sim, cria-se um animal na posição anterior
                        prado=inserir_animal(\
                            prado,reproduz_animal(animal),posicao)
            else:
                #predadores
                animal=aumenta_idade(animal)
                animal=aumenta_fome(animal)
                if not posicoes_iguais(posicao,movimento):
                    #verifica se o animal pode-se mover
                    if eh_presa(obter_animal(prado,movimento)):
                        #verifica se a posição para onde se move é uma presa
                        prado=eliminar_animal(prado,movimento)
                        lista_comidos.append(movimento)
                        #elimina a presa, adicionando-a à lista_comidos
                        animal=reset_fome(animal)
    
                    prado=mover_animal(prado,posicao,movimento)
                    if eh_animal_fertil(animal):
                        #após mover, verifica a fertilidade e sim
                        #coloca um animal na posição anterior
                        prado=inserir_animal(\
                            prado,reproduz_animal(animal),posicao)
                        
                if eh_animal_faminto(animal):
                    #verifica a fome do animal
                    prado=eliminar_animal(prado,movimento)                    

    return prado

#2.2.2-simulação do ecossistema
def simula_ecossistema(f,geracoes,verboso):
    """
    simula ecossitema(f, geracoes, verboso) é a função principal que 
    permite simular  o ecossistema de um prado. A função recebe uma 
    cadeia de caracteres f,  um valor inteiro geracoes e um valor booleano  
    verboso e devolve o tuplo de dois  elementos correspondentes ao número de 
    predadores e presas no prado no fim  da simulação. A cadeia de caracteres 
    f passada por argumento corresponde  ao nome do ficheiro de configuração 
    da simulação. O valor inteiro geracoes corresponde ao número de gerações 
    a simular. O argumento booleano verboso ativa o modo verboso (True) ou o 
    modo quiet (False). No modo quiet  mostra-se pela saída standard o prado, 
    o número de animais e o número  de geração no início da simulação e 
    após a última geração. No modo verboso, após cada geração, 
    mostra-se também o prado,  o número de animais e o número de geração, 
    apenas se o número de animais predadores ou presas se tiver alterado.
    
    simula ecossistema: str × int × booleano → tuplo
    """
    with open(f,"r") as fich:
        linhas=[eval(linha) for linha in fich.readlines()]
        #transformação das stt em tuplos e retirar o \n
        d=cria_posicao(linhas[0][0],linhas[0][1])
        #posição do canto inferior direito
        r=()
        for el in linhas[1]:
            #posições dos rochedos
            r=r+(cria_posicao(el[0],el[1]),)
        a=()
        p=()
        for el in linhas[2:]:
            #tuplo dos animais
            a=a+(cria_animal(el[0],el[1],el[2]),)
            #tuplo das posições dos animais
            p=p+(cria_posicao(el[3][0],el[3][1]),)
        prado=cria_prado(d,r,a,p) #criação do prado
        
        
    print("Predadores:",obter_numero_predadores(prado),"vs Presas:",\
            obter_numero_presas(prado),"(Gen. {})".format(0))
    print(prado_para_str(prado)) #prado na Ger.0
    
    for ger in range(1,geracoes+1):
        #gerações seguintes até à desejada
        prado_ant=cria_copia_prado(prado) #prado antes da geracao
        
        predadores=obter_numero_predadores(prado_ant)
        #predadores antes da geracao
        presas=obter_numero_presas(prado_ant)
        #presas antes da geracao
        
        geracao(prado) #prado depois da geracao
        
        predadores_ger_seg=obter_numero_predadores(prado)
        #predadores depois da geracao
        presas_ger_seg=obter_numero_presas(prado) 
        #presas depois da geracao
        
        if verboso:
            if obter_posicao_animais(prado_ant)==obter_posicao_animais(prado) and\
               predadores==predadores_ger_seg and presas==presas_ger_seg:
                #quando o número de animais não se altera nem as suas 
                #posições
                return (predadores_ger_seg,presas_ger_seg)  
            
            if predadores!=predadores_ger_seg or presas!=presas_ger_seg:
                #número de animais alterou-se
                print("Predadores:",predadores_ger_seg,"vs Presas:",\
                      presas_ger_seg,"(Gen. {})".format(ger))
                print(prado_para_str(prado))
                
            if ger==geracoes:
                #no caso da última geração ser diferente da anterior
                print("Predadores:",predadores_ger_seg,"vs Presas:",\
                      presas_ger_seg,"(Gen. {})".format(ger))
                print(prado_para_str(prado))
                return (predadores_ger_seg,presas_ger_seg)                
        else: 
            if ger==geracoes:
                #última geração
                print("Predadores:",predadores_ger_seg,"vs Presas:",\
                      presas_ger_seg,"(Gen. {})".format(ger))
                print(prado_para_str(prado))
                return (predadores_ger_seg,presas_ger_seg)
