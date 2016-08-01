import junit.framework.TestSuite; 
import junit.framework.Test; 
import junit.textui.TestRunner; 

public class unitTest { 
    public static Test suite() { 
        TestSuite suite = new TestSuite("TestSuite Test"); 
        suite.addTestSuite(arithTest.class); 
        return suite; 
    } 
    public static void main(String args[]){ 
        TestRunner.run(suite()); 
    } 
}
