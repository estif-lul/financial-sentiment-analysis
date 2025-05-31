import talib

class TechnicalIndicators:
    def __init__(self, df, price_col='Close'):
        self.df = df
        self.price_col = price_col

    def add_sma(self, period=20, col_name=None):
        col_name = col_name or f'SMA_{period}'
        self.df[col_name] = talib.SMA(self.df[self.price_col], timeperiod=period)

    def add_ema(self, period=20, col_name=None):
        col_name = col_name or f'EMA_{period}'
        self.df[col_name] = talib.EMA(self.df[self.price_col], timeperiod=period)

    def add_rsi(self, period=14, col_name='RSI'):
        self.df[col_name] = talib.RSI(self.df[self.price_col], timeperiod=period)

    def add_macd(self, fastperiod=12, slowperiod=26, signalperiod=9):
        macd, macd_signal, macd_hist = talib.MACD(
            self.df[self.price_col], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod
        )
        self.df['MACD'] = macd
        self.df['MACD_signal'] = macd_signal
        self.df['MACD_hist'] = macd_hist

    def add_all(self):
        self.add_sma()
        self.add_ema()
        self.add_rsi()
        self.add_macd()