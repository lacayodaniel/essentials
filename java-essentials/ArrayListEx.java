import java.util.ArrayList;
public class ArrayListEx{


  public static void main(String[] args){
    // declaring
    ArrayList<Integer> ages;
    // also <Char> <String> <Double> <Object>

    // initializing
    ages = new ArrayList<Integer>();

    // declare and initialize in one oneline
    ArrayList<String> babyNames = new ArrayList<String>();
    babyNames.add("Daniel"); //["Daniel"]
    // note that types must must match!
    babyNames.add("Chris"); // ["Daniel", "Chris"]
    System.out.println(babyNames);


    // to hold different types in the same array
    // although not great because have to cast inorder to use object's methods
    ArrayList<Object> assortment = new ArrayList<Object>();
    assortment.add("Daniel");
    assortment.add(21);
    assortment.add(true);
    System.out.println(assortment);
  }
}
