#include<iostream>
#include<string>
using namespace std;

class normal_lms
{
private:
    string book_list[101] = {"Power Of Habit", "Dopamine Detox", "Strategic Mindset", "Rich Dad Poor Dad", "Atomic Habit"}; //Book list
public:
    normal_lms(){ //Constructor 
        // book_list[0] = "Power Of Habit";
        // book_list[1] = "Dopamine Detox";
        // book_list[2] = "Strategic Mindset";
        // book_list[3] = "Rich Dad Poor Dad";
        // book_list[4] = "Atomic Habit";
        // int he;
    
    }
    void show_books(){
        for(auto i: book_list){
            cout<<book_list<<endl;
        }
    }
    ~normal_lms(){} //Destructor
};


int main(){
    int user_inp;
    cout<<"<<<<<-----Welcome to Library Management System----->>>>>\n"<<endl;
    normal_lms o1;
    do
    {
        // Taking input from the user
        cout<<"--> 1. Show Books"<<endl;
        cout<<"--> 2. Borrow Book"<<endl;
        cout<<"--> 3. Return/Add Book"<<endl;
        cout<<"--> 4. Rules"<<endl;
        cout<<"--> 0. Exit"<<endl;
        cout<<endl;
        cout<<"Enter your choice:- ";
        cin>>user_inp;

        // Action according to user input
        switch (user_inp)
        {
        case 1:
            o1.show_books(); //Showing books
            break;
        
        default:
            break;
        }
    } while (user_inp!=0);
    return 0;
}