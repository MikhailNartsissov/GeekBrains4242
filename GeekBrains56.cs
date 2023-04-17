//Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку
//с наименьшей суммой элементов.
//
//Например, задан массив:
//
//1 4 7 2
//
//5 9 2 3
//
//8 4 2 4
//
//5 2 6 7
//
//Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C__Learning
{
    internal class GeekBrains56
    {
        //Метод определения наименьшей суииы элементов строки двумерного массива
        private static int MinSum(int[,] farray) 
        {
            int flines = farray.GetUpperBound(0) + 1;
            int fcolumns = farray.GetUpperBound(1) + 1;
            int fmin = int.MaxValue;
            int fsum = 0;
            int fresult = -1;
            for (int fline = 0; fline < flines; fline++)
            {
                for (int fcolumn = 0; fcolumn < fcolumns; fcolumn++)
                {
                    fsum += farray[fline, fcolumn];
                }
                if (fmin > fsum) 
                    {
                    fmin = fsum;
                    fresult = fline;
                    }
                fsum = 0;
            }
            return fresult;
        }
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
                    Console.Write($"{farr[fline, fcolumn]}, ");
                }
                Console.Write($"{farr[fline, fcolumns]}|\n");
            }
            Console.Write("\n\n");
        }

        //Метод запроса размерности массива и заполнения массива случайными числами
        private static int[,] AskAndFill()
        {
            var frand = new Random();
            Console.WriteLine("\nВведите размерность массива в виде двух целых чисел через запятую: \n");
            int[] fuserArray = Console.ReadLine().Trim().Split(',').Select(e => Convert.ToInt32(e)).ToArray();
            int[,] fWorkArray = new int[fuserArray[0], fuserArray[1]];
            for (int fline = 0; fline < fuserArray[0]; fline++)
            {
                for (int fcolumn = 0; fcolumn < fuserArray[1]; fcolumn++)
                {
                    fWorkArray[fline, fcolumn] = frand.Next(10); //Случайные числа от 0 до 10
                }
            }
            PrintArray(fWorkArray, "\nСформирован следующий массив случайных чисел:\n");
            return fWorkArray;
        }

        public static void Main()
        {
            int[,] WorkArray = AskAndFill();
            Console.WriteLine($"\nНаименьшая сумма элементов в строке номер {MinSum(WorkArray) + 1}\n");
        }
    }
}
