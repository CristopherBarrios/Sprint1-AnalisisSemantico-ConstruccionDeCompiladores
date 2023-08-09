class Main inherits IO {
   num1 : Int <- 0;
   num2 : Int <- 0;
   x : Int <- 0;
   main(): SELF_TYPE {{
    x <- num1 + num2;
   (new Main).main();
   }};
};