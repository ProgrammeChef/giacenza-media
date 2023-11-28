# Giacenza Media – Calcolo della giacenza media da file CSV
Average Stock – Calculation of average stock from CSV file

Demo 1             |  Demo 2
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/bobcorn/giacenza-media/master/demo/demo_1.jpg)  |  ![](https://raw.githubusercontent.com/bobcorn/giacenza-media/master/demo/demo_2.jpg)

This simple and intuitive script can be used to accomplish this task. Guided by the terminal, some information necessary to perform the required calculation will be requested.

To be able to run this small program, you only need to have Python installed (version 3 or higher) and have the **.csv file** available relating to the movements for the current account (or card) for which you want to calculate the average balance . A .csv file is a small document, widespread among most credit institutions, to synthetically represent a list of movements. This file can be downloaded by accessing the home banking of your credit institution, specifying the period from 01/01 to 31/12 for the year of interest for the current account (or card) of interest.

## Instructions
1. Download the "giacenza-media.py" file from this repository.
2. Place the downloaded file in a folder of your choice, then open a terminal window within the folder of your choice.
3. Run the following command:
```bash
python stock-media.py
```
or:
```bash
python3 stock-media.py
```
who will launch the program.

4. At the request **"Reference year: "**, enter the year to which the list of movements in the .csv file refers (for example "2019"). To calculate the average stock, the program will independently check whether the year is a leap year or not.
5. At the request **"Initial balance (as of 01/01/----): "** enter the initial balance at the beginning of the year (for example "1240.36", or "1240.36").
6. At the **"File name: "** prompt, enter the name of the .csv file downloaded from your credit institution's home banking for the year of interest (for example "movimenti.csv"). This file must be placed in the same folder where the "giacenza-media.py" script is present.
7. At the request **"In which column is the date of each movement present?: "** specify, by opening the .csv file with a text editor or with spreadsheet software, in which column the date is positioned relating to each movement. A column is a series of characters separated by a semicolon ";". If the list of movements, represented in the .csv files one per line, shows for example the date in the second block, enter "2".
8. At the request **"In which column is the amount of each movement present?: "** specify the column relating to the amount in euros (positive or negative) of each movement (for example "4"), so similar to the previous point.

After entering the last information, the program will perform the required calculation. The information will be available in the terminal window itself, or in the output text file that will be generated in the same folder where the script is present.

In addition to the average balance, the final balance at 12/31 will also be calculated for the year of interest. It will also be possible to view the detail of daily stocks and income/exits for each day of the year, as demonstrative documentation (if requested) of the calculation itself.
