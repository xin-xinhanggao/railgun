public class remove {
	public String remove(BinNode x) {
		if (!x.has_lc())
			return "rChild";
		else if (!x.has_rc())
			return "lChild";
		else {
			if (x.p == null)
				return "x.rChild";
			else {
				BinNode w = x.succ();
				BinNode u = w.p;
				if (u == x)
					return "u.rChild";
				else
					return "u.lChild";
			}
		}
	}
}
