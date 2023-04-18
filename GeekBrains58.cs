//Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
//Например, даны 2 матрицы:
//2 4 | 3 4
//3 2 | 3 3
//Результирующая матрица будет:
//18 20
//15 18


using System;


namespace C__Learning
{
    internal class GeekBrains58
    {
        private static int [,] MultArray(int[,] farr1, int[,] farr2) //Метод умножения двумерных массивов
        {
            int flines = farr1.GetUpperBound(0) + 1;
            int fcolumns = farr1.GetUpperBound(1) + 1;
            int[,] fresult = new int[flines, fcolumns];
            for (int fline = 0; fline < flines; fline++)
            {
                for (int fcolumn = 0; fcolumn < fcolumns; fcolumn++)
                {
                    for (int frow = 0; frow < flines; frow++)
                    {
                        fresult[fline, fcolumn] += farr1[fline, frow] * farr2[frow, fcolumn];
                    }
                }
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
                Console.Write($"{farr[fline, fcolumns]} |\n");
            }
            Console.Write("\n\n");
        }

        private static (int[,], int[,]) AskAndFill()
        {
            var frand = new Random();
            Console.WriteLine("\nВведите размерность умножаемых массивов в виде двух целых числ через запятую: \n");
            int[] fuserArray = Console.ReadLine().Trim().Split(',').Select(e => Convert.ToInt32(e)).ToArray();
            int[,] fWorkArray1 = new int[fuserArray[0], fuserArray[1]];
            int[,] fWorkArray2 = new int[fuserArray[0], fuserArray[1]];
            for (int fline = 0; fline < fuserArray[0]; fline++)
            {
                for (int fcolumn = 0; fcolumn < fuserArray[1]; fcolumn++)
                {
                    fWorkArray1[fline, fcolumn] = frand.Next(10); //Случайные числа от 0 до 10
                    fWorkArray2[fline, fcolumn] = frand.Next(10); //Случайные числа от 0 до 10
                }
            }
            PrintArray(fWorkArray1, "\nПервый массив случайных чисел:\n");
            PrintArray(fWorkArray2, "\nВторой массив случайных чисел:\n");
            return (fWorkArray1, fWorkArray2);
        }

        public static void Main()
        {
            (int[,], int[,]) arrays = AskAndFill();
            int[,] WorkArray1 = arrays.Item1;
            int[,] WorkArray2 = arrays.Item2;
            PrintArray(MultArray(WorkArray1, WorkArray2), "\nРезультат умножения массивов:\n");
        }
    }
}
