
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

COMPETITION_NAME = '2023_WILA' # name of DB

"""===========================================
Scout HTML input field names (form dependency)=
-------------------------------------------"""

#  form value name that contains the match and team number. (change second name)
TEAM_FIELD_NUMBER = {'team_number': 'TeamNumber'}
MATCH_NUMBER = {'match_number': 'MatchNumber'}

CHECKBOX_NAMES = [
    'AutoStart',
    'ScoredCones',
    'ScoredCubes',
    'FloorPickup',
    'HumanShelfPickup',
    'HumanFloorPickup',
]
NUMBER_NAMES = [
    MATCH_NUMBER['match_number'],
    'UpperLevel',
    'MiddleLevel',
    'LowerLevel',
    'UpperLevelAuton',
    'MiddleLevelAuton',
    'LowerLevelAuton',
    'ChargingStation',
    'ChargingStationAuton'

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
    'Avg High Level',
    'Avg Middle Level',
    'Avg Low Level',
    'Avg High Level Auton',
    'Avg Middle Level Auton',
    'Avg Low Level Auton',
    'Avg Charging Station',
    'Avg Charging Station Auton'
]

# Shows up as a ranking Option only
RANK_ONLY_HEADERS = [
    'Move In Auto',
    'Scored Cones',
    'Scored Cubes',
    'Floor Pickup',
    'Human Shelf Pickup',
    'Human Floor Pickup',
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
    ('UpperLevel', 'Avg High Goal', 'descending'),
    ('MiddleLevel', 'Avg middle Goal', 'descending'),
    ('LowerLevel', 'Avg Low Goal', 'descending'),
    ('ChargingStation', 'Avg Charging Station', 'descending'),
    ('AutoStart', 'Move In Auton', 'descending'),
    ('ScoredCones', 'Scored Cones', 'descending'),
    ('ScoredCubes', 'Scored Cubes', 'descending'),
    ('FloorPickup', 'Floor Pickup', 'descending'),
    ('HumanShelfPickup', 'Human Shelf Pickup', 'descending'),
    ('HumanFloorPickup', 'Human Floor Pickup', 'descending'),
    ('UpperLevelAuton', 'Avg High Goal Auton', 'descending'),
    ('MiddleLevelAuton', 'Avg Middle Goal Auton', 'descending'),
    ('LowerLevelAuton', 'Avg Low Goal Auton', 'descending'),
    ('ChargingStationAuton', 'Avg Charging Station Auton', 'descending')
]
