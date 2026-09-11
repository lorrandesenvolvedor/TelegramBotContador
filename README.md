![telegrambotcontador](./telegrambotcontador.jpg)
# TelegramBotContador
Bot feito para te ajudar a contar seus gastos através do telegram 
# Diretórios 
dados = usada para armazenar arquivos de dados do usuário.
# Arquivos
start.py = usado como arquivo principal servindo para dar início ao programa.
dados/banco.db = usado para armazenar informações de gasto e valor base.
banco_de_dados_editor.py = aqui você pode configurar as colunas do banco de dados.
# Ideia 
Você manda o comando “/limite” o bot armazena o valor que você insere após em uma variável e usa esse valor como base para calcular se você gastou mais do que deveria.

Você manda o comando “/gasto” o bot armazena e calcula o valor que você adicionou para assim ver se já atingiu seu limite.

Caso você já bata o limite posto, o bot envia uma mensagem para você indicando quanto gastou.
Função
Calcular gastos diários semanais e mensais.
Enviar notificações assim que o valor adicionado for atingido.

