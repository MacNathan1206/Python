#!/usr/bin/env python3
"""
Script simples para somar dois números
Autor: Claude
"""

def somar(a, b):
    """
    Função que soma dois números
    
    Args:
        a (float): Primeiro número
        b (float): Segundo número
    
    Returns:
        float: Soma dos dois números
    """
    return a + b

def restar(a,b):
    """
    Função que resta dois números
    
    Args:
        a (float): Primeiro número
        b (float): Segundo número
    
    Returns:
        float: Resta dos dois números
    """
    return a-b

def main():
    """
    Função principal do programa
    """
    print("=== Calculadora de Números ===")
    print()
    
    try:
        # Solicita os números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Calcula a soma
        resultado = somar(num1, num2)
        resultado1 = restar(num1, num2)
        
        # Calcula a substracao
 
        # Exibe o resultado
        print(f"\nResultado: {num1} + {num2} = {resultado}")
        print(f'\nResultado: {num1} - {num2} = {resultado1}')
        
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()