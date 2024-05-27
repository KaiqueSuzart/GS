# Dicionário com informações sobre diferentes espécies marinhas
info_especies = {
    "Tartaruga Verde": "A tartaruga-verde é uma espécie de tartaruga marinha encontrada em todo o mundo. Ela é conhecida por sua coloração verde-oliva e é uma espécie ameaçada de extinção.",
    "Baleia Jubarte": "A baleia-jubarte é uma das maiores espécies de baleia, conhecida por seus saltos espetaculares. Ela migra grandes distâncias entre suas áreas de alimentação e reprodução.",
    "Tubarão Martelo": "O tubarão-martelo é uma espécie de tubarão facilmente reconhecível pelo seu formato de cabeça em forma de martelo. Eles são predadores eficientes e desempenham um papel importante nos ecossistemas marinhos."
    # Adicione mais informações sobre outras espécies marinhas aqui
}

# Dicionário com informações sobre energia renovável marinha
info_energia_marinha = {
    "Energia das Ondas": "A energia das ondas é gerada pela captura da energia cinética das ondas do mar e sua conversão em eletricidade.",
    "Energia das Marés": "A energia das marés é gerada pelo aproveitamento das correntes de maré para girar turbinas e gerar eletricidade.",
    # Adicione mais informações sobre outras formas de energia renovável marinha aqui
}

# Função para acessar informações sobre uma espécie marinha específica
def informacoes_especie():
    print("\nEspécies marinhas disponíveis:")
    for especie in info_especies:
        print("-", especie)
    
    especie_escolhida = input("\nDigite o nome da espécie para ver mais informações: ")
    if especie_escolhida in info_especies:
        print("\n", info_especies[especie_escolhida])
    else:
        print("Espécie não encontrada. Por favor, verifique a ortografia e tente novamente.")

# Função para acessar informações sobre energia renovável marinha
def informacoes_energia_marinha():
    print("\nFormas de energia renovável marinha disponíveis:")
    for energia in info_energia_marinha:
        print("-", energia)
    
    energia_escolhida = input("\nDigite o nome da forma de energia para ver mais informações: ")
    if energia_escolhida in info_energia_marinha:
        print("\n", info_energia_marinha[energia_escolhida])
    else:
        print("Forma de energia não encontrada. Por favor, verifique a ortografia e tente novamente.")

# Função para calcular o potencial de energia marinha em uma determinada área
def calcular_potencial_energia_marinha():
    print("\nVamos calcular o potencial de energia marinha em uma área específica.")
    print("Insira os dados necessários para estimar o potencial de energia.")

    # Coletando dados do usuário
    area = float(input("Área da região marinha (em km²): "))
    profundidade_media = float(input("Profundidade média da região (em metros): "))
    altura_ondas = float(input("Altura média das ondas (em metros): "))
    velocidade_corrente = float(input("Velocidade média da corrente marinha (em m/s): "))

    # Calculando o potencial de energia marinha (exemplo simplificado)
    potencial_energia = area * profundidade_media * altura_ondas * velocidade_corrente
    print("\nO potencial de energia marinha estimado na área fornecida é de:", potencial_energia, "kW.")

# Função para fornecer dicas de conservação dos oceanos
def dicas_conservacao():
    print("\nDicas para a conservação dos oceanos:")
    print("- Reduza o uso de plástico descartável, como sacolas plásticas e garrafas de água.")
    print("- Participe de limpezas de praias e rios para remover o lixo acumulado.")
    print("- Apoie organizações de conservação marinha e participe de programas de voluntariado.")
    print("- Eduque os outros sobre a importância da conservação dos oceanos e inspire mudanças positivas.")

# Função para realizar um quiz sobre vida marinha
def quiz_vida_marinha():
    print("\nBem-vindo ao quiz sobre vida marinha!")
    print("Responda às seguintes perguntas para testar seus conhecimentos:")
    
    # Dicionário de perguntas e respostas
    perguntas_respostas = {
        "Qual é o maior animal do mundo?": "Baleia Azul",
        "Qual é o maior peixe do mundo?": "Tubarão-Baleia",
        "Quantos braços têm os polvos?": "Oito",
        # Adicione mais perguntas e respostas aqui
    }
    
    # Variável para acompanhar a pontuação do usuário
    pontuacao = 0
    
    # Loop através das perguntas e respost
    perguntas_respostas = {
        "Qual é o maior animal do mundo?": "Baleia Azul",
        "Qual é o maior peixe do mundo?": "Tubarão-Baleia",
        "Quantos braços têm os polvos?": "Oito",
        # Adicione mais perguntas e respostas aqui
    }
    
    # Variável para acompanhar a pontuação do usuário
    pontuacao = 0
    
    # Loop através das perguntas e respostas
    for pergunta, resposta in perguntas_respostas.items():
        print("\n" + pergunta)
        resposta_usuario = input("Sua resposta: ").strip().capitalize()
        if resposta_usuario == resposta:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print("Resposta incorreta. A resposta correta é:", resposta)
    
    # Exibindo a pontuação final do usuário
    print("\nPontuação final:", pontuacao)

# Função principal que exibe o menu e processa as opções do usuário
def main():
    while True:
        print("\nMenu:")
        print("1. Informações sobre espécies marinhas")
        print("2. Informações sobre energia renovável marinha")
        print("3. Calcular potencial de energia marinha")
        print("4. Dicas de conservação dos oceanos")
        print("5. Quiz sobre vida marinha")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            informacoes_especie()
        elif opcao == "2":
            informacoes_energia_marinha()
        elif opcao == "3":
            calcular_potencial_energia_marinha()
        elif opcao == "4":
            dicas_conservacao()
        elif opcao == "5":
            quiz_vida_marinha()
        elif opcao == "6":
            print("Obrigado por usar o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chamada da função principal para iniciar o programa
main()
