create virtual environment:
run python -m venv env
run cd env
run env/Scripts/activate

Houdini Instrospection:
run python -m sgqlc.introspection --exclude-deprecated --exclude-description -H "x-hasura-admin-secret: verystrongsecret" https://rough-shape-6577.fly.dev/v1/graphql ticker_schema.json
run  sgqlc-codegen schema ticker_schema.json ticker_schema.py

Generate operations:
run  sgqlc-codegen operation --schema ticker_schema.json ticker_schema insertTicks.py insertTicks.gql