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
		bool removed = false;
	};
	
	vector<Ve> g;
	int n;
	Graph(int _n) : g(_n), n(_n) {};
	
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
					Q.push(it.v);
				}
			}
		}
		g[s].d = d;
	}
	
	void removeV(int v) {
		for(auto it : g[v]) {
			g[it.v].erase(v);
		}
		g[v].clear();
		g[v].removed = true;
	}
	
	void softRemoveV(int v) {
		g[v].removed = true;
	}
	
	void restoreV(int v) {
		/*for(auto it : g[v]) {
			g[it.v].erase(v);
		}
		g[v].clear(); */
		g[v].removed = false;
	}
};

typedef Graph<V, E>  GraphVE;

GraphVE input(int W, int H, int L, int K) {
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
	GraphVE G(n);
	loop(i,0,H) {
		loop(j,0,W) {
			if(A[i][j] != '.') {
				G.setXY(I[i][j], j, i);
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

void print(const GraphVE & G) {
	loop(i,0,(int) G.g.size()) {
		ps(i);ps(": ");
		for(auto it : G.g[i]) {
			ps(it.v);
		}
		entr;
	}
}

void addMissingEdges(GraphVE & G, int L) {
	loop(i,0,G.n) {
		loop(j,0,G.n) {
			if(G.g[i].d[j] > 1 && G.g[i].d[j] <= L){
				G.edge(i,j);
			} 
		}
	}
}

int lowestDegree(const GraphVE & G) {
	int minv = -1;
	loop(i,0,G.n) {
		if(!G.g[i].removed && (minv == -1 || G.g[minv].size()>G.g[i].size())) 
			minv = i;
	}
	return minv;
}

vector<PII> algo1(GraphVE G, int L, int K) {
	loop(i,0,G.n) {
		G.bfs(i);
	}
	addMissingEdges(G, L);
	vector<PII> res;
	while(K > 0) {
		int v = lowestDegree(G);
		if(v == -1) {
			return vector<PII>();
		}
		res.pb({ G.g[v].x, G.g[v].y });
		VI toRemove;
		for(auto neigh : G.g[v]) {
			toRemove.pb(neigh.v);
		}
		toRemove.pb(v);
		for(auto vr : toRemove) {
			G.removeV(vr);
		}
		K--;
	}
	return res;
}

int countEdgesWithNeigh(const GraphVE & G, int v) {
	int e = 0;
	for(auto it : G.g[v]) {
		if(v < it.v) e++;
		for(auto itn : G.g[it.v]) {
			if(it.v < itn.v) e++;
		}
	}
	//ps(v);pln(e);
	return e;
}

int superLowestDegree(const GraphVE & G) {
	int minv = -1;
	loop(i,0,G.n) {
		if(!G.g[i].removed && (minv == -1 || G.g[minv].size()>G.g[i].size())) {
			minv = i;
		} else if(!G.g[i].removed && minv != -1 && G.g[minv].size()==G.g[i].size() && countEdgesWithNeigh(G, i) > countEdgesWithNeigh(G, minv)) {
			minv = i;
		}
	}
	return minv;
}

vector<PII> algo2(GraphVE G, int L, int K) {
	loop(i,0,G.n) {
		G.bfs(i);
	}
	addMissingEdges(G, L);
	vector<PII> res;
	while(K > 0) {
		int v = superLowestDegree(G);
		if(v == -1) {
			return vector<PII>();
		}
		res.pb({ G.g[v].x, G.g[v].y });
		VI toRemove;
		for(auto neigh : G.g[v]) {
			toRemove.pb(neigh.v);
		}
		toRemove.pb(v);
		for(auto vr : toRemove) {
			G.removeV(vr);
		}
		K--;
	}
	return res;
}

VI removeVAndNeighs(GraphVE & G, int v) {
	VI toRemove;
	for(auto neigh : G.g[v]) {
		if(!G.g[neigh.v].removed)
			toRemove.pb(neigh.v);
	}
	toRemove.pb(v);
	for(auto vr : toRemove) {
		G.softRemoveV(vr);
	}
	return toRemove;
}

vector<PII> backtrack(GraphVE & G, int K) {
	if(K == 1) {
		for(int i = 0; i<G.n; i++) {
			if(!G.g[i].removed){ return vector<PII>(1, {G.g[i].x, G.g[i].y});}
		}	
		return vector<PII>();
	}
	for(int i = 0; i<G.n; i++) {
		if(!G.g[i].removed) {
			auto removed = removeVAndNeighs(G, i);
			auto res = backtrack(G, K-1);
			if(res.size() != 0) {
				res.pb({G.g[i].x, G.g[i].y});
				return res;
			}
			for(auto r: removed)
				G.restoreV(r);
		}
	}
	return vector<PII>();
}

vector<PII> algo3(GraphVE G, int L, int K) {
	loop(i,0,G.n) {
		G.bfs(i);
	}
	addMissingEdges(G, L);
	return backtrack(G, K);
}

int main() {
	ios_base::sync_with_stdio(0);
	int W,H,L,K;
	cin>>W>>H>>L>>K;
	auto G = input(W,H,L,K);
	auto algos = { algo1, algo2, algo3 };
	for(auto algo : algos) {
		auto res = algo(G, L, K);
		if(res.size() > 0){
			for(auto p : res) {
				ps(p.ff);pln(p.ss);
			}
			break;
		}
	}
}	
