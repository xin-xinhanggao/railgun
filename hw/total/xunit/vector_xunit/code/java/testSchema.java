public class testSchema {
	public static void main(String[] argv) {
		SchemaResultCollector collector = new SchemaResultCollector();
		javaschema schema = new javaschema();

		classSchema cs = schema._class("OperationTest");
		cs._method("test_zero_cross_zero");
		cs._method("test_zero_cross_normal");
		cs._method("test_p1_cross_p2");
		cs._method("test_n1_cross_n2");
		cs._method("test_zero_dot_zero");
		cs._method("test_zero_dot_n1");
		cs._method("test_v1_dot_v2");
		cs._method("test_n1_dot_n2");

		classSchema cs2 = schema._class("GetVerticalTest");
		cs2._method("test_z_z");
		cs2._method("test_z_n");
		cs2._method("test_p_p");
		cs2._method("test_n_n");

		schema.check(collector);

		collector.print();
	}
}
