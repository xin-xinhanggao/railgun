public class testSchema {
	public static void main(String[] argv) {
		SchemaResultCollector collector = new SchemaResultCollector();
		javaschema schema = new javaschema();

		classSchema cs = schema._class("arithTest");
		cs._method("test_positive_add_positive");
		cs._method("test_positive_add_negative");
		cs._method("test_negative_add_negative");
		cs._method("test_positive_pow_positive");
		cs._method("test_positive_pow_negative");
		cs._method("test_negative_pow_positive_success");
		cs._method("test_negative_pow_positive_failure");
		cs._method("test_negative_pow_negative_success");
		cs._method("test_negative_pow_negative_failure");

		classSchema cs2 = schema._class("minmaxTest");
		cs2._method("test_abc");
		cs2._method("test_acb");
		cs2._method("test_bac");
		cs2._method("test_bca");
		cs2._method("test_cab");
		cs2._method("test_cba");

		schema.check(collector);

		collector.print();
	}
}
