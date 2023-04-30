#include<iostream>
#include<string>
#include<array>
using namespace std;

// void func1(string arr[]){
//     cout<<arr[0]<<endl;
//     cout<<arr[1]<<endl;
//     cout<<arr[2]<<endl;
// }
class test
{
private:
    string list[101] = {"Hello", "World"};
public:
    test(){}
    void get_data(int arr_size){
        // list[0] = "Hello";
        // cout<<arr[0]<<endl;
        // cout<<arr[1]<<endl;
        // cout<<arr[2]<<endl;
        // cout<<arr[3]<<endl;
        // cout<<end(arr)-begin(arr)<<endl;
        // int counter=0;
        // for(auto i:arr){
        //     counter++;
        // }
        // cout<<counter<<endl;
        // arr[arr_size] = "HELLO WORLD";
    }
    ~test(){}
};


int main(){
    // string arr[] = {"Hello", "World"};
    // int arr[101] = {2,3};
    // func1(arr);
    // int counter;
    // counter = end(arr)-begin(arr);
    // cout<<counter<<endl;
    // test o1;
    // o1.get_data(counter);
    // cout<<end(arr)-begin(arr)<<endl;
    // for(auto i:arr){
    //     counter++;
    // }
    // cout<<counter<<endl;
    string book_list[101] = {"Power Of Habit", "Dopamine Detox", "Strategic Mindset", "Rich Dad Poor Dad", "Atomic Habit"};
    for(int i=0;i<(sizeof(book_list)/sizeof(string));i++){
        cout<<book_list[i]<<endl;
    }
    return 0;
}

// #include<iostream>
// #include<string>
// using namespace std;

// class normal_lms
// {
// private:
//     string book_list[] = {"Power Of Habit", "Dopamine Detox", "Strategic Mindset", "Rich Dad Poor Dad", "Atomic Habit"}; //Book list
// public:
//     normal_lms(){ //Constructor 
//         // book_list[0] = "Power Of Habit";
//         // book_list[1] = "Dopamine Detox";
//         // book_list[2] = "Strategic Mindset";
//         // book_list[3] = "Rich Dad Poor Dad";
//         // book_list[4] = "Atomic Habit";
//         int he;
    
//     }
//     // void show_books(){
//     //     cout<<sizeof(string);
//     // }
//     // ~normal_lms(); //Destructor
// };


// int main(){
//     int user_inp;
//     cout<<"<<<<<-----Welcome to Library Management System----->>>>>\n"<<endl;
//     normal_lms o1;
//     // do
//     // {
//     //     // Taking input from the user
//     //     cout<<"--> 1. Show Books"<<endl;
//     //     cout<<"--> 2. Borrow Book"<<endl;
//     //     cout<<"--> 3. Return/Add Book"<<endl;
//     //     cout<<"--> 4. Rules"<<endl;
//     //     cout<<"--> 0. Exit"<<endl;
//     //     cout<<endl;
//     //     cout<<"Enter your choice:- ";
//     //     cin>>user_inp;

//     //     // Action according to user input
//     //     switch (user_inp)
//     //     {
//     //     case 1:
//     //         o1.show_books(); //Showing books
//     //         break;
        
//     //     default:
//     //         break;
//     //     }
//     // } while (user_inp!=0);
//     // o1.show_books();
//     return 0;
// }