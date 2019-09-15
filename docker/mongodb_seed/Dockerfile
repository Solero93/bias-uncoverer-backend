FROM mongo:latest
COPY seed_data/* /

CMD mongoimport --host mongo --db $MONGO_INITDB_DATABASE --collection algorithm_types --drop --file /algorithm_types.json --jsonArray \
    && mongoimport --host mongo --db $MONGO_INITDB_DATABASE --collection bias_types --drop --file /bias_types.json --jsonArray