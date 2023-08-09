class Main inherits IO {
   x : Int <- 0;
   main(): SELF_TYPE {{
    x <- 4;
    if 2 = x then x <- 3 else x <- 4 fi
   (new Main).main();
   }};
};