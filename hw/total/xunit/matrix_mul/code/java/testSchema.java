public class testSchema {
	public static void main(String[] argv) {
		SchemaResultCollector collector = new SchemaResultCollector();
		javaschema schema = new javaschema();

		classSchema cs = schema._class("operationTest");
		cs._method("test_empty");
		cs._method("test_column_different");
		cs._method("test_legal");
		cs._method("test_legal_mul_illegal");
		cs._method("test_illegal_mul_legal");
		cs._method("test_illegal_mul_illegal");
		cs._method("test_scale_error");
		cs._method("test_legal_mul_legal");

		schema.check(collector);

		collector.print();
	}
}
