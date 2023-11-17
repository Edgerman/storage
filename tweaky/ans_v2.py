import json
import requests

# test_id = 152779160
# bear_id = "eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyMjQzMDE2NzYiLCJUZW5hbnRJZCI6MiwiUm9sZU5hbWUiOiJTdHVkZW50IiwiREJJZCI6IjM0NDU4NzQiLCJGaXJzdE5hbWUiOiJBQUtBU0giLCJUZW5hbnRDb2RlIjoic3JpY2hhaXRhbnlhIiwiTGFzdE5hbWUiOiJBIiwiZXhwIjoxNjk4OTQyNTg4LCJSb2xlSWQiOiIxIiwiaWF0IjoxNjk4ODU2MTg4fQ.sJ7nYp_BeQ9VqaqJpFDgpFmPvipqdaCFBgqTB8SuE20"

test_id = 171672561
bear_id = "eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyMjQzMDE2NzYiLCJUZW5hbnRJZCI6MiwiUm9sZU5hbWUiOiJTdHVkZW50IiwiREJJZCI6IjM0NDU4NzQiLCJGaXJzdE5hbWUiOiJBQUtBU0giLCJUZW5hbnRDb2RlIjoic3JpY2hhaXRhbnlhIiwiTGFzdE5hbWUiOiJBIiwiZXhwIjoxNzAwMzA3ODUxLCJSb2xlSWQiOiIxIiwiaWF0IjoxNzAwMjIxNDUxfQ.l-KXs-y22EgyxZfZjjbxr2DKmzRKfEYzvMymq-qu4fw"

def parseit(js):
	print('\n\n',js['testName'])
	ans = js['scheduleTest'][0]['subjectStructures']
	count=1
	for sub in ans:
		print('\n', sub['subjectName'])
		for sec in sub['sections']:
			print('\t', sec['sectionName'], ' - ', sec['questionListDetails'][0]['question_type'])
			for ques in sec['questionListDetails']:
				print('\t\t',count,'\b) ',ques['question_data']['question']['correct_answer'])
				count=count+1
	print('\n')

url = f"https://prodslms.ilteacher.com/v2/test/getStudentTestDetails?studentTestId={test_id}&platform=WEB&platformVersion=Chrome%20110"
headers = {
		"Host": "prodslms.ilteacher.com",
		"Sec-Ch-Ua": '"Not A(Brand";v="24", "Chromium";v="110"',
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"Sec-Ch-Ua-Mobile": "?0",
		"Authorization": f"Bearer {bear_id}",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36",
		"Sec-Ch-Ua-Platform": '"Linux"',
		"Origin": "https://srichaitanyameta.com",
		"Sec-Fetch-Site": "cross-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://srichaitanyameta.com",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

if response.status_code==200:
	print('Json extraction initiated')
	try:
		parseit(json.loads(response.text))
	except:
		print("Response Content:", response.text)
elif response.status_code==401:
	print("Response Content:", response.text)

input("\nPress Enter to Exit")
