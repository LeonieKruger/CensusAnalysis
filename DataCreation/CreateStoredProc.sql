USE m5699140_aWare

DROP PROCEDURE dbo.uspGetCrimeCountTotal

CREATE PROCEDURE dbo.uspGetCrimeCountTotal
AS
SELECT 'HomeRobbery', count(case Q10cHomeRob  when 1 then 1 else null end)    FROM dbo.CRIME_STATS_2017
UNION
SELECT 'LivestockTheft', count(case Q10dLiveStck  when 1 then 1 else null end) FROM dbo.CRIME_STATS_2017
UNION
SELECT 'TheftOfCrop', count(case Q10eCrops when 1 then 1 else null end)  FROM dbo.CRIME_STATS_2017
UNION
SELECT 'Murder', count(case Q10fMurder  when 1 then 1 else null end)  FROM dbo.CRIME_STATS_2017
UNION
SELECT 'TraffickingInPersons', count(case Q10gTrafpersons when 1 then 1 else null end) FROM dbo.CRIME_STATS_2017
UNION
SELECT 'TheftOutOfMotorVehicle' ,count(case Q10hMVehicle when 1 then 1 else null end) FROM dbo.CRIME_STATS_2017
UNION
SELECT 'DamagingOfDwellings', count(case Q10iDamageDU when 1 then 1 else null end) FROM dbo.CRIME_STATS_2017
UNION
SELECT 'MotorVehicleVandalism',count(case Q10jDamageVeh when 1 then 1 else null end) FROM dbo.CRIME_STATS_2017
UNION
SELECT 'TheftOfBicycl',count(case Q10kTheftBic when 1 then 1 else null end)  FROM dbo.CRIME_STATS_2017
UNION
SELECT 'SexualOffence', count(case Q10mSexual when 1 then 1 else null end)   FROM dbo.CRIME_STATS_2017
UNION
SELECT 'Assualt' ,count(case Q10nAssault when 1 then 1 else null end) FROM dbo.CRIME_STATS_2017


EXEC dbo.uspGetCrimeCountTotal
