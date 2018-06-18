CREATE TABLE `movement`(
  `team_id` int,
  `player_id` int,
  `x_loc` float,
  `y_loc` float,
  `radius` float,
  `game_clock` float,
  `shot_clock` float,
  `quarter` int,
  `game_id` char(25),
  `event_id` int)
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n';
