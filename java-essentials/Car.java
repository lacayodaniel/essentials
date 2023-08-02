/*
constructor overloading example
classes can have multiple constructors as long as each has a unique signature
*/
public class Car {
  String color;
  int mpg;
  boolean isElectric;

  // constructor 1
  public Car(String carColor, int milesPerGallon) {
    // instance fields
    color = carColor;
    mpg = milesPerGallon;
  }
  // constructor 2
  public Car(boolean electricCar, int milesPerGallon) {
    isElectric = electricCar;
    mpg = milesPerGallon;
  }

  public static void main(String[] args){
    Car constructor1 = new Car("blue", 127000);
    Car constructor2 = new Car(true, 100);
    println(constructor1.color);

    // try and catch clause
    try {
      println(4/0);
    } catch(Exception e){
      println("Division by zero. Error caught.");
    } finally {
      println("The finally block executes regardless of the try-catch outcome");
    }
  }

  // // the pinkies thank me for this one
  public static void println(Object obj){
    System.out.println(obj);
  }
}
