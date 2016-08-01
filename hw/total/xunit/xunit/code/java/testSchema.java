public class testSchema {
	public static void main(String[] argv) {
		SchemaResultCollector collector = new SchemaResultCollector();
		javaschema schema = new javaschema();
		classSchema cs = schema._class("arithTest");
		cs._method("estAdd");

		schema.check(collector);

		collector.print();
	}
}
