class Main inherits IO {
   x : Int <- 0;
   y : Int <- 0;
   main(): SELF_TYPE {{
    x <- 2;
    y <- 1;
    while y <= x loop
    {
        y <- y + 1;
    }
    pool
   (new Main).main();
   }};
};