# Giacenza Media – Calcolo della giacenza media da file CSV
Il calcolo della giacenza media è un'operazione tediosa, ma necessaria per richiedere il rilascio di documenti relativi alla propria situazione economica, come l'Indicatore della **Situazione Economica Equivalente (ISEE)**, non sempre messo a disposizione dal proprio istituto di credito.

Questo script, semplice e intuitivo, può essere lanciato e utilizzato seguendo le richieste che compariranno sul terminale. Saranno richieste alcune informazioni necessarie per eseguire il calcolo richiesto.

Per poter eseguire questo piccolo programma, è necessario solamente avere installato Python (versione 3, o superiore) e avere a disposizione il **file .csv** relativo ai movimenti per il conto corrente (o carta), di cui si desidera calcolare la giacenza media. Un file .csv è un piccolo documento, diffuso tra la maggior parte degli istituti di credito, per rappresentare sinteticamente una lista di movimenti. Questo file può essere scaricato accedendo all'home banking del proprio istituto di credito, specificando il periodo dal 01/01 al 31/12 per l'anno di interesse per il conto corrente (o carta) di interesse.

## Istruzioni
1. Scaricare il file "giacenza-media.py" da questa repository.
2. Posizionare il file scaricato in una cartella a scelta, quindi aprire una finestra di terminale all'interno della cartella scelta.
3. Eseguire il seguente comando:
```bash
python giacenza-media.py
```
oppure:
```bash
python3 giacenza-media.py
```
che lancerà il programma.

4. Alla richiesta **"Anno di riferimento: "** inserire l'anno a cui fa riferimento la lista dei movimenti nel file .csv (ad esempio "2019"). Per il calcolo della giacenza media, il programma verificherà autonomamente se l'anno è bisestile o meno.
5. Alla richiesta **"Saldo iniziale (al 01/01/----): "** inserire il saldo iniziale all'inizio dell'anno (ad esempio "1240,36", oppure "1240.36").
6. Alla richiesta **"Nome file: "** inserire il nome del file .csv scaricato dall'home banking del proprio istituto di credito per l'anno di interesse (ad esempio "movimenti.csv"). Tale file deve essere posizionato nella stessa cartella in cui è presente lo script "giacenza-media.py".
7. Alla richiesta **"In quale colonna è presente la data di ogni movimento?: "** specificare, aprendo il file .csv con un editor di testo oppure con un software per fogli di calcolo, in quale colonna è posizionata la data relativa ad ogni movimento. Una colonna è una serie di caratteri separata da un punto e virgola ";". Se la lista di movimenti, rappresentati nei file .csv uno per riga, mostra ad esempio la data nel secondo blocco, inserire "2".
8. Alla richiesta **"In quale colonna è presente l'importo di ogni movimento?: "** specificare la colonna relativa all'importo in euro (positivo o negativo) di ogni movimento (ad esempio "4"), in maniera analoga al punto precedente.

Dopo aver inserito l'ultima informazione, il programma effettuerà il calcolo richiesto. Le informazioni saranno consultabili nella finestra di terminale stessa, oppure nel file di testo di output che verrà generato nella stessa cartella in cui è presente lo script.

Oltre alla giacenza media verrà calcolato, per l'anno di interesse, anche il saldo finale al 31/12. Sarà inoltre possibile visualizzare il dettaglio delle giacenze giornaliere e delle entrate/uscite per ogni giorno dell'anno, come documentazione dimostrativa (in caso venisse richiesta) del calcolo stesso.

Demo 1             |  Demo 2
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/bobcorn/giacenza-media/master/Demo%201.png)  |  ![](https://raw.githubusercontent.com/bobcorn/giacenza-media/master/Demo%202.png)
