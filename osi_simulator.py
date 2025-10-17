#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulador da Camada OSI (OSI Layer Simulator)

Este simulador demonstra como os dados fluem através das 7 camadas do modelo OSI,
mostrando o processo de encapsulamento e desencapsulamento.

Autor: Natália Granato
"""

from typing import Dict, Any
import json


class OSILayer:
    """Classe base para representar uma camada OSI"""
    
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
    
    def encapsulate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Adiciona cabeçalho da camada aos dados"""
        return {
            'layer': self.number,
            'layer_name': self.name,
            'header': self._create_header(data),
            'payload': data
        }
    
    def decapsulate(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        """Remove cabeçalho da camada e retorna os dados"""
        if packet.get('layer') != self.number:
            raise ValueError(f"Pacote não pertence à camada {self.number}")
        return packet.get('payload', {})
    
    def _create_header(self, data: Dict[str, Any]) -> Dict[str, str]:
        """Cria cabeçalho específico da camada"""
        return {'layer': self.name}
    
    def __str__(self):
        return f"Camada {self.number}: {self.name}"


class PhysicalLayer(OSILayer):
    """Camada 1: Física - Transmissão de bits brutos através do meio físico"""
    
    def __init__(self):
        super().__init__("Física (Physical)", 1)
    
    def _create_header(self, data: Dict[str, Any]) -> Dict[str, str]:
        return {
            'type': 'bits',
            'encoding': 'Manchester',
            'signal': 'Elétrico/Óptico'
        }
    
    def transmit(self, packet: Dict[str, Any]) -> str:
        """Simula a transmissão de bits"""
        return f"[Camada Física] Transmitindo bits: {json.dumps(packet)[:50]}..."


class DataLinkLayer(OSILayer):
    """Camada 2: Enlace de Dados - Transferência confiável entre nós adjacentes"""
    
    def __init__(self):
        super().__init__("Enlace de Dados (Data Link)", 2)
    
    def _create_header(self, data: Dict[str, Any]) -> Dict[str, str]:
        return {
            'mac_source': 'AA:BB:CC:DD:EE:FF',
            'mac_dest': '11:22:33:44:55:66',
            'frame_type': 'Ethernet'
        }


class NetworkLayer(OSILayer):
    """Camada 3: Rede - Roteamento e endereçamento lógico"""
    
    def __init__(self):
        super().__init__("Rede (Network)", 3)
    
    def _create_header(self, data: Dict[str, Any]) -> Dict[str, str]:
        return {
            'ip_source': '192.168.1.100',
            'ip_dest': '192.168.1.1',
            'protocol': 'IPv4',
            'ttl': '64'
        }


class TransportLayer(OSILayer):
    """Camada 4: Transporte - Entrega confiável de dados fim-a-fim"""
    
    def __init__(self):
        super().__init__("Transporte (Transport)", 4)
    
    def _create_header(self, data: Dict[str, Any]) -> Dict[str, str]:
        return {
            'port_source': '8080',
            'port_dest': '443',
            'protocol': 'TCP',
            'seq_number': '12345'
        }


class SessionLayer(OSILayer):
    """Camada 5: Sessão - Gerenciamento de sessões entre aplicações"""
    
    def __init__(self):
        super().__init__("Sessão (Session)", 5)
    
    def _create_header(self, data: Dict[str, Any]) -> Dict[str, str]:
        return {
            'session_id': 'sess_abc123',
            'dialog_control': 'full-duplex',
            'synchronization': 'enabled'
        }


class PresentationLayer(OSILayer):
    """Camada 6: Apresentação - Formatação e criptografia de dados"""
    
    def __init__(self):
        super().__init__("Apresentação (Presentation)", 6)
    
    def _create_header(self, data: Dict[str, Any]) -> Dict[str, str]:
        return {
            'encoding': 'UTF-8',
            'compression': 'gzip',
            'encryption': 'TLS 1.3'
        }


class ApplicationLayer(OSILayer):
    """Camada 7: Aplicação - Interface com o usuário e aplicações"""
    
    def __init__(self):
        super().__init__("Aplicação (Application)", 7)
    
    def _create_header(self, data: Dict[str, Any]) -> Dict[str, str]:
        return {
            'protocol': 'HTTPS',
            'method': 'GET',
            'content_type': 'application/json'
        }


class OSISimulator:
    """Simulador completo do modelo OSI"""
    
    def __init__(self):
        self.layers = [
            ApplicationLayer(),      # Camada 7
            PresentationLayer(),     # Camada 6
            SessionLayer(),          # Camada 5
            TransportLayer(),        # Camada 4
            NetworkLayer(),          # Camada 3
            DataLinkLayer(),         # Camada 2
            PhysicalLayer()          # Camada 1
        ]
    
    def send_data(self, data: str, verbose: bool = True) -> Dict[str, Any]:
        """
        Simula o envio de dados através das camadas OSI (encapsulamento)
        
        Args:
            data: Dados a serem enviados
            verbose: Se True, imprime informações detalhadas
        
        Returns:
            Pacote final encapsulado
        """
        if verbose:
            print("\n" + "="*70)
            print("ENVIANDO DADOS - Processo de Encapsulamento")
            print("="*70)
            print(f"\nDados originais: '{data}'")
            print("\n" + "-"*70)
        
        packet = {'data': data}
        
        for layer in self.layers:
            packet = layer.encapsulate(packet)
            if verbose:
                print(f"\n{layer}")
                print(f"Cabeçalho adicionado: {json.dumps(layer._create_header({}), indent=2)}")
        
        if verbose:
            print("\n" + "-"*70)
            if isinstance(self.layers[-1], PhysicalLayer):
                print(f"\n{self.layers[-1].transmit(packet)}")
        
        return packet
    
    def receive_data(self, packet: Dict[str, Any], verbose: bool = True) -> str:
        """
        Simula o recebimento de dados através das camadas OSI (desencapsulamento)
        
        Args:
            packet: Pacote encapsulado recebido
            verbose: Se True, imprime informações detalhadas
        
        Returns:
            Dados originais extraídos
        """
        if verbose:
            print("\n" + "="*70)
            print("RECEBENDO DADOS - Processo de Desencapsulamento")
            print("="*70)
            print("\nRecebendo pacote da camada física...")
            print("\n" + "-"*70)
        
        for layer in reversed(self.layers):
            if verbose:
                print(f"\n{layer}")
                print(f"Removendo cabeçalho da camada {layer.number}")
            packet = layer.decapsulate(packet)
        
        data = packet.get('data', '')
        
        if verbose:
            print("\n" + "-"*70)
            print(f"\nDados recebidos: '{data}'")
            print("="*70 + "\n")
        
        return data
    
    def simulate_communication(self, message: str):
        """
        Simula uma comunicação completa através do modelo OSI
        
        Args:
            message: Mensagem a ser transmitida
        """
        print("\n" + "#"*70)
        print("# SIMULADOR DA CAMADA OSI")
        print("#"*70)
        
        # Envio (Encapsulamento)
        packet = self.send_data(message, verbose=True)
        
        # Simulação de transmissão
        print("\n" + "~"*70)
        print(">>> TRANSMITINDO PELA REDE <<<")
        print("~"*70)
        
        # Recebimento (Desencapsulamento)
        received = self.receive_data(packet, verbose=True)
        
        # Verificação
        if received == message:
            print("✓ Transmissão bem-sucedida! Dados recebidos corretamente.")
        else:
            print("✗ Erro na transmissão! Dados corrompidos.")
    
    def show_layers(self):
        """Exibe informações sobre todas as camadas OSI"""
        print("\n" + "="*70)
        print("MODELO OSI - 7 CAMADAS")
        print("="*70)
        
        descriptions = {
            7: "Interface com aplicações e serviços de rede",
            6: "Formatação, criptografia e compressão de dados",
            5: "Gerenciamento de sessões entre aplicações",
            4: "Entrega confiável de dados fim-a-fim",
            3: "Roteamento e endereçamento lógico",
            2: "Transferência de dados entre nós adjacentes",
            1: "Transmissão de bits através do meio físico"
        }
        
        for layer in self.layers:
            print(f"\n{layer}")
            print(f"  Descrição: {descriptions.get(layer.number, 'N/A')}")


def main():
    """Função principal para demonstração do simulador"""
    simulator = OSISimulator()
    
    # Mostrar as camadas
    simulator.show_layers()
    
    # Simular uma comunicação
    simulator.simulate_communication("Hello, OSI Model!")
    
    # Exemplo adicional
    print("\n\n" + "#"*70)
    print("# EXEMPLO ADICIONAL")
    print("#"*70)
    simulator.simulate_communication("Dados importantes do sistema")


if __name__ == "__main__":
    main()
