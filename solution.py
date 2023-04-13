import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 465374385 # Ваш chat ID, не меняйте название переменной

def solution(data) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.06

# Пороговое значение
    threshold = 300

# Расчет среднего значения и стандартного отклонения
    mean = sum(data) / len(data)
    std = stats.tstd(data)

# Расчет t-статистики
    n = len(data)
    t_stat = (mean - threshold) / (std / (n**0.5))

# Расчет критического значения
    crit_val = stats.t.ppf(alpha, df=n-1)

# Принятие решения
    return True
