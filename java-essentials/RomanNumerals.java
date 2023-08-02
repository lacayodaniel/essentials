
import java.util.HashMap;

public class RomanNumerals {
  public static void main(String[] args) {
    HashMap<Character, Integer> dictionary = new HashMap<Character, Integer>();
    dictionary.put('I', 1);
    dictionary.put('V', 5);
    dictionary.put('X', 10);
    dictionary.put('L', 50);
    dictionary.put('C', 100);
    dictionary.put('D', 500);
    dictionary.put('M', 1000);
    String s = "MCMXCIV";
    int count = 0;
    int len = s.length();
    for (int i = 0; i < len-1; i++){
        int n1 = dictionary.get(s.charAt(i));
        int n2 = dictionary.get(s.charAt(i+1));
        if (n1 < n2){
            count -= n1;
        }else{
            count += n1;
        }
    }
    count += dictionary.get(s.charAt(len-1));
    System.out.println(count);
  }
}
