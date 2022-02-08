import telebot
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

dcc_bot = telebot.TeleBot(API_KEY)

PERIODOS = ["","PrimeiroPeriodo", "SegundoPeriodo", "TerceiroPeriodo", "QuartoPeriodo", "QuintoPeriodo", "SextoPeriodo", "SetimoPeriodo", "OitavoPeriodo"]


@dcc_bot.message_handler(commands=[PERIODOS[8]])
def oitavo_periodo(mensagem):
    dcc_bot.reply_to(mensagem, """Agora, escolha a disciplina do oitavo período que deseja consultar.

/TP""")
    pass

@dcc_bot.message_handler(commands=[PERIODOS[7]])
def setimo_periodo(mensagem):
    dcc_bot.reply_to(mensagem,"""Agora, escolha a disciplina do setimo período que deseja consultar.

/AD
/SistemasOperacionaisI""")
    pass

@dcc_bot.message_handler(commands=[PERIODOS[6]])
def sexto_periodo(mensagem):
    dcc_bot.reply_to(mensagem,"""Agora, escolha a disciplina do sexto período que deseja consultar.

/ComputacaoGraficaI
/Probest
/InteligenciaArtificial
/ProgramacaoLinearI""")
    pass

@dcc_bot.message_handler(commands=[PERIODOS[5]])
def quinto_periodo(mensagem):
    dcc_bot.reply_to(mensagem,"""Agora, escolha a disciplina do quinto período que deseja consultar.

/ArqCompI
/BancoDeDadosI
/CompiadoresI
/CompSoc
/FundamentosEngenhariaDeSoftware
/Logica""")
    pass

@dcc_bot.message_handler(commands=[PERIODOS[4]])
def quarto_periodo(mensagem):
    dcc_bot.reply_to(mensagem,"""Agora, escolha a disciplina do quarto período que deseja consultar.

/AlgGrafos
/CalcNumerico
/ComputacaoConcorrente""")
    pass

@dcc_bot.message_handler(commands=[PERIODOS[3]])
def terceiro_periodo(mensagem):
    dcc_bot.reply_to(mensagem,"""Agora, escolha a disciplina do terceiro período que deseja consultar.

/AlgebraLinearAlgoritmica
/CalculoII
/CompProg
/EstruturaDeDados
/LF
""")


@dcc_bot.message_handler(commands=[PERIODOS[2]])
def segundo_periodo(mensagem):
    dcc_bot.reply_to(mensagem,"""Agora, escolha a disciplina do segundo período que deseja consultar.

/CompII
/OrganizacaoDaInformacao
/MatematicaCombinatoria
/CircuitosLogicos
/CalculoI""")


@dcc_bot.message_handler(commands=[PERIODOS[1]])
def primeiro_periodo(mensagem):
    dcc_bot.reply_to(mensagem, """
Agora, escolha a disciplina do primeiro período que deseja consultar.

/IPD
/SistemasDeInformacao
/NumerosInteirosCriptografia
/Comp1
/ProjetoDeCarreira
/FundamentosDaComputacaoDigital""")


# Função que faz verificação um tipo de mensagem. Por enquanto, retorna true, isso faz com que o bot responda qualquer mensagem digitada no chat.
def verificar(mensagem):
    return True


# Função que mostra uma mensagem padrão no chat não importa o que o usuário digite.
@dcc_bot.message_handler(func=verificar)
def mensagem_padrao(mensagem):
    dcc_bot.send_message(mensagem.chat.id, """
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
