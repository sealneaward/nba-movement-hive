CREATE EXTERNAL TABLE ddb_features
(
    team_id   BIGINT,
    player_id  BIGINT,
    x_loc DOUBLE,
    y_loc DOUBLE,
    radius  DOUBLE,
    game_clock DOUBLE,
    shot_clock DOUBLE,
    quarter  BIGINT,
    game_id  STRING,
    event_id  BIGINT,
)
STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
TBLPROPERTIES(
    "dynamodb.table.name" = "movement",
    "dynamodb.column.mapping"="feature_id:Id,feature_name:Name,feature_class:Class,state_alpha:State,prim_lat_dec:Latitude,prim_long_dec:Longitude,elev_in_ft:Elevation"
);
