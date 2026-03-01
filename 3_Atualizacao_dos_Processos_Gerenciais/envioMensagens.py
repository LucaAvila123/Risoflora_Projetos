# pre-requisito de WhatsApp Web logado no navegador
# Tutorial: https://www.hashtagtreinamentos.com/automacao-whatsapp-web-python
# Documentação: https://github.com/Ankit404butfound/PyWhatKit/wiki

import pywhatkit as kit
import csv

with open('./3_Atualizacao_dos_Processos_Gerenciais/cronograma.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    
    # Pular o cabeçalho, se necessário
    next(leitor)
    
    # Percorrer cada linha
    for linha in leitor:
        # A linha é tratada como uma lista
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
        # talvez dê problema futuramente com o tempo para fechamento de aba e envio de mensagens, sendo um desafio para compreensão
        kit.sendwhatmsg_instantly(phone_no=numero, message=mensagem, tab_close=True, close_time=2)