import sqlite3

def banco_de_dados_editor_funcao():
    with sqlite3.connect('dados/banco.db') as banco:
        interagir_banco = banco.cursor()
        interagir_banco.execute("""
            CREATE TABLE IF NOT EXISTS FINANCAS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            valor REAL NOT NULL,
            valor_gasto REAL,
            adc_valor REAL
            );
        """)


def ARM_VALORES(ordem):
    with sqlite3.connect('dados/banco.db') as banco:
        interagir_banco = banco.cursor()

        interagir_banco.execute("""
            INSERT INTO FINANCAS (id_usuario, valor, valor_gasto)
            VALUES (?, ?, ?)
        """, (
            ordem['id_usuario'],
            ordem['valor'],
            ordem['valor_gasto']
        ))
    
def ADC_VALORES(adc):
    with sqlite3.connect('dados/banco.db') as banco:
        interagir_banco = banco.cursor()

        interagir_banco.execute("""
            INSERT INTO FINANCAS (id_usuario, valor, adc_valor)
            VALUES (?, ?, ?)
        """, (
            adc['id_usuario'],
            0.0,
            adc['adc_valor']
        ))