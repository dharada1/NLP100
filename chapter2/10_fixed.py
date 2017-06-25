# -*- coding: utf-8 -*-

import sys

#withをつかうとブロック終了時に必ずcloseしてくれる
#sys.argv[1]は第1引数

with open(sys.argv[1]) as f:
	print len(f.readlines())
