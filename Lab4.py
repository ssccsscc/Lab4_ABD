import pandas as pd
import numpy as np
import csv
import io
import re
import datetime
import dateutil

result = pd.read_csv("result.csv", sep=',', delimiter=",", index_col=[0], na_values=['NA'], low_memory=False)

def replace(what, wth):
    expr = re.compile(what, re.IGNORECASE)
    result["Vacancy Name"] = result["Vacancy Name"].apply(lambda x: expr.sub(wth,x))


result["Vacancy Name"] = result["Vacancy Name"].apply(lambda x: x.lower().strip())

replace('\s*-\s*', ' ')
replace('\s+$', '')
replace('\s+', ' ')
replace('\([^\)]*\)', '')
replace('\[[^\]]*\]', '')

replace('back end', 'backend')
replace('back-end', 'backend')
replace('бэкенд', 'backend')
replace('бэк-енд', 'backend')

replace('front end', 'frontend')
replace('front-end', 'frontend')
replace('фронтенд', 'frontend')
replace('фронт-енд', 'frontend')

replace('full stack', 'fullstack')
replace('full-stack', 'fullstack')
replace('фуллстек', 'fullstack')
replace('фулл-стек', 'fullstack')

replace('team leader', 'team lead')
replace('teamlead', 'team lead')
replace('тимлид', 'team lead')

replace('techlead', 'tech lead')
replace('техлид', 'tech lead')

replace('младший', 'junior')
replace('миддл', 'middle')
replace('мидл', 'middle')

replace('programmer', 'программист')
replace('manager', 'менеджер')
replace('developer', 'разработчик')
replace('адміністратор', 'администратор')
replace('аналітик', 'аналитик')
replace('artist', 'художник')
replace('animator', 'аниматор')
replace('web', 'вэб')
replace('analyst', 'аналитик')
replace('designer', 'дизайнер')
replace('гейм дизайнер', 'геймдизайнер')
replace('game designer', 'геймдизайнер')
replace('девопс', 'devops')
replace('2д', '2d')
replace('3д', '3d')

replace(' в .*', '')
replace('удаленно', '')
replace('удалённая', '')
replace('удалёнка', '')
replace('remote', '')

replace(',\s*', ' ')
replace('г\..*', ' ')

replace('\s*\|s*', '\\\\')
replace('\s*\\/\s*', '\\\\')
replace('\s*\\\\\s*', '\\\\')

replace('\s+$', '')
replace('\s+', ' ')

result["City"] = result["City"].fillna("Не указан")

result["Salary Min"] = result.groupby(["Vacancy Name", "City"])["Salary Min"].transform(lambda x: x.fillna(x.mean()))
result["Salary Max"] = result.groupby(["Vacancy Name", "City"])["Salary Max"].transform(lambda x: x.fillna(x.mean()))
result["Days"] = result["Date"].apply(lambda x: (datetime.datetime.now()-dateutil.parser.parse(x, ignoretz=True)).days)

result["Company Name"] = result["Company Name"].fillna("Не указано")
result["Expierence"] = result["Expierence"].fillna("Не требуется")
result["Employment"] = result["Employment"].fillna("Любой")
result["Schedule"] = result["Schedule"].fillna("Любой")
result["Description"] = result["Description"].fillna("")
result["Responsibility"] = result["Responsibility"].fillna("Нету")
result["Requirement"] = result["Requirement"].fillna("Нету")
result["Key Skills"] = result["Key Skills"].fillna("Нету")

result.to_csv("lab4-result.csv",  na_rep = 'NA', index=True, index_label="",quotechar='"',quoting=csv.QUOTE_NONNUMERIC, encoding="utf-8-sig")

print(result)