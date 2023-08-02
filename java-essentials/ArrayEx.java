

public class ArrayEx{
  // array initialization
  // dataType[] varName = {dataType, dataType, ...}
  int[] intArr;
  String[] strArr;
  boolean[] boolArr;
  double[] doubArr;
  char[] charArr;

  public ArrayEx(int[] ints, String[] strings, boolean[] bools, double[] doubs, char[] chars){
    intArr = ints;
    strArr = strings;
    boolArr = bools;
    doubArr = doubs;
    charArr = chars;
  }

  public void printData(){
    System.out.print("Int array:[ ");
    for (int i : intArr) {
      System.out.print(i + " ");
    }
    System.out.print("]\n");

    System.out.print("String array:[ ");
    for (String i : strArr) {
      System.out.print(i + " ");
    }
    System.out.print("]\n");

    System.out.print("Boolean array:[ ");
    for (boolean i : boolArr) {
      System.out.print(i + " ");
    }
    System.out.print("]\n");

    System.out.print("Double array:[ ");
    for (double i : doubArr) {
      System.out.print(i + " ");
    }
    System.out.print("]\n");

    System.out.print("Char array:[ ");
    for (char i : charArr) {
      System.out.print(i + " ");
    }
    System.out.print("]\n");
  }

  public static void main(String[] args){
    ArrayEx arrObject = new ArrayEx(new int[]{1,2,3},
                                    new String[]{"abc","def","ghi"},
                                    new boolean[]{false,true,true},
                                    new double[]{3.14,2.71,0.69},
                                    new char[]{'a','b','c'});
    arrObject.printData();
  }
}
