import random

#Curiosidade sobre espécies marinhas
infospecies = {
    "Tartaruga Verde": "A tartaruga-verde é uma espécie de tartaruga marinha encontrada em todo o mundo. Ela é conhecida por sua coloração verde-oliva e é uma espécie ameaçada de extinção.",
    "Baleia Jubarte": "A baleia-jubarte é uma das maiores espécies de baleia, conhecida por seus saltos espetaculares. Ela migra grandes distâncias entre suas áreas de alimentação e reprodução.",
    "Tubarão Martelo": "O tubarão-martelo é uma espécie de tubarão facilmente reconhecível pelo seu formato de cabeça em forma de martelo. Eles são predadores eficientes e desempenham um papel importante nos ecossistemas marinhos."
}

#Curiosidade sobre energia marinha
infoEnergiaMarinha = {
    "Energia das Ondas": "A energia das ondas é gerada pela captura da energia cinética das ondas do mar e sua conversão em eletricidade.",
    "Energia das Marés": "A energia das marés é gerada pelo aproveitamento das correntes de maré para girar turbinas e gerar eletricidade."
}

#Função para acessar informações sobre uma espécie marinha específica
def informacoesEspecie():
    print("\nEspécies marinhas disponíveis:")
    for especie in infospecies:
        print("-", especie)
        
    
    especieEscolhida = input("\nDigite o nome da espécie para ver mais informações: ")
    if especieEscolhida in infospecies:
        print("\n", infospecies[especieEscolhida])
    else:
        print("Espécie não encontrada. Por favor, verifique a ortografia e tente novamente.")
        

#Função para acessar informações sobre energia renovável marinha
def informacoesEnergiaMarinha():
    print("\nFormas de energia renovável marinha disponíveis:")
    for energia in infoEnergiaMarinha:
        print("-", energia)
    
    energiaEscolhida = input("\nDigite o nome da forma de energia para ver mais informações: ")
    if energiaEscolhida in infoEnergiaMarinha:
        print("\n", infoEnergiaMarinha[energiaEscolhida])
    else:
        print("Forma de energia não encontrada. Por favor, verifique a ortografia e tente novamente.")

#Função para oferecer orientações sobre como preservar os oceanos
def dicasConservacao():
    print("\nDicas para a conservação dos oceanos:")
    print("- Reduza o uso de plástico descartável, como sacolas plásticas e garrafas de água.")
    print("- Participe de limpezas de praias e rios para remover o lixo acumulado.")
    print("- Apoie organizações de conservação marinha e participe de programas de voluntariado.")
    print("- Eduque os outros sobre a importância da conservação dos oceanos e inspire mudanças positivas.")

