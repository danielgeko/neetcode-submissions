public class Solution {
    public int ScoreOfString(string s) {
        int sum = 0, i = 0, int1 = 0, int2 = 0;


        for (int j = 1; j < s.Length; j++)
        {
            int1 = (int)s[i];
            int2 = (int)s[j];
            sum += Math.Abs(int2 - int1);
            i++;
        }

        return sum;
    }

}