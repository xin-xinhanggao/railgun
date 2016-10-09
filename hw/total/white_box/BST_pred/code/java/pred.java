public class pred {
	public BinNode findPred(BinNode node) {
		if (node.has_lc()) {
			node = node.lc;
			while (true) {
				if (node.has_rc())
					node = node.rc;
				else
					break;
			}
			return node;
		}
		BinNode y = node.p;
		BinNode x = node;
		while (true) {
			if (y != null && x == y.lc) {
				x = y;
				y = y.p;
			}
			else
				break;
		}
		return y;
	}	
}
