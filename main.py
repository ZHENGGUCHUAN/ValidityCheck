# -*- coding: UTF-8 -*-
'''
Created on 2014-02-25

@author: Grayson
'''
import traceback, sys, os, datetime, time, sched
import validityCheck
sys.path.append(os.getcwd() + r'\..\Common')
import operateFile, readDbInfo, dbServer, heartBeat


def execValidityCheck():
  conditionFile = operateFile.OperateFile('condition.txt')
  conditionDict = conditionFile.readItem2List()
  mssql = readDbInfo.ReadDbInfo(dbServer.mssqlDbServer['46']['LAN'])
  for tableName in conditionDict:
    dbRecords = mssql.query(str(tableName))
    validityCheck.validityCheck(dbRecords, conditionDict, tableName)


if __name__ == '__main__':
  try:
    heartBeatHandle = heartBeat.HeartBeat(name = 'ValidityCheck', interval = 60 * 60)
    heartBeatHandle.startThread()
    #execValidityCheck()
    while True:
      #Get date time now
      timetuple = datetime.datetime.now().timetuple()
      #Set execute time 00:00:00 every morning.
      executeTime = datetime.datetime(timetuple.tm_year, timetuple.tm_mon, timetuple.tm_mday, 0)
      #If date time now great than 00:00:00, set next execute time at 06:00:00 tomorrow morning.
      if timetuple.tm_hour >= 0:
        executeTime += datetime.timedelta(days=1)
        print("Next execute(sync multiple close price) time: %s" % executeTime.strftime("%Y-%m-%d %X"))
      #Get delta time within next execute time and date time now.
      deltaTime = executeTime - datetime.datetime.now()
      print("Delta time: %f (seconds)" % deltaTime.total_seconds())

      updateScheduler = sched.scheduler(time.time, time.sleep)
      #schedule run
      updateScheduler.enter(deltaTime.total_seconds(), 1, execValidityCheck, ())
      updateScheduler.run()
    print 'All correct!'
  except:
    print traceback.format_exc()
