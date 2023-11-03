# programmers - 개인정보 수집(Level 1)
# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3

from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    terms_dict = {term.split(' ')[0]: int(term.split(' ')[1]) for term in terms}
    today_list = list(map(int, today.split('.')))
    today = dt(year=today_list[0], month=today_list[1], day=today_list[2])
    answer = []
    for index, privacy in enumerate(privacies):
        temp_date, term = privacy.split(' ')
        temp_date = list(map(int, temp_date.split('.')))
        date = dt(year = temp_date[0], month = temp_date[1], day = temp_date[2])
        expiration = date + relativedelta(months = terms_dict[term])
        if(expiration <= today): answer.append(index + 1) 
    return answer
