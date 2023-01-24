import sgqlc.types
import sgqlc.operation
import ticker_schema

_schema = ticker_schema
_schema_root = _schema.ticker_schema

__all__ = ('Operations',)


def mutation_master_mutation():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='MasterMutation', variables=dict(listofticks=sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(_schema.master_data_insert_input))))))
    _op_insert_master_data = _op.insert_master_data(objects=sgqlc.types.Variable('listofticks'), on_conflict={'constraint': 'master_data_pkey', 'update_columns': ('instrument_token', 'name', 'segment', 'instrument_type', 'expiry', 'strike')})
    _op_insert_master_data.affected_rows()
    return _op


def mutation_indices_mutation():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='IndicesMutation', variables=dict(listofindiceticks=sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(_schema.indices_ticks_insert_input))))))
    _op_insert_indices_ticks = _op.insert_indices_ticks(objects=sgqlc.types.Variable('listofindiceticks'), on_conflict={'update_columns': ('last_price',), 'constraint': 'indice_ticks_pkey'})
    _op_insert_indices_ticks.affected_rows()
    return _op


def mutation_futures_mutation():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='FuturesMutation', variables=dict(listoffuturesticks=sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(_schema.futures_ticks_insert_input))))))
    _op_insert_futures_ticks = _op.insert_futures_ticks(objects=sgqlc.types.Variable('listoffuturesticks'), on_conflict={'constraint': 'futures_ticks_pkey', 'update_columns': ('last_price', 'volume_traded', 'open_interest')})
    _op_insert_futures_ticks.affected_rows()
    return _op


def mutation_stock_mutation():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='StockMutation', variables=dict(listofstockticks=sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(_schema.stocks_ticks_insert_input))))))
    _op_insert_stocks_ticks = _op.insert_stocks_ticks(objects=sgqlc.types.Variable('listofstockticks'), on_conflict={'constraint': 'stock_ticks_pkey', 'update_columns': ('last_price', 'open_interest', 'volume_traded')})
    _op_insert_stocks_ticks.affected_rows()
    return _op


def mutation_options_mutation():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='optionsMutation', variables=dict(listofoptionsticks=sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(_schema.options_ticks_insert_input))))))
    _op_insert_options_ticks = _op.insert_options_ticks(objects=sgqlc.types.Variable('listofoptionsticks'), on_conflict={'constraint': 'options_ticks_pkey', 'update_columns': ('last_price', 'volume_traded', 'open_interest')})
    _op_insert_options_ticks.affected_rows()
    return _op


class Mutation:
    futures_mutation = mutation_futures_mutation()
    indices_mutation = mutation_indices_mutation()
    master_mutation = mutation_master_mutation()
    options_mutation = mutation_options_mutation()
    stock_mutation = mutation_stock_mutation()


class Operations:
    mutation = Mutation
