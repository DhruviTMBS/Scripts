import sgqlc.types


ticker_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Float = sgqlc.types.Float

Int = sgqlc.types.Int

String = sgqlc.types.String

class cont_futures_15min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')


class cont_futures_1day_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')


class cont_futures_1hour_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')


class cont_futures_1min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')


class cont_futures_2hour_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')


class cont_futures_30min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')


class cont_futures_3min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')


class cont_indices_15min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')


class cont_indices_1hour_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')


class cont_indices_1min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')


class cont_indices_2hour_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')


class cont_indices_30min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')


class cont_indices_3min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')


class cont_options_1min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')


class cursor_ordering(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('ASC', 'DESC')


class date(sgqlc.types.Scalar):
    __schema__ = ticker_schema


class features_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'build_up_status', 'close', 'expiry', 'high', 'instrument_token', 'low', 'name', 'ohl_status', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'tradingsymbol', 'volume', 'volume_change_per')


class float8(sgqlc.types.Scalar):
    __schema__ = ticker_schema


class futures_15min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')


class futures_1day_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')


class futures_1hour_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')


class futures_1min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')


class futures_2hour_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')


class futures_30min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')


class futures_3min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')


class futures_ticks_constraint(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('futures_ticks_pkey',)


class futures_ticks_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')


class futures_ticks_select_column_futures_ticks_aggregate_bool_exp_avg_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class futures_ticks_select_column_futures_ticks_aggregate_bool_exp_corr_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class futures_ticks_select_column_futures_ticks_aggregate_bool_exp_covar_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class futures_ticks_select_column_futures_ticks_aggregate_bool_exp_max_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class futures_ticks_select_column_futures_ticks_aggregate_bool_exp_min_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class futures_ticks_select_column_futures_ticks_aggregate_bool_exp_stddev_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class futures_ticks_select_column_futures_ticks_aggregate_bool_exp_sum_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class futures_ticks_select_column_futures_ticks_aggregate_bool_exp_var_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class futures_ticks_update_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')


class indices_ticks_constraint(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('indice_ticks_pkey',)


class indices_ticks_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange_timestamp', 'instrument_token', 'last_price')


class indices_ticks_select_column_indices_ticks_aggregate_bool_exp_avg_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price',)


class indices_ticks_select_column_indices_ticks_aggregate_bool_exp_corr_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price',)


class indices_ticks_select_column_indices_ticks_aggregate_bool_exp_covar_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price',)


class indices_ticks_select_column_indices_ticks_aggregate_bool_exp_max_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price',)


class indices_ticks_select_column_indices_ticks_aggregate_bool_exp_min_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price',)


class indices_ticks_select_column_indices_ticks_aggregate_bool_exp_stddev_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price',)


class indices_ticks_select_column_indices_ticks_aggregate_bool_exp_sum_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price',)


class indices_ticks_select_column_indices_ticks_aggregate_bool_exp_var_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price',)


class indices_ticks_update_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange_timestamp', 'instrument_token', 'last_price')


class master_data_constraint(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('master_data_instrument_token_key', 'master_data_pkey')


class master_data_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange', 'expiry', 'instrument_token', 'instrument_type', 'is_nifty', 'name', 'segment', 'strike', 'tradingsymbol')


class master_data_update_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange', 'expiry', 'instrument_token', 'instrument_type', 'is_nifty', 'name', 'segment', 'strike', 'tradingsymbol')


class options_15min_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')


class options_chain_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('ce_build_up_status', 'ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_trend', 'ce_volume', 'es_time_field', 'pcr_oi', 'pcr_volumn', 'pe_build_up_status', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_trend', 'pe_volume', 'ps_time_field')


class options_ticks_constraint(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('options_ticks_pkey',)


class options_ticks_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')


class options_ticks_select_column_options_ticks_aggregate_bool_exp_avg_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest')


class options_ticks_select_column_options_ticks_aggregate_bool_exp_corr_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest')


class options_ticks_select_column_options_ticks_aggregate_bool_exp_covar_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest')


class options_ticks_select_column_options_ticks_aggregate_bool_exp_max_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest')


class options_ticks_select_column_options_ticks_aggregate_bool_exp_min_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest')


class options_ticks_select_column_options_ticks_aggregate_bool_exp_stddev_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest')


class options_ticks_select_column_options_ticks_aggregate_bool_exp_sum_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest')


class options_ticks_select_column_options_ticks_aggregate_bool_exp_var_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest')


class options_ticks_update_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')


class order_by(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('asc', 'asc_nulls_first', 'asc_nulls_last', 'desc', 'desc_nulls_first', 'desc_nulls_last')


class stocks_ticks_constraint(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('stock_ticks_pkey',)


class stocks_ticks_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')


class stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_avg_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_corr_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_covar_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_max_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_min_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_stddev_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_sum_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_var_samp_arguments_columns(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('last_price', 'open_interest', 'volume_traded')


class stocks_ticks_update_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')


class timestamptz(sgqlc.types.Scalar):
    __schema__ = ticker_schema


class timetz(sgqlc.types.Scalar):
    __schema__ = ticker_schema


class user_constraint(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('user_pkey',)


class user_select_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('age', 'name')


class user_update_column(sgqlc.types.Enum):
    __schema__ = ticker_schema
    __choices__ = ('age', 'name')



########################################################################
# Input Objects
########################################################################
class Boolean_comparison_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(Boolean, graphql_name='_eq')
    _gt = sgqlc.types.Field(Boolean, graphql_name='_gt')
    _gte = sgqlc.types.Field(Boolean, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(Boolean, graphql_name='_lt')
    _lte = sgqlc.types.Field(Boolean, graphql_name='_lte')
    _neq = sgqlc.types.Field(Boolean, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='_nin')


class Int_comparison_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(Int, graphql_name='_eq')
    _gt = sgqlc.types.Field(Int, graphql_name='_gt')
    _gte = sgqlc.types.Field(Int, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(Int, graphql_name='_lt')
    _lte = sgqlc.types.Field(Int, graphql_name='_lte')
    _neq = sgqlc.types.Field(Int, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='_nin')


class String_comparison_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_eq', '_gt', '_gte', '_ilike', '_in', '_iregex', '_is_null', '_like', '_lt', '_lte', '_neq', '_nilike', '_nin', '_niregex', '_nlike', '_nregex', '_nsimilar', '_regex', '_similar')
    _eq = sgqlc.types.Field(String, graphql_name='_eq')
    _gt = sgqlc.types.Field(String, graphql_name='_gt')
    _gte = sgqlc.types.Field(String, graphql_name='_gte')
    _ilike = sgqlc.types.Field(String, graphql_name='_ilike')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_in')
    _iregex = sgqlc.types.Field(String, graphql_name='_iregex')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _like = sgqlc.types.Field(String, graphql_name='_like')
    _lt = sgqlc.types.Field(String, graphql_name='_lt')
    _lte = sgqlc.types.Field(String, graphql_name='_lte')
    _neq = sgqlc.types.Field(String, graphql_name='_neq')
    _nilike = sgqlc.types.Field(String, graphql_name='_nilike')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_nin')
    _niregex = sgqlc.types.Field(String, graphql_name='_niregex')
    _nlike = sgqlc.types.Field(String, graphql_name='_nlike')
    _nregex = sgqlc.types.Field(String, graphql_name='_nregex')
    _nsimilar = sgqlc.types.Field(String, graphql_name='_nsimilar')
    _regex = sgqlc.types.Field(String, graphql_name='_regex')
    _similar = sgqlc.types.Field(String, graphql_name='_similar')


class cont_futures_15min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_15min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_futures_15min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_15min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    volume = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume')


class cont_futures_15min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')


class cont_futures_15min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_15min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_futures_15min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1day_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1day_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_futures_1day_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1day_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    volume = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume')


class cont_futures_1day_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')


class cont_futures_1day_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1day_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_futures_1day_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1hour_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1hour_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_futures_1hour_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1hour_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    volume = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume')


class cont_futures_1hour_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')


class cont_futures_1hour_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1hour_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_futures_1hour_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_futures_1min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    volume = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume')


class cont_futures_1min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')


class cont_futures_1min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_futures_1min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_2hour_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_2hour_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_futures_2hour_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_2hour_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    volume = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume')


class cont_futures_2hour_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')


class cont_futures_2hour_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_2hour_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_futures_2hour_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_30min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_30min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_futures_30min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_30min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    volume = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume')


class cont_futures_30min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')


class cont_futures_30min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_30min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_futures_30min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_3min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_3min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_futures_3min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_3min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    volume = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume')


class cont_futures_3min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')


class cont_futures_3min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_3min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_futures_3min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_indices_15min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_15min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_indices_15min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_15min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')


class cont_indices_15min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')


class cont_indices_15min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_15min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_indices_15min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1hour_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1hour_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_indices_1hour_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1hour_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')


class cont_indices_1hour_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')


class cont_indices_1hour_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_1hour_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_indices_1hour_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_indices_1min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')


class cont_indices_1min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')


class cont_indices_1min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_1min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_indices_1min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_2hour_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_2hour_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_indices_2hour_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_2hour_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')


class cont_indices_2hour_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')


class cont_indices_2hour_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_2hour_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_indices_2hour_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_30min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_30min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_indices_30min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_30min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')


class cont_indices_30min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')


class cont_indices_30min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_30min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_indices_30min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_3min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_3min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_indices_3min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_3min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')


class cont_indices_3min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')


class cont_indices_3min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_3min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_indices_3min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_options_1min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_options_1min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('cont_options_1min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('cont_options_1min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    volume = sgqlc.types.Field(Int_comparison_exp, graphql_name='volume')


class cont_options_1min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')


class cont_options_1min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('cont_options_1min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class cont_options_1min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(Int, graphql_name='volume')


class date_comparison_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(date, graphql_name='_eq')
    _gt = sgqlc.types.Field(date, graphql_name='_gt')
    _gte = sgqlc.types.Field(date, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(date)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(date, graphql_name='_lt')
    _lte = sgqlc.types.Field(date, graphql_name='_lte')
    _neq = sgqlc.types.Field(date, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(date)), graphql_name='_nin')


class features_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'build_up_status', 'close', 'expiry', 'high', 'instrument_token', 'low', 'name', 'ohl_status', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'tradingsymbol', 'volume', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('features_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('features_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('features_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field('float8_comparison_exp', graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    build_up_status = sgqlc.types.Field(String_comparison_exp, graphql_name='build_up_status')
    close = sgqlc.types.Field('float8_comparison_exp', graphql_name='close')
    expiry = sgqlc.types.Field(date_comparison_exp, graphql_name='expiry')
    high = sgqlc.types.Field('float8_comparison_exp', graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field('float8_comparison_exp', graphql_name='low')
    name = sgqlc.types.Field(String_comparison_exp, graphql_name='name')
    ohl_status = sgqlc.types.Field(String_comparison_exp, graphql_name='ohl_status')
    open = sgqlc.types.Field('float8_comparison_exp', graphql_name='open')
    open_interest = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field('float8_comparison_exp', graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field('float8_comparison_exp', graphql_name='price_change')
    price_change_per = sgqlc.types.Field('float8_comparison_exp', graphql_name='price_change_per')
    tradingsymbol = sgqlc.types.Field(String_comparison_exp, graphql_name='tradingsymbol')
    volume = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume')
    volume_change_per = sgqlc.types.Field('float8_comparison_exp', graphql_name='volume_change_per')


class features_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'build_up_status', 'close', 'expiry', 'high', 'instrument_token', 'low', 'name', 'ohl_status', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'tradingsymbol', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    build_up_status = sgqlc.types.Field(order_by, graphql_name='build_up_status')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    expiry = sgqlc.types.Field(order_by, graphql_name='expiry')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    ohl_status = sgqlc.types.Field(order_by, graphql_name='ohl_status')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    tradingsymbol = sgqlc.types.Field(order_by, graphql_name='tradingsymbol')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class features_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('features_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class features_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'build_up_status', 'close', 'expiry', 'high', 'instrument_token', 'low', 'name', 'ohl_status', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'tradingsymbol', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    build_up_status = sgqlc.types.Field(String, graphql_name='build_up_status')
    close = sgqlc.types.Field(float8, graphql_name='close')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    name = sgqlc.types.Field(String, graphql_name='name')
    ohl_status = sgqlc.types.Field(String, graphql_name='ohl_status')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class float8_comparison_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(float8, graphql_name='_eq')
    _gt = sgqlc.types.Field(float8, graphql_name='_gt')
    _gte = sgqlc.types.Field(float8, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(float8)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(float8, graphql_name='_lt')
    _lte = sgqlc.types.Field(float8, graphql_name='_lte')
    _neq = sgqlc.types.Field(float8, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(float8)), graphql_name='_nin')


class futures_15min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_15min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('futures_15min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_15min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field(float8_comparison_exp, graphql_name='close')
    high = sgqlc.types.Field(float8_comparison_exp, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8_comparison_exp, graphql_name='low')
    open = sgqlc.types.Field(float8_comparison_exp, graphql_name='open')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change_per')


class futures_15min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change = sgqlc.types.Field(order_by, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class futures_15min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('futures_15min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class futures_15min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1day_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_1day_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('futures_1day_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_1day_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field(float8_comparison_exp, graphql_name='close')
    high = sgqlc.types.Field(float8_comparison_exp, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8_comparison_exp, graphql_name='low')
    open = sgqlc.types.Field(float8_comparison_exp, graphql_name='open')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change_per')


class futures_1day_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change = sgqlc.types.Field(order_by, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class futures_1day_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('futures_1day_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class futures_1day_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1hour_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_1hour_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('futures_1hour_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_1hour_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field(float8_comparison_exp, graphql_name='close')
    high = sgqlc.types.Field(float8_comparison_exp, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8_comparison_exp, graphql_name='low')
    open = sgqlc.types.Field(float8_comparison_exp, graphql_name='open')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change_per')


class futures_1hour_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change = sgqlc.types.Field(order_by, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class futures_1hour_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('futures_1hour_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class futures_1hour_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_1min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('futures_1min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_1min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field(float8_comparison_exp, graphql_name='close')
    high = sgqlc.types.Field(float8_comparison_exp, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8_comparison_exp, graphql_name='low')
    open = sgqlc.types.Field(float8_comparison_exp, graphql_name='open')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change_per')


class futures_1min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change = sgqlc.types.Field(order_by, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class futures_1min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('futures_1min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class futures_1min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_2hour_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_2hour_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('futures_2hour_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_2hour_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field(float8_comparison_exp, graphql_name='close')
    high = sgqlc.types.Field(float8_comparison_exp, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8_comparison_exp, graphql_name='low')
    open = sgqlc.types.Field(float8_comparison_exp, graphql_name='open')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change_per')


class futures_2hour_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change = sgqlc.types.Field(order_by, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class futures_2hour_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('futures_2hour_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class futures_2hour_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_30min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_30min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('futures_30min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_30min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field(float8_comparison_exp, graphql_name='close')
    high = sgqlc.types.Field(float8_comparison_exp, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8_comparison_exp, graphql_name='low')
    open = sgqlc.types.Field(float8_comparison_exp, graphql_name='open')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change_per')


class futures_30min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change = sgqlc.types.Field(order_by, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class futures_30min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('futures_30min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class futures_30min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_3min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_3min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('futures_3min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_3min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field(float8_comparison_exp, graphql_name='close')
    high = sgqlc.types.Field(float8_comparison_exp, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8_comparison_exp, graphql_name='low')
    open = sgqlc.types.Field(float8_comparison_exp, graphql_name='open')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_change_per')


class futures_3min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change = sgqlc.types.Field(order_by, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class futures_3min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('futures_3min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class futures_3min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_ticks_aggregate_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'corr', 'count', 'covar_samp', 'max', 'min', 'stddev_samp', 'sum', 'var_samp')
    avg = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_avg', graphql_name='avg')
    corr = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_corr', graphql_name='corr')
    count = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_count', graphql_name='count')
    covar_samp = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_covar_samp', graphql_name='covar_samp')
    max = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_max', graphql_name='max')
    min = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_min', graphql_name='min')
    stddev_samp = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_stddev_samp', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_sum', graphql_name='sum')
    var_samp = sgqlc.types.Field('futures_ticks_aggregate_bool_exp_var_samp', graphql_name='var_samp')


class futures_ticks_aggregate_bool_exp_avg(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_avg_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_bool_exp_corr(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null('futures_ticks_aggregate_bool_exp_corr_arguments'), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_bool_exp_corr_arguments(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_corr_arguments_columns), graphql_name='X')
    y = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_corr_arguments_columns), graphql_name='Y')


class futures_ticks_aggregate_bool_exp_count(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_select_column)), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(Int_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_bool_exp_covar_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null('futures_ticks_aggregate_bool_exp_covar_samp_arguments'), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_bool_exp_covar_samp_arguments(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_covar_samp_arguments_columns), graphql_name='X')
    y = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_covar_samp_arguments_columns), graphql_name='Y')


class futures_ticks_aggregate_bool_exp_max(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_max_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_bool_exp_min(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_min_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_bool_exp_stddev_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_stddev_samp_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_bool_exp_sum(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_sum_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_bool_exp_var_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_select_column_futures_ticks_aggregate_bool_exp_var_samp_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class futures_ticks_aggregate_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_ticks_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('futures_ticks_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('futures_ticks_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('futures_ticks_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_ticks_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_ticks_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_ticks_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_ticks_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_ticks_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_ticks_variance_order_by', graphql_name='variance')


class futures_ticks_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_ticks_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('futures_ticks_on_conflict', graphql_name='on_conflict')


class futures_ticks_avg_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_ticks_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('futures_ticks_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('futures_ticks_bool_exp')), graphql_name='_or')
    exchange_timestamp = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='last_price')
    master_datum = sgqlc.types.Field('master_data_bool_exp', graphql_name='master_datum')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_traded')


class futures_ticks_inc_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class futures_ticks_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    master_datum = sgqlc.types.Field('master_data_obj_rel_insert_input', graphql_name='master_datum')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class futures_ticks_max_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_on_conflict(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(futures_ticks_bool_exp, graphql_name='where')


class futures_ticks_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    master_datum = sgqlc.types.Field('master_data_order_by', graphql_name='master_datum')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_pk_columns_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token')
    exchange_timestamp = sgqlc.types.Field(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')


class futures_ticks_set_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class futures_ticks_stddev_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('futures_ticks_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class futures_ticks_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class futures_ticks_sum_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_updates(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_inc', '_set', 'where')
    _inc = sgqlc.types.Field(futures_ticks_inc_input, graphql_name='_inc')
    _set = sgqlc.types.Field(futures_ticks_set_input, graphql_name='_set')
    where = sgqlc.types.Field(sgqlc.types.non_null(futures_ticks_bool_exp), graphql_name='where')


class futures_ticks_var_pop_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_var_samp_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class futures_ticks_variance_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class indices_ticks_aggregate_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'corr', 'count', 'covar_samp', 'max', 'min', 'stddev_samp', 'sum', 'var_samp')
    avg = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_avg', graphql_name='avg')
    corr = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_corr', graphql_name='corr')
    count = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_count', graphql_name='count')
    covar_samp = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_covar_samp', graphql_name='covar_samp')
    max = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_max', graphql_name='max')
    min = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_min', graphql_name='min')
    stddev_samp = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_stddev_samp', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_sum', graphql_name='sum')
    var_samp = sgqlc.types.Field('indices_ticks_aggregate_bool_exp_var_samp', graphql_name='var_samp')


class indices_ticks_aggregate_bool_exp_avg(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_avg_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_bool_exp_corr(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null('indices_ticks_aggregate_bool_exp_corr_arguments'), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_bool_exp_corr_arguments(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_corr_arguments_columns), graphql_name='X')
    y = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_corr_arguments_columns), graphql_name='Y')


class indices_ticks_aggregate_bool_exp_count(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_select_column)), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(Int_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_bool_exp_covar_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null('indices_ticks_aggregate_bool_exp_covar_samp_arguments'), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_bool_exp_covar_samp_arguments(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_covar_samp_arguments_columns), graphql_name='X')
    y = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_covar_samp_arguments_columns), graphql_name='Y')


class indices_ticks_aggregate_bool_exp_max(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_max_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_bool_exp_min(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_min_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_bool_exp_stddev_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_stddev_samp_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_bool_exp_sum(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_sum_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_bool_exp_var_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_select_column_indices_ticks_aggregate_bool_exp_var_samp_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class indices_ticks_aggregate_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('indices_ticks_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('indices_ticks_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('indices_ticks_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('indices_ticks_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('indices_ticks_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('indices_ticks_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('indices_ticks_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('indices_ticks_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('indices_ticks_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('indices_ticks_variance_order_by', graphql_name='variance')


class indices_ticks_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('indices_ticks_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('indices_ticks_on_conflict', graphql_name='on_conflict')


class indices_ticks_avg_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'exchange_timestamp', 'instrument_token', 'last_price', 'master_datum')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('indices_ticks_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('indices_ticks_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('indices_ticks_bool_exp')), graphql_name='_or')
    exchange_timestamp = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='last_price')
    master_datum = sgqlc.types.Field('master_data_bool_exp', graphql_name='master_datum')


class indices_ticks_inc_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')


class indices_ticks_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    master_datum = sgqlc.types.Field('master_data_obj_rel_insert_input', graphql_name='master_datum')


class indices_ticks_max_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_on_conflict(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(indices_ticks_bool_exp, graphql_name='where')


class indices_ticks_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    master_datum = sgqlc.types.Field('master_data_order_by', graphql_name='master_datum')


class indices_ticks_pk_columns_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token')
    exchange_timestamp = sgqlc.types.Field(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')


class indices_ticks_set_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')


class indices_ticks_stddev_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('indices_ticks_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class indices_ticks_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')


class indices_ticks_sum_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_updates(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_inc', '_set', 'where')
    _inc = sgqlc.types.Field(indices_ticks_inc_input, graphql_name='_inc')
    _set = sgqlc.types.Field(indices_ticks_set_input, graphql_name='_set')
    where = sgqlc.types.Field(sgqlc.types.non_null(indices_ticks_bool_exp), graphql_name='where')


class indices_ticks_var_pop_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_var_samp_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class indices_ticks_variance_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')


class master_data_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'exchange', 'expiry', 'futures_ticks', 'futures_ticks_aggregate', 'indices_ticks', 'indices_ticks_aggregate', 'instrument_token', 'instrument_type', 'is_nifty', 'name', 'options_ticks', 'options_ticks_aggregate', 'segment', 'stocks_ticks', 'stocks_ticks_aggregate', 'strike', 'tradingsymbol')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('master_data_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('master_data_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('master_data_bool_exp')), graphql_name='_or')
    exchange = sgqlc.types.Field(String_comparison_exp, graphql_name='exchange')
    expiry = sgqlc.types.Field(date_comparison_exp, graphql_name='expiry')
    futures_ticks = sgqlc.types.Field(futures_ticks_bool_exp, graphql_name='futures_ticks')
    futures_ticks_aggregate = sgqlc.types.Field(futures_ticks_aggregate_bool_exp, graphql_name='futures_ticks_aggregate')
    indices_ticks = sgqlc.types.Field(indices_ticks_bool_exp, graphql_name='indices_ticks')
    indices_ticks_aggregate = sgqlc.types.Field(indices_ticks_aggregate_bool_exp, graphql_name='indices_ticks_aggregate')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    instrument_type = sgqlc.types.Field(String_comparison_exp, graphql_name='instrument_type')
    is_nifty = sgqlc.types.Field(Boolean_comparison_exp, graphql_name='is_nifty')
    name = sgqlc.types.Field(String_comparison_exp, graphql_name='name')
    options_ticks = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='options_ticks')
    options_ticks_aggregate = sgqlc.types.Field('options_ticks_aggregate_bool_exp', graphql_name='options_ticks_aggregate')
    segment = sgqlc.types.Field(String_comparison_exp, graphql_name='segment')
    stocks_ticks = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='stocks_ticks')
    stocks_ticks_aggregate = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp', graphql_name='stocks_ticks_aggregate')
    strike = sgqlc.types.Field(float8_comparison_exp, graphql_name='strike')
    tradingsymbol = sgqlc.types.Field(String_comparison_exp, graphql_name='tradingsymbol')


class master_data_inc_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    strike = sgqlc.types.Field(float8, graphql_name='strike')


class master_data_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange', 'expiry', 'futures_ticks', 'indices_ticks', 'instrument_token', 'instrument_type', 'is_nifty', 'name', 'options_ticks', 'segment', 'stocks_ticks', 'strike', 'tradingsymbol')
    exchange = sgqlc.types.Field(String, graphql_name='exchange')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    futures_ticks = sgqlc.types.Field(futures_ticks_arr_rel_insert_input, graphql_name='futures_ticks')
    indices_ticks = sgqlc.types.Field(indices_ticks_arr_rel_insert_input, graphql_name='indices_ticks')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    instrument_type = sgqlc.types.Field(String, graphql_name='instrument_type')
    is_nifty = sgqlc.types.Field(Boolean, graphql_name='is_nifty')
    name = sgqlc.types.Field(String, graphql_name='name')
    options_ticks = sgqlc.types.Field('options_ticks_arr_rel_insert_input', graphql_name='options_ticks')
    segment = sgqlc.types.Field(String, graphql_name='segment')
    stocks_ticks = sgqlc.types.Field('stocks_ticks_arr_rel_insert_input', graphql_name='stocks_ticks')
    strike = sgqlc.types.Field(float8, graphql_name='strike')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')


class master_data_obj_rel_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(master_data_insert_input), graphql_name='data')
    on_conflict = sgqlc.types.Field('master_data_on_conflict', graphql_name='on_conflict')


class master_data_on_conflict(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(master_data_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(master_data_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(master_data_bool_exp, graphql_name='where')


class master_data_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange', 'expiry', 'futures_ticks_aggregate', 'indices_ticks_aggregate', 'instrument_token', 'instrument_type', 'is_nifty', 'name', 'options_ticks_aggregate', 'segment', 'stocks_ticks_aggregate', 'strike', 'tradingsymbol')
    exchange = sgqlc.types.Field(order_by, graphql_name='exchange')
    expiry = sgqlc.types.Field(order_by, graphql_name='expiry')
    futures_ticks_aggregate = sgqlc.types.Field(futures_ticks_aggregate_order_by, graphql_name='futures_ticks_aggregate')
    indices_ticks_aggregate = sgqlc.types.Field(indices_ticks_aggregate_order_by, graphql_name='indices_ticks_aggregate')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    instrument_type = sgqlc.types.Field(order_by, graphql_name='instrument_type')
    is_nifty = sgqlc.types.Field(order_by, graphql_name='is_nifty')
    name = sgqlc.types.Field(order_by, graphql_name='name')
    options_ticks_aggregate = sgqlc.types.Field('options_ticks_aggregate_order_by', graphql_name='options_ticks_aggregate')
    segment = sgqlc.types.Field(order_by, graphql_name='segment')
    stocks_ticks_aggregate = sgqlc.types.Field('stocks_ticks_aggregate_order_by', graphql_name='stocks_ticks_aggregate')
    strike = sgqlc.types.Field(order_by, graphql_name='strike')
    tradingsymbol = sgqlc.types.Field(order_by, graphql_name='tradingsymbol')


class master_data_pk_columns_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange', 'tradingsymbol')
    exchange = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='exchange')
    tradingsymbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tradingsymbol')


class master_data_set_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange', 'expiry', 'instrument_token', 'instrument_type', 'is_nifty', 'name', 'segment', 'strike', 'tradingsymbol')
    exchange = sgqlc.types.Field(String, graphql_name='exchange')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    instrument_type = sgqlc.types.Field(String, graphql_name='instrument_type')
    is_nifty = sgqlc.types.Field(Boolean, graphql_name='is_nifty')
    name = sgqlc.types.Field(String, graphql_name='name')
    segment = sgqlc.types.Field(String, graphql_name='segment')
    strike = sgqlc.types.Field(float8, graphql_name='strike')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')


class master_data_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('master_data_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class master_data_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange', 'expiry', 'instrument_token', 'instrument_type', 'is_nifty', 'name', 'segment', 'strike', 'tradingsymbol')
    exchange = sgqlc.types.Field(String, graphql_name='exchange')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    instrument_type = sgqlc.types.Field(String, graphql_name='instrument_type')
    is_nifty = sgqlc.types.Field(Boolean, graphql_name='is_nifty')
    name = sgqlc.types.Field(String, graphql_name='name')
    segment = sgqlc.types.Field(String, graphql_name='segment')
    strike = sgqlc.types.Field(float8, graphql_name='strike')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')


class master_data_updates(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_inc', '_set', 'where')
    _inc = sgqlc.types.Field(master_data_inc_input, graphql_name='_inc')
    _set = sgqlc.types.Field(master_data_set_input, graphql_name='_set')
    where = sgqlc.types.Field(sgqlc.types.non_null(master_data_bool_exp), graphql_name='where')


class options_15min_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('options_15min_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('options_15min_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('options_15min_bool_exp')), graphql_name='_or')
    avg_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='avg_price')
    bucket = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='bucket')
    close = sgqlc.types.Field(float8_comparison_exp, graphql_name='close')
    high = sgqlc.types.Field(float8_comparison_exp, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8_comparison_exp, graphql_name='low')
    open = sgqlc.types.Field(float8_comparison_exp, graphql_name='open')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8_comparison_exp, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Int_comparison_exp, graphql_name='volume')
    volume_change = sgqlc.types.Field(Int_comparison_exp, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Int_comparison_exp, graphql_name='volume_change_per')


class options_15min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(order_by, graphql_name='avg_price')
    bucket = sgqlc.types.Field(order_by, graphql_name='bucket')
    close = sgqlc.types.Field(order_by, graphql_name='close')
    high = sgqlc.types.Field(order_by, graphql_name='high')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    low = sgqlc.types.Field(order_by, graphql_name='low')
    open = sgqlc.types.Field(order_by, graphql_name='open')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(order_by, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(order_by, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(order_by, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(order_by, graphql_name='price_change_per')
    volume = sgqlc.types.Field(order_by, graphql_name='volume')
    volume_change = sgqlc.types.Field(order_by, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(order_by, graphql_name='volume_change_per')


class options_15min_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('options_15min_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class options_15min_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Int, graphql_name='volume')
    volume_change = sgqlc.types.Field(Int, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Int, graphql_name='volume_change_per')


class options_chain_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'ce_build_up_status', 'ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_trend', 'ce_volume', 'es_time_field', 'pcr_oi', 'pcr_volumn', 'pe_build_up_status', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_trend', 'pe_volume', 'ps_time_field')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('options_chain_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('options_chain_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('options_chain_bool_exp')), graphql_name='_or')
    ce_build_up_status = sgqlc.types.Field(String_comparison_exp, graphql_name='ce_build_up_status')
    ce_change_pts = sgqlc.types.Field(float8_comparison_exp, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(float8_comparison_exp, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(float8_comparison_exp, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(float8_comparison_exp, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='ce_strike_price')
    ce_trend = sgqlc.types.Field(String_comparison_exp, graphql_name='ce_trend')
    ce_volume = sgqlc.types.Field(Int_comparison_exp, graphql_name='ce_volume')
    es_time_field = sgqlc.types.Field('timetz_comparison_exp', graphql_name='es_time_field')
    pcr_oi = sgqlc.types.Field(float8_comparison_exp, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Int_comparison_exp, graphql_name='pcr_volumn')
    pe_build_up_status = sgqlc.types.Field(String_comparison_exp, graphql_name='pe_build_up_status')
    pe_change_pts = sgqlc.types.Field(float8_comparison_exp, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(float8_comparison_exp, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(float8_comparison_exp, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(float8_comparison_exp, graphql_name='pe_oi_chg')
    pe_trend = sgqlc.types.Field(String_comparison_exp, graphql_name='pe_trend')
    pe_volume = sgqlc.types.Field(Int_comparison_exp, graphql_name='pe_volume')
    ps_time_field = sgqlc.types.Field('timetz_comparison_exp', graphql_name='ps_time_field')


class options_chain_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('ce_build_up_status', 'ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_trend', 'ce_volume', 'es_time_field', 'pcr_oi', 'pcr_volumn', 'pe_build_up_status', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_trend', 'pe_volume', 'ps_time_field')
    ce_build_up_status = sgqlc.types.Field(order_by, graphql_name='ce_build_up_status')
    ce_change_pts = sgqlc.types.Field(order_by, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(order_by, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(order_by, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(order_by, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(order_by, graphql_name='ce_strike_price')
    ce_trend = sgqlc.types.Field(order_by, graphql_name='ce_trend')
    ce_volume = sgqlc.types.Field(order_by, graphql_name='ce_volume')
    es_time_field = sgqlc.types.Field(order_by, graphql_name='es_time_field')
    pcr_oi = sgqlc.types.Field(order_by, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(order_by, graphql_name='pcr_volumn')
    pe_build_up_status = sgqlc.types.Field(order_by, graphql_name='pe_build_up_status')
    pe_change_pts = sgqlc.types.Field(order_by, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(order_by, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(order_by, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(order_by, graphql_name='pe_oi_chg')
    pe_trend = sgqlc.types.Field(order_by, graphql_name='pe_trend')
    pe_volume = sgqlc.types.Field(order_by, graphql_name='pe_volume')
    ps_time_field = sgqlc.types.Field(order_by, graphql_name='ps_time_field')


class options_chain_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('options_chain_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class options_chain_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('ce_build_up_status', 'ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_trend', 'ce_volume', 'es_time_field', 'pcr_oi', 'pcr_volumn', 'pe_build_up_status', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_trend', 'pe_volume', 'ps_time_field')
    ce_build_up_status = sgqlc.types.Field(String, graphql_name='ce_build_up_status')
    ce_change_pts = sgqlc.types.Field(float8, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(float8, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(float8, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(float8, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(float8, graphql_name='ce_strike_price')
    ce_trend = sgqlc.types.Field(String, graphql_name='ce_trend')
    ce_volume = sgqlc.types.Field(Int, graphql_name='ce_volume')
    es_time_field = sgqlc.types.Field(timetz, graphql_name='es_time_field')
    pcr_oi = sgqlc.types.Field(float8, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Int, graphql_name='pcr_volumn')
    pe_build_up_status = sgqlc.types.Field(String, graphql_name='pe_build_up_status')
    pe_change_pts = sgqlc.types.Field(float8, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(float8, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(float8, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(float8, graphql_name='pe_oi_chg')
    pe_trend = sgqlc.types.Field(String, graphql_name='pe_trend')
    pe_volume = sgqlc.types.Field(Int, graphql_name='pe_volume')
    ps_time_field = sgqlc.types.Field(timetz, graphql_name='ps_time_field')


class options_ticks_aggregate_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'corr', 'count', 'covar_samp', 'max', 'min', 'stddev_samp', 'sum', 'var_samp')
    avg = sgqlc.types.Field('options_ticks_aggregate_bool_exp_avg', graphql_name='avg')
    corr = sgqlc.types.Field('options_ticks_aggregate_bool_exp_corr', graphql_name='corr')
    count = sgqlc.types.Field('options_ticks_aggregate_bool_exp_count', graphql_name='count')
    covar_samp = sgqlc.types.Field('options_ticks_aggregate_bool_exp_covar_samp', graphql_name='covar_samp')
    max = sgqlc.types.Field('options_ticks_aggregate_bool_exp_max', graphql_name='max')
    min = sgqlc.types.Field('options_ticks_aggregate_bool_exp_min', graphql_name='min')
    stddev_samp = sgqlc.types.Field('options_ticks_aggregate_bool_exp_stddev_samp', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('options_ticks_aggregate_bool_exp_sum', graphql_name='sum')
    var_samp = sgqlc.types.Field('options_ticks_aggregate_bool_exp_var_samp', graphql_name='var_samp')


class options_ticks_aggregate_bool_exp_avg(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_avg_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_bool_exp_corr(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null('options_ticks_aggregate_bool_exp_corr_arguments'), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_bool_exp_corr_arguments(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_corr_arguments_columns), graphql_name='X')
    y = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_corr_arguments_columns), graphql_name='Y')


class options_ticks_aggregate_bool_exp_count(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_select_column)), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(Int_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_bool_exp_covar_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null('options_ticks_aggregate_bool_exp_covar_samp_arguments'), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_bool_exp_covar_samp_arguments(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_covar_samp_arguments_columns), graphql_name='X')
    y = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_covar_samp_arguments_columns), graphql_name='Y')


class options_ticks_aggregate_bool_exp_max(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_max_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_bool_exp_min(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_min_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_bool_exp_stddev_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_stddev_samp_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_bool_exp_sum(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_sum_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_bool_exp_var_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_select_column_options_ticks_aggregate_bool_exp_var_samp_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class options_ticks_aggregate_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('options_ticks_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('options_ticks_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('options_ticks_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('options_ticks_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('options_ticks_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('options_ticks_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('options_ticks_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('options_ticks_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('options_ticks_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('options_ticks_variance_order_by', graphql_name='variance')


class options_ticks_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_ticks_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('options_ticks_on_conflict', graphql_name='on_conflict')


class options_ticks_avg_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('options_ticks_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('options_ticks_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('options_ticks_bool_exp')), graphql_name='_or')
    exchange_timestamp = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='last_price')
    master_datum = sgqlc.types.Field(master_data_bool_exp, graphql_name='master_datum')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Int_comparison_exp, graphql_name='volume_traded')


class options_ticks_inc_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Int, graphql_name='volume_traded')


class options_ticks_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    master_datum = sgqlc.types.Field(master_data_obj_rel_insert_input, graphql_name='master_datum')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Int, graphql_name='volume_traded')


class options_ticks_max_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_on_conflict(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(options_ticks_bool_exp, graphql_name='where')


class options_ticks_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    master_datum = sgqlc.types.Field(master_data_order_by, graphql_name='master_datum')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_pk_columns_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token')
    exchange_timestamp = sgqlc.types.Field(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')


class options_ticks_set_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Int, graphql_name='volume_traded')


class options_ticks_stddev_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('options_ticks_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class options_ticks_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Int, graphql_name='volume_traded')


class options_ticks_sum_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_updates(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_inc', '_set', 'where')
    _inc = sgqlc.types.Field(options_ticks_inc_input, graphql_name='_inc')
    _set = sgqlc.types.Field(options_ticks_set_input, graphql_name='_set')
    where = sgqlc.types.Field(sgqlc.types.non_null(options_ticks_bool_exp), graphql_name='where')


class options_ticks_var_pop_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_var_samp_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class options_ticks_variance_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_aggregate_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'corr', 'count', 'covar_samp', 'max', 'min', 'stddev_samp', 'sum', 'var_samp')
    avg = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_avg', graphql_name='avg')
    corr = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_corr', graphql_name='corr')
    count = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_count', graphql_name='count')
    covar_samp = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_covar_samp', graphql_name='covar_samp')
    max = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_max', graphql_name='max')
    min = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_min', graphql_name='min')
    stddev_samp = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_stddev_samp', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_sum', graphql_name='sum')
    var_samp = sgqlc.types.Field('stocks_ticks_aggregate_bool_exp_var_samp', graphql_name='var_samp')


class stocks_ticks_aggregate_bool_exp_avg(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_avg_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_bool_exp_corr(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null('stocks_ticks_aggregate_bool_exp_corr_arguments'), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_bool_exp_corr_arguments(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_corr_arguments_columns), graphql_name='X')
    y = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_corr_arguments_columns), graphql_name='Y')


class stocks_ticks_aggregate_bool_exp_count(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_select_column)), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(Int_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_bool_exp_covar_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null('stocks_ticks_aggregate_bool_exp_covar_samp_arguments'), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_bool_exp_covar_samp_arguments(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_covar_samp_arguments_columns), graphql_name='X')
    y = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_covar_samp_arguments_columns), graphql_name='Y')


class stocks_ticks_aggregate_bool_exp_max(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_max_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_bool_exp_min(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_min_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_bool_exp_stddev_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_stddev_samp_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_bool_exp_sum(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_sum_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_bool_exp_var_samp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('arguments', 'distinct', 'filter', 'predicate')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_select_column_stocks_ticks_aggregate_bool_exp_var_samp_arguments_columns), graphql_name='arguments')
    distinct = sgqlc.types.Field(Boolean, graphql_name='distinct')
    filter = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='filter')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(float8_comparison_exp), graphql_name='predicate')


class stocks_ticks_aggregate_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('stocks_ticks_avg_order_by', graphql_name='avg')
    count = sgqlc.types.Field(order_by, graphql_name='count')
    max = sgqlc.types.Field('stocks_ticks_max_order_by', graphql_name='max')
    min = sgqlc.types.Field('stocks_ticks_min_order_by', graphql_name='min')
    stddev = sgqlc.types.Field('stocks_ticks_stddev_order_by', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('stocks_ticks_stddev_pop_order_by', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('stocks_ticks_stddev_samp_order_by', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('stocks_ticks_sum_order_by', graphql_name='sum')
    var_pop = sgqlc.types.Field('stocks_ticks_var_pop_order_by', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('stocks_ticks_var_samp_order_by', graphql_name='var_samp')
    variance = sgqlc.types.Field('stocks_ticks_variance_order_by', graphql_name='variance')


class stocks_ticks_arr_rel_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('data', 'on_conflict')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('stocks_ticks_insert_input'))), graphql_name='data')
    on_conflict = sgqlc.types.Field('stocks_ticks_on_conflict', graphql_name='on_conflict')


class stocks_ticks_avg_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('stocks_ticks_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('stocks_ticks_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('stocks_ticks_bool_exp')), graphql_name='_or')
    exchange_timestamp = sgqlc.types.Field('timestamptz_comparison_exp', graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int_comparison_exp, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8_comparison_exp, graphql_name='last_price')
    master_datum = sgqlc.types.Field(master_data_bool_exp, graphql_name='master_datum')
    open_interest = sgqlc.types.Field(float8_comparison_exp, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8_comparison_exp, graphql_name='volume_traded')


class stocks_ticks_inc_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class stocks_ticks_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    master_datum = sgqlc.types.Field(master_data_obj_rel_insert_input, graphql_name='master_datum')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class stocks_ticks_max_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_min_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_on_conflict(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(stocks_ticks_bool_exp, graphql_name='where')


class stocks_ticks_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(order_by, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    master_datum = sgqlc.types.Field(master_data_order_by, graphql_name='master_datum')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_pk_columns_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token')
    exchange_timestamp = sgqlc.types.Field(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')


class stocks_ticks_set_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class stocks_ticks_stddev_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_stddev_pop_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_stddev_samp_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('stocks_ticks_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class stocks_ticks_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class stocks_ticks_sum_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_updates(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_inc', '_set', 'where')
    _inc = sgqlc.types.Field(stocks_ticks_inc_input, graphql_name='_inc')
    _set = sgqlc.types.Field(stocks_ticks_set_input, graphql_name='_set')
    where = sgqlc.types.Field(sgqlc.types.non_null(stocks_ticks_bool_exp), graphql_name='where')


class stocks_ticks_var_pop_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_var_samp_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class stocks_ticks_variance_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(order_by, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(order_by, graphql_name='last_price')
    open_interest = sgqlc.types.Field(order_by, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(order_by, graphql_name='volume_traded')


class timestamptz_comparison_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(timestamptz, graphql_name='_eq')
    _gt = sgqlc.types.Field(timestamptz, graphql_name='_gt')
    _gte = sgqlc.types.Field(timestamptz, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(timestamptz)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(timestamptz, graphql_name='_lt')
    _lte = sgqlc.types.Field(timestamptz, graphql_name='_lte')
    _neq = sgqlc.types.Field(timestamptz, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(timestamptz)), graphql_name='_nin')


class timetz_comparison_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_eq', '_gt', '_gte', '_in', '_is_null', '_lt', '_lte', '_neq', '_nin')
    _eq = sgqlc.types.Field(timetz, graphql_name='_eq')
    _gt = sgqlc.types.Field(timetz, graphql_name='_gt')
    _gte = sgqlc.types.Field(timetz, graphql_name='_gte')
    _in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(timetz)), graphql_name='_in')
    _is_null = sgqlc.types.Field(Boolean, graphql_name='_is_null')
    _lt = sgqlc.types.Field(timetz, graphql_name='_lt')
    _lte = sgqlc.types.Field(timetz, graphql_name='_lte')
    _neq = sgqlc.types.Field(timetz, graphql_name='_neq')
    _nin = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(timetz)), graphql_name='_nin')


class user_bool_exp(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_and', '_not', '_or', 'age', 'name')
    _and = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('user_bool_exp')), graphql_name='_and')
    _not = sgqlc.types.Field('user_bool_exp', graphql_name='_not')
    _or = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('user_bool_exp')), graphql_name='_or')
    age = sgqlc.types.Field(Int_comparison_exp, graphql_name='age')
    name = sgqlc.types.Field(String_comparison_exp, graphql_name='name')


class user_inc_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Int, graphql_name='age')


class user_insert_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('age', 'name')
    age = sgqlc.types.Field(Int, graphql_name='age')
    name = sgqlc.types.Field(String, graphql_name='name')


class user_on_conflict(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('constraint', 'update_columns', 'where')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(user_constraint), graphql_name='constraint')
    update_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(user_update_column))), graphql_name='update_columns')
    where = sgqlc.types.Field(user_bool_exp, graphql_name='where')


class user_order_by(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('age', 'name')
    age = sgqlc.types.Field(order_by, graphql_name='age')
    name = sgqlc.types.Field(order_by, graphql_name='name')


class user_pk_columns_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class user_set_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('age', 'name')
    age = sgqlc.types.Field(Int, graphql_name='age')
    name = sgqlc.types.Field(String, graphql_name='name')


class user_stream_cursor_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('initial_value', 'ordering')
    initial_value = sgqlc.types.Field(sgqlc.types.non_null('user_stream_cursor_value_input'), graphql_name='initial_value')
    ordering = sgqlc.types.Field(cursor_ordering, graphql_name='ordering')


class user_stream_cursor_value_input(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('age', 'name')
    age = sgqlc.types.Field(Int, graphql_name='age')
    name = sgqlc.types.Field(String, graphql_name='name')


class user_updates(sgqlc.types.Input):
    __schema__ = ticker_schema
    __field_names__ = ('_inc', '_set', 'where')
    _inc = sgqlc.types.Field(user_inc_input, graphql_name='_inc')
    _set = sgqlc.types.Field(user_set_input, graphql_name='_set')
    where = sgqlc.types.Field(sgqlc.types.non_null(user_bool_exp), graphql_name='where')



########################################################################
# Output Objects and Interfaces
########################################################################
class cont_futures_15min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_15min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_futures_15min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min))), graphql_name='nodes')


class cont_futures_15min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_futures_15min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_futures_15min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_futures_15min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_futures_15min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_futures_15min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_futures_15min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_futures_15min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_futures_15min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_futures_15min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_futures_15min_variance_fields', graphql_name='variance')


class cont_futures_15min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_15min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_15min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_15min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_15min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_15min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_15min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_15min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_15min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_15min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1day(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1day_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_futures_1day_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day))), graphql_name='nodes')


class cont_futures_1day_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_futures_1day_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_futures_1day_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_futures_1day_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_futures_1day_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_futures_1day_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_futures_1day_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_futures_1day_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_futures_1day_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_futures_1day_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_futures_1day_variance_fields', graphql_name='variance')


class cont_futures_1day_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1day_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1day_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1day_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1day_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1day_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1day_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1day_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1day_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1day_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1hour(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1hour_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_futures_1hour_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour))), graphql_name='nodes')


class cont_futures_1hour_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_futures_1hour_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_futures_1hour_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_futures_1hour_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_futures_1hour_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_futures_1hour_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_futures_1hour_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_futures_1hour_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_futures_1hour_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_futures_1hour_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_futures_1hour_variance_fields', graphql_name='variance')


class cont_futures_1hour_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1hour_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1hour_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1hour_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1hour_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1hour_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1hour_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1hour_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1hour_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1hour_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_futures_1min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min))), graphql_name='nodes')


class cont_futures_1min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_futures_1min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_futures_1min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_futures_1min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_futures_1min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_futures_1min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_futures_1min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_futures_1min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_futures_1min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_futures_1min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_futures_1min_variance_fields', graphql_name='variance')


class cont_futures_1min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_1min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_1min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_2hour(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_2hour_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_futures_2hour_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour))), graphql_name='nodes')


class cont_futures_2hour_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_futures_2hour_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_futures_2hour_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_futures_2hour_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_futures_2hour_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_futures_2hour_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_futures_2hour_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_futures_2hour_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_futures_2hour_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_futures_2hour_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_futures_2hour_variance_fields', graphql_name='variance')


class cont_futures_2hour_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_2hour_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_2hour_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_2hour_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_2hour_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_2hour_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_2hour_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_2hour_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_2hour_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_2hour_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_30min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_30min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_futures_30min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min))), graphql_name='nodes')


class cont_futures_30min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_futures_30min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_futures_30min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_futures_30min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_futures_30min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_futures_30min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_futures_30min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_futures_30min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_futures_30min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_futures_30min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_futures_30min_variance_fields', graphql_name='variance')


class cont_futures_30min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_30min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_30min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_30min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_30min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_30min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_30min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_30min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_30min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_30min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_3min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_3min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_futures_3min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min))), graphql_name='nodes')


class cont_futures_3min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_futures_3min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_futures_3min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_futures_3min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_futures_3min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_futures_3min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_futures_3min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_futures_3min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_futures_3min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_futures_3min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_futures_3min_variance_fields', graphql_name='variance')


class cont_futures_3min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_3min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_3min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_3min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_3min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_3min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_3min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(float8, graphql_name='volume')


class cont_futures_3min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_3min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_futures_3min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_indices_15min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_15min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_indices_15min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min))), graphql_name='nodes')


class cont_indices_15min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_indices_15min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_indices_15min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_indices_15min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_indices_15min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_indices_15min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_indices_15min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_indices_15min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_indices_15min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_indices_15min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_indices_15min_variance_fields', graphql_name='variance')


class cont_indices_15min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_15min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_15min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_15min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_15min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_15min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_15min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_15min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_15min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_15min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1hour(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1hour_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_indices_1hour_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour))), graphql_name='nodes')


class cont_indices_1hour_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_indices_1hour_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_indices_1hour_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_indices_1hour_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_indices_1hour_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_indices_1hour_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_indices_1hour_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_indices_1hour_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_indices_1hour_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_indices_1hour_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_indices_1hour_variance_fields', graphql_name='variance')


class cont_indices_1hour_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1hour_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1hour_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1hour_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1hour_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1hour_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1hour_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1hour_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1hour_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1hour_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_indices_1min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min))), graphql_name='nodes')


class cont_indices_1min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_indices_1min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_indices_1min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_indices_1min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_indices_1min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_indices_1min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_indices_1min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_indices_1min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_indices_1min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_indices_1min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_indices_1min_variance_fields', graphql_name='variance')


class cont_indices_1min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_1min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_1min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_2hour(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_2hour_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_indices_2hour_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour))), graphql_name='nodes')


class cont_indices_2hour_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_indices_2hour_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_indices_2hour_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_indices_2hour_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_indices_2hour_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_indices_2hour_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_indices_2hour_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_indices_2hour_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_indices_2hour_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_indices_2hour_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_indices_2hour_variance_fields', graphql_name='variance')


class cont_indices_2hour_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_2hour_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_2hour_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_2hour_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_2hour_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_2hour_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_2hour_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_2hour_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_2hour_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_2hour_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_30min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_30min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_indices_30min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min))), graphql_name='nodes')


class cont_indices_30min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_indices_30min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_indices_30min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_indices_30min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_indices_30min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_indices_30min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_indices_30min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_indices_30min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_indices_30min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_indices_30min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_indices_30min_variance_fields', graphql_name='variance')


class cont_indices_30min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_30min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_30min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_30min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_30min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_30min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_30min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_30min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_30min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_30min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_3min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_3min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_indices_3min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min))), graphql_name='nodes')


class cont_indices_3min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_indices_3min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_indices_3min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_indices_3min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_indices_3min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_indices_3min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_indices_3min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_indices_3min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_indices_3min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_indices_3min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_indices_3min_variance_fields', graphql_name='variance')


class cont_indices_3min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_3min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_3min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_3min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_3min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_3min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_3min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')


class cont_indices_3min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_3min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_indices_3min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')


class cont_options_1min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(Int, graphql_name='volume')


class cont_options_1min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('cont_options_1min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min))), graphql_name='nodes')


class cont_options_1min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('cont_options_1min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('cont_options_1min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('cont_options_1min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('cont_options_1min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('cont_options_1min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('cont_options_1min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('cont_options_1min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('cont_options_1min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('cont_options_1min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('cont_options_1min_variance_fields', graphql_name='variance')


class cont_options_1min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_options_1min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(Int, graphql_name='volume')


class cont_options_1min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(Int, graphql_name='volume')


class cont_options_1min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_options_1min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_options_1min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_options_1min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume = sgqlc.types.Field(Int, graphql_name='volume')


class cont_options_1min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_options_1min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class cont_options_1min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'volume')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume = sgqlc.types.Field(Float, graphql_name='volume')


class features(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'build_up_status', 'close', 'expiry', 'high', 'instrument_token', 'low', 'name', 'ohl_status', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'tradingsymbol', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    build_up_status = sgqlc.types.Field(String, graphql_name='build_up_status')
    close = sgqlc.types.Field(float8, graphql_name='close')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    name = sgqlc.types.Field(String, graphql_name='name')
    ohl_status = sgqlc.types.Field(String, graphql_name='ohl_status')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class features_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('features_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(features))), graphql_name='nodes')


class features_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('features_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('features_max_fields', graphql_name='max')
    min = sgqlc.types.Field('features_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('features_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('features_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('features_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('features_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('features_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('features_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('features_variance_fields', graphql_name='variance')


class features_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class features_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'build_up_status', 'close', 'expiry', 'high', 'instrument_token', 'low', 'name', 'ohl_status', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'tradingsymbol', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    build_up_status = sgqlc.types.Field(String, graphql_name='build_up_status')
    close = sgqlc.types.Field(float8, graphql_name='close')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    name = sgqlc.types.Field(String, graphql_name='name')
    ohl_status = sgqlc.types.Field(String, graphql_name='ohl_status')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class features_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'build_up_status', 'close', 'expiry', 'high', 'instrument_token', 'low', 'name', 'ohl_status', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'tradingsymbol', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    build_up_status = sgqlc.types.Field(String, graphql_name='build_up_status')
    close = sgqlc.types.Field(float8, graphql_name='close')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    name = sgqlc.types.Field(String, graphql_name='name')
    ohl_status = sgqlc.types.Field(String, graphql_name='ohl_status')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class features_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class features_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class features_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class features_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class features_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class features_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class features_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_15min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_15min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('futures_15min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min))), graphql_name='nodes')


class futures_15min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_15min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('futures_15min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('futures_15min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('futures_15min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_15min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_15min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_15min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_15min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_15min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_15min_variance_fields', graphql_name='variance')


class futures_15min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_15min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_15min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_15min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_15min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_15min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_15min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_15min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_15min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_15min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1day(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1day_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('futures_1day_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day))), graphql_name='nodes')


class futures_1day_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_1day_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('futures_1day_max_fields', graphql_name='max')
    min = sgqlc.types.Field('futures_1day_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('futures_1day_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_1day_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_1day_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_1day_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_1day_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_1day_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_1day_variance_fields', graphql_name='variance')


class futures_1day_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1day_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1day_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1day_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1day_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1day_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1day_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1day_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1day_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1day_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1hour(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1hour_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('futures_1hour_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour))), graphql_name='nodes')


class futures_1hour_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_1hour_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('futures_1hour_max_fields', graphql_name='max')
    min = sgqlc.types.Field('futures_1hour_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('futures_1hour_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_1hour_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_1hour_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_1hour_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_1hour_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_1hour_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_1hour_variance_fields', graphql_name='variance')


class futures_1hour_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1hour_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1hour_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1hour_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1hour_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1hour_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1hour_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1hour_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1hour_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1hour_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('futures_1min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min))), graphql_name='nodes')


class futures_1min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_1min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('futures_1min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('futures_1min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('futures_1min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_1min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_1min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_1min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_1min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_1min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_1min_variance_fields', graphql_name='variance')


class futures_1min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_1min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_1min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_2hour(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_2hour_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('futures_2hour_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour))), graphql_name='nodes')


class futures_2hour_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_2hour_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('futures_2hour_max_fields', graphql_name='max')
    min = sgqlc.types.Field('futures_2hour_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('futures_2hour_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_2hour_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_2hour_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_2hour_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_2hour_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_2hour_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_2hour_variance_fields', graphql_name='variance')


class futures_2hour_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_2hour_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_2hour_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_2hour_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_2hour_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_2hour_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_2hour_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_2hour_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_2hour_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_2hour_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_30min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_30min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('futures_30min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min))), graphql_name='nodes')


class futures_30min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_30min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('futures_30min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('futures_30min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('futures_30min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_30min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_30min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_30min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_30min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_30min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_30min_variance_fields', graphql_name='variance')


class futures_30min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_30min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_30min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_30min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_30min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_30min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_30min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_30min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_30min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_30min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_3min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_3min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('futures_3min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min))), graphql_name='nodes')


class futures_3min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_3min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('futures_3min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('futures_3min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('futures_3min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_3min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_3min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_3min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_3min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_3min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_3min_variance_fields', graphql_name='variance')


class futures_3min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_3min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_3min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_3min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_3min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_3min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_3min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(float8, graphql_name='volume')
    volume_change = sgqlc.types.Field(float8, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(float8, graphql_name='volume_change_per')


class futures_3min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_3min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_3min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class futures_ticks(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')
    last_price = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='last_price')
    master_datum = sgqlc.types.Field(sgqlc.types.non_null('master_data'), graphql_name='master_datum')
    open_interest = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='volume_traded')


class futures_ticks_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('futures_ticks_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks))), graphql_name='nodes')


class futures_ticks_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('futures_ticks_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('futures_ticks_max_fields', graphql_name='max')
    min = sgqlc.types.Field('futures_ticks_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('futures_ticks_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('futures_ticks_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('futures_ticks_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('futures_ticks_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('futures_ticks_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('futures_ticks_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('futures_ticks_variance_fields', graphql_name='variance')


class futures_ticks_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class futures_ticks_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class futures_ticks_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class futures_ticks_mutation_response(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks))), graphql_name='returning')


class futures_ticks_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class futures_ticks_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class futures_ticks_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class futures_ticks_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class futures_ticks_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class futures_ticks_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class futures_ticks_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class indices_ticks(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum')
    exchange_timestamp = sgqlc.types.Field(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')
    last_price = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='last_price')
    master_datum = sgqlc.types.Field(sgqlc.types.non_null('master_data'), graphql_name='master_datum')


class indices_ticks_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('indices_ticks_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks))), graphql_name='nodes')


class indices_ticks_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('indices_ticks_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('indices_ticks_max_fields', graphql_name='max')
    min = sgqlc.types.Field('indices_ticks_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('indices_ticks_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('indices_ticks_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('indices_ticks_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('indices_ticks_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('indices_ticks_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('indices_ticks_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('indices_ticks_variance_fields', graphql_name='variance')


class indices_ticks_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')


class indices_ticks_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')


class indices_ticks_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')


class indices_ticks_mutation_response(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks))), graphql_name='returning')


class indices_ticks_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')


class indices_ticks_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')


class indices_ticks_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')


class indices_ticks_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')


class indices_ticks_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')


class indices_ticks_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')


class indices_ticks_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')


class master_data(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange', 'expiry', 'futures_ticks', 'futures_ticks_aggregate', 'indices_ticks', 'indices_ticks_aggregate', 'instrument_token', 'instrument_type', 'is_nifty', 'name', 'options_ticks', 'options_ticks_aggregate', 'segment', 'stocks_ticks', 'stocks_ticks_aggregate', 'strike', 'tradingsymbol')
    exchange = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='exchange')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    futures_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_ticks'))), graphql_name='futures_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_ticks_aggregate'), graphql_name='futures_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    indices_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('indices_ticks'))), graphql_name='indices_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(indices_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    indices_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('indices_ticks_aggregate'), graphql_name='indices_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(indices_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')
    instrument_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='instrument_type')
    is_nifty = sgqlc.types.Field(Boolean, graphql_name='is_nifty')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    options_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_ticks'))), graphql_name='options_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    options_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('options_ticks_aggregate'), graphql_name='options_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    segment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='segment')
    stocks_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('stocks_ticks'))), graphql_name='stocks_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(stocks_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    stocks_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('stocks_ticks_aggregate'), graphql_name='stocks_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(stocks_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    strike = sgqlc.types.Field(float8, graphql_name='strike')
    tradingsymbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tradingsymbol')


class master_data_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('master_data_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(master_data))), graphql_name='nodes')


class master_data_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('master_data_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('master_data_max_fields', graphql_name='max')
    min = sgqlc.types.Field('master_data_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('master_data_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('master_data_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('master_data_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('master_data_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('master_data_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('master_data_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('master_data_variance_fields', graphql_name='variance')


class master_data_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    strike = sgqlc.types.Field(Float, graphql_name='strike')


class master_data_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange', 'expiry', 'instrument_token', 'instrument_type', 'name', 'segment', 'strike', 'tradingsymbol')
    exchange = sgqlc.types.Field(String, graphql_name='exchange')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    instrument_type = sgqlc.types.Field(String, graphql_name='instrument_type')
    name = sgqlc.types.Field(String, graphql_name='name')
    segment = sgqlc.types.Field(String, graphql_name='segment')
    strike = sgqlc.types.Field(float8, graphql_name='strike')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')


class master_data_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange', 'expiry', 'instrument_token', 'instrument_type', 'name', 'segment', 'strike', 'tradingsymbol')
    exchange = sgqlc.types.Field(String, graphql_name='exchange')
    expiry = sgqlc.types.Field(date, graphql_name='expiry')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    instrument_type = sgqlc.types.Field(String, graphql_name='instrument_type')
    name = sgqlc.types.Field(String, graphql_name='name')
    segment = sgqlc.types.Field(String, graphql_name='segment')
    strike = sgqlc.types.Field(float8, graphql_name='strike')
    tradingsymbol = sgqlc.types.Field(String, graphql_name='tradingsymbol')


class master_data_mutation_response(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(master_data))), graphql_name='returning')


class master_data_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    strike = sgqlc.types.Field(Float, graphql_name='strike')


class master_data_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    strike = sgqlc.types.Field(Float, graphql_name='strike')


class master_data_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    strike = sgqlc.types.Field(Float, graphql_name='strike')


class master_data_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    strike = sgqlc.types.Field(float8, graphql_name='strike')


class master_data_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    strike = sgqlc.types.Field(Float, graphql_name='strike')


class master_data_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    strike = sgqlc.types.Field(Float, graphql_name='strike')


class master_data_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'strike')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    strike = sgqlc.types.Field(Float, graphql_name='strike')


class mutation_root(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('delete_futures_ticks', 'delete_futures_ticks_by_pk', 'delete_indices_ticks', 'delete_indices_ticks_by_pk', 'delete_master_data', 'delete_master_data_by_pk', 'delete_options_ticks', 'delete_options_ticks_by_pk', 'delete_stocks_ticks', 'delete_stocks_ticks_by_pk', 'delete_user', 'delete_user_by_pk', 'insert_futures_ticks', 'insert_futures_ticks_one', 'insert_indices_ticks', 'insert_indices_ticks_one', 'insert_master_data', 'insert_master_data_one', 'insert_options_ticks', 'insert_options_ticks_one', 'insert_stocks_ticks', 'insert_stocks_ticks_one', 'insert_user', 'insert_user_one', 'update_futures_ticks', 'update_futures_ticks_by_pk', 'update_futures_ticks_many', 'update_indices_ticks', 'update_indices_ticks_by_pk', 'update_indices_ticks_many', 'update_master_data', 'update_master_data_by_pk', 'update_master_data_many', 'update_options_ticks', 'update_options_ticks_by_pk', 'update_options_ticks_many', 'update_stocks_ticks', 'update_stocks_ticks_by_pk', 'update_stocks_ticks_many', 'update_user', 'update_user_by_pk', 'update_user_many')
    delete_futures_ticks = sgqlc.types.Field(futures_ticks_mutation_response, graphql_name='delete_futures_ticks', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(futures_ticks_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_futures_ticks_by_pk = sgqlc.types.Field(futures_ticks, graphql_name='delete_futures_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    delete_indices_ticks = sgqlc.types.Field(indices_ticks_mutation_response, graphql_name='delete_indices_ticks', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(indices_ticks_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_indices_ticks_by_pk = sgqlc.types.Field(indices_ticks, graphql_name='delete_indices_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    delete_master_data = sgqlc.types.Field(master_data_mutation_response, graphql_name='delete_master_data', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(master_data_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_master_data_by_pk = sgqlc.types.Field(master_data, graphql_name='delete_master_data_by_pk', args=sgqlc.types.ArgDict((
        ('exchange', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='exchange', default=None)),
        ('tradingsymbol', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tradingsymbol', default=None)),
))
    )
    delete_options_ticks = sgqlc.types.Field('options_ticks_mutation_response', graphql_name='delete_options_ticks', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(options_ticks_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_options_ticks_by_pk = sgqlc.types.Field('options_ticks', graphql_name='delete_options_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    delete_stocks_ticks = sgqlc.types.Field('stocks_ticks_mutation_response', graphql_name='delete_stocks_ticks', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(stocks_ticks_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_stocks_ticks_by_pk = sgqlc.types.Field('stocks_ticks', graphql_name='delete_stocks_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    delete_user = sgqlc.types.Field('user_mutation_response', graphql_name='delete_user', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(user_bool_exp), graphql_name='where', default=None)),
))
    )
    delete_user_by_pk = sgqlc.types.Field('user', graphql_name='delete_user_by_pk', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    insert_futures_ticks = sgqlc.types.Field(futures_ticks_mutation_response, graphql_name='insert_futures_ticks', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(futures_ticks_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_futures_ticks_one = sgqlc.types.Field(futures_ticks, graphql_name='insert_futures_ticks_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(futures_ticks_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(futures_ticks_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_indices_ticks = sgqlc.types.Field(indices_ticks_mutation_response, graphql_name='insert_indices_ticks', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(indices_ticks_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_indices_ticks_one = sgqlc.types.Field(indices_ticks, graphql_name='insert_indices_ticks_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(indices_ticks_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(indices_ticks_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_master_data = sgqlc.types.Field(master_data_mutation_response, graphql_name='insert_master_data', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(master_data_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(master_data_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_master_data_one = sgqlc.types.Field(master_data, graphql_name='insert_master_data_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(master_data_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(master_data_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_options_ticks = sgqlc.types.Field('options_ticks_mutation_response', graphql_name='insert_options_ticks', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(options_ticks_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_options_ticks_one = sgqlc.types.Field('options_ticks', graphql_name='insert_options_ticks_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(options_ticks_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(options_ticks_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_stocks_ticks = sgqlc.types.Field('stocks_ticks_mutation_response', graphql_name='insert_stocks_ticks', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(stocks_ticks_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_stocks_ticks_one = sgqlc.types.Field('stocks_ticks', graphql_name='insert_stocks_ticks_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(stocks_ticks_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(stocks_ticks_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_user = sgqlc.types.Field('user_mutation_response', graphql_name='insert_user', args=sgqlc.types.ArgDict((
        ('objects', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(user_insert_input))), graphql_name='objects', default=None)),
        ('on_conflict', sgqlc.types.Arg(user_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    insert_user_one = sgqlc.types.Field('user', graphql_name='insert_user_one', args=sgqlc.types.ArgDict((
        ('object', sgqlc.types.Arg(sgqlc.types.non_null(user_insert_input), graphql_name='object', default=None)),
        ('on_conflict', sgqlc.types.Arg(user_on_conflict, graphql_name='on_conflict', default=None)),
))
    )
    update_futures_ticks = sgqlc.types.Field(futures_ticks_mutation_response, graphql_name='update_futures_ticks', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(futures_ticks_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(futures_ticks_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(futures_ticks_bool_exp), graphql_name='where', default=None)),
))
    )
    update_futures_ticks_by_pk = sgqlc.types.Field(futures_ticks, graphql_name='update_futures_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(futures_ticks_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(futures_ticks_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(futures_ticks_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_futures_ticks_many = sgqlc.types.Field(sgqlc.types.list_of(futures_ticks_mutation_response), graphql_name='update_futures_ticks_many', args=sgqlc.types.ArgDict((
        ('updates', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_updates))), graphql_name='updates', default=None)),
))
    )
    update_indices_ticks = sgqlc.types.Field(indices_ticks_mutation_response, graphql_name='update_indices_ticks', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(indices_ticks_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(indices_ticks_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(indices_ticks_bool_exp), graphql_name='where', default=None)),
))
    )
    update_indices_ticks_by_pk = sgqlc.types.Field(indices_ticks, graphql_name='update_indices_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(indices_ticks_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(indices_ticks_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(indices_ticks_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_indices_ticks_many = sgqlc.types.Field(sgqlc.types.list_of(indices_ticks_mutation_response), graphql_name='update_indices_ticks_many', args=sgqlc.types.ArgDict((
        ('updates', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_updates))), graphql_name='updates', default=None)),
))
    )
    update_master_data = sgqlc.types.Field(master_data_mutation_response, graphql_name='update_master_data', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(master_data_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(master_data_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(master_data_bool_exp), graphql_name='where', default=None)),
))
    )
    update_master_data_by_pk = sgqlc.types.Field(master_data, graphql_name='update_master_data_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(master_data_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(master_data_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(master_data_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_master_data_many = sgqlc.types.Field(sgqlc.types.list_of(master_data_mutation_response), graphql_name='update_master_data_many', args=sgqlc.types.ArgDict((
        ('updates', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(master_data_updates))), graphql_name='updates', default=None)),
))
    )
    update_options_ticks = sgqlc.types.Field('options_ticks_mutation_response', graphql_name='update_options_ticks', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(options_ticks_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(options_ticks_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(options_ticks_bool_exp), graphql_name='where', default=None)),
))
    )
    update_options_ticks_by_pk = sgqlc.types.Field('options_ticks', graphql_name='update_options_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(options_ticks_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(options_ticks_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(options_ticks_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_options_ticks_many = sgqlc.types.Field(sgqlc.types.list_of('options_ticks_mutation_response'), graphql_name='update_options_ticks_many', args=sgqlc.types.ArgDict((
        ('updates', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_updates))), graphql_name='updates', default=None)),
))
    )
    update_stocks_ticks = sgqlc.types.Field('stocks_ticks_mutation_response', graphql_name='update_stocks_ticks', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(stocks_ticks_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(stocks_ticks_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(stocks_ticks_bool_exp), graphql_name='where', default=None)),
))
    )
    update_stocks_ticks_by_pk = sgqlc.types.Field('stocks_ticks', graphql_name='update_stocks_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(stocks_ticks_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(stocks_ticks_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(stocks_ticks_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_stocks_ticks_many = sgqlc.types.Field(sgqlc.types.list_of('stocks_ticks_mutation_response'), graphql_name='update_stocks_ticks_many', args=sgqlc.types.ArgDict((
        ('updates', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_updates))), graphql_name='updates', default=None)),
))
    )
    update_user = sgqlc.types.Field('user_mutation_response', graphql_name='update_user', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(user_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(user_set_input, graphql_name='_set', default=None)),
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(user_bool_exp), graphql_name='where', default=None)),
))
    )
    update_user_by_pk = sgqlc.types.Field('user', graphql_name='update_user_by_pk', args=sgqlc.types.ArgDict((
        ('_inc', sgqlc.types.Arg(user_inc_input, graphql_name='_inc', default=None)),
        ('_set', sgqlc.types.Arg(user_set_input, graphql_name='_set', default=None)),
        ('pk_columns', sgqlc.types.Arg(sgqlc.types.non_null(user_pk_columns_input), graphql_name='pk_columns', default=None)),
))
    )
    update_user_many = sgqlc.types.Field(sgqlc.types.list_of('user_mutation_response'), graphql_name='update_user_many', args=sgqlc.types.ArgDict((
        ('updates', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(user_updates))), graphql_name='updates', default=None)),
))
    )


class options_15min(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Int, graphql_name='volume')
    volume_change = sgqlc.types.Field(Int, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Int, graphql_name='volume_change_per')


class options_15min_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('options_15min_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(options_15min))), graphql_name='nodes')


class options_15min_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('options_15min_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('options_15min_max_fields', graphql_name='max')
    min = sgqlc.types.Field('options_15min_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('options_15min_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('options_15min_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('options_15min_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('options_15min_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('options_15min_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('options_15min_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('options_15min_variance_fields', graphql_name='variance')


class options_15min_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class options_15min_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Int, graphql_name='volume')
    volume_change = sgqlc.types.Field(Int, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Int, graphql_name='volume_change_per')


class options_15min_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'bucket', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    bucket = sgqlc.types.Field(timestamptz, graphql_name='bucket')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Int, graphql_name='volume')
    volume_change = sgqlc.types.Field(Int, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Int, graphql_name='volume_change_per')


class options_15min_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class options_15min_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class options_15min_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class options_15min_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(float8, graphql_name='avg_price')
    close = sgqlc.types.Field(float8, graphql_name='close')
    high = sgqlc.types.Field(float8, graphql_name='high')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    low = sgqlc.types.Field(float8, graphql_name='low')
    open = sgqlc.types.Field(float8, graphql_name='open')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(float8, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(float8, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(float8, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(float8, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Int, graphql_name='volume')
    volume_change = sgqlc.types.Field(Int, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Int, graphql_name='volume_change_per')


class options_15min_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class options_15min_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class options_15min_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg_price', 'close', 'high', 'instrument_token', 'low', 'open', 'open_interest', 'open_interest_change', 'open_interest_change_per', 'price_change', 'price_change_per', 'volume', 'volume_change', 'volume_change_per')
    avg_price = sgqlc.types.Field(Float, graphql_name='avg_price')
    close = sgqlc.types.Field(Float, graphql_name='close')
    high = sgqlc.types.Field(Float, graphql_name='high')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    low = sgqlc.types.Field(Float, graphql_name='low')
    open = sgqlc.types.Field(Float, graphql_name='open')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    open_interest_change = sgqlc.types.Field(Float, graphql_name='open_interest_change')
    open_interest_change_per = sgqlc.types.Field(Float, graphql_name='open_interest_change_per')
    price_change = sgqlc.types.Field(Float, graphql_name='price_change')
    price_change_per = sgqlc.types.Field(Float, graphql_name='price_change_per')
    volume = sgqlc.types.Field(Float, graphql_name='volume')
    volume_change = sgqlc.types.Field(Float, graphql_name='volume_change')
    volume_change_per = sgqlc.types.Field(Float, graphql_name='volume_change_per')


class options_chain(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_build_up_status', 'ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_trend', 'ce_volume', 'es_time_field', 'pcr_oi', 'pcr_volumn', 'pe_build_up_status', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_trend', 'pe_volume', 'ps_time_field')
    ce_build_up_status = sgqlc.types.Field(String, graphql_name='ce_build_up_status')
    ce_change_pts = sgqlc.types.Field(float8, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(float8, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(float8, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(float8, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(float8, graphql_name='ce_strike_price')
    ce_trend = sgqlc.types.Field(String, graphql_name='ce_trend')
    ce_volume = sgqlc.types.Field(Int, graphql_name='ce_volume')
    es_time_field = sgqlc.types.Field(timetz, graphql_name='es_time_field')
    pcr_oi = sgqlc.types.Field(float8, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Int, graphql_name='pcr_volumn')
    pe_build_up_status = sgqlc.types.Field(String, graphql_name='pe_build_up_status')
    pe_change_pts = sgqlc.types.Field(float8, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(float8, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(float8, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(float8, graphql_name='pe_oi_chg')
    pe_trend = sgqlc.types.Field(String, graphql_name='pe_trend')
    pe_volume = sgqlc.types.Field(Int, graphql_name='pe_volume')
    ps_time_field = sgqlc.types.Field(timetz, graphql_name='ps_time_field')


class options_chain_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('options_chain_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(options_chain))), graphql_name='nodes')


class options_chain_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('options_chain_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('options_chain_max_fields', graphql_name='max')
    min = sgqlc.types.Field('options_chain_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('options_chain_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('options_chain_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('options_chain_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('options_chain_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('options_chain_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('options_chain_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('options_chain_variance_fields', graphql_name='variance')


class options_chain_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_volume', 'pcr_oi', 'pcr_volumn', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_volume')
    ce_change_pts = sgqlc.types.Field(Float, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(Float, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(Float, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(Float, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(Float, graphql_name='ce_strike_price')
    ce_volume = sgqlc.types.Field(Float, graphql_name='ce_volume')
    pcr_oi = sgqlc.types.Field(Float, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Float, graphql_name='pcr_volumn')
    pe_change_pts = sgqlc.types.Field(Float, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(Float, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(Float, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(Float, graphql_name='pe_oi_chg')
    pe_volume = sgqlc.types.Field(Float, graphql_name='pe_volume')


class options_chain_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_build_up_status', 'ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_trend', 'ce_volume', 'es_time_field', 'pcr_oi', 'pcr_volumn', 'pe_build_up_status', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_trend', 'pe_volume', 'ps_time_field')
    ce_build_up_status = sgqlc.types.Field(String, graphql_name='ce_build_up_status')
    ce_change_pts = sgqlc.types.Field(float8, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(float8, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(float8, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(float8, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(float8, graphql_name='ce_strike_price')
    ce_trend = sgqlc.types.Field(String, graphql_name='ce_trend')
    ce_volume = sgqlc.types.Field(Int, graphql_name='ce_volume')
    es_time_field = sgqlc.types.Field(timetz, graphql_name='es_time_field')
    pcr_oi = sgqlc.types.Field(float8, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Int, graphql_name='pcr_volumn')
    pe_build_up_status = sgqlc.types.Field(String, graphql_name='pe_build_up_status')
    pe_change_pts = sgqlc.types.Field(float8, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(float8, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(float8, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(float8, graphql_name='pe_oi_chg')
    pe_trend = sgqlc.types.Field(String, graphql_name='pe_trend')
    pe_volume = sgqlc.types.Field(Int, graphql_name='pe_volume')
    ps_time_field = sgqlc.types.Field(timetz, graphql_name='ps_time_field')


class options_chain_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_build_up_status', 'ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_trend', 'ce_volume', 'es_time_field', 'pcr_oi', 'pcr_volumn', 'pe_build_up_status', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_trend', 'pe_volume', 'ps_time_field')
    ce_build_up_status = sgqlc.types.Field(String, graphql_name='ce_build_up_status')
    ce_change_pts = sgqlc.types.Field(float8, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(float8, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(float8, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(float8, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(float8, graphql_name='ce_strike_price')
    ce_trend = sgqlc.types.Field(String, graphql_name='ce_trend')
    ce_volume = sgqlc.types.Field(Int, graphql_name='ce_volume')
    es_time_field = sgqlc.types.Field(timetz, graphql_name='es_time_field')
    pcr_oi = sgqlc.types.Field(float8, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Int, graphql_name='pcr_volumn')
    pe_build_up_status = sgqlc.types.Field(String, graphql_name='pe_build_up_status')
    pe_change_pts = sgqlc.types.Field(float8, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(float8, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(float8, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(float8, graphql_name='pe_oi_chg')
    pe_trend = sgqlc.types.Field(String, graphql_name='pe_trend')
    pe_volume = sgqlc.types.Field(Int, graphql_name='pe_volume')
    ps_time_field = sgqlc.types.Field(timetz, graphql_name='ps_time_field')


class options_chain_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_volume', 'pcr_oi', 'pcr_volumn', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_volume')
    ce_change_pts = sgqlc.types.Field(Float, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(Float, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(Float, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(Float, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(Float, graphql_name='ce_strike_price')
    ce_volume = sgqlc.types.Field(Float, graphql_name='ce_volume')
    pcr_oi = sgqlc.types.Field(Float, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Float, graphql_name='pcr_volumn')
    pe_change_pts = sgqlc.types.Field(Float, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(Float, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(Float, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(Float, graphql_name='pe_oi_chg')
    pe_volume = sgqlc.types.Field(Float, graphql_name='pe_volume')


class options_chain_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_volume', 'pcr_oi', 'pcr_volumn', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_volume')
    ce_change_pts = sgqlc.types.Field(Float, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(Float, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(Float, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(Float, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(Float, graphql_name='ce_strike_price')
    ce_volume = sgqlc.types.Field(Float, graphql_name='ce_volume')
    pcr_oi = sgqlc.types.Field(Float, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Float, graphql_name='pcr_volumn')
    pe_change_pts = sgqlc.types.Field(Float, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(Float, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(Float, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(Float, graphql_name='pe_oi_chg')
    pe_volume = sgqlc.types.Field(Float, graphql_name='pe_volume')


class options_chain_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_volume', 'pcr_oi', 'pcr_volumn', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_volume')
    ce_change_pts = sgqlc.types.Field(Float, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(Float, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(Float, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(Float, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(Float, graphql_name='ce_strike_price')
    ce_volume = sgqlc.types.Field(Float, graphql_name='ce_volume')
    pcr_oi = sgqlc.types.Field(Float, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Float, graphql_name='pcr_volumn')
    pe_change_pts = sgqlc.types.Field(Float, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(Float, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(Float, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(Float, graphql_name='pe_oi_chg')
    pe_volume = sgqlc.types.Field(Float, graphql_name='pe_volume')


class options_chain_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_volume', 'pcr_oi', 'pcr_volumn', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_volume')
    ce_change_pts = sgqlc.types.Field(float8, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(float8, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(float8, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(float8, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(float8, graphql_name='ce_strike_price')
    ce_volume = sgqlc.types.Field(Int, graphql_name='ce_volume')
    pcr_oi = sgqlc.types.Field(float8, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Int, graphql_name='pcr_volumn')
    pe_change_pts = sgqlc.types.Field(float8, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(float8, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(float8, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(float8, graphql_name='pe_oi_chg')
    pe_volume = sgqlc.types.Field(Int, graphql_name='pe_volume')


class options_chain_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_volume', 'pcr_oi', 'pcr_volumn', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_volume')
    ce_change_pts = sgqlc.types.Field(Float, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(Float, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(Float, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(Float, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(Float, graphql_name='ce_strike_price')
    ce_volume = sgqlc.types.Field(Float, graphql_name='ce_volume')
    pcr_oi = sgqlc.types.Field(Float, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Float, graphql_name='pcr_volumn')
    pe_change_pts = sgqlc.types.Field(Float, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(Float, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(Float, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(Float, graphql_name='pe_oi_chg')
    pe_volume = sgqlc.types.Field(Float, graphql_name='pe_volume')


class options_chain_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_volume', 'pcr_oi', 'pcr_volumn', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_volume')
    ce_change_pts = sgqlc.types.Field(Float, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(Float, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(Float, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(Float, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(Float, graphql_name='ce_strike_price')
    ce_volume = sgqlc.types.Field(Float, graphql_name='ce_volume')
    pcr_oi = sgqlc.types.Field(Float, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Float, graphql_name='pcr_volumn')
    pe_change_pts = sgqlc.types.Field(Float, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(Float, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(Float, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(Float, graphql_name='pe_oi_chg')
    pe_volume = sgqlc.types.Field(Float, graphql_name='pe_volume')


class options_chain_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('ce_change_pts', 'ce_ltp', 'ce_oi', 'ce_oi_chg', 'ce_strike_price', 'ce_volume', 'pcr_oi', 'pcr_volumn', 'pe_change_pts', 'pe_ltp', 'pe_oi', 'pe_oi_chg', 'pe_volume')
    ce_change_pts = sgqlc.types.Field(Float, graphql_name='ce_change_pts')
    ce_ltp = sgqlc.types.Field(Float, graphql_name='ce_ltp')
    ce_oi = sgqlc.types.Field(Float, graphql_name='ce_oi')
    ce_oi_chg = sgqlc.types.Field(Float, graphql_name='ce_oi_chg')
    ce_strike_price = sgqlc.types.Field(Float, graphql_name='ce_strike_price')
    ce_volume = sgqlc.types.Field(Float, graphql_name='ce_volume')
    pcr_oi = sgqlc.types.Field(Float, graphql_name='pcr_oi')
    pcr_volumn = sgqlc.types.Field(Float, graphql_name='pcr_volumn')
    pe_change_pts = sgqlc.types.Field(Float, graphql_name='pe_change_pts')
    pe_ltp = sgqlc.types.Field(Float, graphql_name='pe_ltp')
    pe_oi = sgqlc.types.Field(Float, graphql_name='pe_oi')
    pe_oi_chg = sgqlc.types.Field(Float, graphql_name='pe_oi_chg')
    pe_volume = sgqlc.types.Field(Float, graphql_name='pe_volume')


class options_ticks(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')
    last_price = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='last_price')
    master_datum = sgqlc.types.Field(sgqlc.types.non_null(master_data), graphql_name='master_datum')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='volume_traded')


class options_ticks_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('options_ticks_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks))), graphql_name='nodes')


class options_ticks_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('options_ticks_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('options_ticks_max_fields', graphql_name='max')
    min = sgqlc.types.Field('options_ticks_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('options_ticks_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('options_ticks_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('options_ticks_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('options_ticks_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('options_ticks_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('options_ticks_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('options_ticks_variance_fields', graphql_name='variance')


class options_ticks_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class options_ticks_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Int, graphql_name='volume_traded')


class options_ticks_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Int, graphql_name='volume_traded')


class options_ticks_mutation_response(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks))), graphql_name='returning')


class options_ticks_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class options_ticks_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class options_ticks_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class options_ticks_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Int, graphql_name='volume_traded')


class options_ticks_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class options_ticks_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class options_ticks_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class query_root(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('cont_futures_15min', 'cont_futures_15min_aggregate', 'cont_futures_1day', 'cont_futures_1day_aggregate', 'cont_futures_1hour', 'cont_futures_1hour_aggregate', 'cont_futures_1min', 'cont_futures_1min_aggregate', 'cont_futures_2hour', 'cont_futures_2hour_aggregate', 'cont_futures_30min', 'cont_futures_30min_aggregate', 'cont_futures_3min', 'cont_futures_3min_aggregate', 'cont_indices_15min', 'cont_indices_15min_aggregate', 'cont_indices_1hour', 'cont_indices_1hour_aggregate', 'cont_indices_1min', 'cont_indices_1min_aggregate', 'cont_indices_2hour', 'cont_indices_2hour_aggregate', 'cont_indices_30min', 'cont_indices_30min_aggregate', 'cont_indices_3min', 'cont_indices_3min_aggregate', 'cont_options_1min', 'cont_options_1min_aggregate', 'features', 'features_aggregate', 'futures_15min', 'futures_15min_aggregate', 'futures_1day', 'futures_1day_aggregate', 'futures_1hour', 'futures_1hour_aggregate', 'futures_1min', 'futures_1min_aggregate', 'futures_2hour', 'futures_2hour_aggregate', 'futures_30min', 'futures_30min_aggregate', 'futures_3min', 'futures_3min_aggregate', 'futures_ticks', 'futures_ticks_aggregate', 'futures_ticks_by_pk', 'indices_ticks', 'indices_ticks_aggregate', 'indices_ticks_by_pk', 'master_data', 'master_data_aggregate', 'master_data_by_pk', 'options_15min', 'options_15min_aggregate', 'options_chain', 'options_chain_aggregate', 'options_ticks', 'options_ticks_aggregate', 'options_ticks_by_pk', 'stocks_ticks', 'stocks_ticks_aggregate', 'stocks_ticks_by_pk', 'user', 'user_aggregate', 'user_by_pk')
    cont_futures_15min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_15min'))), graphql_name='cont_futures_15min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_15min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_15min_aggregate'), graphql_name='cont_futures_15min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1day = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1day'))), graphql_name='cont_futures_1day', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1day_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1day_aggregate'), graphql_name='cont_futures_1day_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1hour'))), graphql_name='cont_futures_1hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1hour_aggregate'), graphql_name='cont_futures_1hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1min'))), graphql_name='cont_futures_1min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1min_aggregate'), graphql_name='cont_futures_1min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_2hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_2hour'))), graphql_name='cont_futures_2hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_2hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_2hour_aggregate'), graphql_name='cont_futures_2hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_30min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_30min'))), graphql_name='cont_futures_30min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_30min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_30min_aggregate'), graphql_name='cont_futures_30min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_3min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_3min'))), graphql_name='cont_futures_3min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_3min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_3min_aggregate'), graphql_name='cont_futures_3min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_15min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_15min'))), graphql_name='cont_indices_15min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_15min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_15min_aggregate'), graphql_name='cont_indices_15min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1hour'))), graphql_name='cont_indices_1hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_1hour_aggregate'), graphql_name='cont_indices_1hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1min'))), graphql_name='cont_indices_1min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_1min_aggregate'), graphql_name='cont_indices_1min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_2hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_2hour'))), graphql_name='cont_indices_2hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_2hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_2hour_aggregate'), graphql_name='cont_indices_2hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_30min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_30min'))), graphql_name='cont_indices_30min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_30min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_30min_aggregate'), graphql_name='cont_indices_30min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_3min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_3min'))), graphql_name='cont_indices_3min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_3min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_3min_aggregate'), graphql_name='cont_indices_3min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_options_1min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_options_1min'))), graphql_name='cont_options_1min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_options_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_options_1min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_options_1min_aggregate'), graphql_name='cont_options_1min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_options_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    features = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('features'))), graphql_name='features', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(features_bool_exp, graphql_name='where', default=None)),
))
    )
    features_aggregate = sgqlc.types.Field(sgqlc.types.non_null('features_aggregate'), graphql_name='features_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(features_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_15min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_15min'))), graphql_name='futures_15min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_15min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_15min_aggregate'), graphql_name='futures_15min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1day = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1day'))), graphql_name='futures_1day', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1day_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_1day_aggregate'), graphql_name='futures_1day_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1hour'))), graphql_name='futures_1hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_1hour_aggregate'), graphql_name='futures_1hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1min'))), graphql_name='futures_1min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_1min_aggregate'), graphql_name='futures_1min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_2hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_2hour'))), graphql_name='futures_2hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_2hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_2hour_aggregate'), graphql_name='futures_2hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_30min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_30min'))), graphql_name='futures_30min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_30min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_30min_aggregate'), graphql_name='futures_30min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_3min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_3min'))), graphql_name='futures_3min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_3min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_3min_aggregate'), graphql_name='futures_3min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_ticks'))), graphql_name='futures_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_ticks_aggregate'), graphql_name='futures_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_ticks_by_pk = sgqlc.types.Field('futures_ticks', graphql_name='futures_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    indices_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('indices_ticks'))), graphql_name='indices_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(indices_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    indices_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('indices_ticks_aggregate'), graphql_name='indices_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(indices_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    indices_ticks_by_pk = sgqlc.types.Field('indices_ticks', graphql_name='indices_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    master_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('master_data'))), graphql_name='master_data', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(master_data_bool_exp, graphql_name='where', default=None)),
))
    )
    master_data_aggregate = sgqlc.types.Field(sgqlc.types.non_null('master_data_aggregate'), graphql_name='master_data_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(master_data_bool_exp, graphql_name='where', default=None)),
))
    )
    master_data_by_pk = sgqlc.types.Field('master_data', graphql_name='master_data_by_pk', args=sgqlc.types.ArgDict((
        ('exchange', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='exchange', default=None)),
        ('tradingsymbol', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tradingsymbol', default=None)),
))
    )
    options_15min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_15min'))), graphql_name='options_15min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    options_15min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('options_15min_aggregate'), graphql_name='options_15min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    options_chain = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_chain'))), graphql_name='options_chain', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_chain_bool_exp, graphql_name='where', default=None)),
))
    )
    options_chain_aggregate = sgqlc.types.Field(sgqlc.types.non_null('options_chain_aggregate'), graphql_name='options_chain_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_chain_bool_exp, graphql_name='where', default=None)),
))
    )
    options_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_ticks'))), graphql_name='options_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    options_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('options_ticks_aggregate'), graphql_name='options_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    options_ticks_by_pk = sgqlc.types.Field('options_ticks', graphql_name='options_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    stocks_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('stocks_ticks'))), graphql_name='stocks_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(stocks_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    stocks_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('stocks_ticks_aggregate'), graphql_name='stocks_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(stocks_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    stocks_ticks_by_pk = sgqlc.types.Field('stocks_ticks', graphql_name='stocks_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('user'))), graphql_name='user', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(user_bool_exp, graphql_name='where', default=None)),
))
    )
    user_aggregate = sgqlc.types.Field(sgqlc.types.non_null('user_aggregate'), graphql_name='user_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(user_bool_exp, graphql_name='where', default=None)),
))
    )
    user_by_pk = sgqlc.types.Field('user', graphql_name='user_by_pk', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )


class stocks_ticks(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'master_datum', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instrument_token')
    last_price = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='last_price')
    master_datum = sgqlc.types.Field(sgqlc.types.non_null(master_data), graphql_name='master_datum')
    open_interest = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(sgqlc.types.non_null(float8), graphql_name='volume_traded')


class stocks_ticks_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('stocks_ticks_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks))), graphql_name='nodes')


class stocks_ticks_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('stocks_ticks_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('stocks_ticks_max_fields', graphql_name='max')
    min = sgqlc.types.Field('stocks_ticks_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('stocks_ticks_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('stocks_ticks_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('stocks_ticks_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('stocks_ticks_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('stocks_ticks_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('stocks_ticks_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('stocks_ticks_variance_fields', graphql_name='variance')


class stocks_ticks_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class stocks_ticks_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class stocks_ticks_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('exchange_timestamp', 'instrument_token', 'last_price', 'open_interest', 'volume_traded')
    exchange_timestamp = sgqlc.types.Field(timestamptz, graphql_name='exchange_timestamp')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class stocks_ticks_mutation_response(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks))), graphql_name='returning')


class stocks_ticks_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class stocks_ticks_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class stocks_ticks_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class stocks_ticks_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Int, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(float8, graphql_name='last_price')
    open_interest = sgqlc.types.Field(float8, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(float8, graphql_name='volume_traded')


class stocks_ticks_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class stocks_ticks_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class stocks_ticks_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('instrument_token', 'last_price', 'open_interest', 'volume_traded')
    instrument_token = sgqlc.types.Field(Float, graphql_name='instrument_token')
    last_price = sgqlc.types.Field(Float, graphql_name='last_price')
    open_interest = sgqlc.types.Field(Float, graphql_name='open_interest')
    volume_traded = sgqlc.types.Field(Float, graphql_name='volume_traded')


class subscription_root(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('cont_futures_15min', 'cont_futures_15min_aggregate', 'cont_futures_15min_stream', 'cont_futures_1day', 'cont_futures_1day_aggregate', 'cont_futures_1day_stream', 'cont_futures_1hour', 'cont_futures_1hour_aggregate', 'cont_futures_1hour_stream', 'cont_futures_1min', 'cont_futures_1min_aggregate', 'cont_futures_1min_stream', 'cont_futures_2hour', 'cont_futures_2hour_aggregate', 'cont_futures_2hour_stream', 'cont_futures_30min', 'cont_futures_30min_aggregate', 'cont_futures_30min_stream', 'cont_futures_3min', 'cont_futures_3min_aggregate', 'cont_futures_3min_stream', 'cont_indices_15min', 'cont_indices_15min_aggregate', 'cont_indices_15min_stream', 'cont_indices_1hour', 'cont_indices_1hour_aggregate', 'cont_indices_1hour_stream', 'cont_indices_1min', 'cont_indices_1min_aggregate', 'cont_indices_1min_stream', 'cont_indices_2hour', 'cont_indices_2hour_aggregate', 'cont_indices_2hour_stream', 'cont_indices_30min', 'cont_indices_30min_aggregate', 'cont_indices_30min_stream', 'cont_indices_3min', 'cont_indices_3min_aggregate', 'cont_indices_3min_stream', 'cont_options_1min', 'cont_options_1min_aggregate', 'cont_options_1min_stream', 'features', 'features_aggregate', 'features_stream', 'futures_15min', 'futures_15min_aggregate', 'futures_15min_stream', 'futures_1day', 'futures_1day_aggregate', 'futures_1day_stream', 'futures_1hour', 'futures_1hour_aggregate', 'futures_1hour_stream', 'futures_1min', 'futures_1min_aggregate', 'futures_1min_stream', 'futures_2hour', 'futures_2hour_aggregate', 'futures_2hour_stream', 'futures_30min', 'futures_30min_aggregate', 'futures_30min_stream', 'futures_3min', 'futures_3min_aggregate', 'futures_3min_stream', 'futures_ticks', 'futures_ticks_aggregate', 'futures_ticks_by_pk', 'futures_ticks_stream', 'indices_ticks', 'indices_ticks_aggregate', 'indices_ticks_by_pk', 'indices_ticks_stream', 'master_data', 'master_data_aggregate', 'master_data_by_pk', 'master_data_stream', 'options_15min', 'options_15min_aggregate', 'options_15min_stream', 'options_chain', 'options_chain_aggregate', 'options_chain_stream', 'options_ticks', 'options_ticks_aggregate', 'options_ticks_by_pk', 'options_ticks_stream', 'stocks_ticks', 'stocks_ticks_aggregate', 'stocks_ticks_by_pk', 'stocks_ticks_stream', 'user', 'user_aggregate', 'user_by_pk', 'user_stream')
    cont_futures_15min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_15min'))), graphql_name='cont_futures_15min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_15min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_15min_aggregate'), graphql_name='cont_futures_15min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_15min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_15min'))), graphql_name='cont_futures_15min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_futures_15min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1day = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1day'))), graphql_name='cont_futures_1day', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1day_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1day_aggregate'), graphql_name='cont_futures_1day_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1day_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1day_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1day'))), graphql_name='cont_futures_1day_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_futures_1day_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1hour'))), graphql_name='cont_futures_1hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1hour_aggregate'), graphql_name='cont_futures_1hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1hour_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1hour'))), graphql_name='cont_futures_1hour_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_futures_1hour_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1min'))), graphql_name='cont_futures_1min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_1min_aggregate'), graphql_name='cont_futures_1min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_1min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_1min'))), graphql_name='cont_futures_1min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_futures_1min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_2hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_2hour'))), graphql_name='cont_futures_2hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_2hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_2hour_aggregate'), graphql_name='cont_futures_2hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_2hour_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_2hour'))), graphql_name='cont_futures_2hour_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_futures_2hour_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_30min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_30min'))), graphql_name='cont_futures_30min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_30min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_30min_aggregate'), graphql_name='cont_futures_30min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_30min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_30min'))), graphql_name='cont_futures_30min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_futures_30min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_3min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_3min'))), graphql_name='cont_futures_3min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_3min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_futures_3min_aggregate'), graphql_name='cont_futures_3min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_futures_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_futures_3min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_futures_3min'))), graphql_name='cont_futures_3min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_futures_3min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_15min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_15min'))), graphql_name='cont_indices_15min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_15min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_15min_aggregate'), graphql_name='cont_indices_15min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_15min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_15min'))), graphql_name='cont_indices_15min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_indices_15min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1hour'))), graphql_name='cont_indices_1hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_1hour_aggregate'), graphql_name='cont_indices_1hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1hour_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1hour'))), graphql_name='cont_indices_1hour_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_indices_1hour_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1min'))), graphql_name='cont_indices_1min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_1min_aggregate'), graphql_name='cont_indices_1min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_1min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_1min'))), graphql_name='cont_indices_1min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_indices_1min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_2hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_2hour'))), graphql_name='cont_indices_2hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_2hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_2hour_aggregate'), graphql_name='cont_indices_2hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_2hour_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_2hour'))), graphql_name='cont_indices_2hour_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_indices_2hour_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_30min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_30min'))), graphql_name='cont_indices_30min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_30min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_30min_aggregate'), graphql_name='cont_indices_30min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_30min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_30min'))), graphql_name='cont_indices_30min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_indices_30min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_3min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_3min'))), graphql_name='cont_indices_3min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_3min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_indices_3min_aggregate'), graphql_name='cont_indices_3min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_indices_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_indices_3min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_indices_3min'))), graphql_name='cont_indices_3min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_indices_3min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_indices_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_options_1min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_options_1min'))), graphql_name='cont_options_1min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_options_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_options_1min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('cont_options_1min_aggregate'), graphql_name='cont_options_1min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(cont_options_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(cont_options_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    cont_options_1min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('cont_options_1min'))), graphql_name='cont_options_1min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(cont_options_1min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(cont_options_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    features = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('features'))), graphql_name='features', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(features_bool_exp, graphql_name='where', default=None)),
))
    )
    features_aggregate = sgqlc.types.Field(sgqlc.types.non_null('features_aggregate'), graphql_name='features_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(features_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(features_bool_exp, graphql_name='where', default=None)),
))
    )
    features_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('features'))), graphql_name='features_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(features_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(features_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_15min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_15min'))), graphql_name='futures_15min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_15min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_15min_aggregate'), graphql_name='futures_15min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_15min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_15min'))), graphql_name='futures_15min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(futures_15min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(futures_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1day = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1day'))), graphql_name='futures_1day', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1day_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_1day_aggregate'), graphql_name='futures_1day_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1day_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1day_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1day'))), graphql_name='futures_1day_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(futures_1day_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(futures_1day_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1hour'))), graphql_name='futures_1hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_1hour_aggregate'), graphql_name='futures_1hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1hour_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1hour'))), graphql_name='futures_1hour_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(futures_1hour_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(futures_1hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1min'))), graphql_name='futures_1min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_1min_aggregate'), graphql_name='futures_1min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_1min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_1min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_1min'))), graphql_name='futures_1min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(futures_1min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(futures_1min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_2hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_2hour'))), graphql_name='futures_2hour', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_2hour_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_2hour_aggregate'), graphql_name='futures_2hour_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_2hour_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_2hour_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_2hour'))), graphql_name='futures_2hour_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(futures_2hour_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(futures_2hour_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_30min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_30min'))), graphql_name='futures_30min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_30min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_30min_aggregate'), graphql_name='futures_30min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_30min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_30min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_30min'))), graphql_name='futures_30min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(futures_30min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(futures_30min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_3min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_3min'))), graphql_name='futures_3min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_3min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_3min_aggregate'), graphql_name='futures_3min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_3min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_3min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_3min'))), graphql_name='futures_3min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(futures_3min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(futures_3min_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_ticks'))), graphql_name='futures_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('futures_ticks_aggregate'), graphql_name='futures_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(futures_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(futures_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    futures_ticks_by_pk = sgqlc.types.Field('futures_ticks', graphql_name='futures_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    futures_ticks_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('futures_ticks'))), graphql_name='futures_ticks_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(futures_ticks_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(futures_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    indices_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('indices_ticks'))), graphql_name='indices_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(indices_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    indices_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('indices_ticks_aggregate'), graphql_name='indices_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(indices_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(indices_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    indices_ticks_by_pk = sgqlc.types.Field('indices_ticks', graphql_name='indices_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    indices_ticks_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('indices_ticks'))), graphql_name='indices_ticks_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(indices_ticks_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(indices_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    master_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('master_data'))), graphql_name='master_data', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(master_data_bool_exp, graphql_name='where', default=None)),
))
    )
    master_data_aggregate = sgqlc.types.Field(sgqlc.types.non_null('master_data_aggregate'), graphql_name='master_data_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(master_data_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(master_data_bool_exp, graphql_name='where', default=None)),
))
    )
    master_data_by_pk = sgqlc.types.Field('master_data', graphql_name='master_data_by_pk', args=sgqlc.types.ArgDict((
        ('exchange', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='exchange', default=None)),
        ('tradingsymbol', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tradingsymbol', default=None)),
))
    )
    master_data_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('master_data'))), graphql_name='master_data_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(master_data_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(master_data_bool_exp, graphql_name='where', default=None)),
))
    )
    options_15min = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_15min'))), graphql_name='options_15min', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    options_15min_aggregate = sgqlc.types.Field(sgqlc.types.non_null('options_15min_aggregate'), graphql_name='options_15min_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_15min_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    options_15min_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_15min'))), graphql_name='options_15min_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(options_15min_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(options_15min_bool_exp, graphql_name='where', default=None)),
))
    )
    options_chain = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_chain'))), graphql_name='options_chain', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_chain_bool_exp, graphql_name='where', default=None)),
))
    )
    options_chain_aggregate = sgqlc.types.Field(sgqlc.types.non_null('options_chain_aggregate'), graphql_name='options_chain_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_chain_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_chain_bool_exp, graphql_name='where', default=None)),
))
    )
    options_chain_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_chain'))), graphql_name='options_chain_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(options_chain_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(options_chain_bool_exp, graphql_name='where', default=None)),
))
    )
    options_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_ticks'))), graphql_name='options_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    options_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('options_ticks_aggregate'), graphql_name='options_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(options_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(options_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    options_ticks_by_pk = sgqlc.types.Field('options_ticks', graphql_name='options_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    options_ticks_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('options_ticks'))), graphql_name='options_ticks_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(options_ticks_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(options_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    stocks_ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('stocks_ticks'))), graphql_name='stocks_ticks', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(stocks_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    stocks_ticks_aggregate = sgqlc.types.Field(sgqlc.types.non_null('stocks_ticks_aggregate'), graphql_name='stocks_ticks_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(stocks_ticks_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(stocks_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    stocks_ticks_by_pk = sgqlc.types.Field('stocks_ticks', graphql_name='stocks_ticks_by_pk', args=sgqlc.types.ArgDict((
        ('exchange_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(timestamptz), graphql_name='exchange_timestamp', default=None)),
        ('instrument_token', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='instrument_token', default=None)),
))
    )
    stocks_ticks_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('stocks_ticks'))), graphql_name='stocks_ticks_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(stocks_ticks_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(stocks_ticks_bool_exp, graphql_name='where', default=None)),
))
    )
    user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('user'))), graphql_name='user', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(user_bool_exp, graphql_name='where', default=None)),
))
    )
    user_aggregate = sgqlc.types.Field(sgqlc.types.non_null('user_aggregate'), graphql_name='user_aggregate', args=sgqlc.types.ArgDict((
        ('distinct_on', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_select_column)), graphql_name='distinct_on', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_order_by)), graphql_name='order_by', default=None)),
        ('where', sgqlc.types.Arg(user_bool_exp, graphql_name='where', default=None)),
))
    )
    user_by_pk = sgqlc.types.Field('user', graphql_name='user_by_pk', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    user_stream = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('user'))), graphql_name='user_stream', args=sgqlc.types.ArgDict((
        ('batch_size', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='batch_size', default=None)),
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(user_stream_cursor_input)), graphql_name='cursor', default=None)),
        ('where', sgqlc.types.Arg(user_bool_exp, graphql_name='where', default=None)),
))
    )


