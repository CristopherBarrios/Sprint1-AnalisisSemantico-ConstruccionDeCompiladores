class Main inherits IO {
        a: Int <- 5;
        b: Int <- 2;
        c: Int <- 3;
  main() : Int {
    {
    a <- a + b * c;
    (new Main).main();
    }
  };
 };
