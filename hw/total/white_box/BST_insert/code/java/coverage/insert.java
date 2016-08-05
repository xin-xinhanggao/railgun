public class insert {
	public boolean insert(Tree T, BinNode z) {
		BinNode now = T.root;
		if (now == null) {
			T.root = z;
			return true;
		}
		BinNode parent = now;
		while (now != null) {
			parent = now;
			if (now.v > z.v)
				now = now.lc;
			else if (now.v < z.v)
				now = now.rc;
			else
				return false;
		}
		z.set_p(parent);
		if (parent.v > z.v)
			parent.lc = z;
		else
			parent.rc = z;
		return true;
	}
}
