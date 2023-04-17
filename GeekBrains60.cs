//Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
//Массив размером 2 x 2 x 2
//66(0,0,0) 25(0, 1, 0)
//34(1, 0, 0) 41(1, 1, 0)
//27(0, 0, 1) 90(0, 1, 1)
//26(1, 0, 1) 55(1, 1, 1)

using System;
using System.Data.Common;

namespace C__Learning
{
    internal class GeekBrains60
    {
        private static void PrintArray(int[,,] farr, string fstr) //Метод вывода трёхмерного массива на экран
        {
            Console.WriteLine(fstr);
            int flines = farr.GetUpperBound(0);
            int fcolumns = farr.GetUpperBound(1);
            int frows = farr.GetUpperBound(2);
            for (int fline = 0; fline <= flines; fline++)
            {
                for (int fcolumn = 0; fcolumn <= fcolumns; fcolumn++)
                {
                    for (int frow = 0; frow <= frows; frow++)
                    {
                        if ((fcolumn != fcolumns) || (frow != frows))
                        {
                            if (frow != frows)
                            {
                                Console.Write($"{farr[fline, fcolumn, frow]} ({fline}, {fcolumn}, {frow}), ");
                            }
                            else
                            {
                                Console.Write($"{farr[fline, fcolumn, frow]} ({fline}, {fcolumn}, {frow})");
                            }
                        }
                    }
                    if (fcolumn != fcolumns)
                    {
                        Console.Write('\n');
                    }
                }
                Console.Write($"{farr[fline, fcolumns, frows]} ({fline}, {fcolumns}, {frows})\n");
            }
            Console.Write("\n\n");
        }
        //Метод запроса размерности массива и заполнения массива случайными числами
        private static int[,,] AskAndFill()
        {
            var frand = new Random();
            var fknownNumbers = new HashSet<int>();
            Console.WriteLine("\nВведите размерность массива в виде трёх целых чисел через запятую: \n");
            int[] fuserArray = Console.ReadLine().Trim().Split(',').Select(e => Convert.ToInt32(e)).ToArray();
            int[,,] fWorkArray = new int[fuserArray[0], fuserArray[1], fuserArray[2]];

            for (int fline = 0; fline < fuserArray[0]; fline++)
            {
                for (int fcolumn = 0; fcolumn < fuserArray[1]; fcolumn++)
                {
                    for (int frow = 0; frow < fuserArray[2]; frow++)
                    {
                        int fnewElement;
                        do
                        {
                            fnewElement = frand.Next(10, 100); //Случайные числа от 10 до 99
                        } while (fknownNumbers.Contains(fnewElement));
                        fWorkArray[fline, fcolumn, frow] = fnewElement;
                    }
                }
            }
            PrintArray(fWorkArray, "\nСформирован следующий массив случайных чисел:\n");
            return fWorkArray;
        }

        public static void Main()
        {
          AskAndFill();
        }
    }
}
