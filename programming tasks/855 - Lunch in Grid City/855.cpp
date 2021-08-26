#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    int anzahlprobleme, xsize, ysize, people;
    cin >> anzahlprobleme;
    
    for(int i = 0; i < anzahlprobleme; i++){
        cin >> xsize >> ysize >> people;
        
        int x [people];
        int y [people];
        
        for(int j = 0; j < people; j++){
            cin >> x[j] >> y[j];
        }
        
        sort(x,x + people);
        sort(y,y + people);
        
        cout << "(Street: " << x[(people-1)/2] << ", Avenue: " <<  y[(people-1)/2] << ")\n";
        
        
    }
    
}