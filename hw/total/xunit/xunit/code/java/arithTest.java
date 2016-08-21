import static org.junit.Assert.*;

import org.junit.Test;

//import java.arith;

public class arithTest { 
    @Test
    public void test_positive_add_positive(){ 
        arith test = new arith(); 
        double result = test.add(1,2); 
        assertEquals(3,result,0); 
    } 

    @Test
    public void test_positive_add_negative(){ 
        arith test = new arith(); 
        double result = test.add(1,-2); 
        assertEquals(-1,result,0); 
    } 

    @Test
    public void test_negative_add_negative(){ 
        arith test = new arith(); 
        double result = test.add(-1,-2); 
        assertEquals(-3,result,0); 
    } 

    @Test
    public void test_positive_pow_positive(){ 
        arith test = new arith(); 
        double result = test.pow(2,3); 
        assertEquals(8,result,0); 
    } 

	@Test
    public void test_positive_pow_negative(){ 
        arith test = new arith(); 
        double result = test.pow(2,-2); 
        assertEquals(0.25,result,0); 
    } 

	@Test
    public void test_negative_pow_positive_success(){ 
        arith test = new arith(); 
        double result = test.pow(-2,2); 
        assertEquals(4,result,0); 
    } 

	@Test
    public void test_negative_pow_positive_failure(){ 
        arith test = new arith(); 
        double result = test.pow(-2,3); 
        assertEquals(4,result,0); 
    } 

	@Test
    public void test_negative_pow_negative_success(){ 
        arith test = new arith(); 
        double result = test.pow(-2,-2); 
        assertEquals(0.25,result,0); 
    } 

	@Test
    public void test_negative_pow_negative_failure(){ 
        arith test = new arith(); 
        double result = test.pow(-2,-3); 
        assertEquals(0.125,result,0); 
    } 
}


