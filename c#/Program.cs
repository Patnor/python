//************************************************************************
//After creating the application, you can run it with the dotnet run command
//*************************************************************************

// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
int [] arr = { 12, 11, 13, 5, 6, 7 };
MergeSortPJN.MergeSort(arr);
Console.WriteLine("Sorted array is");
for (int i = 0; i < arr.Length; i++)
{
    Console.Write(arr[i] + " ");
}

