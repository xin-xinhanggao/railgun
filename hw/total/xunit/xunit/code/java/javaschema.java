import java.util.*; 
import java.io.*;

class SchemaResultCollector {
	public int total = 0;
	public int error = 0;
	public Vector errors = new Vector();

	public void addSuccess() {
		total += 1;
	}

	public void addError(String msg) {
		errors.add(msg);
		total += 1;
		error += 1;
	}

	public void print() {
		int size = errors.size();
		for (int i = 0; i < size; ++i)
			System.out.println((String)errors.get(i));
		System.out.println(total);
		System.out.print(error);
	}
}

class BaseSchema {
	public Vector children = new Vector();

	public void check(SchemaResultCollector collector) {
		check_self(collector);
		check_children(collector);
	}

	public void check_self(SchemaResultCollector collector) {

	}

	public void check_children(SchemaResultCollector collector) {

	}
}

public class javaschema extends BaseSchema {
	public classSchema _class(String classname) {
		classSchema cs = new classSchema(classname);
		children.add(cs);
		return cs;
	}

	public void check_children(SchemaResultCollector collector) {
		int size = children.size();
		for (int i = 0; i < size; ++i)
			((classSchema)children.get(i)).check(collector);
	}
}

class classSchema extends BaseSchema {
	public String classname;

	public classSchema(String classname) {
		this.classname = classname;
	}

	public methodSchema _method(String methodname) {
		methodSchema ms = new methodSchema(classname, methodname);
		children.add(ms);
		return ms;
	}

	public void check_self(SchemaResultCollector collector) {
		Class objclass = null;
		try {
			objclass = Class.forName(classname);
			collector.addSuccess();
		} catch (Exception e) {
			collector.addError(String.format("%s 是必须的，但该类不存在或无法载入。", classname));
		}
	}

	public void check_children(SchemaResultCollector collector) {
		int size = children.size();
		for (int i = 0; i < size; ++i)
			((methodSchema)children.get(i)).check(collector);
	}
}

class methodSchema extends BaseSchema {
	public String classname;
	public String methodname;

	public methodSchema(String classname, String methodname) {
		this.classname = classname;
		this.methodname = methodname;
	}

	public void check_self(SchemaResultCollector collector) {
		try {
			Class objclass = Class.forName(classname);
			objclass.getDeclaredMethod(methodname);
		} catch (ClassNotFoundException e) {
			collector.addError(String.format("%s.%s 是必须的，但该方法不存在或无法载入。", classname, methodname));
		} catch (NoSuchMethodException e) {
			collector.addError(String.format("%s.%s 是必须的，但该方法不存在或无法载入。", classname, methodname));
		}
	}
}