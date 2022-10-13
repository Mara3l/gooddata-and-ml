with stock as (
    select id, symbol, date, to_json(data) as data_json from input_stage.stock
),

final as (
    select
        id,
        symbol,
        date,
        CAST(json_extract_path_text(data_json, '1. open') as float) as open,
        CAST(json_extract_path_text(data_json, '2. high') as float) as high,
        CAST(json_extract_path_text(data_json, '3. low') as float) as low,
        CAST(json_extract_path_text(data_json, '4. close') as float) as close,
        CAST(json_extract_path_text(data_json, '5. volume') as float) as volume
    from stock
)

select * from final