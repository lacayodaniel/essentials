// compile command: (this generates a filename.class binary file to run on the JVM)
// javac filename.java

// execute command:
// java filename

// files must be named after the class they hold
public class hello {
  public static void main(String[] args) {
    // print equivalent syntax
    System.out.println("Hello, World!");

    // function calling
    System.out.println(square());

    // variable declaration
    int x_squared = squared(2);
    System.out.println(x_squared);

    // constant declaration (known as final)
    final double pi = 3.14;

    // datatype variableName
    int age, height, weight;
    double salaryRequirement;
    boolean isEmployed;
    char grade = 'A'; // note char must have single quote
    String openingLyrics = "Yesterday, all my troubles seemed so far away";

    // int variable declaration
    int yearJavaWasCreated;
    // assignment
    yearJavaWasCreated = 1996;
    // declaration and assignment
    int numberOfPrimitiveTypes = 8;

    // increment and decrement
    numberOfPrimitiveTypes++;
    numberOfPrimitiveTypes--;
    // also: += -= *= /= %= (yes thats modulo)

    // equality check
    boolean haveTimeTraveled = yearJavaWasCreated == 2022;
    boolean objectsDoMatch = "Hello".equals("Hello");
    println("When testing object equivalency, use .equals(): " + objectsDoMatch);

    // string methods
    String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    System.out.println("The length of the txt string is: " + txt.length());
    txt = "Hello World";
    // equivalent upper()
    System.out.println(txt.toUpperCase());   // Outputs "HELLO WORLD"
    // equivalent lower()
    System.out.println(txt.toLowerCase());   // Outputs "hello world"
    // equivalent find() (counts whitespace)
    txt = "Please locate where 'locate' occurs!";
    System.out.println(txt.indexOf("Please")); // Outputs 0
    System.out.println(txt.indexOf("'")); // Outputs 20 (the first ' before locate)
    System.out.println(txt.indexOf("locate")); // Outputs 7
    // concatination
    String firstName = "John ";
    String lastName = "Doe";
    println(firstName.concat(lastName)); // outputs John Doe
    println(firstName + lastName); // outputs John Doe
    // note that int + String = String (using concatination)
    int y = 10;
    println(firstName + y); // outputs John 10

    // math
    println(Math.sqrt(64)); // outputs 8
    println(Math.min(10,5)); // outputs 5
    println(Math.max(5,10)); // outputs 10
    println(Math.abs(-4.7)); // outputs 4.7
    println(Math.random()); // outputs random double between [0.0, 1.0] inclusive
    println(Math.random() * 100); // [0.0 to 100.0) (ex. 99.99 allowed)
    println((int)(Math.random() * 11)); // [0, 10]



  }

  // returns the string 'square'
  public static String square(){
    return "Square";
  }

  // f(x) = x^2
  public static int squared(int x){
    return x*x;
  }

  // the pinkies thank me for this one
  public static void println(String str){
    System.out.println(str);
  }

  // variation for double
  public static void println(double d){
    System.out.println(d);
  }


  /*
  multiline
  comment
  example
  weee
  */



}
