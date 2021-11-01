#include<cstdio>
#include<cstring>
using namespace std;
const int N=10;
int n,cas,a[N];
int query(){
    int cnt=0;
    for(int i=1;i<n;i++) if(a[i-1]+1!=a[i]) cnt++;
    if(cnt>0) cnt++;
    return cnt;
}
bool success(){
    for(int i=1;i<n;i++) if(a[i-1]+1!=a[i]) return 0;
    return 1;
}
void create(int start,int len,int k){//Move the numbers in the range of A ~ B to the back of C, that is, [A, B] and (B, C] interchange
    int olda[N];
    memcpy(olda,a,sizeof a);
    int i=0;
    for(int z=0;z<k;z++){
        if(z>=start&&z<start+len){z+=len-1;continue;}
        a[i++]=olda[z];
    }
    for(int z=0;z<len;z++) a[i++]=olda[start+z];
    for(int z=k;z<n;z++){
        if(z>=start&&z<start+len){z+=len-1;continue;}
        a[i++]=olda[z];
    }
}
bool dfs(int d,int maxd){
    int h=query();
    if(3*d+h>3*maxd) return 0;
    if(success()) return 1;
    int tmp[N];
    memcpy(tmp,a,sizeof a);
    for(int i=0;i<n;i++){
        for(int j=i+1;j<=n;j++){
            for(int k=0;k<=n;k++){
                if(k>=i&&k<=j){k=j;continue;}
                create(i,j-i,k);//Move the arrays in the range of K to I to the rear of J
                if(dfs(d+1,maxd)) return 1;
                memcpy(a,tmp,sizeof a);
            }
        }
    }
    return 0;
}
int solve(){
    if(success()) return 0;
    for(int k=1;k<5;k++) if(dfs(0,k)) return k;
    return 5;
}
int main(){
    while(scanf("%d",&n)==1&&n){
        for(int i=0;i<n;i++) scanf("%d",a+i);
        int ans=solve();
        printf("Case %d: %d\n",++cas,ans);
    }
    return 0;
}