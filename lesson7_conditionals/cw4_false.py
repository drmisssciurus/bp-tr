"""
false:
-false
-''
-0
-None
-[]
-{}
-set()
"""

test = None
if not test:
	print("False1")
test = False
if not test:
	print("False2")
test = 0
if not test:
	print("False3")
test = ""
if not test:
	print("False4")
test = []
if not test:
	print("False5")
test = {}
if not test:
	print("False6")
test = set()
if not test:
	print("False7")

test = "d"
if test:
	print("True1")

test = 1
if  test:
	print("True2")

test = True
if  test:
	print("True3")

test = [2]
if  test:
	print("True4")

test = {"d"}
if  test:
	print("True5")

test = set(["1", "2", "3"])
if  test:
	print("True6")