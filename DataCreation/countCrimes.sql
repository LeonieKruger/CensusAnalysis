SELECT
count(case Q10bHous when 1 then 1 else null end) AS 'Housebreaking',
count(case Q10cHomeRob  when 1 then 1 else null end) AS 'Home robbery',
count(case Q10dLiveStck  when 1 then 1 else null end)  AS 'Livestock theft',
count(case Q10eCrops when 1 then 1 else null end) AS 'Theft of crop',
count(case Q10fMurder  when 1 then 1 else null end) AS 'Murder',
count(case Q10gTrafpersons when 1 then 1 else null end) AS 'Trafficking in persons',
count(case Q10hMVehicle when 1 then 1 else null end) AS 'Theft out of motor vehicle',
count(case Q10iDamageDU when 1 then 1 else null end) AS 'Damaging of dwellings',
count(case Q10jDamageVeh when 1 then 1 else null end) AS 'Motor vehicle vandalism',
count(case Q10kTheftBic when 1 then 1 else null end)  AS 'Theft of bicycl',
count(case Q10mSexual when 1 then 1 else null end) AS 'Sexual offence',
count(case Q10nAssault when 1 then 1 else null end) AS 'Assualt'
FROM dbo.CRIME_STATS_2017