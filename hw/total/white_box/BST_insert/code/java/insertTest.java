import static org.junit.Assert.*;

import org.junit.Test;

//import java.arith;

public class insertTest { 
	Tree tree = new Tree();

	public insertTest() {
		insert test = new insert();
		test.insert(tree, new BinNode(null, 44));
		test.insert(tree, new BinNode(null, 22));
		test.insert(tree, new BinNode(null, 66));
		test.insert(tree, new BinNode(null, 11));
		test.insert(tree, new BinNode(null, 33));
		test.insert(tree, new BinNode(null, 55));
		test.insert(tree, new BinNode(null, 77));
	}

    @Test
    public void test1(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 44)))
			result = 1;
        assertEquals(0,result,0); 
    } 

    @Test
    public void test2(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 1)))
			result = 1;
        assertEquals(1,result,0); 
    } 

    @Test
    public void test3(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 12)))
			result = 1;
        assertEquals(1,result,0); 
    } 

    @Test
    public void test4(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 23)))
			result = 1;
        assertEquals(1,result,0); 
    } 

    @Test
    public void test5(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 34)))
			result = 1;
        assertEquals(1,result,0); 
    } 

    @Test
    public void test6(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 45)))
			result = 1;
        assertEquals(1,result,0); 
    } 

    @Test
    public void test7(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 56)))
			result = 1;
        assertEquals(1,result,0); 
    } 

    @Test
    public void test8(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 67)))
			result = 1;
        assertEquals(1,result,0); 
    } 

    @Test
    public void test9(){ 
        insert test = new insert(); 
		double result = 0;
        if (test.insert(tree, new BinNode(null, 78)))
			result = 1;
        assertEquals(1,result,0); 
    } 
}


