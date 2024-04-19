SELECT 
    INS.ANIMAL_ID,
    INS.NAME
FROM ANIMAL_INS AS INS
JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY DATEDIFF(OUTS.DATETIME, INS.DATETIME) DESC
LIMIT 2
;
