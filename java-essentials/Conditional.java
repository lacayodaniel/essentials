
public class Conditional{
  int x, y;

  public Conditional(int a, int b){
    x = a;
    y = b;
  }

  public void checkEquivalency(){
    if (x == y){
      System.out.println(x + " == " + y);
    } else if (x > y){
      System.out.println(x + " > " + y);
    } else System.out.println(x + " < " + y); // notice braces are omitted for oneliners
  }

  public void switchDemo(int day){
    switch (day) {
      case 1:
        System.out.println("Monday");
        break;
        // very important to note: without the break, code blocks that aren't
        // conditionally satisfied will still execute
      case 2:
        System.out.println("Tuesday");
        break;
      case 3:
        System.out.println("Wednesday");
        break;
      case 4:
        System.out.println("Thursday");
        break;
      case 5:
        System.out.println("Friday");
        break;
      case 6:
        System.out.println("Saturday");
        break;
      case 7:
        System.out.println("Sunday");
        break;
      default:
        System.out.println("Days are between [1, 7], inclusive.");
        // if the default statement is used last it doesn't need a break
    }
  }

  // while loop counts from [0, n)
  public void whileDemo(int n){
    int i = 0;
    while (i < n) {
      System.out.print(i + " ");
      i++;
    }
    System.out.println();

    // break example, stops at 3 on [0,n)
    // int i = 0;
    // while (i < n{
    //   System.out.println(i);
    //   i++;
    //   if (i == 4) {
    //     break;
    //   }
    // }

    // continue example, skips 4 on [0,n)
    // int i = 0;
    // while (i < n) {
    //   if (i == 4) {
    //     i++;
    //     continue;
    //   }
    //   System.out.println(i);
    //   i++;
    // }
  }

  // do-while loop counts from [0, n) or [0]
  public void doWhileDemo(int n){
    int i = 0;
    do {
      // this executes even if it's false initially
      // in other words, this code block is guaranteed to run at least once
      System.out.print(i + " ");
      i++;
    } while (i < n);
    System.out.println();
  }

  // for loop counts from [0, n)
  public void forDemo(int n){
    /*
    for (statement 1; statement 2; statement 3) {
      // code block to be executed
    }
    Statement 1 is executed (one time) before the execution of the code block.
    Statement 2 defines the condition for executing the code block.
    Statement 3 is executed (every time) after the code block has been executed.
    */
    for (int i = 0; i < n; i++) {
      System.out.print(i + " ");
    }
    System.out.println();

    // break example, stops at 3 on [0,n)
    // for (int i = 0; i < n; i++) {
    //   if (i == 4) {
    //     break;
    //   }
    //   System.out.println(i);
    // }

    // continue example, skips 4 on [0,n)
    // for (int i = 0; i < n; i++) {
    //   if (i == 4) {
    //     continue;
    //   }
    //   System.out.println(i);
    // }

  }

  // demonstrates element-wise looping (as opposed to index-wise looping)
  public void forEachDemo(){
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    for (String i : cars) {
      System.out.print(i + " ");
    }
    System.out.println();
  }



  public static void main(String[] args){
    Conditional truthy = new Conditional(1,1);
    Conditional falsey = new Conditional(3,2);
    Conditional elsey = new Conditional(1,2);
    truthy.checkEquivalency(); // outputs 1 == 1
    falsey.checkEquivalency(); // outputs 3 > 2
    elsey.checkEquivalency(); // outputs 1 < 2

    // ternary operator
    // variable = (condition) ? expressionTrue :  expressionFalse;
    System.out.println(truthy.x == truthy.y ? "True" : "False");

    truthy.switchDemo(1); // outputs Monday

    truthy.whileDemo(5); // outputs 0 1 2 3 4
    truthy.whileDemo(0); // outputs (nothing)

    truthy.doWhileDemo(5); // outputs 0 1 2 3 4
    truthy.doWhileDemo(0); // outputs 0

    truthy.forDemo(5); // outputs 0 1 2 3 4
    truthy.forDemo(0); // outputs (nothing)

    truthy.forEachDemo(); // outputs Volvo BMW Ford Mazda




  }
}
