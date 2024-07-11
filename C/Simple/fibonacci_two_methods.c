#include<stdio.h>
int fib_recursive(int n){
    // if (n==1||n==2){
    //     return n-1;
    if (n==1||n==0){
        return n;
    }
    else{
        return fib_recursive(n-1)+fib_recursive(n-2);
    }
}
int fib_iterative(int n){
    int fib_series[n];
    fib_series[0] = 0;
    fib_series[1] = 1;
    int j = n+1;
    for (int i=2;i<j;i++){
        fib_series[i] = fib_series[i-1]+fib_series[i-2];
    }
    // return fib_series;
    return fib_series[n];
}
int main()
{
    int n=9;
    printf("%d\n",fib_iterative(n));
    printf("%d\n",fib_recursive(n));
}