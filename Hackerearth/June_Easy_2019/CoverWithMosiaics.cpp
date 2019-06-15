/*
// Sample code to perform I/O:

cin >> name;                            // Reading input from STDIN
cout << "Hi, " << name << ".\n";        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
#include<bits/stdc++.h>
using namespace std;
const int maxn = 1000 + 10;
bool b[maxn][maxn];
bool ps[maxn][maxn];
bool ar[maxn][maxn];
 
int main(){
    int n, m, k;
    cin >> n >> m >> k;
    for(int i = 1; i <= n; i++)
	for(int j = 1; j <= m; j++)
	    cin >> b[i][j];
    int ans = 0;
    for(int i = 1; i <= n; i++)
	for(int j = 1; j <= m; j++){
	    ps[i][j] = ps[i - 1][j - 1] ^ ps[i][j] ^ ps[i - 1][j] ^ ps[i][j - 1];
	    if(ps[i][j] == b[i][j]){
		if(i + k > n + 1 || j + k > m + 1)
		    return cout << -1 << endl , 0;
		ps[i][j] ^= 1;
		ps[i + k][j] ^= 1;
		ps[i][j + k] ^= 1;
		ps[i + k][j + k] ^= 1;
		ans++;
	    }
	}
    cout << ans << endl;
}
