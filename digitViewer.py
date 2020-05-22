import argparse
from tkinter import Tk, Canvas, Frame, BOTH
import math
import pandas as pd

PIXELSIZE = 10;

class Example(Frame):

    def __init__(self, args):
        super().__init__()

        self.initUI(args)


    def initUI(self, args):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        
        canvas.pack(fill=BOTH, expand=1)
        dim = int (math.sqrt(len(args)))
        count = 0
        for i in range(dim):
            for j in range(dim):
                thisPixel = args.iloc[count]
                print(thisPixel)
                if thisPixel == 0:
                    canvas.create_rectangle(PIXELSIZE, PIXELSIZE, i*PIXELSIZE, j*PIXELSIZE,
                        outline="#ffffff", fill="#ffffff")   
                elif thisPixel <= 64:
                    canvas.create_rectangle(PIXELSIZE, PIXELSIZE, i*PIXELSIZE, j*PIXELSIZE,
                        outline="#8a8a8a", fill="#8a8a8a")   
                elif thisPixel <= 128:
                    canvas.create_rectangle(PIXELSIZE, PIXELSIZE, i*PIXELSIZE, j*PIXELSIZE,
                        outline="#696969", fill="#696969")
                elif thisPixel <= 192:
                    canvas.create_rectangle(PIXELSIZE, PIXELSIZE, i*PIXELSIZE, j*PIXELSIZE,
                        outline="#303030", fill="#303030")
                elif thisPixel <= 256:
                    canvas.create_rectangle(PIXELSIZE, PIXELSIZE, i*PIXELSIZE, j*PIXELSIZE,
                        outline="#000", fill="#000")
                count += 1





def getParser():
    parser = argparse.ArgumentParser(description='Process some integers.');
#    parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator');
#    parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')
    return parser.parse_args();

def main():
  #argparse content
    args = getParser();
    vals = args.integers;
    testCSV = pd.read_csv("/home/ben/Programming/WebDev/Node/neural/dataSets/test.csv")
    print(testCSV.iloc[0, 1:])
    root = Tk() 
    ex = Example(testCSV.iloc[0, 1:])
    root.geometry("600x400+300+300")
    root.mainloop()
   
if __name__ == '__main__':
    main();