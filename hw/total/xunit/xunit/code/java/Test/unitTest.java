package Test;

import junit.framework.TestSuite; 
import junit.framework.Test; 
import junit.textui.TestRunner; 

public class unitTest extends TestSuite { 
    public static Test suite() { 
        TestSuite suite = new TestSuite("TestSuite Test"); 
        suite.addTestSuite(test_arith.class); 
        return suite; 
    } 
    public static void main(String args[]){ 
        TestRunner.run(suite()); 
    } 
}
