#include<iostream>
#include<bits.h>
#include<vector>

using namespace std;

class Solution {
public:
    bool isValid(vector<vector<char>>& a,int r,int c,char val){
        int x=r/3*3,y=c/3*3;
        for(int i=0;i<9;i++){
            if(a[r][i]==val)return false;
            if(a[i][c]==val)return false;
            if(a[x+i/3][y+i%3]==val)return false;
        }
        return true;
    }
    bool backtrack(vector<vector<char>>& a,int r,int c){
        if(r==9)return true;
        if(c==9)return backtrack(a,r+1,0);
        if(a[r][c]!='.')return backtrack(a,r,c+1);
        for(char i='1';i<='9';i++){
            if(isValid(a,r,c,i)){
                a[r][c]=i;
                if(backtrack(a,r,c+1))return true;
                a[r][c]='.';
            }
        }
        return false;
    }
    void solveSudoku(vector<vector<char>>& board) {
        backtrack(board,0,0);
    }
};