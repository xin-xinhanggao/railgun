import static org.junit.Assert.*;

import org.junit.Test;

//import java.arith;

public class myfuncTest { 
    @Test
    public void test1(){ 
        myfunc test = new myfunc(); 
        double result = test.myfunc(1, 2, 3); 
        assertEquals(1,result,0); 
    } 
	
	@Test
    public void test2(){ 
        myfunc test = new myfunc(); 
        double result = test.myfunc(1, -2, 3); 
        assertEquals(-2,result,0); 
    }

	@Test
    public void test3(){ 
        myfunc test = new myfunc(); 
        double result = test.myfunc(1, 2, -3); 
        assertEquals(-3,result,0); 
    } 


	@Test
    public void test4(){ 
        myfunc test = new myfunc(); 
        double result = test.myfunc(1, -2, -3); 
        assertEquals(-3,result,0); 
    } 


	@Test
    public void test5(){ 
        myfunc test = new myfunc(); 
        double result = test.myfunc(4, -2, 3); 
        assertEquals(-2,result,0); 
    } 


	@Test
    public void test6(){ 
        myfunc test = new myfunc(); 
        double result = test.myfunc(1, 2, 1.5); 
        assertEquals(1,result,0); 
    } 

	@Test
    public void test7(){ 
        myfunc test = new myfunc(); 
        double result = test.myfunc(100000000, 2, 3); 
        assertEquals(2,result,0); 
    }  
}


