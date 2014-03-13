# -*- coding: UTF-8 -*-
'''
Created on 2014-02-26

@author: Grayson
'''
import sys, os, traceback
sys.path.append(os.getcwd() + r'\..\Common')
import logFile


fieldName   = 0
CompMethod  = 1
CompValue   = 2
valueType   = 3
notation    = 4


def validityCheck(dbRecords, conditionDict, tableName):
  logHandle = logFile.LogFile(name = 'ValidityCheck')
  for record in dbRecords:
    for conditionItem in conditionDict[tableName]:
      if (conditionItem == []):
        continue
      #NULL值
      logStr = isNullCheck(record, tableName, conditionItem)
      if (logStr is not None):
        logHandle.logInfo(logStr)
        continue

      logStr = None
      #大于比较，比较对象包括整型、浮点型
      if (conditionItem[CompMethod] == '>'):
        logStr = gtCheck(record, tableName, conditionItem)
      #等于比较，比较对象包括整型、浮点型、字符串
      elif (conditionItem[CompMethod] == '=='):
        logStr = equalCheck(record, tableName, conditionItem)
      #非等于比较，比较对象包括整型、浮点型、字符串
      elif (conditionItem[CompMethod] == '!='):
        logStr = notEqualCheck(record, tableName, conditionItem)
      #小于比较，比较对象包括整型、浮点型
      elif (conditionItem[CompMethod] == '<'):
        logStr = ltCheck(record, tableName, conditionItem)
      #大于等于比较，比较对象包括整型、浮点型
      elif (conditionItem[CompMethod] == '>='):
        logStr = gteCheck(record, tableName, conditionItem)
      #小于等于比较，比较对象包括整型、浮点型
      elif (conditionItem[CompMethod] == '<='):
        logStr = (record, tableName, conditionItem)
      else:
        logStr = 'Invalid format.'
      #检测结果判定
      if (logStr is not None):
        logHandle.logInfo(logStr)
  logHandle.logInfo('Validity check complete, total check: ' + str(len(dbRecords)) + ' records.')


def isNullCheck(record, tableName, conditionItem):
  '''
  空值检测
  '''
  if (record[conditionItem[fieldName]] is None):
    logStr = '['+ str(tableName) +']' + str(conditionItem[fieldName]) +' is Null, ' + str(record)
    print logStr
    return logStr
  else:
    return None


def gtCheck(record, tableName, conditionItem):
  '''
  大于检测
  '''
  if (conditionItem[valueType] == 'int'):
    if (int(record[conditionItem[fieldName]]) > int(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' > ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  elif (conditionItem[valueType] == 'float'):
    if (float(record[conditionItem[fieldName]]) > float(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' > ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  else:
    logStr = 'Invalid value type.'
    return logStr


def equalCheck(record, tableName, conditionItem):
  '''
  等于检测
  '''
  if (conditionItem[valueType] == 'int'):
    if (int(record[conditionItem[fieldName]]) == int(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' == ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  elif (conditionItem[valueType] == 'float'):
    if (float(record[conditionItem[fieldName]]) - float(conditionItem[CompValue]) >  float(1e-7)) or \
       (float(record[conditionItem[fieldName]]) - float(conditionItem[CompValue]) <  -float(1e-7)):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' == ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  elif (conditionItem[valueType] == 'string'):
    if (str(record[conditionItem[fieldName]]) == str(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' == ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  else:
    logStr = 'Invalid value type.'
    return logStr


def notEqualCheck(record, tableName, conditionItem):
  '''
  非等于检测
  '''
  if (conditionItem[valueType] == 'int'):
    if (int(record[conditionItem[fieldName]]) != int(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' != ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  elif (conditionItem[valueType] == 'float'):
    if (float(record[conditionItem[fieldName]]) - float(conditionItem[CompValue]) <  float(1e-7)) and \
       (float(record[conditionItem[fieldName]]) - float(conditionItem[CompValue]) >  -float(1e-7)):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' != ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  elif (conditionItem[valueType] == 'string'):
    if (str(record[conditionItem[fieldName]]) != str(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' != ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  else:
    logStr = 'Invalid value type.'
    return logStr


def ltCheck(record, tableName, conditionItem):
  '''
  小于检测
  '''
  if (conditionItem[valueType] == 'int'):
    if (int(record[conditionItem[fieldName]]) < int(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' < ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  elif (conditionItem[valueType] == 'float'):
    if (float(record[conditionItem[fieldName]]) < float(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' < ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  else:
    logStr = 'Invalid value type.'
    return logStr


def gteCheck(record, tableName, conditionItem):
  '''
  大于或等于检测
  '''
  if (conditionItem[valueType] == 'int'):
    if (int(record[conditionItem[fieldName]]) >= int(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' >= ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  elif (conditionItem[valueType] == 'float'):
    if (float(record[conditionItem[fieldName]]) >= float(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' >= ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  else:
    logStr = 'Invalid value type.'
    return logStr


def lteCheck(record, tableName, conditionItem):
  '''
  小于或等于检测
  '''
  if (conditionItem[valueType] == 'int'):
    if (int(record[conditionItem[fieldName]]) <= int(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' <= ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  elif (conditionItem[valueType] == 'float'):
    if (float(record[conditionItem[fieldName]]) <= float(conditionItem[CompValue])):
      logStr = '['+ str(tableName) +']' + str(conditionItem[notation]) + ': ' + str(record[conditionItem[fieldName]]) + ' <= ' + str(conditionItem[CompValue]) + ', ' + str(record)
      return logStr
    else:
      return None
  else:
    logStr = 'Invalid value type.'
    return logStr
