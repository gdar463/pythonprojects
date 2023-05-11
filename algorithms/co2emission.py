kmrate = input("Inserisci il tasso di produzione di CO2 della tua macchina in g/km: (solo numero) ")
kmavg = input("Inserisci il numero di km che fai in media al giorno: (solo numero) ")
days = input("Inserisci il numero di giorni che usi la macchina in media alla settimana: ")
weeks = input("Inserisci il numero di settimane che usi la macchina in un anno: ")

dayrate = float(kmrate) * float(kmavg)
yearrate = dayrate * int(days) * int(weeks)
tons = yearrate/1000

print(f"Al giorno produci {dayrate}gr/giorno\nAll'anno produci {yearrate}gr/anno o {tons}t/anno")