#Função para administrar um quiz sobre vida marinha
def quizVidaMarinha():
    print("\nBem-vindo ao quiz sobre vida marinha!")
    print("Responda às seguintes perguntas para testar seus conhecimentos:")
    
    #Lista de perguntas e respostas corretas
    perguntasRespostas = {
        "Qual é o maior animal do mundo?": ["Baleia Azul", "Elefante", "Tigre", "Gorila", "Baleia Azul"],
        "Qual é o maior peixe do mundo?": ["Tubarão-Baleia", "Peixe-Espada", "Atum", "Sardinha", "Tubarão-Baleia"],
        "Quantos braços têm os polvos?": ["Seis", "Oito", "Dez", "Doze", "Oito"],
        "Qual é o maior molusco do mundo?": ["Polvo", "Lula Colossal", "Caracol", "Mexilhão", "Lula Colossal"],
        "Quanto tempo pode viver uma tartaruga marinha?": ["Até 50 anos", "Até 75 anos", "Mais de 100 anos", "Mais de 200 anos", "Mais de 100 anos"],
        "Qual é o nome dado às florestas submarinas de algas?": ["Coral", "Algas Vermelhas", "Algas Marrons", "Kelp forests", "Kelp forests"],
        "Qual é o menor cetáceo do mundo?": ["Orca", "Golfinho", "Narval", "Boto Rosa", "Boto Rosa"],
        "Quantas espécies de golfinhos existem aproximadamente?": ["Cerca de 10", "Cerca de 20", "Cerca de 30", "Cerca de 40", "Cerca de 40"],
        "Onde vive o peixe-palhaço?": ["Recife de Coral", "Lagoas", "Estuários", "Anêmonas de mar", "Anêmonas de mar"],
        "Como são chamados os animais que vivem fixos no fundo do mar?": ["Planctônicos", "Nectônicos", "Pelágicos", "Bentônicos", "Bentônicos"]
    }
    
    #Variável para registrar a pontuação do usuário
    pontuacao = 0

    #Repetição através das perguntas e respostas  quiz VidaMarinha
    for pergunta, respostas in perguntasRespostas.items():
        print("\n" + pergunta)
        #Extrair a resposta correta
        resposta_correta = respostas[-1]
        #Embaralhar as alternativas de resposta
        alternativas = respostas[:-1]
        random.shuffle(alternativas)
        
        #Exibir as alternativas embaralhadas com letras correspondentes
        letras = ['a', 'b', 'c', 'd']
        alternativas_dict = dict(zip(letras, alternativas))
        for letra, alternativa in alternativas_dict.items():
            print(f"{letra}) {alternativa}")
        
        resposta_usuario = input("Sua resposta (a, b, c ou d): ").strip().lower()
        
        #Verificar se a resposta do usuário está correta
        if alternativas_dict.get(resposta_usuario) == resposta_correta:
            print("Resposta correta!")
            pontuacao += 1
        else:
            # Encontrar a letra da resposta correta para exibir
            letra_correta = [letra for letra, alternativa in alternativas_dict.items() if alternativa == resposta_correta][0]
            print(f"Resposta incorreta. A resposta correta é a letra '{letra_correta}'.")
    
    #Exibindo a pontuação final
    print("\nPontuação final:", pontuacao)
#Função para administrar um quiz sobre a importância da conservação dos oceanos
def quizImportanciaConservacao():
    print("\nBem-vindo ao quiz sobre a importância da conservação dos oceanos!")
    print("Responda às seguintes perguntas para testar seus conhecimentos:")

    #Lista de perguntas e respostas do quiz Importancia Conservacao
    perguntasRespostas = {
        "Qual das seguintes afirmações descreve melhor a importância da conservação dos oceanos?": {
            "a) Os oceanos são importantes apenas como fonte de alimentos para humanos.": False,
            "b) Os oceanos regulam o clima, fornecem oxigênio, alimentos e meios de subsistência para milhões de pessoas em todo o mundo, além de abrigar uma incrível diversidade de vida.": True,
            "c) Os oceanos são apenas vastos corpos de água sem valor ecológico.": False
        },
        "Qual é o principal fator que contribui para a acidificação dos oceanos?": {
            "a) A emissão de gases do efeito estufa.": True,
            "b) A pesca excessiva.": False,
            "c) O aumento da temperatura da água do mar.": False
        },
        "Qual das seguintes ações humanas não contribui para a poluição dos oceanos?": {
            "a) Descarte inadequado de plásticos.": False,
            "b) Vazamento de óleo durante a perfuração offshore.": True,
            "c) Plantio de árvores.": False
        },
        "Qual das seguintes espécies marinhas é considerada uma espécie ameaçada?": {
            "a) Sardinha comum.": False,
            "b) Tubarão-branco.": True,
            "c) Tartaruga-de-couro.": False
        },
        "Qual é o maior recife de coral do mundo?": {
            "a) Grande Barreira de Coral, na Austrália.": True,
            "b) Recife de Coral de Tubbataha, nas Filipinas.": False,
            "c) Recife de Coral de Belize, na América Central.": False
        }
    }
    
    #Variável para registrar a pontuação do usuário
    pontuacao = 0

    #Repetição através das perguntas e respostas do quiz Importancia Conservacao
    for pergunta, respostas in perguntasRespostas.items():
        print("\n" + pergunta)
        
        #Embaralhando as respostas
        respostas = list(respostas.items())
        random.shuffle(respostas)
        
        #Exibindo as respostas embaralhadas
        for resposta, correta in respostas:
            print(resposta)
        
        #Obtendo a resposta correta
        resposta_correta = [resposta for resposta, correta in respostas if correta][0]
        
        #Recebendo a resposta do usuário
        resposta_usuario = input("Sua resposta (a, b, c): ").strip().lower()
        
        #Verificando se a resposta do usuário está correta
        if resposta_usuario == resposta_correta.split(")")[0].strip().lower():
            print("Resposta correta!")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta é: {resposta_correta}")

    #Exibindo a pontuação final
    print("\nPontuação final:", pontuacao)

