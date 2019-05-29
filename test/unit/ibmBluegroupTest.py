#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from ibmBluegroup import ibmBluegroup

import unittest
class ibmBluegroupTestCase(unittest.TestCase):

	def testUserInGroup(self):
		self.assertEqual(ibmBluegroup.userInGroup(self, "guojial@cn.ibm.com", "CDL-DSE-webtool"), False)
		self.assertEqual(ibmBluegroup.userInGroup(self, "guojial@cn.ibm.com", "CDL-DSE-Emtech"), True)

	def testListMembers(self):
		print(ibmBluegroup.listMembers(self, "CDL-DSE-Emtech"))
		self.assertEqual(ibmBluegroup.listMembers(self, "CDL-DSE-Emtech")[0], "guojial@cn.ibm.com")

if __name__ == "__main__":
    unittest.main()