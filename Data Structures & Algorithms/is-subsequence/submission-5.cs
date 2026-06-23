public class Solution {
    public bool IsSubsequence(string s, string t) {
        int i = 0, j = 0;
        if (s.Length == 0) return true;

        while (j < t.Length)
        {
            if (s[i] == t[j])
            {
                i++;
            }

            if (i == s.Length)
                return true;

            j++;
        }

        return false;



        
    }
}




