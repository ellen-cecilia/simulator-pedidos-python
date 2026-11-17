# Simulador de Caixa e Cálculo de Pedidos
# Desenvolvido por Ellen Cecilia Londo

print("=== BEM-VINDO AO SISTEMA DE PEDIDOS ===")

carrinho = []
total = 0.0

while True:
    produto = input("\nDigite o nome do item (ou 'sair' para finalizar): ")
    
    if produto.lower() == 'sair':
        break
        
    preco = float(input(f"Digite o valor de {produto} (R$): "))
    carrinho.append((produto, preco))
    total += preco

print("\n--- RESUMO DO PEDIDO ---")
for item, valor in carrinho:
    print(f"- {item}: R$ {valor:.2f}")

print(f"\nSubtotal: R$ {total:.2f}")

# Aplicação de cupom de desconto simples
cupom = input("Possui cupom de desconto? (Digite 'IFOOD10' ou 'nao'): ")

if cupom.upper() == 'IFOOD10':
    desconto = total * 0.10
    total_final = total - desconto
    print(f"Desconto aplicado (10%): -R$ {desconto:.2f}")
else:
    total_final = total

print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
print("=======================================")
