    def desligar_computador():
    # Obter o valor da caixa de texto
        tempo_str = page.get_control("tempo_texto").value

    # Validar o valor
        try:
            tempo = int(tempo_str)
            if tempo <= 0:
                raise ValueError
        except ValueError:
            print("Valor inválido. Insira um número positivo.")
            return

    # Converter para a unidade correta
        if value_time == "minutos":
            tempo *= 60

    # Definir o tempo de desligamento
        time.sleep(tempo)
        print("Computador desligado!")

# Adicionar um botão para acionar o desligamento
        page.add(ft.ElevatedButton("Desligar!", on_click=desligar_computador))