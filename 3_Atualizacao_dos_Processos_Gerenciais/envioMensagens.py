# pre-requisito de WhatsApp Web logado no navegador
# Tutorial: https://www.hashtagtreinamentos.com/automacao-whatsapp-web-python
# Documentação: https://github.com/Ankit404butfound/PyWhatKit/wiki

import pywhatkit as kit
import csv

# necessário ter um arquivo dentro da pasta desse código chamado cronograma.csv com cabeçalho Nome,Numero,Disciplina,Data,Horario
with open('./3_Atualizacao_dos_Processos_Gerenciais/cronograma.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    
    # Pular o cabeçalho, é necessário
    next(leitor)
    
    # Percorrer cada linha
    for linha in leitor:
        # Cada linha é tratada como uma lista de strings
        # Formato de Numero: ++55XXYYYYYYYYY, sendo XX o DDD e Y o numero de fato; vai funcionar se tiver WhatsApp
        # print(linha[0], linha[1], linha[2], linha[3], linha[4]) # Acessando colunas pelo índice
        nome = linha[0]
        numero = linha[1]
        disciplina = linha[2]
        data = linha[3]
        horario = linha[4]
        mensagem = f"Olá, {nome}, seu nome está inscrito para a disciplina de {disciplina} no dia {data}, o teste foi efetivo?"
        hora_e_minuto = horario.split(":")
        hora = int(hora_e_minuto[0])
        minuto = int(hora_e_minuto[1])
        print(hora, minuto)
        # não gostei do envio de mensagens cronometradas nativo da biblioteca pywhatkit
        # talvez dê problema futuramente com o tempo para fechamento de aba e envio de mensagens, sendo um desafio para o funcionamento pleno
        try:
            kit.sendwhatmsg_instantly(phone_no=numero, message=mensagem, tab_close=True, close_time=2)
        except Exception as e:
            print(f"Problema {e} no nome de {nome}")
