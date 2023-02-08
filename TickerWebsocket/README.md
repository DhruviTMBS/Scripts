create virtual environment:
run python -m venv env
run cd env
run env/Scripts/activate

Houdini Instrospection:
run python -m sgqlc.introspection --exclude-deprecated --exclude-description -H "x-hasura-admin-secret: verystrongsecret" https://squid-app-i98od.ondigitalocean.app/v1/graphql ticker_schema.json
run  sgqlc-codegen schema ticker_schema.json ticker_schema.py

Generate operations:
run  sgqlc-codegen operation --schema ticker_schema.json ticker_schema insertTickerData.py insertTickerData.gql