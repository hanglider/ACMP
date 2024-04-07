#include <iostream> 
#include <iomanip> 
using namespace std; 
int main() 
{ 
    freopen ("input.txt","r",stdin); 
    freopen ("output.txt","w",stdout); 
    char a,b,c,x,y,z; 
    cin.get(a); 
    cin.get(b); 
    cin.get(c); 
    cin.get(x); 
    cin.get(y); 
    cin.get(z); 
    if ((a+b+c)==(x+y+z)) cout << "YES"; 
    else cout << "NO"; 
}