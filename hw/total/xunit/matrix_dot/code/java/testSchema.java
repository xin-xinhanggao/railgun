public class testSchema {
	public static void main(String[] argv) {
		SchemaResultCollector collector = new SchemaResultCollector();
		javaschema schema = new javaschema();

		classSchema cs = schema._class("operationTest");
		cs._method("test_empty");
		cs._method("test_column_different");
		cs._method("test_legal");
		cs._method("test_illegal");
		cs._method("test_rec");
		cs._method("test_one");
		cs._method("test_high");

		schema.check(collector);

		collector.print();
	}
}
