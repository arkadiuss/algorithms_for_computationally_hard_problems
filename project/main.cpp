#include<bits/stdc++.h>
#define VAR(i,n) __typeof(n) i = (n)
#define loop(i,j,s) for(int i=j;i<s;i++)
#define loopback(i,j,s) for(int i=j;i>=s;i--)
#define foreach(i,c) for(VAR(i,(c).begin());i!=(c).end();i++)
#define pln( x ) cout << x << "\n"
#define ps( x ) cout << x << " "
#define entr cout << "\n"
#define pcnt(i) __builtin_popcount(i)
#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define SIZE(c) (c).size()
#define ALL(c) (c).begin(), (c).end()
using namespace std;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<vector<int> > VVI;
const int INFTY=20000000;
const int MAX=100100;
const int MOD=10000000;

void coutTab(int* tab,int n){
	loop(i,0,n){
		cout<<tab[i]<<" ";
	}
	cout<<"\n";
}

template<class T> void coutVec(vector<T> tab){
	for(T t : tab){
		cout<<t<<" ";
	}
	cout<<"\n";
}
//------------------------------------------

class E {
	
};

class V {
public:
	int x, y;
};

template<class V, class E> struct Graph {
	
	struct Ed: E {
		int v;
		Ed(int _v, E e = E()) : E(e), v(_v) {};
		
		bool operator<(const Ed & e) const{
			return v < e.v;
		}
	};

	struct Ve: V, set<Ed> {
		vector<int> d;
	};
	
	vector<Ve> g;
	Graph(int n) : g(n) {};
	
	void setXY(int i, int x, int y) {
		g[i].x = x;
		g[i].y = y;
	}
	
	void edge(int a, int b, E e = E()) {
		Ed ea(a, e);
		Ed eb(b, e);
		g[b].insert(ea);
		g[a].insert(eb);
	}
	
	void bfs(int s) {
		queue<int> Q;
		VI d(g.size(), -1);
		Q.push(s);
		d[s]=0;
		while(!Q.empty()) {
			int v = Q.front();
			Q.pop();
			for(auto it : g[v]){
				if(d[it.v] == -1) {
					d[it.v] = d[v] + 1;
					Q.push(g[it.v]);
				}
			}
		}
		g[s].d = d;
	}
};

Graph<V,E> input(int W, int H, int L, int K) {
	string name;
	cin>>name;
	vector<vector<char>> A(H, vector<char>(W));
	vector<vector<int>> I(H, vector<int>(W, -1));
	char a;
	int n=0;
	loop(i,0,H) {
		loop(j,0,W) {
			cin>>a;
			A[i][j] = a;
			if(a != '.') {
				I[i][j] = n;	
				n++;
			}
		}	
	}
	Graph<V, E> G(n);
	loop(i,0,H) {
		loop(j,0,W) {
			if(a != '.') {
				G.setXY(I[i][j], i, j);
			}
			if((A[i][j] == '|' || A[i][j] == '+') && i > 0 && (A[i-1][j] == '|' || A[i-1][j] == '+')) {
				G.edge(I[i][j], I[i-1][j]);
			}  
			if((A[i][j] == '-' || A[i][j] == '+') && j > 0 && (A[i][j-1] == '-' || A[i][j-1] == '+')) {
				G.edge(I[i][j], I[i][j-1]);
			} 
		}
	}
	return G;
}

void print(const Graph<V, E> & G) {
	loop(i,0,(int) G.g.size()) {
		ps(i);ps(": ");
		for(auto it : G.g[i]) {
			ps(it.v);
		}
		entr;
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	int W,H,L,K;
	cin>>W>>H>>L>>K;
	auto G = input(W,H,L,K);
	print(G);
}	
