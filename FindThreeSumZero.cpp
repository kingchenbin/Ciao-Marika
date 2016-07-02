#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

#define random(x) (rand()%x)
#define DATA_AMOUNT 100000
#define PRINT_INFO 0

void PrintResult(const char *_Format, int a, int b, int c)
{
#if PRINT_INFO
    printf(_Format, a, b, c);
#endif
}

void FindTwoSumKInTimeN(int *array, int len, int K)
{
    int *a = &(array[0]);
    int *b = &(array[len - 1]);

    while(a < b)
    {
        if (*a + *b > K)
        {
            --b;
        }
        else if (*a + *b < K)
        {
            ++a;
        }
        else
        {
            PrintResult("Find case: %5d %5d %5d\n", -K, *a, *b);
            ++a;
            --b;
        }
    }
}

// N^2 Totally useless when N gets bigger
void FindTwoSumK(int *array, int len, int K)
{
    if (len < 2)
        return;

    // array[0]     --- smallest number
    // array[len-1] --- biggest number
    if (array[0] >= K)
    {
        if (array[0] > 0)
            return;

        for (int i = 0; i < len && array[i] <= 0; ++i)
        {
            for (int j = i + 1; j < len && array[j] <= 0; ++j)
            {
                if (array[i] + array[j] == K)
                {
                    PrintResult("Find case: %5d %5d %5d\n", -K, array[i], array[j]);
                }
            }
        }
    }
    else if (array[len-1] <= K)
    {
        if (array[len-1] < 0)
            return;

        for (int i = len-1; i >= 0 && array[i] >= 0; --i)
        {
            for (int j = i - 1; j >= 0 && array[j] >= 0; --j)
            {
                if (array[i] + array[j] == K)
                {
                    PrintResult("Find case: %5d %5d %5d\n", -K, array[i], array[j]);
                }
            }
        }
    }
    else
    {
        for (int i = 0; i < len; ++i)
        {
            for (int j = i + 1; j < len; ++j)
            {
                if (array[i] + array[j] == K)
                {
                    PrintResult("Find case: %5d %5d %5d\n", -K, array[i], array[j]);
                }
            }
        }
    }
}

void bubbleSort(int *array, int len)
{
    for (int i = 0; i < len - 1; ++i)
    {
        for (int j = 0; j < len - i - 1; ++j)
        {
            if (array[j] > array[j+1])
            {
                int swap = array[j];
                array[j] = array[j+1];
                array[j+1] = swap;
            }
        }
    }
}

void main()
{
    int array[DATA_AMOUNT];
    srand(time(0));

    for (int i = 0; i < DATA_AMOUNT; ++i)
    {
        int n = random((DATA_AMOUNT+1)/2);
        int flag = (random(2) - 0.5) * 2;
        array[i] = flag * n;
    }

    LARGE_INTEGER t1,t2,tc;
    QueryPerformanceFrequency(&tc);
    QueryPerformanceCounter(&t1);

    bubbleSort(array, DATA_AMOUNT);

    QueryPerformanceCounter(&t2);
    printf("BubbleSort with %d number use time:%f\n", DATA_AMOUNT, (t2.QuadPart - t1.QuadPart)*1.0/tc.QuadPart);
    QueryPerformanceCounter(&t1);

    for (int j = 0; j < DATA_AMOUNT; ++j)
    {
        //FindTwoSumK(&(array[j+1]),DATA_AMOUNT-1-j,-array[j]);
        FindTwoSumKInTimeN(&(array[j+1]),DATA_AMOUNT-1-j,-array[j]);
    }

    QueryPerformanceCounter(&t2);
    printf("FindThreeSumZero with %d number use time:%f\n", DATA_AMOUNT, (t2.QuadPart - t1.QuadPart)*1.0/tc.QuadPart);
}