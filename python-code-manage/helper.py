import re

SUFFIXES = ["*.html", "*.php"]
SWAPS = {
    "ETF": "Etf",
    "FIGI": "Figi",
    "ID": "Id",
    "PERatio": "PeRatio",
    "CrankNicolsonFD": "CrankNicolsonFd",
    "SP500EMini": "sp500_emini",
    "CrudeOilWTI": "CrudeOilWti",
    "BinanceUS": "BinanceUs",
    "OECDRecessionIndicators": "OecdRecessionIndicators",
    "QuantConnectBrokerage": "QuantconnectBrokerage",
    "TDAmeritrade": "TdAmeritrade",
    "VWAP": "Vwap",
    "OneWeekBasedOnUSD": "OneWeekBasedOnUsd"
}
EXCEPTIONS = [
    "ElementTree",
    "SMA",
    "EMA",
    "QuantConnect.Data",
    "QuantConnect.Data.UniverseSelection",
    "QuantConnect.DataSource",
    "QuantConnect.Python",
    "QuantConnect.symbol",
    "GaussianHMM",
    "ht_auth.SetToken",
    "nn.Module",
    "nn.Sequential",
    "nn.Linear",
    "nn.Flatten",
    "nn.ReLU",
    "nn.MSELoss",
    "gym.Env",
    "gym.spaces.Discrete",
    "gym.spaces.Box",
    "tf.Session",
    "tf.Variable",
    "tf.train.AdamOptimizer",
    "json_format.MessageToJson",
    "json_format.Parse",
    "tf.MetaGraphDef",
    "xgb.DMatrix",
    "Selection.OptionUniverseSelectionModel",
    "Selection.FutureUniverseSelectionModel",
    "pd.DataFrame",
    "pd.Series",
    "pd.MultiIndex",
    "opt.TargetWeights",
    "opt.MaxGrossExposure",
    "opt.DollarNeutral",
    "go.Candlestick",
    "go.Layout",
    "go.layout.Title",
    "go.Figure",
    "go.Scatter",
    "go.scatter.Marker",
    "Newtonsoft.Json",
    "System.Collections.Generic",
    "JsonConvert.SerializeObject",
    "Calculators.TaxesCalculator"
]

def get_code_snippet(pre_content):
    content = str(pre_content).split('>', maxsplit=1)[1].rsplit("</pre>", 1)[0]
    return content

def conversion(content):
    # do not check for the string in EXCEPTIONS list
    content_to_check = content
    for e in EXCEPTIONS:
        content_to_check = content_to_check.replace(e, "")
    
    methods = re.findall(r"def\s+([A-Za-z0-9_]+)\s*\(", content_to_check)

    for method in sorted(methods, key=len, reverse=True):
        snake_case_method = _title_to_snake_case(method)
        content = content.replace(f"def {method}(", f"def {snake_case_method}(")
    
    methods = re.findall(r"\.([A-Za-z0-9_]+)", content_to_check)

    for method in sorted(methods, key=len, reverse=True):
        snake_case_method = _title_to_snake_case(method)
        content = content.replace(f".{method}", f".{snake_case_method}")
    
    methods = re.findall(r"<\?=\$research \? \"qb\.\" : \"self\.\"\?>([A-Za-z0-9_]+)", content_to_check)

    for method in sorted(methods, key=len, reverse=True):
        snake_case_method = _title_to_snake_case(method)
        content = content.replace(f"<?=$research ? \"qb.\" : \"self.\"?>{method}", f"<?=$research ? \"qb.\" : \"self.\"?>{snake_case_method}")
    
    methods = re.findall(r"<\?=\$pythonPrefix\?>([A-Za-z0-9_]+)", content_to_check)

    for method in sorted(methods, key=len, reverse=True):
        snake_case_method = _title_to_snake_case(method)
        content = content.replace(f"<?=$pythonPrefix?>{method}", f"<?=$pythonPrefix?>{snake_case_method}")
        
    return content

def _title_to_snake_case(title):
    for original, new in SWAPS.items():
        if original in title:
            title = title.replace(original, new)
        
    # for whole method is upper case: indicators, ID, ...
    if title.isupper():
        return title
    
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', title).lower()
    return snake_case