#Função para oferecer informações sobre a poluição marinha
def quizInformacoesPoluicaoMarinha():
    print("\nBem-vindo ao quiz sobre poluição marinha!")
    print("Responda às seguintes perguntas para testar seus conhecimentos:")

    #Lista de perguntas e respostas quiz Informacoes Poluicao Marinha
    perguntasRespostas = {
        "Qual das seguintes opções descreve melhor um tipo comum de poluição marinha?": {"a) Poluição por poeira atmosférica.": False, "b) Poluição por plásticos, que afeta a vida marinha e ameaça espécies com ingestão e emaranhamento.": True, "c) Poluição por resíduos nucleares.": False},
        "Qual das seguintes fontes de poluição é a maior contribuinte para a poluição dos oceanos?": {"a) Despejo de esgoto doméstico.": True, "b) Derramamentos de petróleo devido a vazamentos de plataformas de petróleo.": False, "c) Lixo plástico de uso único.": False},
        "Qual é o impacto da poluição por nutrientes nos oceanos?": {"a) Estimula o crescimento excessivo de algas, levando à eutrofização.": True, "b) Causa a morte de peixes por asfixia.": False, "c) Não tem impacto significativo nos ecossistemas marinhos.": False},
        "Qual é o principal tipo de poluição gerado por atividades agrícolas?": {"a) Poluição por esgoto doméstico.": False, "b)Poluição por lixo plástico.": False, "c)Poluição por fertilizantes e pesticidas.": True},
        "Quais são alguns dos efeitos da poluição do petróleo nos ecossistemas marinhos?": {"a) Mortalidade de aves marinhas.": True, "b) Destruição de habitats costeiros.": False, "c) Todas as opções acima.": False}
    }

    #Variável para registrar a pontuação do usuário
    pontuacao = 0

    #Repetição através das perguntas e respostas
    for pergunta, respostas in perguntasRespostas.items():
        print("\n" + pergunta)
        
        #Embaralhando as respostas
        respostas = list(respostas.items())
        random.shuffle(respostas)
        
        #Exibindo as respostas embaralhadas
        for resposta, correta in respostas:
            print(resposta)
        
        #Obtendo a resposta correta
        resposta_correta = [resposta for resposta, correta in respostas if correta][0]
        
        #Recebendo a resposta do usuário
        resposta_usuario = input("Sua resposta: ").strip().lower()
        
        #Verificando se a resposta do usuário está correta
        if resposta_usuario == resposta_correta.split(")")[0].strip().lower():
            print("Resposta correta!")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta é: {resposta_correta}")

    #Exibindo a pontuação final
    print("\nPontuação final:", pontuacao)
