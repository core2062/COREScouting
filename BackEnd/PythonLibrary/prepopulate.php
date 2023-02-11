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
                          						<label>Items Scored on the lower level in Autonomous:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("LowerLevelAuton").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="LowerLevelAuton" id="LowerLevelAuton" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("LowerLevelAuton").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
										</div> 
										<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Items Scored on the middle level in Autonomous:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("MiddleLevelAuton").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="MiddleLevelAuton" id="MiddleLevelAuton" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("MiddleLevelAuton").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
										  </div>
										<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Items Scored on the high level in Autonomous:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("UpperLevelAuton").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="UpperLevelAuton" id="UpperLevelAuton" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("UpperLevelAuton").stepUp(1);' value='+'/>
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
                          						<label>Items Scored on the lower level:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("LowerLevel").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="LowerLevel" id="LowerLevel" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("LowerLevel").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>

										<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Items Scored on the middle level:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("MiddleLevel").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="MiddleLevel" id="MiddleLevel" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("MiddleLevel").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>

									<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Items Scored on the high level:</label>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("UpperLevel").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           								 <input required type="number" name="UpperLevel" id="UpperLevel" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("UpperLevel").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>
								<fieldset>
									<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Charging station:</label>
                        							<!--
													<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("ClimbLevel").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           								 <input required type="number" name="ClimbLevel" id="ClimbLevel" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("ClimbLevel").stepUp(1);' value='+'/>
													</div>
													-->
													<div class="climber-radio">
														<input type="radio" id="Level 0" name="ClimbLevel" value="0" checked>
														<label for="Level 0">Not Docked</label>
														<input type="radio" id="Level 1" name="ClimbLevel" value="1">
														<label for="Level 1">Docked and not Engaged</label>
														<input type="radio" id="Level 2" name="ClimbLevel" value="2">
														<label for="Level 2">Docked and Engaged</label>
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