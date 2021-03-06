
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

COMPETITION_NAME = 'test'

"""===========================================
Scout HTML input field names (form dependency)
-------------------------------------------"""

#  form value name that contains the match and team number. (change second name)
TEAM_FIELD_NUMBER = {'team_number': 'TeamNumber'}
MATCH_NUMBER = {'match_number': 'MatchNumber'}

CHECKBOX_NAMES = [
    'Climb',
    'AutoStart',
    'ControlPanel1',
    'ControlPanel2'
]
NUMBER_NAMES = [
    MATCH_NUMBER['match_number'],
    'UpperPort',
    'LowerPort',
    'UpperPortAuton',
    'LowerPortAuton'

]
TEXT_NAMES = [
    'ScoutName',
    'comments'
]
RADIO_NAMES = [

]
RADIO_VALUES = {

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
    'Avg High Goal',
    'Avg Low Goal',
    'Avg High Goal Auton',
    'Avg Low Goal Auton',
    'Climbing Percentage',
    'Control Panel 1 Percentage',
    'Control Panel 2 Percentage'
]

# Shows up as a ranking Option only
RANK_ONLY_HEADERS = [
    'Move In Auto'
]

# Shows up on Match Report only
MATCH_HEADERS = [
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
    ('UpperPort', 'Avg High Goal', 'descending'),
    ('LowerPort', 'Avg Low Goal', 'descending'),
    ('Climb', 'Climbing Percentage', 'descending'),
    ('AutoStart', 'Move In Auton', 'descending'),
    ('ControlPanel1', 'Control Panel 1 Percentage', 'descending'),
    ('ControlPanel2', 'Control Panel 2 Peercentage', 'descending'),
    ('UpperPortAuton', 'Avg High Goal Auton', 'descending'),
    ('LowerPortAuton', 'Avg Low Goal Auton', 'descending'),
]