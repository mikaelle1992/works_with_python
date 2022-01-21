SELECT regiao as 'Regiao',
    sum(populacao) as Total
from estados
GROUP by regiao
order by Total desc


SELECT 
    sum(populacao) as Total
from estados


SELECT 
    avg(populacao) as Total
from estados