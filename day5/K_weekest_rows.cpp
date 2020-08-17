class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<pair<int,int> > ones;
        for(int i=0;i<mat.size();i++)
        {
            for(int j=0;j<mat[0].size();j++)
            {
                if(mat[i][mat[i].size()-1]==1)
                {
                    ones.push_back(make_pair(mat[i].size(),i));
                    break;
                }
                else if(mat[i][j]!=1)
                {
                    ones.push_back(make_pair(j,i));
                    break;
                }
            }
        }
        sort(ones.begin(),ones.end());
        int i=0;
        vector<int> weekest_row;
        while(k--)
        {
            weekest_row.push_back(ones[i].second);
            i++;
        }
        return weekest_row;
        
    }
};
