package Test;

import junit.framework.TestCase; 
//import java.arith;

public class test_arith extends TestCase { 
    public void testAdd(){ 
        arith test = new arith(); 
        double result = test.add(1,2); 
        assertEquals(3,result,0); 
    } 

}
