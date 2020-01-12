import datetime
import re
import os


def in_or_out(amount):
    if amount > 0:
        return "Entrate: +" + f'{amount:.2f}' + " euro"
    elif amount < 0:
        return "Uscite: " + f'{amount:.2f}' + " euro"
    else:
        return "Nessun movimento"


def add_movements(stocks, movements, out_string):
    year = next(iter(stocks.keys())).year

    year_start = datetime.date(year, 1, 1)
    year_end = datetime.date(year, 12, 31)
    step = datetime.timedelta(days=1)

    while year_start <= year_end:
        out_string += "Data: " + str(year_start) + "\n" + in_or_out(
            movements[year_start]) + "\nGiacenza giornaliera: " + f'{stocks[year_start]:.2f}' + " euro"
        if year_start.day == 31 and year_start.month == 12:
            break
        out_string += "\n\n"
        year_start += step

    return out_string


def run():
    total_sum = 0
    dates = []
    out_string = ""
    in_file = None
    out_file = None

    while True:
        year = input("\nAnno di riferimento: ")
        if len(year) != 4 or not year.isdigit():
            print("\nL'anno inserito non è valido, riprova.")
            continue
        else:
            year = int(year)
            break

    year_start = datetime.date(year, 1, 1)
    year_end = datetime.date(year, 12, 31)
    step = datetime.timedelta(days=1)

    while year_start <= year_end:
        dates.append(year_start)
        year_start += step

    year_start = datetime.date(year, 1, 1)
    stocks = {key: 0 for key in dates}
    movements = {key: 0 for key in dates}

    while True:
        op_bal = input("\nSaldo iniziale (al 01/01/" + str(year) + "): ").replace(",", ".")
        if not re.match(r'\d+(?:[.]\d{2})?$', op_bal):
            print("\nIl saldo iniziale inserito non è valido, riprova.")
            continue
        else:
            op_bal = round(float(op_bal.replace(",", ".")), 2)
            break

    cur_bal = op_bal
    stocks[year_start] = cur_bal

    while True:
        file_name = input("\nNome file: ")
        if not os.path.isfile(file_name):
            print("\nIl nome del file inserito non esiste nella cartella di questo script, riprova.")
            continue
        else:
            in_file = open(file_name, "r")
            out_file = open("./" + file_name.split(".")[0] + "_output.txt", "w")
            break

    while True:
        date_index = input("\nIn quale colonna è presente la data di ogni movimento?: ")
        if not date_index.isdigit():
            print("\nIl numero di colonna inserito per la data di ogni movimento non è valido, riprova.")
            continue
        else:
            date_index = int(date_index) - 1
            break

    while True:
        amount_index = input("\nIn quale colonna è presente l'importo di ogni movimento?: ")
        if not amount_index.isdigit():
            print("\nIl numero di colonna inserito per l'importo di ogni movimento non è valido, riprova.")
            continue
        else:
            amount_index = int(amount_index) - 1
            break

    print("\n")

    while year_start <= year_end:
        in_file.seek(0)
        for line in in_file:
            fields = line.split(";")

            if len(fields) < 2:
                continue

            cur_date_raw = fields[date_index].replace(".", "/").split("/")

            if not cur_date_raw[0].isdigit():
                continue

            cur_date = datetime.date(int(cur_date_raw[2]), int(cur_date_raw[1]), int(cur_date_raw[0]))
            amount = float(fields[amount_index].replace(".", "").replace(",", "."))

            if cur_date == year_start:
                stocks[cur_date] += amount
                movements[cur_date] += amount

        stocks[year_start] = round(stocks[year_start], 2)
        movements[year_start] = round(movements[year_start], 2)

        if year_start.day == 31 and year_start.month == 12:
            break

        year_start += step
        stocks[year_start] = stocks[year_start - datetime.timedelta(1)]

    for v in stocks.values():
        total_sum += v

    out_string += "----------------------------------------------------\n"
    out_string += "SALDI E GIACENZA\n"
    out_string += "----------------------------------------------------\n"
    out_string += "Saldo iniziale (al 01/01/" + str(year) + "): " + str(op_bal) + " euro\n"
    out_string += "Saldo finale (al 31/12/" + str(year) + "): " + str(stocks[year_end]) + " euro\n"
    out_string += "Giacenza media (nel " + str(year) + "): " + str(
        round(total_sum / len(stocks), 2)) + " euro/giorno\n\n"
    out_string += "----------------------------------------------------\n"
    out_string += "DETTAGLIO MOVIMENTI\n"
    out_string += "----------------------------------------------------\n"

    out_string = add_movements(stocks, movements, out_string)

    print(out_string)
    out_file.write(out_string)

    in_file.close()
    out_file.close()

    print("\n----------------------------------------------------")
    print(
        "Operazione eseguita con successo!\nPuoi trovare tutte le informazioni richieste in questo terminale,\noppure nel file di testo \"" +
        file_name.split(".")[0] + "_output.txt\"\nche è stato creato in questa cartella.")
    print("----------------------------------------------------")


if __name__ == "__main__":
    run()
