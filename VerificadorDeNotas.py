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


'''                                                       #Formato de lista de RA's, Nomes, Notas(5 AC's, Prova e Sub) e Faltas é, por exemplo: 2101613;Bárbara Correia;6;5;8;3;7;5;0;8
notas.txt:
2101254;Benício Pires;3;7;6;8;0;5;6;4
2101624;Bruna Gonçalves;4;6;8;3;0;4;0;0
2101533;Danilo Jesus;8;7;7.25;7;0;3.75;5;0
2101969;Ana Carolina Silva;4;6;7;6;0;8.5;0;8
2101623;Ana Lívia Gomes;5;7;8;3;0;8;0;20
2101779;Lavínia Duarte;10;5;7;8;0;7;0;8
2101764;Gustavo Henrique Barros;8;5;6;7;0;3;8;4
2101346;Marcos Vinicius Sales;5;7;9;8;0;9;0;0
2102630;Maria Vitória Jesus;9.5;0;0;7;0;1;0;0
2102562;Sarah Rodrigues;6;6;6;1;0;1;9;8
2101999;Stephany Novaes;4;9;8;8;0;3;6;8
2101199;Vitor Hugo Farias;5;5;8;1;0;6;9.25;12
2101635;Yasmin Fernandes;5;7;6;8;0;5;6;8
2101681;Maria Julia Martins;8;8;6.5;6;1;7;0;8
2101100;Ana Beatriz Cunha;4;9;7;7;1;0;5;4
2101145;João Vitor Moraes;1;8;8;0;1;10;0;4
2101757;Juliana Peixoto;6.5;7;8;7;1;10;0;0
2101583;Mariane Caldeira;8;6;6;6;1;4;0;0
2102637;Isadora Souza;1;6;9;7;1.5;5.25;0;16
2101504;Lucas Gabriel Alves;3;5;7;5;2;8;0;8
2101702;Benício Cavalcanti;10;6;7;5;3;5;0;4
2101116;Luna Melo;9;7;0;3;3;8;0;4
2101707;Ian Novaes;3;7;6;4;3;8;0;0
2101653;Alícia Sales;2;6;8;7;3.5;7;0;0
2101784;Nicole Melo;10;5;9;0;4;7;0;0
2101367;Beatriz Caldeira;6.5;5;7;7;5;0;7;0
2102650;Leonardo Novaes;3;7;8;7;5;4;3.5;28
2101158;Maria Cecília da Rocha;9;7;8;4;5;8;4;4
2101315;Maria Fernanda Dias;2;6;7.5;2;5;0;0;4
2102195;Nina Fogaça;7;8;7;8;5;0;8;0
2102216;João Gabriel Fernandes;2;5;9;4;6;7;0;0
2101996;Lorenzo Cavalcanti;10;0;7;7;6;6;0;4
2101908;Pedro Miguel da Mata;4;0;9;6;6;3;0;8
2101672;Samuel Vieira;1;10;7;3;6;8;0;24
2101384;Nathan Nascimento;4;8;8;5.5;6;4;0;24
2101811;Carlos Eduardo Nunes;8;7;6;1;6.5;7;0;8
2101613;Bárbara Correia;6;5;8;3;7;5;0;8
2102641;Paulo da Conceição;5;9.25;9;0;7;6.5;0;28
2102600;Vitória Barbosa;8;9;7;6;7;5;0;12
2101700;Catarina Campos;5;10;8;2;8;8;0;12
2101812;Fernando Vieira;10;7;7;2;8;4;0;8
2101426;Isabella Souza;2;8;8;0;8;1;6;0
2101777;Rodrigo Cardoso;7;9.25;7;0;8;0;5;0
2101235;Guilherme Viana;2;5;7;3;8.1;7;0;4
2101253;Gabriela Porto;6;6;8;2;9;1;5;4
2101924;Heloísa Costela;4;5;6;7;9;7;0;0
2102454;João Lucas Ferreira;2;0;8;8;10;6;0;0
2101535;João Miguel Almeida;9;10;7;1;10;5;0;0
2101207;Nina Ferreira;1;9;7;6;10;6;0;0
2102484;Noah da Luz;7;10;9.25;6;10;5;0;16
'''
