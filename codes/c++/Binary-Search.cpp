#include <bits/stdc++.h>
using namespace std;

int binarysearch(int arr[],int n,int target){

    int low=0;
    int high=n-1;
    while(low<=high)
    {
        int mid=low+(high-low)/2;

        if(arr[mid]==target)    
            return mid;
        else if(arr[mid]<target)
            low=mid+1;
        else    
            high=mid-1;
    }
    return -1;
}


int main(){
    int n;
    cout<<"Enter number of elements in array:";
    cin>>n;

    int arr[n];
    cout<<"\nEnter elements of array(Array must be in sorted order)"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }

    int target;
    cout<<"Enter element to be searched"<<endl;  
    cin>>target; 

    cout<<"Array is"<<endl;

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    int index=binarysearch(arr,n,target);
    if(index==-1){
        cout<<"Element Not Found";
    }else{
        cout<<"Element Found At Index:"<<index;
    }
    return 0;
}
