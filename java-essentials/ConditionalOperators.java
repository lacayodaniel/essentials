import java.util.Scanner;
public class ConditionalOperators{
  int x;

  // Constructor
  public ConditionalOperators(int a){
    // Instance field
    x = a; // holds user input
  }

  public void operators(){
    // AND operator &&
    if (x > 1 && x < 10) System.out.println("1 < "+x+" < 10");
    // OR operator ||
    else if (x < 1 || x > 10) System.out.println(x+" < 1 || "+x+" > 10");
    // NOT operator !
    else if (!(x % 2 == 0)) System.out.println(x+" is odd");
  }

  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Please enter an int: ");
    int num = input.nextInt();

    ConditionalOperators condo = new ConditionalOperators(num);
    condo.operators();
  }
}
