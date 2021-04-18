# 🤖 stockmarket-ai

• An advanced ai algorithm program to chose stocks •

• This is an accurate and profitable ai algorithm program, but trade using it at your own risk •

• The backtesting proved that its yearly ROI is 100% •

## 🔨 Setup

Clone the repo <kbd>git clone https://github.com/fineans/sudoku-solver.git</kbd>.
You need Python 3. Install The modules from the python files using <kbd>pip install</kbd> or <kbd>pip3 install</kbd>. 

## Usage

Make a file called <kbd>list.csv</kbd> with the symbols (In Yahoo Finance Format) of the stocks you want to run the scan on. The colunm header at top of the list must of symbols be <kbd>Symbols</kbd>. When you add your own csv file, change the variable 'number_of_stocks' in the <kbd>main.py</kbd> file to the number of stocks you have in your csv file. Instead of using your own <kbd>list.csv</kbd>, you can use the csv file already provided which contains a few symbols of NYSE stocks. Run the program with <kbd>python main.py</kbd> or <kbd>python main.py</kbd>. It will run the scan on all the stocks. The program prints out all its scanning steps for each stock. To find stocks in which a buy signal has been given, go through the output and find all the stocks where 'Buy' has also been printed at the end of it's scanning steps.

## To Do

- [x] Backtest
- [ ] Give Buy Signals In A CSV Output File


© Fineans 2021