#Função para oferecer informações sobre os impactos das mudanças climáticas nos oceanos
def quizImpactoMudancasClimaticas():
    print("\nBem-vindo ao quiz sobre o impacto das mudanças climáticas nos oceanos!")
    print("Responda às seguintes perguntas para testar seus conhecimentos:")

    #Lista de perguntas e respostas do quiz Impacto Mudancas Climaticas
    perguntasRespostas = {
        "Qual das seguintes opções descreve melhor um dos efeitos das mudanças climáticas nos oceanos?": {
            "a) Aumento da temperatura e acidificação dos oceanos.": True,
            "b) Diminuição da salinidade dos oceanos.": False,
            "c) Redução do nível do mar.": False
        },
        "O que é o branqueamento de corais e como é afetado pelas mudanças climáticas?": {
            "a) Processo de morte dos corais devido à poluição por plásticos.": False,
            "b) Descoloração dos corais devido ao aumento da temperatura da água.": True,
            "c) Proliferação de algas que cobrem os corais.": False
        },
        "Qual é o impacto do derretimento do gelo marinho nos oceanos?": {
            "a) Aumento do nível do mar e mudanças na circulação oceânica.": True,
            "b) Diminuição da salinidade dos oceanos.": False,
            "c) Não tem impacto nos ecossistemas marinhos.": False
        },
        "O que é acidificação dos oceanos e como isso afeta os organismos marinhos?": {
            "a) Aumento do pH da água do mar, beneficiando os organismos marinhos.": False,
            "b) Redução do pH da água do mar, prejudicando organismos como corais e moluscos.": True,
            "c) Aumento da salinidade da água do mar, tornando-a mais alcalina.": False
        },
        "Quais são algumas das consequências das mudanças climáticas nos oceanos?": {
            "a) Aumento da frequência e intensidade de tempestades.": False,
            "b) Alterações nos padrões de migração de animais marinhos.": False,
            "c) Todas as opções acima.": True
        }
    }

    #Variável para registrar a pontuação do usuário
    pontuacao = 0

    #Repetição através das perguntas e respostas do quiz Impacto Mudancas Climaticas
    for pergunta, respostas in perguntasRespostas.items():
        print("\n" + pergunta)
        
        #Embaralhando as alternativas de resposta
        alternativas = list(respostas.items())
        random.shuffle(alternativas)
        
        #Exibindo as alternativas embaralhadas com letras correspondentes
        for i, (resposta, correta) in enumerate(alternativas):
            letra = chr(97 + i)
            print(f"{letra}) {resposta}")

        resposta_usuario = input("Sua resposta (a, b ou c): ").strip().lower()

        #Verificando se a resposta do usuário está correta
        letra_correta = [chr(97 + i) for i, (resposta, correta) in enumerate(alternativas) if correta][0]
        if resposta_usuario == letra_correta:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta é a letra '{letra_correta}'.")

    #Exibindo a pontuação final
    print("\nPontuação final:", pontuacao)

#Função principal que exibe o menu
def main():
    while True:
        print("""
╔═════════════════════════════════════════════════════════╗
║                     🌊  MarQuizz  🌊                    ║
╠═════════════════════════════════════════════════════════╣
║ [1] 🌐 Informações sobre espécies marinhas              ║
║ [2] 🌞 Informações sobre energia renovável marinha      ║
║ [3] 🌱 Dicas de conservação dos oceanos                 ║
║ [4] 🐠 Quiz sobre vida marinha                          ║
║ [5] 🐋 Quiz importância da conservação dos oceanos      ║
║ [6] 🚯 Quiz informações sobre poluição marinha          ║
║ [7] 🌍 Quiz impacto das mudanças climáticas nos oceanos ║
║ [8] ❌ Sair                                             ║
╚═════════════════════════════════════════════════════════╝
            
               """)
        
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                informacoesEspecie()
            case "2":
                informacoesEnergiaMarinha()
            case "3":
                dicasConservacao()
            case "4":
                quizVidaMarinha()
            case "5":
                quizImportanciaConservacao()
            case "6":
                quizInformacoesPoluicaoMarinha()
            case "7":
                quizInformacoesPoluicaoMarinha()
            case "8":
                print("Obrigado por usar o programa. Até logo!")
                break
            case none:
                print("Opção inválida. Por favor, escolha uma opção válida.")


main()

