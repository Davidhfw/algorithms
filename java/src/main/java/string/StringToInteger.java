package main.java.string;

public class StringToInteger {

    public static int Atoi(String str) {
        if(str == null || str.length() <= 0) return 0;
        int MAX = Integer.MAX_VALUE;
        int MIN = Integer.MIN_VALUE;
        int res = 0, index = 0;
        while(index < str.length() && str.charAt(index) == ' ') index ++;
        //过滤空格
        if(index == str.length()) return 0;
        //取正负号
        char firstChar = str.charAt(index);
        boolean positive = true;
        if(!isDigit(firstChar)) {
            if(firstChar != '+' && firstChar != '-') return 0;
            index ++;
            positive = firstChar != '-';
        }
        int limit = positive?-MAX:MIN;
        while (index < str.length() && str.charAt(index) == '0') index ++;
        while (index < str.length() && isDigit(str.charAt(index))) {
            int digit = str.charAt(index ++) - '0';
            if(res < (limit + digit) / 10) {
                return positive?MAX:MIN;
            }
            res = res * 10 - digit;
        }
        return positive?res:-res;

    }

    private static boolean isDigit(char c) {
        return c>='0' && c<='9';
    }

    public static void main(String[] args) {
        String str = "andnv799999999998";
        int n = StringToInteger.Atoi(str);
        System.out.println(n);
    }
}

