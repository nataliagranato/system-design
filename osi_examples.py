#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso do Simulador OSI

Este arquivo demonstra diferentes formas de usar o simulador da camada OSI.
"""

from osi_simulator import OSISimulator

def example_basic():
    """Exemplo básico de uso do simulador"""
    print("\n" + "="*70)
    print("EXEMPLO 1: Uso Básico")
    print("="*70)
    
    simulator = OSISimulator()
    simulator.simulate_communication("Olá, Mundo!")


def example_custom_message():
    """Exemplo com mensagem customizada"""
    print("\n" + "="*70)
    print("EXEMPLO 2: Mensagem Customizada")
    print("="*70)
    
    simulator = OSISimulator()
    message = "Esta é uma mensagem importante sobre redes de computadores!"
    simulator.simulate_communication(message)


def example_layers_info():
    """Exemplo mostrando informações das camadas"""
    print("\n" + "="*70)
    print("EXEMPLO 3: Informações das Camadas OSI")
    print("="*70)
    
    simulator = OSISimulator()
    simulator.show_layers()


def example_encapsulation_only():
    """Exemplo mostrando apenas o processo de encapsulamento"""
    print("\n" + "="*70)
    print("EXEMPLO 4: Apenas Encapsulamento")
    print("="*70)
    
    simulator = OSISimulator()
    packet = simulator.send_data("Dados de teste", verbose=True)
    
    print("\n\nPacote final gerado:")
    print(f"Número de camadas atravessadas: 7")
    print(f"Camada atual: {packet['layer']}")


def example_silent_mode():
    """Exemplo em modo silencioso (sem verbose)"""
    print("\n" + "="*70)
    print("EXEMPLO 5: Modo Silencioso")
    print("="*70)
    
    simulator = OSISimulator()
    
    # Encapsular sem verbose
    packet = simulator.send_data("Teste silencioso", verbose=False)
    print(f"✓ Dados encapsulados. Camada: {packet['layer']}")
    
    # Desencapsular sem verbose
    data = simulator.receive_data(packet, verbose=False)
    print(f"✓ Dados desencapsulados: '{data}'")


def main():
    """Executa todos os exemplos"""
    print("\n" + "#"*70)
    print("# EXEMPLOS DE USO DO SIMULADOR OSI")
    print("#"*70)
    
    # Executar exemplos
    example_basic()
    example_layers_info()
    example_custom_message()
    example_encapsulation_only()
    example_silent_mode()
    
    print("\n" + "#"*70)
    print("# FIM DOS EXEMPLOS")
    print("#"*70 + "\n")


if __name__ == "__main__":
    main()
