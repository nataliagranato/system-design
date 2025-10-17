# Simulador da Camada OSI

Este é um simulador educacional do Modelo OSI (Open Systems Interconnection) que demonstra como os dados fluem através das 7 camadas do modelo, mostrando os processos de encapsulamento e desencapsulamento.

## 📋 Sobre o Modelo OSI

O Modelo OSI é um modelo de referência que padroniza as funções de um sistema de comunicação em 7 camadas distintas:

### As 7 Camadas (de cima para baixo):

1. **Camada 7 - Aplicação (Application Layer)**
   - Interface com o usuário e aplicações
   - Protocolos: HTTP, HTTPS, FTP, SMTP, DNS

2. **Camada 6 - Apresentação (Presentation Layer)**
   - Formatação, criptografia e compressão de dados
   - Conversão de formatos, codificação

3. **Camada 5 - Sessão (Session Layer)**
   - Gerenciamento de sessões entre aplicações
   - Controle de diálogo e sincronização

4. **Camada 4 - Transporte (Transport Layer)**
   - Entrega confiável de dados fim-a-fim
   - Protocolos: TCP, UDP

5. **Camada 3 - Rede (Network Layer)**
   - Roteamento e endereçamento lógico
   - Protocolos: IP, ICMP, ARP

6. **Camada 2 - Enlace de Dados (Data Link Layer)**
   - Transferência de dados entre nós adjacentes
   - Endereçamento MAC, controle de erros

7. **Camada 1 - Física (Physical Layer)**
   - Transmissão de bits através do meio físico
   - Cabos, sinais elétricos, ópticos

## 🚀 Como Usar

### Requisitos

- Python 3.6 ou superior

### Executando o Simulador

```bash
python3 osi_simulator.py
```

### Exemplo de Uso no Código

```python
from osi_simulator import OSISimulator

# Criar uma instância do simulador
simulator = OSISimulator()

# Exibir informações sobre as camadas
simulator.show_layers()

# Simular uma comunicação completa
simulator.simulate_communication("Olá, Mundo!")
```

## 📊 O Que o Simulador Faz

### Processo de Encapsulamento (Envio)

Quando você envia dados através do simulador, ele:

1. **Camada 7 (Aplicação)**: Adiciona cabeçalho com informações do protocolo (ex: HTTP)
2. **Camada 6 (Apresentação)**: Adiciona informações de codificação e criptografia
3. **Camada 5 (Sessão)**: Adiciona informações de gerenciamento de sessão
4. **Camada 4 (Transporte)**: Adiciona portas de origem/destino e número de sequência
5. **Camada 3 (Rede)**: Adiciona endereços IP de origem e destino
6. **Camada 2 (Enlace)**: Adiciona endereços MAC e tipo de frame
7. **Camada 1 (Física)**: Converte tudo em bits para transmissão

### Processo de Desencapsulamento (Recebimento)

No recebimento, o processo é invertido:

1. **Camada 1 (Física)**: Recebe os bits
2. **Camada 2 (Enlace)**: Remove cabeçalho de enlace
3. **Camada 3 (Rede)**: Remove cabeçalho de rede
4. **Camada 4 (Transporte)**: Remove cabeçalho de transporte
5. **Camada 5 (Sessão)**: Remove cabeçalho de sessão
6. **Camada 6 (Apresentação)**: Remove cabeçalho de apresentação
7. **Camada 7 (Aplicação)**: Entrega os dados à aplicação

## 📝 Exemplo de Saída

```
######################################################################
# SIMULADOR DA CAMADA OSI
######################################################################

======================================================================
ENVIANDO DADOS - Processo de Encapsulamento
======================================================================

Dados originais: 'Hello, OSI Model!'

----------------------------------------------------------------------

Camada 7: Aplicação (Application)
Cabeçalho adicionado: {
  "protocol": "HTTPS",
  "method": "GET",
  "content_type": "application/json"
}

Camada 6: Apresentação (Presentation)
Cabeçalho adicionado: {
  "encoding": "UTF-8",
  "compression": "gzip",
  "encryption": "TLS 1.3"
}

[... continua para todas as camadas ...]
```

## 🎓 Propósito Educacional

Este simulador foi criado para fins educacionais, ajudando estudantes e profissionais a entender:

- Como os dados são encapsulados em cada camada
- O papel de cada camada no modelo OSI
- O fluxo de dados em uma rede de computadores
- A importância da padronização em redes

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades!

## 📄 Licença

Este projeto está sob a licença especificada no repositório.

---

Feito com ❤️ por [Natália Granato](https://github.com/nataliagranato)
