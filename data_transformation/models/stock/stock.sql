with weather as (
    select to_json(data) as data_json from input_stage.weather
),

final as (
    select
        CAST(json_extract_path_text(data_json, 'time') as timestamp) as date,
        CAST(json_extract_path_text(data_json, 'pres') as float) as air_pressure,
        CAST(json_extract_path_text(data_json, 'snow') as float) as snow,
        CAST(json_extract_path_text(data_json, 'temp') as float) as temperature,
        CAST(json_extract_path_text(data_json, 'dwpt') as float) as dew_point,
        CAST(json_extract_path_text(data_json, 'rhum') as float) as relative_humidity,
        CAST(json_extract_path_text(data_json, 'prcp') as float) as precipitation,
        CAST(json_extract_path_text(data_json, 'wdir') as float) as wind_direction,
        CAST(json_extract_path_text(data_json, 'wspd') as float) as wind_speed,
        CAST(json_extract_path_text(data_json, 'wpgt') as float) as wind_gust
    from weather
)

select * from final