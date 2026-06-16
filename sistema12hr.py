def sistema_24_horas():
    while True:
        try:
            hora_24 = input("Digite a hora no formato 24 horas (HH:MM): ")
            hora, minuto = map(int, hora_24.split(':'))
            if 0 <= hora < 24 and 0 <= minuto < 60:
                break
            else:
                print("Hora ou minuto inválidos. Tente novamente.")
        except ValueError:
            print("Formato inválido. Tente novamente.")

    if hora == 0:
        hora_12 = 12
        periodo = "AM"
    elif 1 <= hora < 12:
        hora_12 = hora
        periodo = "AM"
    elif hora == 12:
        hora_12 = 12
        periodo = "PM"
    else:
        hora_12 = hora - 12
        periodo = "PM"

    print(f"A hora no formato 12 horas é: {hora_12:02d}:{minuto:02d} {periodo}")

sistema_24_horas()