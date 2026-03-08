#p1 crear u3 inventario de 10 
billetes_1000=10
billetes_500=10
billetes_200=10
billetes_100=10
billetes_50=10

#paso 2 crear variables de los billetes para que e entregan 
entregar_1000=0 
entregar_500=0 
entregar_200=0 
entregar_100=0 
entregar_50=0

#paso 3 Mensaje inicial y solicitud de monto 
print ("Cajero automatico ")
monto = int (input ("ingrese el monto que va a retirar: "))
monto_original = monto  

if monto>=1000:
    necesarios = monto //1000
    if necesarios <= billetes_1000:
        entregar_1000 = necesarios 
        monto = monto - (entregar_1000 * 1000)
    else:
        entregar_1000 = billetes_1000
        monto = monto - (entregar_1000 * 1000)

if monto>=500:
    necesarios = monto //500
    if necesarios <= billetes_500:
        entregar_500 = necesarios 
        monto = monto - (entregar_500 * 500)
    else:
        entregar_500 = billetes_500
        monto = monto - (entregar_500 * 500)

if monto>=200:
    necesarios = monto //200
    if necesarios <= billetes_200:
        entregar_200 = necesarios 
        monto = monto - (entregar_200 * 200)
    else:
        entregar_200 = billetes_200
        monto = monto - (entregar_200 * 200)

if monto>=100:
    necesarios = monto //100
    if necesarios <= billetes_100:
        entregar_100 = necesarios 
        monto = monto - (entregar_100 * 100)
    else:
        entregar_100 = billetes_100
        monto = monto - (entregar_100 * 100)

if monto>=50:
    necesarios = monto //50
    if necesarios <= billetes_50:
        entregar_50 = necesarios 
        monto = monto - (entregar_50 * 50)
    else:
        entregar_50 = billetes_50
        monto = monto - (entregar_50 * 50)

#verififcar si se puede entregar el dinero necesario
if monto == 0:
    #actualizar billetes 
    billetes_1000 = billetes_1000 - entregar_1000
    billetes_500 = billetes_500 - entregar_500
    billetes_200 = billetes_200 - entregar_200
    billetes_100 = billetes_100 - entregar_100
    billetes_50 = billetes_50 - entregar_50

    #mostar resultado 
    print (f"\a Retiro exitoso: ${monto_original}")
    print (f"Billetes de 1000: {entregar_1000}")
    print (f"Billetes de 500: {entregar_500}")
    print (f"Billetes de 200: {entregar_200}")
    print (f"Billetes de 100: {entregar_100}")
    print (f"Billetes de 50: {entregar_50}")

else: 
    print ("No hay money suficiente para este monto ")