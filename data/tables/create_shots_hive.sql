CREATE TABLE `shots`(
  `grid_type` char(50),
  `game_id` char(25),
  `event_id` int,
  `player_id` int,
  `player_name` char(100),
  `team_id` int,
  `team_name` char(100),
  `period` int,
  `minutes_remaining` int,
  `seconds_remaining` int,
  `event_type` char(100),
  `action_type` char(100),
  `shot_type` char(100),
  `shot_zone_basic` char(100),
  `shot_zone_area` char(100),
  `shot_zone_range` char(100),
  `shot_distance` int,
  `loc_x` float,
  `loc_y` float,
  `shot_attempted_flag` int,
  `shot_made_flag` int,
  `game_date` char(50),
  `htm` char(25),
  `vtm` char(25)
)
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  tblproperties("skip.header.line.count"="1");
