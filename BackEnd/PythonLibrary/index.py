import COREConstants

print('<!DOCTYPE html>')
print('<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]-->')
print('<html class="no-js" lang="en" >')

print('<head>')
print('<meta charset="utf-8">')
print('<link rel="shortcut icon" href="favicon.ico" />')
print('<meta name="description" content="CORE 2062 Scouting">')
print('<meta name="author" content="CORE2062">')
print('<meta name="robots" content="noindex, nofollow">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />')
print('<title>CORE 2062 Scouting | Index</title>')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" /> ')
print('<link rel="stylesheet" href="css/style.css">')
print('<!--<link rel="stylesheet" href="css/app.css">/-->')



print('<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" integrity="sha256-0rguYS0qgS6L4qVzANq4kjxPLtvnp5nn2nB5G1lWRv4=" crossorigin="anonymous"></script>')

print('</head>')
print('<body>')
print('<!-- <img src="images/header.png"> This for some reason failed to load on server -->')

print('<hr>')
print('<nav>')
print('<ul>')
print('<li><a href="index.html"><button class = "active">HOME</button></a></li>')
print('<li><a href="PythonLibrary/CORETeamSelect.py"><button>SCOUT FORM</button></a></li>')
print('<li><a href="PythonLibrary/COREMatchScheduleDisplay.py"><button>MATCH REPORT</button></a></li>')
print('<li><a href="GenerateRankingReport.html"><button>RANKING REQUEST</button></a></li>')
print('<li><a href="PythonLibrary/CORETeamReportDisplay.py"><button>TEAM ANALYSIS</button></a></li>')
print('</ul>')
print('</nav>')
print('<h1>CORE Scouting</h1>')
print('<div>')
print('<p>This is the CORE 2062 scouting homepage</p>')
print('</div>')
print('<div class="sched">')
print('<h1>CORE 2062 Schedule</h1>')
print('<!-- replace w/ table of events -->')
print('<!-- Will be changed to pull from database for our schedule -->')
print('<table>')
print('<tr>')
print('<th>Match Number</th>')
print('<th>Blue 1</th>')
print('<th>Blue 2</th>')
print('<th>Blue 3</th>')
print('<th>Red 2</th>')
print('<th>Red 1</th>')
print('<th>Red 3</th>')
print('</tr>')
for index,match in enumerate(COREConstants.COREMatchSchedule.SCHEDULE): # looks through entire schedule and finds matches with us in it
    if COREDependencies.COREConstants.TEAM_NUMBER in match:
        print("<tr>")
		print(f'<td>{index}</td>')
		for team in match:
            if team != COREDependencies.COREConstants.TEAM_NUMBER:
                print(f'<td>{team}</td>')
            else:
                print(f'<td class="us">{team}</td>')
        print("</tr>")
print("\t\t</table>")
print('</div>')

print('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity="sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>')
print('<script>')
print('$(document).foundation();')
print('</script>')
print('</body>')
print('<footer>')
print('<p>')
print('This page was made for the CORE 2062 scouting team for use in the 2023 season.')
print('</p>')
print('</footer>')
print('</html>') # taken from replit testing @ https://replit.com/@necromacers2nd/test-1#index.html

