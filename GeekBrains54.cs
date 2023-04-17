//Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
//Например, задан массив:
//1 4 7 2
//5 9 2 3
//8 4 2 4
//В итоге получается вот такой массив:
//7 4 2 1
//9 5 3 2
//8 4 4 2

using System;

internal class GeekBrains54
{
    // Метод разделения строки массива по схеме Ломуто
    private static int Partition(int [,] frow, int fline, int fstart, int fend)
    {
        // Выбираем крайний правый элемент в качестве опорного элемента строки
        int fpivot = frow[fline, fend];

        // элементы меньше опорной точки, будут перемещены влево от `fpIndex`
        // элементы больше опорной точки, будут перемещены вправо от `fpIndex`
        int fpIndex = fstart;

        // каждый раз, когда мы находим элемент, меньший или равный опорному, `fpIndex`
        // увеличивается, и этот элемент помещается перед опорной точкой.
        for (int i = fstart; i < fend; i++)
        {
            if (frow[fline, i] >= fpivot)
            {
                (frow[fline, fpIndex], frow[fline, i]) = (frow[fline, i], frow[fline, fpIndex]);
                fpIndex++;
            }
        }

        // меняем местами элемент массива с индексом fpIndex с опорным элементом
        (frow[fline, fpIndex], frow[fline, fend]) = (frow[fline, fend], frow[fline, fpIndex]);

        // возвращаем индекс опорного элемента
        return fpIndex;
    }

    // Метод быстрой сортировки по алгоритму Хоара
    private static void QuickSort(int [,] farray, int fline, int fstart, int fend)
    {
        // базовое условие
        if (fstart >= fend)
        {
            return;
        }
        // переставляем элементы по оси
        int fpivot = Partition(farray, fline, fstart, fend);
        // рекурсивно вызываем метод для подмассива, содержащего элементы меньше опорной точки
        QuickSort(farray, fline, fstart, fpivot - 1);
        // рекурсивно вызываем метод для подмассива, содержащего элементы больше опорной точки
        QuickSort(farray, fline, fpivot + 1, fend);
    }

    private static int[,] ArraySort(int[,] farray) //Принимающий метод сортировки двумерного массива
    {
        int lines = farray.GetUpperBound(0) + 1;
        int columns = farray.GetUpperBound(1) + 1;
        for (int line = 0; line < lines; line++)
            {
                QuickSort(farray, line, 0, columns - 1);
           }
        return farray;
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
        PrintArray(ArraySort(WorkArray), "\nМасив с отсортированными по убыванию стрками:\n");
    }
}
