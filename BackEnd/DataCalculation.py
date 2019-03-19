
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
        #Average High Hatch 
        AverageHighHatch = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[1])
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[0]] = AverageHighHatch
        #Average Medium Hatch
        AverageMediumHatch = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[2])
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[1]] = AverageMediumHatch
        #Average Low Hatch
        AverageLowHatch = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[3])
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[2]]  = AverageLowHatch
        #Average High Cargo
        AverageHighCargo = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[4])
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[3]] = AverageHighCargo
        #Average Medium Cargo
        AverageMediumCargo = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[5])
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[4]] = AverageMediumCargo
        #Average Low Cargo
        AverageLowCargo = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[6])
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[5]] = AverageLowCargo
        #Average Cargo
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[2]] = AverageHighCargo + AverageMediumCargo + AverageLowCargo
        #Average Hatches
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[3]] = AverageHighHatch + AverageLowHatch + AverageMediumHatch
        #Climbs
        TotalNoClimbs = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], 'NoClimb')
        Total1stLevelClimbs = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], '1stLevel')
        Total2ndLevelClimbs = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], '2ndLevel')
        Total3rdLevelClimbs = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], '3rdLevel')
        TotalClimbFails = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], 'ClimbFail')
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[0]] = str(Total1stLevelClimbs) + ' : ' + str(Total2ndLevelClimbs) + ' : ' + str(Total3rdLevelClimbs) + ' : ' + str(TotalClimbFails) + ' : ' + str(TotalNoClimbs)
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[6]] = ((Total3rdLevelClimbs) / MatchesPlayed)
        # Comments
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[1]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[1])
        # Average Hatches Auton
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[0]]=self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[7])
        #Average Cargo Auton
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[1]]=self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[8])
        # Climb Assist
        # self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[5]] = self.times_key_exists_in_category('ClimbAssist', 'ON') / MatchesPlayed
