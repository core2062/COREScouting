
import PythonLibrary.COREDependencies as COREDependencies
import PythonLibrary.CORETeamData as CORETeamData


class TeamData(CORETeamData.Team):

    """ use populate_data() to fill team_data with:
        Key - row name
        Value - calculation """

    def populate_data(self):

        """ Use Constants from RANK_AND_MATCH_HEADERS, MATCH_HEADERS, and RANK_ONLY_HEADERS when defining keys for team_data self.team_data[COREDependencies.COREConstants.REPORT_HEADER[0]] = 76
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[0])
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[2]] = self.return_best(COREDependencies.COREConstants.RADIO_NAMES[0], ('Moat', 'Rockwall', 'RoughTerrain'))
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[3]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[0])"""
        # Total amount of matches played
        MatchesPlayed = self.num_data_entries('MatchNumber')
        # Comments
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[0]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[1])
        # Average # of Balls in High Goal
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[0]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[1])
        # Average # of Balls in Low Goal
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[2])
        # Average # of Balls in High Goal Auton
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[2]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[3])
        # Average # of Balls in Low Goal Auton
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[3]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[4])
        # Average Climb Level
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[4]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[5])
        # Percent Move in Autonomous
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[0]] = self.times_key_exists_in_category('AutoStart', 'ON')# / MatchesPlayed