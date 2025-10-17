## 📦 Instalação das Ferramentas de Rede

### **🍺 macOS (Homebrew)**
```bash
# Instalar Homebrew (se ainda não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Ferramentas básicas de rede (muitas já vêm no macOS)
brew install iproute2mac          # Comandos ip equivalentes para macOS
brew install nmap                 # Scanner de rede e portas
brew install wget                 # Download de arquivos
brew install curl                 # Cliente HTTP/HTTPS (já incluso no macOS)

# Ferramentas de análise de rede
brew install wireshark            # Analisador de protocolos gráfico
brew install tcpdump              # Captura de pacotes (já incluso no macOS)
brew install ngrep                # Grep para tráfego de rede
brew install iftop                # Monitor de largura de banda
brew install nethogs              # Monitor de uso de rede por processo

# Ferramentas de conectividade

brew install netcat              # Utilitário de rede versátil
brew install telnet              # Cliente telnet
brew install fping               # Ping rápido para múltiplos hosts
brew install mtr                 # Combinação de ping e traceroute

# Ferramentas SSL/TLS
brew install openssl             # Toolkit SSL/TLS (já incluso no macOS)
brew install gnutls              # Implementação alternativa de TLS

# Ferramentas DNS
brew install bind                # Inclui dig, nslookup, host
brew install dog                 # Alternativa moderna ao dig
brew install dnsutils            # Utilitários DNS adicionais

# Ferramentas de monitoramento
brew install htop                # Monitor de processos melhorado
brew install lsof                # Lista arquivos abertos (já incluso no macOS)

# Ferramentas avançadas
brew install masscan            # Scanner de portas de alta velocidade
brew install zmap               # Scanner de rede para toda a Internet
```

### **🐧 Linux (Ubuntu/Debian)**
```bash
# Atualizar repositórios
sudo apt update

# Ferramentas básicas (muitas já inclusas)
sudo apt install -y net-tools         # ifconfig, netstat, arp
sudo apt install -y iproute2          # ip, ss, tc
sudo apt install -y iputils-ping      # ping
sudo apt install -y traceroute        # traceroute
sudo apt install -y dnsutils          # dig, nslookup, host
sudo apt install -y curl wget         # clientes HTTP

# Ferramentas de análise
sudo apt install -y wireshark         # Analisador gráfico
sudo apt install -y tcpdump           # Captura de pacotes
sudo apt install -y ngrep             # Grep para rede
sudo apt install -y iftop             # Monitor de banda
sudo apt install -y nethogs           # Monitor por processo

# Ferramentas de conectividade
sudo apt install -y netcat-openbsd    # Netcat
sudo apt install -y telnet            # Cliente telnet
sudo apt install -y fping             # Ping múltiplo
sudo apt install -y mtr-tiny          # MTR

# Ferramentas SSL/TLS
sudo apt install -y openssl           # Toolkit SSL/TLS

# Ferramentas avançadas
sudo apt install -y nmap              # Scanner de rede
sudo apt install -y masscan           # Scanner rápido
sudo apt install -y ethtool           # Configuração ethernet
sudo apt install -y bridge-utils      # Utilitários de bridge
```

### **🪟 Windows (Chocolatey)**
```powershell
# Instalar Chocolatey (como Administrador)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Ferramentas de rede
choco install -y wireshark           # Analisador de protocolos
choco install -y nmap                # Scanner de rede
choco install -y curl                # Cliente HTTP
choco install -y wget                # Download de arquivos
choco install -y putty               # Cliente SSH/Telnet
choco install -y openssl             # Toolkit SSL/TLS

# Ferramentas adicionais
choco install -y fping               # Ping avançado
choco install -y netcat              # Utilitário de rede
```

### **📋 Verificação da Instalação**
```bash
# Verificar se as ferramentas estão instaladas
which curl wget nmap wireshark tcpdump
# ou
command -v curl wget nmap wireshark tcpdump

# Testar algumas ferramentas básicas
curl --version
nmap --version
wireshark --version
openssl version
```

### **⚠️ Comandos que já vêm no macOS por padrão:**
```bash
# Estes comandos NÃO precisam ser instalados no macOS:
ping, traceroute, netstat, lsof, arp, ifconfig, openssl, curl, ssh, scp, telnet
```

### **💡 Dicas de Instalação:**

1. **Para macOS**: A maioria dos comandos básicos já está disponível. Instale apenas as ferramentas extras.
2. **Para Linux**: Muitas distribuições já incluem a maioria das ferramentas.
3. **Para Windows**: Use o Windows Subsystem for Linux (WSL) para uma experiência mais próxima ao Unix.
4. **Wireshark**: Pode requerer privilégios administrativos para capturar pacotes.
