# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import httplib2
from xml.dom.minidom import parse
import xml.dom.minidom


# author: guojial@cn.ibm.com
# version: v1.06
# Date:   2017-10-27
# Last Modified by: rahul.kalluri@ibm.com
# Last Modified time: 2020-03-18

class ibmBluegroup:

    # check the user exist in group
    def userInGroup(self, intranetID, groupname):

        http = httplib2.Http()
        content = http.request(
            "https://bluepages.ibm.com/tools/groups/groupsxml.wss?task=listMembers&group=" + groupname, "GET")
        # print(content)

        DOMTree = xml.dom.minidom.parseString(content[1])
        collection = DOMTree.documentElement

        # print(collection.getElementsByTagName("member")[0].childNodes[0].data)
        flag = False
        for member in collection.getElementsByTagName("member"):
            if intranetID.lower() == member.childNodes[0].data.lower():
                flag = True
                break
            else:
                flag = False
        # print(flag)
        return flag

    def listMembers(self, groupname):

        http = httplib2.Http()
        content = http.request(
            "https://bluepages.ibm.com/tools/groups/groupsxml.wss?task=listMembers&group=" + groupname, "GET")
        # print(content)

        DOMTree = xml.dom.minidom.parseString(content[1])
        collection = DOMTree.documentElement

        # print(collection.getElementsByTagName("member")[0].childNodes[0].data)
        members = [];
        for member in collection.getElementsByTagName("member"):
            members.append(member.childNodes[0].data)
        # print(members)
        return members
