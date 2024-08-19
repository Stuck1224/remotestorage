import requests
headers = {
'Cookie':'lastCity=101040100; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1723884483; HMACCOUNT=A2B799B1EF4F0EE8; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1723884487; __zp_stoken__=fce8fMDDDncK2wrvCsz0hDwMBDg89KjcwJjYyMCQ%2BMTYwMDAzNDAwOBE6IMO6wrIyU8O3XcOHBD0lMDA%2BPTA%2BMDEwFTA8xLfCujExK8Kuwr8zXsO3XMOKAxIDKw5CA2Unw6DCsDoiwqDCvTc3PzYXwrPCmsK9w4vCv8Kawr3DisKzwpfCvTc3NjotM1AMDFMzN0VLUgVFWUpYX0kEQ05OJTYxMTAkZMO6KzIAAQ0AAAMCDgMDCgsHCwsODwMODgABDQAAKDHCnsK3wqgIw6HDjsO7xJHClknDs8K3wpvCsMKawqfCnEnCiEPCrMKqwoFswrhjwq9FSlvCq8KmwrHCpE9nRcK9bkjCqVDCu2JeSkZJYmFcZQ0LW1FfMw%2FDj8Ktw4A%3D; __c=1723884483; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3DPython%26city%3D101040100&s=3&friend_source=0&s=3&friend_source=0; __a=46472011.1723884483..1723884483.8.1.8.8',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=Python&city=101040100&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30'
response = requests.get(url=url,headers=headers)
json_data = response.json()
jobList = json_data['zpData']['jobList']
for job in jobList:
    jobName = job['jobName']
    salaryDesc= job['salaryDesc']
    cityName = job['cityName']
    jobDegree = job['jobDegree']
    print(jobName,salaryDesc,cityName,jobDegree)
