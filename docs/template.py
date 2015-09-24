#!/usr/bin/env python
# coding: utf-8
from pocsuite.net import req
from pocsuite.poc import POCBase, Output
from pocsuite.utils import register


class TestPOC(POCBase):
    vulID = ''  # ssvid
    version = ''
    author = ['']
    vulDate = ''
    createDate = ''
    updateDate = ''
    references = ['']
    name = ''
    appPowerLink = ''
    appName = ''
    appVersion = ''
    vulType = ''
    desc = ''''''
    samples = ['']

    def _attack(self):
        result = {}
        #Write your code here

        return self.parse_output(result)

    def _verify(self):
        result = {}
        #Write your code here

        return self.parse_output(result)

    def parse_output(self, result):
        #parse output
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('Internet nothing returned')
        return output


register(TestPOC)
