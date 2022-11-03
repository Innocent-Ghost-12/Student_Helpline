#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
using namespace std;
vector <int> cls1,cls2;
int mean(vector <int> v){
	int sum = 0;
	for(int i=0;i<v.size();i++){
		sum+=v[i];
	}
	float mean = (float)sum/(float)v.size();
	return round(mean);
}

int main(){
	vector <int> arr{2,3,4,10,11,12,20,25,30};
//	int arr[] = {2,3,4,10,11,12,20,25,30};
	int m1 = 4, m2 = 12,nm1=0,nm2=0,c=0;

	vector <int> cls1,cls2;
	
	for(int j=0;j<10;j++){
		for(int i=0;i<9;i++){
			if( abs(m1-arr[i]) < abs(m2-arr[i]) ){
				cls1.push_back(arr[i]);
			}
			else{
				cls2.push_back(arr[i]);
			}
		}
		nm1 = m1;
		nm2 = m2;
		m1 = mean(cls1);
		m2 = mean(cls2);

		if(nm1==m1 && nm2==m2){
			cout<<"Iterations: "<<c<<endl;
			break;
		}
		cls1.clear();
		cls2.clear();
		c++;
	}
	
	for(int i=0;i<cls1.size();i++){
		cout<<cls1[i]<<" ";
	}
	cout<<"\n";
	for(int i=0;i<cls2.size();i++){
		cout<<cls2[i]<<" ";
	}
	cout<<"\n";
	
	return 0;
}
