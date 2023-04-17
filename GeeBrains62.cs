//Задача 62.Напишите программу, которая заполнит спирально массив 4 на 4.
//Например, на выходе получается вот такой массив:
//01 02 03 04
//12 13 14 05
//11 16 15 06
//10 09 08 07

using System;


namespace C__Learning
{
    internal class GeeBrains62
    {
        private static void PrintArray(int[,] farr, string fstr) //Метод вывода двумерного массива на экран
        {
            Console.WriteLine(fstr);
            int flines = farr.GetUpperBound(0);
            int fcolumns = farr.GetUpperBound(1);
            for (int fline = 0; fline <= flines; fline++)
            {
                Console.Write("|");
                for (int fcolumn = 0; fcolumn < fcolumns; fcolumn++)
                {
                    Console.Write("{0:d2} ", farr[fline, fcolumn]);
                }
                Console.Write("{0:d2}|\n", farr[fline, fcolumns]);
            }
            Console.Write("\n\n");
        }

        //Метод заполнения массива по спирали
        private static int[,] FillArray()
        {
            int[,] fWorkArray = new int[4, 4];
            
            int fistart = 0, fiend = 0, fjstart = 0, fjend = 0;

            int k = 1;
            int i = 0;
            int j = 0;

            while (k <= 16)
            {
                fWorkArray[i,j] = k;
                if (i == fistart && j < 4 - fjend - 1)
                    ++j;
                else if (j == 4 - fjend - 1 && i < 4 - fiend - 1)
                    ++i;
                else if (i == 4 - fiend - 1 && j > fjstart)
                    --j;
                else
                    --i;

                if ((i == fistart + 1) && (j == fjstart) && (fjstart != 4 - fjend - 1))
                {
                    ++fistart;
                    ++fiend;
                    ++fjstart;
                    ++fjend;
                }
                ++k;
            }
            PrintArray(fWorkArray, "\nСформирован следующий массив:\n");
            return fWorkArray;
        }

        public static void Main()
        {
            FillArray();
        }
    }
}
