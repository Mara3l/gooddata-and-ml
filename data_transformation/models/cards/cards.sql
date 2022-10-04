with cards as (
    select * from input_stage.card_transdata
),

final as (
    select
        md5(concat(cards.distance_from_home, cards.distance_from_last_transaction)) as unique_id,
        cards.distance_from_home,
        cards.distance_from_last_transaction,
        cards.ratio_to_median_purchase_price,
        cards.repeat_retailer,
        cards.used_chip,
        cards.used_pin_number,
        cards.online_order,
        cards.fraud,
        case
            when cards.fraud = 0 then 'no'
            when cards.fraud = 1 then 'yes'
        end as label__fraud__text
    from cards
)

select * from final