import telebot
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

dcc_bot = telebot.TeleBot(API_KEY)


@dcc_bot.message_handler(commands= ["PrimeiroPeriodo"])
def primeiro_periodo(message):
    dcc_bot.reply_to(message, """
Agora escolha a disciplina do primeiro período que deseja consultar.

/IPD
/SistemasDeInformacao
/NumerosInteirosCriptografia
/Comp1
/ProjetoDeCarreira
/FundamentosDaComputacaoDigital""")

# Função que faz verificação um tipo de mensagem. Por enquanto, retorna true, isso faz com que o bot responda qualquer mensagem digitada no chat.
def verificar():
    return True

# Função que mostra uma mensagem padrão no chat não importa o que o usuário digite.
@dcc_bot.message_handler(func= True)
def mensagem_padrao(message):
    dcc_bot.send_message(message.chat.id,"""
    Olá! Bem-vindo ao repositório de provas do DCC. Escolha alguma das opções abaixo de acordo com o período que deseja consultar as provas.

/PrimeiroPeriodo
/SegundoPeriodo
/TerceiroPeriodo
/QuartoPeriodo
/QuintoPeriodo
/SextoPeriodo
/SetimoPeriodo
/OitavoPeriodo
""")


def main():
    dcc_bot.polling()

main()