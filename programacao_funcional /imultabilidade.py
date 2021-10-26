from functools import reduce
from calendar import mdays, month_name
from functools import reduce


meses = filter(lambda m: mdays[m] == 31, range(1, 13))
mes = map(lambda mes: month_name[mes], meses)
todos_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}', mes, " Meses com 31 dias" )

print(todos_meses)

print(
    reduce(
            lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
            map(
                lambda mes: month_name[mes],
                filter(lambda m: mdays[m] == 31, range(1, 13))
            ),
            " Meses com 31 dias!"
    )
)

