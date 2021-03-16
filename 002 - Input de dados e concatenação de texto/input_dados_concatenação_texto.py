# Obtendo um texto digitado pelo usuário.
comida = input("O que você gostaria de comer: ")
bebida = input("O que você gostaria beber para acompanhar: ")

# Primeira forma de concatenar texto.
# pedidoCliente = "Beleza. Vamos preparar para comer " + comida + ". E para beber, no capricho vai " + bebida + ". Aguarde seu pedido!"

# Segunda forma de concatenar texto.
print(f"Vamos preparar para comer {comida}. E para beber no capricho {bebida}. Aguarde seu pedido!")

# Terceira forma de concatenar texto.
# print("Vamos preparar para comer {}. E para beber no capricho {}. Aguarde seu pedido".format(comida, bebida))