class user(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age', 'name')
    age = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='age')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class user_aggregate(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('aggregate', 'nodes')
    aggregate = sgqlc.types.Field('user_aggregate_fields', graphql_name='aggregate')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(user))), graphql_name='nodes')


class user_aggregate_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('avg', 'count', 'max', 'min', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance')
    avg = sgqlc.types.Field('user_avg_fields', graphql_name='avg')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count', args=sgqlc.types.ArgDict((
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(user_select_column)), graphql_name='columns', default=None)),
        ('distinct', sgqlc.types.Arg(Boolean, graphql_name='distinct', default=None)),
))
    )
    max = sgqlc.types.Field('user_max_fields', graphql_name='max')
    min = sgqlc.types.Field('user_min_fields', graphql_name='min')
    stddev = sgqlc.types.Field('user_stddev_fields', graphql_name='stddev')
    stddev_pop = sgqlc.types.Field('user_stddev_pop_fields', graphql_name='stddev_pop')
    stddev_samp = sgqlc.types.Field('user_stddev_samp_fields', graphql_name='stddev_samp')
    sum = sgqlc.types.Field('user_sum_fields', graphql_name='sum')
    var_pop = sgqlc.types.Field('user_var_pop_fields', graphql_name='var_pop')
    var_samp = sgqlc.types.Field('user_var_samp_fields', graphql_name='var_samp')
    variance = sgqlc.types.Field('user_variance_fields', graphql_name='variance')


class user_avg_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Float, graphql_name='age')


class user_max_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age', 'name')
    age = sgqlc.types.Field(Int, graphql_name='age')
    name = sgqlc.types.Field(String, graphql_name='name')


class user_min_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age', 'name')
    age = sgqlc.types.Field(Int, graphql_name='age')
    name = sgqlc.types.Field(String, graphql_name='name')


class user_mutation_response(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('affected_rows', 'returning')
    affected_rows = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affected_rows')
    returning = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(user))), graphql_name='returning')


class user_stddev_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Float, graphql_name='age')


class user_stddev_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Float, graphql_name='age')


class user_stddev_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Float, graphql_name='age')


class user_sum_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Int, graphql_name='age')


class user_var_pop_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Float, graphql_name='age')


class user_var_samp_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Float, graphql_name='age')


class user_variance_fields(sgqlc.types.Type):
    __schema__ = ticker_schema
    __field_names__ = ('age',)
    age = sgqlc.types.Field(Float, graphql_name='age')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
ticker_schema.query_type = query_root
ticker_schema.mutation_type = mutation_root
ticker_schema.subscription_type = subscription_root

