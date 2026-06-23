public class Solution {
    public bool IsSubsequence(string s, string t) {

        List<char> s_list = s.ToList();
        for (int i = 0; i < t.Length; i++)
        {
            if (s_list.Count == 0) return true;

            if (t[i] == s_list[0])
            {
                s_list.RemoveAt(0);
            }
        }

        return (s_list.Count == 0);




        //s_list =   
        //string t = e

        
    }
}




