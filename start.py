import sqlite3
import banco_de_dados_editor
from dados.variaveis import VARIAVEIS
from dados.variaveis import CODIGO 
from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def limite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        mensagem_usuario = float(" ".join(context.args))
        id_seu = update.effective_user.id
        ordem = {
            'id_usuario': id_seu,
            'valor': mensagem_usuario,
            'valor_gasto': 0.0        
        }
        banco_de_dados_editor.ARM_VALORES(ordem)
        context.user_data['valor_usuario'] = mensagem_usuario
        await update.message.reply_text(f"valor base: {mensagem_usuario}")
    else:
        await update.message.reply_text("adicione um valor após o comando")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"ola {update.effective_user.first_name}! {VARIAVEIS['START']}")
 
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     id_seu = update.effective_user.id
     banco = sqlite3.connect('dados/banco.db')
     interagir_banco = banco.cursor()
     interagir_banco.execute("""
         SELECT valor FROM FINANCAS 
         WHERE id_usuario = ? AND valor > 0
         ORDER BY id DESC LIMIT 1
     """, (id_seu,))
     resultado_limite = interagir_banco.fetchone()
     interagir_banco.execute("""
         SELECT SUM(adc_valor) FROM FINANCAS
         WHERE id_usuario = ?
     """, (id_seu,))
     resultado_gastos = interagir_banco.fetchone()
     banco.close()
     if resultado_limite:
         valor_base = resultado_limite[0]
         adc_valor = resultado_gastos[0] if resultado_gastos[0] else 0.0
         seu_saldo = valor_base - adc_valor
         mensagem_res = (f"""
             usuário:  {update.effective_user.first_name}
             base de limite: {valor_base:.2f}
             valores gastos: {adc_valor:.2f}
             sobrou: {seu_saldo:.2f}
         """)
     else: 
         mensagem_res = "erro digite /limite valor , para se cadastrar"
     await update.message.reply_text(mensagem_res)

async def gasto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        mensagem_usuario = float(" ".join(context.args))
        id_seu = update.effective_user.id
        adc = {
            'id_usuario': id_seu,
            'adc_valor': mensagem_usuario
            }
        banco_de_dados_editor.ADC_VALORES(adc)
        context.user_data['adc_valor'] = mensagem_usuario
        await update.message.reply_text(f" valor adicionado como gasto: {mensagem_usuario}")
    else:
        await update.message.reply_text("pfvr envie um valor após o comando")



               
banco_de_dados_editor.banco_de_dados_editor_funcao()   # fecha a função do banco de dados.               
    
app = ApplicationBuilder().token(f"{CODIGO['codigo']}").build() # apenas adicione o seu token

app.add_handler(CommandHandler("limite", limite))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("gasto", gasto))
app.run_polling()