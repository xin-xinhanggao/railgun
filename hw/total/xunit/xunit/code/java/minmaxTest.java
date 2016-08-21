import static org.junit.Assert.*;

import org.junit.Test;

//import java.arith;

public class minmaxTest { 
    @Test
    public void test_abc(){ 
        minmax test = new minmax(); 
        double result = test.get_min(1,2,3); 
        assertEquals(1,result,0); 
    } 

    @Test
    public void test_acb(){ 
        minmax test = new minmax(); 
        double result = test.get_min(1,3,2); 
        assertEquals(1,result,0); 
    } 

    @Test
    public void test_bac(){ 
        minmax test = new minmax(); 
        double result = test.get_min(-1,-2,1); 
        assertEquals(-2,result,0); 
    } 

    @Test
    public void test_bca(){ 
        minmax test = new minmax(); 
        double result = test.get_min(2,-3,-1); 
        assertEquals(-3,result,0); 
    } 

	@Test
    public void test_cab(){ 
        minmax test = new minmax(); 
        double result = test.get_min(-2,2,-3); 
        assertEquals(-3,result,0); 
    } 

	@Test
    public void test_cba(){ 
        minmax test = new minmax(); 
        double result = test.get_min(2,-2,-3); 
        assertEquals(-3,result,0); 
    } 
}


