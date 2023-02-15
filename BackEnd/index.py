import PythonLibrary.COREConstants

print("""<!DOCTYPE html>
<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]-->
<html class="no-js" lang="en" >

<head>
    <meta charset="utf-8">
    <link rel="shortcut icon" href="favicon.ico" />
    <meta name="description" content="CORE 2062 Scouting">
    <meta name="author" content="CORE2062">
    <meta name="robots" content="noindex, nofollow">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>CORE 2062 Scouting | Index</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" /> 
	<link rel="stylesheet" href="css/style.css">
    <!--<link rel="stylesheet" href="css/app.css">/-->
	
  

    <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" integrity="sha256-0rguYS0qgS6L4qVzANq4kjxPLtvnp5nn2nB5G1lWRv4=" crossorigin="anonymous"></script>

</head>
<body>
	<!-- <img src="images/header.png"> This for some reason failed to load on server -->
	
	<hr>
	<nav>
		<ul>
			<li><a href="index.html"><button class = "active">HOME</button></a></li>
			<li><a href="PythonLibrary/CORETeamSelect.py"><button>SCOUT FORM</button></a></li>
			<li><a href="PythonLibrary/COREMatchScheduleDisplay.py"><button>MATCH REPORT</button></a></li>
			<li><a href="GenerateRankingReport.html"><button>RANKING REQUEST</button></a></li>
			<li><a href="PythonLibrary/CORETeamReportDisplay.py"><button>TEAM ANALYSIS</button></a></li>
		</ul>
	</nav>
	<h1>CORE Scouting</h1>
	<div>
		<p>This is the CORE 2062 scouting homepage</p>
	</div>
	<div class="sched">
		<h1>CORE 2062 Schedule</h1>
		<!-- replace w/ table of events -->
		<!-- Will be changed to pull from database for our schedule -->""")
print("""		<table>
			<tr>
		    <th>Match Number</th>
		    <th>Blue 1</th>
		    <th>Blue 2</th>
				<th>Blue 3</th>
		    <th>Red 2</th>
				<th>Red 1</th>
		    <th>Red 3</th>
		  </tr>""")
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
print("""	</div>
	
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity="sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>
  <script>
    $(document).foundation();
  </script>
</body>
<footer>
	<p>
		This page was made for the CORE 2062 scouting team for use in the 2023 season.
	</p>
</footer>
</html>""") # taken from replit testing @ https://replit.com/@necromacers2nd/test-1#index.html

