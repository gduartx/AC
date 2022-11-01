notas = open('notas.txt', 'r', encoding="UTF-8")          #Pega a lista de RA's, Nomes, Notas e Faltas
aprovados = open('aprovados.txt','w', encoding="UTF-8")   #Cria* um documento txt para alocar os aprovados
reprovados = open('reprovados.txt','w', encoding="UTF-8") #Cria* um documento txt para alocar os reprovados
acs = 0                                                   #Variavel para soma de todas as acs
menorAC = 11                                              #Para a menor Ac *11, porque qualquer nota será menor que 11
mediaAC = 0                                               #Para a media das AC's
prova = 0                                                 #Para a nota da prova
sub = 0                                                   #Para a nota substitutiva
notaf = 0                                                 #Para a nota final entre nota da prova e nota da prova substitutiva
mediaF = 0                                                #Para calcular a media final
nome = ''                                                 #Para alocar o nome em um dos dois arquivos txt
for i in notas:                                           #Percorre linha a linha da lista do arquivo notas.txt
    i = i.split(';')                                      #Separa a linha onde há o caractere ';'
    for j in range(2,7):                                  #Percorre do índice 2(1ª nota de Ac) índice 6(5ª nota de Ac)
        acs += float(i[j])                                #Soma todas as 5 AC's
        if menorAC > float(i[j]):                         #Compara a variavel {menorAC} com a atual nota de AC percorrida
            menorAC = float(i[j])                         #Caso {menorAC} seja menor que a AC percorrida, {menorAC} é atribuida pela AC percorrida
    mediaAC = (acs - menorAC)/4                           #Calcula a média das AC's, subtraindo a menor AC da soma de todas as 5 AC's e dividindo por 4
    prova = float(i[7])                                   #Atribui à variável {prova} a nota da prova
    sub = float(i[8])                                     #Atribui à variável {sub} a nota substitutiva
    if prova > sub:                                       #Compara a nota da prova com a prova substitutiva
        notaf = prova                                     #Caso a nota da prova seja maior do que a substitutiva, atribui à nota final 
    else:
        notaf = sub                                       #Senão, atribui a nota da prova substitutiva
    mediaF = (mediaAC + notaf) / 2                        #Calcula a media final com a soma entre a media das AC's com a nota final dividindo-as por 2
    nome = i[1]                                           #Atribui à vairável {nome} o índice 1, que é o nome e sobrenome do aluno

    if (mediaF >= 6.0) and (float(i[9]) <= 20):           #Verifica se a media final é maior ou igual a 6 e se o numero de faltas é menor ou igua a 20 
        aprovados.write(f'{nome}\n')                      #Caso verdade, o nome é atribuido ao documento aprovados.txt e há uma quebra de linha
    else:
        reprovados.write(f'{nome}\n')                     #Caso falso, o nome é atribuido ao documento reprovados.txt e há uma quebra de linha
    acs = 0                                               #Zera a soma das acs para a proxima linha do documento notas.txt
    menorAC = 10                                          #Zera a soma da menor ac para a proxima linha do documento notas.txt
