import static org.junit.Assert.*;

import org.junit.Test;

//import java.arith;

public class arithTest { 
    @Test
    public void testadd(){ 
        arith test = new arith(); 
        double result = test.add(1,2); 
        assertEquals(3,result); 
    } 

}
