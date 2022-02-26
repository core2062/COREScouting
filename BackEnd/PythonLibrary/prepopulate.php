<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
		<title>CORE 2062 Scouting</title>
		<link rel="shortcut icon" href="favicon.ico" />
		<meta name="description" content="CORE 2062 Scouting Form">
    	<meta name="author" content="CORE2062">
    	<meta name="robots" content="noindex, nofollow">

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />

		<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity="sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation/foundation.accordion.min.js" integrity="sha256-Sf8QyM10GIsdziOWIIfN7V/ah4iRxPt17tvNCHorXjc=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation/foundation.tab.min.js" integrity="sha256-Qyd0HGGzEOB/qkGWHkxliFbXHCjs2VRDm8mzHEwphzk=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/awesomplete/1.1.1/awesomplete.min.js" integrity="sha256-hQ2PYbQiQS3xeguwt5BS+AMzn5V5JJ0P1kQnuoXdTnk=" crossorigin="anonymous"></script>

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/awesomplete/1.1.1/awesomplete.min.css" integrity="sha256-pMulKeKs7Hns5vhu0uluhawM68QSrKg/dFfttaXCKE8=" crossorigin="anonymous" />

		<script src="https://cdnjs.cloudflare.com/ajax/libs/parsley.js/2.6.2/parsley.min.js" integrity="sha256-QKOftzbqahZaXS2amOh27JacZ6TbmT4TmGxNo4Jue4Y=" crossorigin="anonymous"></script>

		<script type="text/javascript" src="show.js?v=1"></script>

	</head>
	<body>

		<form name="main" id="form" action="COREDataEntry.py" method="post" data-parsley-validate>
			<div class="row">
				<div class="small-12 columns">
					<ul class="tabs show-for-medium-up" data-tab>
						<li class="tab-title active"><a href="#panel1">Match/Scout Info</a></li>
      					<li class="tab-title"><a href="#panel2">Autonomous Period</a></li>
      					<li class="tab-title"><a href="#panel3">Teleoperated Period</a></li>
      				</ul>
      				<dl class="accordion" data-accordion>
      					<dd class="accordion-navigation">
      					
      					<a href="#panel1" class="show-for-small-only">Match/Scout Info</a>
      						<div id="panel1" class="content active">
      							<div class="content-box section-box">
      								<div class="row">
      									<div class="small-12 columns">
      										<label>Match Number: *
											  <input  name="MatchNumber" class="form-control" type="number" placeholder="1" value="<?php echo $_GET['match']; ?>" required="" readonly/>
											</label>
										</div>
									</div>

									<div class="row">
										<div class="small-12 columns">
											<label>Team Number: *
												<input name="TeamNumber" class="form-control" type="number" value="<?php echo $_GET['team']; ?>" required="" placeholder="2062" readonly/>
											</label>
										</div>
									</div>

									<div class="row">
										<div class="small-12 columns">
											<label>Scout Name: *
												<input name="ScoutName" placeholder="John Smith" autocomplete="off" data-parsley-required="true"/>
											</label>
										</div>
									</div>
								</div>
							</div>

							<a href="#panel2" class="show-for-small-only">Autonomous Period</a>
	        					<div id="panel2" class="content">
	        						<div class="content-box section-box">
									<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Low Balls Scored in Autonomous:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("LowerHubAuton").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="LowerHubAuton" id="LowerHubAuton" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("LowerHubAuton").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
										</div> 
										<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>High Balls Scored in Autonomous:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("UpperHubAuton").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="UpperHubAuton" id="UpperHubAuton" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("UpperHubAuton").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
										  </div>
										  							
                                        <input name="AutoStart" id="AutoStart" type="checkbox"><label for="AutoStart">Moved in Auto?</label>
      								</div>
								  </div>

      					<a href="#panel3" class="show-for-small-only">Teleoperated Period</a>
      						<div id="panel3" class="content">
      							<div class="content-box section-box">

                   					<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Low Balls Scored:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("LowerHub").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="LowerHub" id="LowerHub" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("LowerHub").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>

									<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>High Balls Scored:</label>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("UpperHub").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           								 <input required type="number" name="UpperHub" id="UpperHub" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("UpperHub").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>
								<fieldset>
									<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Climb height:</label>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("ClimbLevel").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           								 <input required type="number" name="ClimbLevel" id="ClimbLevel" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("ClimbLevel").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>
								</fieldset>
								</div>
      						</div>
                            <div class="row">
                           		<div class="large-12 columns">
                            		<label>Comments
                                		<textarea name="comments" placeholder=""></textarea>
                            		</label>
                            </div>
							<input class="button round SubmitButton" type="submit" value="Submit">
					</dl>
        </form>
<script>
      $(document).foundation();
</script>
<script type="text/javascript">
  $('#form').parsley();
</script>
	</body>
</html>     												