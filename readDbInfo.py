# -*- coding: UTF-8 -*-
'''
Created on 

@author: Grayson
'''
import sys, os
sys.path.append(os.getcwd() + r'\..\Common')
import mssqlAPI


class ReadDbInfo(object):
  '''
  读取MS SQL数据库数据信息
  '''

  def __init__(self, mssqlDict):
    self.mssqlHandle = mssqlAPI.MssqlAPI(mssqlDict['SERVER'], mssqlDict['DB'], mssqlDict['USER'], mssqlDict['PWD'])


  def __del__(self):
    del self.mssqlHandle


  def query(self, name):
    sqlCmd = 'SELECT top 10000 * FROM ' + name
    queryResult = self.mssqlHandle.sqlQuery(sqlCmd)
    return queryResult
