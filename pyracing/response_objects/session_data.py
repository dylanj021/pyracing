from ..helpers import parse_encode

class SubSessionData:
    def __init__(self, dict):
        self.cat_id = dict['catid']
        self.caution_laps = dict['ncautionlaps']
        self.caution_type = dict['cautiontype']
        self.cautions = dict['ncautions']
        self.corners_total = dict['cornersperlap']
        self.driver_change_param_1 = dict['driver_change_param1']
        self.driver_change_param_2 = dict['driver_change_param2']
        self.driver_change_rule = dict['driver_change_rule']
        self.driver_changes = dict['driver_changes']
        self.event_type = dict['evttype']
        self.fog_density = dict['weather_fog_density']
        self.humidity = dict['weather_rh']
        self.lap_avg = dict['eventavglap']
        self.laps_completed = dict['eventlapscomplete']
        self.laps_for_qual_avg = dict['nlapsforqualavg']
        self.laps_for_solo_avg = dict['nlapsforsoloavg']
        self.lead_changes = dict['nleadchanges']
        self.league_id = parse_encode(dict['leagueid'])
        self.league_season_id = parse_encode(dict['league_season_id'])
        self.leave_marbles = dict['leavemarbles']
        self.max_weeks = dict['maxweeks']
        self.points_type = parse_encode(dict['pointstype'])
        self.private_session_id = dict['privatesessionid']
        self.race_week = dict['race_week_num']
        self.reserve_status = parse_encode(['rserv_status'])
        self.rubber_practice = dict['rubberlevel_practice']
        self.rubber_qualify = dict['rubberlevel_qualify']
        self.rubber_race = dict['rubberlevel_race']
        self.rubber_warmup = dict['rubberlevel_warmup']
        self.season_id = dict['seasonid']
        self.season_name = parse_encode(dict['season_name'])
        self.season_name_short = parse_encode(dict['season_shortname'])
        self.season_quarter = dict['season_quarter']
        self.season_year = dict['season_year']
        self.series_id = dict['seriesid']
        self.series_name = dict['series_name']
        self.series_name_short = dict['series_shortname']
        self.session_id = dict['sessionid']
        self.session_name = dict['sessionname']
        self.sim_ses_type = dict['simsestype']
        self.skies = dict['weather_skies']
        self.special_event_type = dict['specialeventtype']
        self.special_event_type_text = parse_encode(dict['specialeventtypetext'])
        self.strength_of_field = dict['eventstrengthoffield']
        self.subsession_id = dict['subsessionid']
        self.team_drivers_max = dict['max_team_drivers']
        self.team_drivers_min = dict['min_team_drivers']
        self.temp_unit = dict['weather_temp_units']
        self.temp_value = dict['weather_temp_value']
        self.time_of_day = dict['timeofday']
        self.time_start = parse_encode(dict['start_time'])
        self.time_start_sim = parse_encode(dict['simulatedstarttime'])
        self.track = parse_encode(dict['track_name'])
        self.track_config = parse_encode(dict['track_config_name'])
        self.track_id = dict['trackid']
        self.weather_initial = dict['weather_var_initial']
        self.weather_ongoing = dict['weather_var_ongoing']
        self.weather_type = dict['weather_type']
        self.wind_direction = dict['weather_wind_dir']
        self.wind_speed_unit = dict['weather_wind_speed_units']
        self.wind_speed_value = dict['weather_wind_speed_value']

        self.drivers = [self.Driver(x) for x in dict['rows']]

    class Driver:
        def __init__(self, dict):
            self.car_class_id = dict['carclassid']
            self.car_class_name = parse_encode(dict['ccName'])
            self.car_class_name_short = parse_encode(dict['ccNameShort'])
            self.car_color_1 = parse_encode(dict['car_color1'])
            self.car_color_2 = parse_encode(dict['car_color2'])
            self.car_color_3 = parse_encode(dict['car_color3'])
            self.car_id = dict['carid']
            self.car_num = parse_encode(dict['carnum'])
            self.car_num_font = dict['carnumberfont']
            self.car_num_slant = dict['carnumberslant']
            self.car_number_color_1 = parse_encode(dict['car_number_color1'])
            self.car_number_color_2 = parse_encode(dict['car_number_color2)
            self.car_number_color_3 = parse_encode(dict['car_number_color3'])
            self.car_pattern = dict['car_pattern']
            self.car_sponser_1 = dict['carsponsor1']
            self.car_sponser_2 = dict['carsponsor2']
            self.club_id = dict['clubid']
            self.club_name = parse_encode(dict['clubname'])
            self.club_name_short = parse_encode(dict['clubshortname'])
            self.club_points = dict['clubpoints']
            self.cpi_new = dict['newcpi']
            self.cpi_old = dict['oldcpi']
            self.cust_id = dict['custid']
            self.damage_model = dict['damage_model']
            self.display_name = parse_encode(dict['displayname'])
            self.division = dict['division']
            self.division_name = dict['divisionname']
            self.drop_race = dict['dropracepoints']
            self.event_type_name = parse_encode(dict['evttypename'])
            self.group_id = dict['groupid']
            self.heat_info_id = dict['heatinfoid']
            self.helm_color_1 = parse_encode(dict['helm_color1'])
            self.helm_color_2 = parse_encode(dict['helm_color2'])
            self.helm_color_3 = parse_encode(dict['helm_color3'])
            self.helm_pattern = dict['helm_pattern']
            self.host_id = parse_encode(dict['hostid'])
            self.incidents = dict['incidents']
            self.interval = dict['interval']
            self.interval_class = dict['classinterval']
            self.irating_new = dict['newirating']
            self.irating_old = dict['oldirating']
            self.lap_avg = dict['avglap']
            self.lap_best = dict['bestlaptime']
            self.lap_best_n = dict['bestlapnum']
            self.lap_qual_best = dict['bestquallaptime']
            self.lap_qual_best_at = dict['bestquallapat']
            self.lap_qual_best_n = dict['bestquallapnum']
            self.lap_qual_best_time = dict['quallaptime']
            self.laps_best_n_num = dict['bestnlapsnum']
            self.laps_best_n_time = dict['bestnlapstime']
            self.laps_comp = dict['lapscomplete']
            self.laps_led = dict['lapslead']
            self.laps_opt_comp = dict['optlapscomplete']
            self.league_points = parse_encode(dict['league_points'])
            self.license_category = parse_encode(dict['licensecategory'])
            self.license_change_oval = dict['license_change_oval']
            self.license_change_road = dict['license_change_road']
            self.license_class = dict['licensegroup']
            self.license_level_new = dict['newlicenselevel']
            self.license_level_old = dict['oldlicenselevel']
            self.multiplier = dict['multiplier']
            self.official = dict['officialsession']
            self.pct_fuel_fill_max = dict['max_pct_fuel_fill']
            self.points_champ = dict['champpoints']
            self.points_champ_agg = dict['aggchamppoints']
            self.pos = dict['pos']
            self.pos_finish = dict['finishpos']
            self.pos_finish_class = dict['finishposinclass']
            self.pos_start = dict['startpos']
            self.reason_out = parse_encode(dict['reasonout'])
            self.reason_out_id = dict['reasonoutid']
            self.restrict_results = parse_encode(dict['restrictresults'])
            self.sim_ses_name = parse_encode(dict['simsesname'])
            self.sim_ses_num = dict['simsesnum']
            self.sim_ses_type_name = parse_encode(dict['simsestypename'])
            self.sub_level_new = dict['newsublevel']
            self.sub_level_old = dict['oldsublevel']
            self.suit_color_1 = parse_encode(dict['suit_color1'])
            self.suit_color_2 = parse_encode(dict['suit_color2'])
            self.suit_color_3 = parse_encode(dict['suit_color3'])
            self.suit_pattern = dict['suit_pattern']
            self.time_session_start = dict['sessionstarttime']
            self.track_cat_id = dict['track_catid']
            self.track_category = parse_encode(dict['track_category'])
            self.ttrating_new = dict['newttrating']
            self.ttrating_old = dict['oldttrating']
            self.vehicle_key_id = dict['vehiclekeyid']
            self.weight_penalty_kg = dict['weight_penalty_kg']
            self.wheel_chrome = dict['wheel_chrome']
            self.wheel_color = parse_encode(dict['wheel_color'])


# Race laps for all drivers of a session
class RaceLapsAll:
    def __init__(self, dict):
        self.details = self.Details(dict['details'])
        self.drivers = [self.Driver(x) for x in dict['startgrid']]
        self.lap_data = [self.Lap(x) for x in dict['lapdata']]

    class Details:
        def __init__(self, dict):
            self.date = dict['eventDate']
            self.date_unix_utc_ms = dict['eventDateUTCMilliSecs']
            self.driver_changes = dict['driverChanges']
            self.event_type = dict['eventType']
            self.event_type_name = dict['eventTypeName']
            self.laps_for_qual_avg = dict['nLapsForQualAvg']
            self.laps_for_solo_avg = dict['nLapsForSoloAvg']
            self.official = dict['officialSession']
            self.private_session_id = dict['privateSessionID']
            self.private_session_name = dict['privateSessionName']
            self.race_panel_img = dict['race_panel_img']
            self.race_week = dict['raceWeek']
            self.season_id = dict['seasonID']
            self.season_name = dict['seasonName']
            self.season_name_short = dict['seasonShortName']
            self.series_name = dict['seriesName']
            self.series_name_short = dict['seriesShortName']
            self.session_id = dict['sessionId']
            self.subsession_id = dict['subSessionId']
            self.track = dict['trackName']
            self.track_config = dict['trackConfig']
            self.track_id = dict['trackid']

    class Driver:
        def __init__(self, dict):
            self.car_num = dict['carnum']
            self.cust_id = dict['custid']
            self.display_name = dict['displayName']
            self.friend = dict['friend']
            self.group_id = dict['groupid']
            self.helmet_color_1 = dict['helmetColor1']
            self.helmet_color_2 = dict['helmetColor2']
            self.helmet_color_3 = dict['helmetColor3']
            self.helmet_pattern = dict['helmetPattern']
            self.incidents = dict['numIncidents']
            self.lap_avg = dict['avgLapTime']
            self.lap_best_num = dict['fastestLapNum']
            self.lap_best_time = dict['fastestLapTime']
            self.license_color = dict['licenseColor']
            self.points_champ = dict['points']
            self.pos_finish = dict['finishPos']
            self.pos_start = dict['startPos']
            self.watch = dict['watch']

    class Lap:
        def __init__(self, dict):
            self.car_num = dict['carnum']
            self.cust_id = dict['custid']
            self.flags = dict['flags']
            self.lap_num = dict['lapnum']
            self.time_ses = dict['sesTime']


# Race laps for single driver of a session
class RaceLapsDriver:
    def __init__(self, dict):
        self.drivers = [self.Driver(x) for x in dict['drivers']]
        self.header = self.Header(dict['header'])
        self.lap_data = [self.Lap(x) for x in dict['lapData']]

    class Lap:
        def __init__(self, dict):
            self.cust_id = dict['custid']
            self.flags = dict['flags']
            self.lap_num = dict['lap_num']
            self.time_ses = dict['ses_time']

    class Header:
        def __init__(self, dict):
            self.car_color_1 = dict['carColor1']
            self.car_color_2 = dict['carColor2']
            self.car_color_3 = dict['carColor3']
            self.car_id = dict['carid']
            self.car_num = dict['carNum']
            self.car_pattern = dict['carPattern']
            self.date_unix_utc_ms = dict['eventDateUTCMilliSecs']
            self.event_date = dict['eventDate']
            self.event_type = dict['eventtype']
            self.event_type_name = dict['eventTypeName']
            self.laps_for_qual = dict['nlapsforqual']
            self.laps_for_solo = dict['nlapsforsolo']
            self.season_name = dict['seasonName']
            self.season_name_short = dict['seasonShortName']
            self.series_name = dict['seriesName']
            self.series_name_short = dict['seriesShortName']
            self.session_id = dict['sessionId']
            self.subsession_id = dict['subSessionId']
            self.suit_color_1 = dict['suitColor1']
            self.suit_color_2 = dict['suitColor2']
            self.suit_color_3 = dict['suitColor3']
            self.suit_pattern = dict['suitPattern']
            self.team_name = dict['teamName']
            self.track_config = dict['trackConfig']
            self.track_id = dict['trackID']
            self.track_name = dict['trackName']

    class Driver:
        def __init__(self, dict):
            self.cust_id = dict['custid']
            self.display_name = dict['displayname']
            self.helm_color_1 = dict['helm_color1']
            self.helm_color_2 = dict['helm_color2']
            self.helm_color_3 = dict['helm_color3']
            self.helm_pattern = dict['helm_pattern']
            self.lap_best = dict['bestlaptime']
            self.lap_best_n = dict['bestlapnum']
            self.lap_qual_best = dict['bestquallaptime']
            self.lap_qual_best_at = dict['bestquallapat']
            self.lap_qual_best_n = dict['bestquallapnum']
            self.laps_n_best_num = dict['bestnlapsnum']
            self.laps_n_best_time = dict['bestnlapstime']
            self.license_level = dict['licenselevel']
