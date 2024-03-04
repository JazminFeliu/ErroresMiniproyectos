# USSD: Unstructured Supplementary Servide Data or quick codes is a communication protocol used
#by GSM cell phones.
# cell Argentina, Tandil: (54) 249 5555 6666 = len(11)

#Ingrese monto de dinero
def checkAmount(cel):
    amt = input("Ingrese monto de dinero: ")
    if amt.isnumeric():
        print(f"El cel {cel} recibió {amt} dólares de cŕedito ")
    else:
        print(
            "Invalido monto de dinero\n"
            "Intente nuevamente"
        )
        checkAmount(cel)

# Credito transacción
def airtimeTrans():
    phone = input("Ingrese el nro. de cel: ")
    if len(phone) == 11 and phone.isnumeric():
        checkAmount(phone)
    else:
        print(
            "Nro. de cel inválido\n"
            "Intente nuevamente\n"
        )
        airtimeTrans()


# Transaction Entry
def transEntry():
    transCode = input(
        "1. Chequear balance\n"
        "2. Comprar crédito\n"
        "3. Transferir\n"
        "Seleccione opción: "
    )

    if transCode == "1":
        print("Su balance es de 200 dolares")
    elif transCode == "2":
        airtimeTrans()
    elif transCode == "3":
        print("Transferir")
    else:
        print(
            "opción inválida\n"
            "Intente nuevamente"
        )
        transEntry()

# Funtion To cross-check USSD Code
def confirmUSSD():
    ussd = input("Ingrese el codigo USSD: ")
    
    if ussd == "*123#":
        print("Bienvenido")
        transEntry()
    else:
        print("USSD code Inválido\n"
            "Intente nuevamente"
            )        
        confirmUSSD()

#Calling the functions
confirmUSSD()
    
