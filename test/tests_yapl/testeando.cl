class D {

    method2(num1 : Int, num2 : Int) : SELF_TYPE {  -- plus
      (let x : Int in
	 {
            x <- num1 + num2;
	 }
      )
   };
}
class Main inherits IO {
   main(): SELF_TYPE {{
    x <- num1 + num2;
    d.method2(2, 3);
   (new Main).main();
   }};
};