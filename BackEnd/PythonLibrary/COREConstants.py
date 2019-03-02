
""" Various constants used throughout the program that are intended primarily to map form fields,
    but also for key names

        form dependency : Needs to be the same names as those given by the html form.
            It is important that these names appear EXACTLY the same as those supplied by the front end!
        no dependency : Names that will be visually displayed on output tables.
            Should be named in accordance of which they are displaying, but the name is not dependant on any
            other input or variable names"""

"""===========================================
General Team Info (no dependency)
-------------------------------------------"""

TEAM_NUMBER = 2062

COMPETITION_NAME = 'week0Test'

"""===========================================
Scout HTML input field names (form dependency)
-------------------------------------------"""

#  form value name that contains the match and team number. (change second name)
TEAM_FIELD_NUMBER = {'team_number': 'TeamNumber'}
MATCH_NUMBER = {'match_number': 'MatchNumber'}

CHECKBOX_NAMES = [
    # 'ClimbAssist'
]
NUMBER_NAMES = [
    MATCH_NUMBER['match_number'],
    'HighHatch',
    'MediumHatch',
    'LowHatch',
    'HighCargo',
    'MediumCargo',
    'LowCargo', 
    'HatchAuton',
    'CargoAuton'
]
TEXT_NAMES = [
    'ScoutName',
    'comments'
]
RADIO_NAMES = [
    'Climb',
    'AutoStart',
    'EndLevel' 
    # 'HatchAuton',
    # 'CargoAuton',
]
RADIO_VALUES = {
    'Climb': ('NoClimb', '1stLevel', '2ndLevel', '3rdLevel', 'ClimbFail'),
    'AutoStart': ('1stLevel', '2ndLevel', 'Fail', 'NoAttempt'),
    'EndLevel': ('Failed', '1stLevel', '2ndLevel', '3rdLevel', 'None')
    # 'HatchAuton': ('Successful', 'Fail', 'NoAttempt'),
    # 'CargoAuton': ('Successful','Fail','NoAttempt'),

}

ALL_NAMES = []

for checkbox in CHECKBOX_NAMES:
    ALL_NAMES.append(checkbox)
for number in NUMBER_NAMES:
    ALL_NAMES.append(number)
for text in TEXT_NAMES:
    ALL_NAMES.append(text)
for radio in RADIO_NAMES:
    ALL_NAMES.append(radio)

"""=====================================
Match Report Row Headers (no dependency)
-------------------------------------"""


# Show up on Match Report and Ranking Report if applicable
RANK_AND_MATCH_HEADERS = [
    # 'Crossed Baseline Percentage',
    # 'Avg Cubes Delivered: Home Switch',
    # 'Avg Cubes Delivered: Scale',
    # 'Avg Cubes Delivered: Opposing Switch',
    # 'Avg Cubes Delivered: Exchange',
    # 'Hatch Auton, Successful Hatch : Fail : No Attempt',
    # 'Cargo Auton, Successful Cargo: Fail : No Attempt',
    'Avg Hatches Auton',
    'Avg Cargo Auton'

]

# Shows up as a ranking Option only
RANK_ONLY_HEADERS = [
    'Avg High Hatch',
    'Avg Medium Hatch',
    'Avg Low Hatch',
    'Avg High Cargo',
    'Avg Medium Cargo',
    'Avg Low Cargo',
    'Climbing Percentage'
    #'ClimbAssist'
]

# Shows up on Match Report only
MATCH_HEADERS = [
    'Climb, 1st Level : 2nd Level : 3rd Level : Fails : None',
    'Avg Cargo',
    'Avg Hatches',
    'Comments'
]


"""=============================================
Match Report input field names (form dependency)
---------------------------------------------"""

RANK_REPORT_FIELD_NAMES = {
    'ranking_options': 'ranking_type'
}

""" The following describes how to use RANK_OPTIONS to map form values to rank statistics.
    it should be a list of tuples that have the following data in them (IN ORDER).

        1. Form value name of RANK_REPORT_FIELD_NAMES['ranking_options'] that you wish to
            correspond the ranking to. (The ranking report form value)
        2. Name of statistic to rank by from RANK_AND_MATCH_HEADERS or RANK_ONLY_HEADERS
        3. Order in which teams should be ranked. The following are accepted
                'descending' - Ranking from best to worst
                'ascending' - Ranks from worst to best
                'category' - Ranks based on multiple strings given a 3'd argument.
        (4). (ORDER SPECIFIC ARGUMENT) Should only be supplied if order is 'category'.
            A tuple of all possible submission data for the supplied rank_statistic
            category corresponding to the statistic's RADIO_VALUES values in order of
            which should be displayed last, worst -> best.
            Intended to be used for ranking based on a priority of strings.
    EX: 'High Goal Accuracy': ('highGoals', 'high Goal Accuracy', 'descending')
    EX: 'Highest Auto Type': ('highest_auto_type', 'Highest Auto', 'category', ('breach', 'reach', 'no_interaction')) """

RANK_OPTIONS = [
    # EXAMPLE     ('Defense', 'Defense Rating', 'category', ('Amazing', 'Good', 'Alright', 'Not Great')) (Also can look above for example^^^
    # ('ClimbPercentage', 'Climbing Percentage', 'descending'),
    # ('AutoSwitchPercent', 'Auto Switch Percentage', 'descending'),
    # ('AutoScalePercent', 'Auto Scale Percentage', 'descending'),
    # ('AutoExchangePercent', 'Auto Exchange Percentage', 'descending'),
    # ('CrossBaselinePercent', 'Crossed Baseline Percentage', 'descending'),
    # ('AvgTeleCubesHSwitch', 'Avg Cubes Delivered: Home Switch', 'descending'),
    # ('AvgTeleCubesOSwitch', 'Avg Cubes Delivered: Opposing Switch', 'descending'),
    # ('AvgTeleCubesScale', 'Avg Cubes Delivered: Scale', 'descending'),
    # ('AvgTeleCubesExchange', 'Avg Cubes Delivered: Exchange', 'descending'),
    ('HighHatch', 'Avg High Hatch', 'descending'),
    ('MediumHatch', 'Avg Medium Hatch', 'descending'),
    ('LowHatch', 'Avg Low Hatch', 'descending'),
    ('HighCargo', 'Avg High Cargo', 'descending'),
    ('MediumCargo', 'Avg Medium Cargo', 'descending'),
    ('LowCargo', 'Avg Low Cargo', 'descending'),
    ('HatchAuton', 'Avg Hatches Auton','descending'),
    ('CargoAuton', 'Avg Cargo Auton','descending'),
    ('ClimbPercentage', 'Climbing Percentage','descending')

    
    

]