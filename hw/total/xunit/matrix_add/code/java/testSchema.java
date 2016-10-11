public class testSchema {
	public static void main(String[] argv) {
		SchemaResultCollector collector = new SchemaResultCollector();
		javaschema schema = new javaschema();

		classSchema cs = schema._class("OperationTest");
		cs._method("test_empty");
		cs._method("test_column_different");
		cs._method("test_legal");
		cs._method("test_legal_add_illegal");
		cs._method("test_illegal_add_legal");
		cs._method("test_illegal_add_illegal");
		cs._method("test_different_row");
		cs._method("test_different_column");
		cs._method("test_legal_and_legal");

		schema.check(collector);

		collector.print();
	}
}
