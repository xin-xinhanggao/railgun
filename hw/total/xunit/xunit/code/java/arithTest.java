import junit.framework.TestCase; 

//import java.arith;

public class arithTest extends TestCase { 
    public void testadd(){ 
        arith test = new arith(); 
        double result = test.add(1,2); 
        assertEquals(3,result); 
    } 

}
