public class Splay {
	public String splay(BinNode v) {
		if (v == null)
			return "None";
		BinNode p = v.getP();
		BinNode g;
		if (p != null)		
			g = p.getP();
		else
			g = null;
		BinNode gg;
		if (g != null)
			gg = g.getP();
		else
			gg = null;
		if (gg != null)
			return "root";
		if (v.is_lc() && p != null)
			if (p.is_lc())
				return "zig-zig";
			else
				return "zig-zag";
		else if (p != null && p.is_rc())
			return "zag-zag";
		else
			return "zag-zig";
	}
}
