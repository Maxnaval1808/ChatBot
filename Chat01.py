from nltk.chat.util import Chat, reflections

expressões_pt = {
    "eu": "você",
    "eu sou": "você é",
    "eu era": "você era",
    "eu iria": "você iria",
    "eu irei": "você irá",
    "meu": "seu",
    "você": "eu",
    "você é": "eu sou",
    "você era": "eu era",
    "você iria": "eu iria",
    "você irá": "eu irei",
    "seu": "meu",
}

sentencas = [
    [
        r"oi|olá|opa|e aí",
        ["Olá!", "Como vai?", "Tudo bem?"]
    ],
    [
        r"Qual é o seu nome?",
        ["Meu nome é TwBot.Em que posso ajudá-lo?"]
    ],
    [
        r"(.*) sua idade",
        ["Eu sou um bot, não tenho idade como os humanos."]
    ],
    [
        r"Meu nome é (.*)",
        ["Olá %1, como você está hoje?"]
    ],
    [
        r"Qual formação você indica em Python?",
        ["Formação Flask", "Formação Django", "Formação ML com Python"]
    ],
    [
        r"Quais tecnologias estão em alta no mercado?",
        ["Flutter", "React", "Next3S"]
    ],
    [
        r"quit",
        ["Até breve! Foi bom conversar com você!"]
    ]
]

print("Olá, sou o TwBot")
chat = Chat(sentencas, expressões_pt)
chat.converse()