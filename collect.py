"""Fetch a bounded NYC 311 extract and export SQL results for BI tools."""
import argparse,csv,json,sqlite3,urllib.parse,urllib.request
p=argparse.ArgumentParser();p.add_argument('--start',default='2024-01-01');p.add_argument('--end',default='2024-02-01');p.add_argument('--limit',type=int,default=50000);a=p.parse_args()
params={'$select':'unique_key,borough,complaint_type,created_date','$where':f"created_date >= '{a.start}T00:00:00' AND created_date < '{a.end}T00:00:00'",'$order':'created_date,unique_key','$limit':a.limit}
url='https://data.cityofnewyork.us/resource/erm2-nwe9.json?'+urllib.parse.urlencode(params)
with urllib.request.urlopen(url,timeout=90) as response: rows=json.load(response)
with sqlite3.connect('data/311.sqlite') as db:
 db.execute('DROP TABLE IF EXISTS requests');db.execute('CREATE TABLE requests (unique_key TEXT PRIMARY KEY, borough TEXT, complaint_type TEXT, created_date TEXT)')
 db.executemany('INSERT INTO requests VALUES (?,?,?,?)',[(r['unique_key'],r.get('borough'),r.get('complaint_type'),r.get('created_date')) for r in rows]);result=db.execute(open('analysis.sql').read());
 with open('data/borough_complaints.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow([x[0] for x in result.description]);w.writerows(result)
print(f'Fetched {len(rows)} rows (limit {a.limit}); query window {a.start} through {a.end}, exclusive. Output data/borough_complaints.csv')
if len(rows)==a.limit: print('WARNING: limit reached; sample may omit later requests.')
