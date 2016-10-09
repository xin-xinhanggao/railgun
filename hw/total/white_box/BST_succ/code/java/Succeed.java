public class Succeed {
    //find the succ of the node
	public BinNode getSucceed(BinNode node) {
		if (node.getRc() != null) {
			node = node.getRc();
			while (true) {
				if (node.getLc() != null)
					node = node.lc;
				else
					break;
			}
			return node;
		}
		BinNode y = node.getP();
		BinNode x = node;
		while (true) {
			if (y != null && x == y.getRc()) {
				x = y;
				y = y.getP();
			}
			else
				break;
		}
		return y;
	}
}
