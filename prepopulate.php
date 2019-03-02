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
                          						<label>Hatches Scored in Autonomous:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("HatchAuton").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="HatchAuton" id="HatchAuton" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("HatchAuton").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
										</div> 
										<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Cargo Scored in Autonomous:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("CargoAuton").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="CargoAuton" id="CargoAuton" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("CargoAuton").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
										  </div>
										  
										  <fieldset>
                                    <legend>Autonomous Starting Level:</legend>
                                    <div class="row">
                                        <input required="" name="AutoStart" id="1stLevel" value="1stLevel" type="radio"><label for="1stLevel">1st Level Start</label>
                                        <input required="" name="AutoStart" id="2ndLevel" value="2ndLevel" type="radio"><label for="2ndLevel">2nd Level Start</label>
                                        <input required="" name="AutoStart" id="Fail" value="Fail" type="radio"><label for="Fail">Fail</label>
                                        <input required="" name="AutoStart" id="NoAttempt" value="NoAttempt" type="radio"><label for="NoAttempt">No Attempt</label>
                                        <!-- <legend>Assisted Robots with Climb:</legend>
                                        <input name="ClimbAssist" id="ClimbAssist" type="checkbox"><label for="ClimbAssist">Climb Assist?</label> -->
                                    </div>
								</fieldset>
      								</div>
								  </div>

      					<a href="#panel3" class="show-for-small-only">Teleoperated Period</a>
      						<div id="panel3" class="content">
      							<div class="content-box section-box">

                   					<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>High Level Hatches Scored:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("HighHatch").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="HighHatch" id="HighHatch" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("HighHatch").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>

									<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Medium Level Hatches Scored:</label>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("MediumHatch").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           								 <input required type="number" name="MediumHatch" id="MediumHatch" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("MediumHatch").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>


                   					<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                                                <label>Low Level Hatches Scored:</label>
                                                <div class="small-4 columns">
                                                    <input required type='button' class="button postfix" onclick='document.getElementById("LowHatch").stepDown(1);' value='-'/>
                                                </div>
                                                <div class="small-4 columns">
                                                     <input required type="number" name="LowHatch" id="LowHatch" min="0" step="1" value ="0" required readonly>
                                                </div>
                                                <div class="small-4 columns">
                                                <input required type='button' class="button postfix" onclick='document.getElementById("LowHatch").stepUp(1);' value='+'/>
                                                </div>
                                 			</div>
                   				 		</div>
                  					</div>
                                    <div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                                                <label>High Level Cargo Scored:</label>
                                                <div class="small-4 columns">
                                                    <input required type='button' class="button postfix" onclick='document.getElementById("HighCargo").stepDown(1);' value='-'/>
                                                </div>
                                                <div class="small-4 columns">
                                                     <input required type="number" name="HighCargo" id="HighCargo" min="0" step="1" value ="0" required readonly>
                                                </div>
                                                <div class="small-4 columns">
                                                <input required type='button' class="button postfix" onclick='document.getElementById("HighCargo").stepUp(1);' value='+'/>
                                                </div>
                                 			</div>
                   				 		</div>
									  </div>
									  <div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                                                <label>Medium Level Cargo Scored:</label>
                                                <div class="small-4 columns">
                                                    <input required type='button' class="button postfix" onclick='document.getElementById("MediumCargo").stepDown(1);' value='-'/>
                                                </div>
                                                <div class="small-4 columns">
                                                     <input required type="number" name="MediumCargo" id="MediumCargo" min="0" step="1" value ="0" required readonly>
                                                </div>
                                                <div class="small-4 columns">
                                                <input required type='button' class="button postfix" onclick='document.getElementById("MediumCargo").stepUp(1);' value='+'/>
                                                </div>
                                 			</div>
                   				 		</div>
									  </div>
									  <div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                                                <label>Low Level Cargo Scored:</label>
                                                <div class="small-4 columns">
                                                    <input required type='button' class="button postfix" onclick='document.getElementById("LowCargo").stepDown(1);' value='-'/>
                                                </div>
                                                <div class="small-4 columns">
                                                     <input required type="number" name="LowCargo" id="LowCargo" min="0" step="1" value ="0" required readonly>
                                                </div>
                                                <div class="small-4 columns">
                                                <input required type='button' class="button postfix" onclick='document.getElementById("LowCargo").stepUp(1);' value='+'/>
                                                </div>
                                 			</div>
                   				 		</div>
								<fieldset>
                                    <legend>Climbing:</legend>
                                    <div class="row">
                                        <input required="" name="Climb" id="NoClimb" value="NoClimb" type="radio"><label for="NoClimb">No Climb</label>
                                        <input required="" name="Climb" id="1stLevel" value="1stLevel" type="radio"><label for="1stLevel">1st Level Climb</label>
                                        <input required="" name="Climb" id="2ndLevel" value="2ndLevel" type="radio"><label for="2ndLevel">2nd Level Climb</label>
                                        <input required="" name="Climb" id="3rdLevel" value="3rdLevel" type="radio"><label for="3rdLevel">3rd Level Climb</label>
                                        <input required="" name="Climb" id="ClimbFail" value="ClimbFail" type="radio"><label for="ClimbFail">Failed Climb</label>
                                        <!-- <legend>Assisted Robots with Climb:</legend>
                                        <input name="ClimbAssist" id="ClimbAssist" type="checkbox"><label for="ClimbAssist">Climb Assist?</label> -->
                                    </div>
								</fieldset>
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