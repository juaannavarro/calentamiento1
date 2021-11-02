customer_basket_cost=34
customer_basket_weight=44
#Write if statement here to calculate the total cost
def calcula_coste(coste,peso):
    if coste >= 100:
        envio=0
    else:
        envio=1.20*peso

    coste_total=coste+envio
    print(coste,envio)
    return coste_total

mi_coste=calcula_coste(customer_basket_cost,customer_basket_weight)
print("tarea6 coste_total", mi_coste)