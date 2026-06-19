#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    
    int n;
    scanf("%d",&n);
    vector<double> m(n),r(n),px(n),py(n),pz(n),vx(n),vy(n),vz(n);
    for(int i=0;i<n;i++){
        scanf("%lf %lf %lf %lf %lf %lf %lf %lf",
            &m[i],&r[i],&px[i],&py[i],&pz[i],&vx[i],&vy[i],&vz[i]);
    }
    double T;
    scanf("%lf",&T);

    const double EPS=1e-12;
    double t=0.0;

    while(true){
        double best=-1; int bi=-1,bj=-1;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                double dx=px[i]-px[j],dy=py[i]-py[j],dz=pz[i]-pz[j];
                double dvx=vx[i]-vx[j],dvy=vy[i]-vy[j],dvz=vz[i]-vz[j];
                double R=r[i]+r[j];
                double a=dvx*dvx+dvy*dvy+dvz*dvz;
                double b=2*(dx*dvx+dy*dvy+dz*dvz);
                double c=dx*dx+dy*dy+dz*dz-R*R;
                if(a<EPS) continue;
                if(b>=0) continue;
                double disc=b*b-4*a*c;
                if(disc<0) continue;
                double sq=sqrt(disc);
                double t1=(-b-sq)/(2*a);
                if(t1<-1e-9) continue;
                if(t1<0) t1=0.0;
                if(t1<=T-t+1e-9){
                    if(bi==-1||t1<best-1e-12){
                        best=t1; bi=i; bj=j;
                    }
                }
            }
        }
        if(bi==-1) break;
        double dt=best;
        for(int i=0;i<n;i++){
            px[i]+=vx[i]*dt;
            py[i]+=vy[i]*dt;
            pz[i]+=vz[i]*dt;
        }
        t+=dt;
        int i=bi,j=bj;
        double nx=px[i]-px[j],ny=py[i]-py[j],nz=pz[i]-pz[j];
        double dist=sqrt(nx*nx+ny*ny+nz*nz);
        nx/=dist; ny/=dist; nz/=dist;
        double v1n=vx[i]*nx+vy[i]*ny+vz[i]*nz;
        double v2n=vx[j]*nx+vy[j]*ny+vz[j]*nz;
        double m1=m[i],m2=m[j];
        double v1n_new=(v1n*(m1-m2)+2*m2*v2n)/(m1+m2);
        double v2n_new=(v2n*(m2-m1)+2*m1*v1n)/(m1+m2);
        double d1=v1n_new-v1n,d2=v2n_new-v2n;
        vx[i]+=d1*nx; vy[i]+=d1*ny; vz[i]+=d1*nz;
        vx[j]+=d2*nx; vy[j]+=d2*ny; vz[j]+=d2*nz;
    }

    double rem=T-t;
    for(int i=0;i<n;i++){
        px[i]+=vx[i]*rem;
        py[i]+=vy[i]*rem;
        pz[i]+=vz[i]*rem;
    }

    for(int i=0;i<n;i++){
        printf("%.3f %.3f %.3f %.3f %.3f %.3f\n",
            px[i],py[i],pz[i],vx[i],vy[i],vz[i]);
    }
    return 0;
}
