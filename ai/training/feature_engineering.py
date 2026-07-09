import math
import statistics
from datetime import datetime, timedelta


DATE_FORMAT = "%d-%m-%Y"


def parse_date(date_str):
    return datetime.strptime(date_str, DATE_FORMAT)


def calculate_return(current_nav, old_nav):

    if old_nav is None or old_nav <= 0:
        return None

    return ((current_nav - old_nav) / old_nav) * 100

def calculate_cagr(beginning_value, ending_value, years):

    if (
        beginning_value is None
        or ending_value is None
        or beginning_value <= 0
        or ending_value <= 0
        or years <= 0
    ):
        return None

    return (((ending_value / beginning_value) ** (1 / years)) - 1) * 100


def calculate_daily_returns(nav_list):
    returns = []

    for i in range(len(nav_list) - 1):
        returns.append(
            (nav_list[i] - nav_list[i + 1]) / nav_list[i + 1]
        )

    return returns


def calculate_volatility(daily_returns):
    if len(daily_returns) < 2:
        return None

    return statistics.stdev(daily_returns) * math.sqrt(252) * 100


def calculate_max_drawdown(nav_list):

    peak = nav_list[0]
    max_drawdown = 0

    for nav in nav_list:

        if nav > peak:
            peak = nav

        drawdown = ((nav - peak) / peak) * 100

        if drawdown < max_drawdown:
            max_drawdown = drawdown

    return max_drawdown

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.06):

    if len(daily_returns) < 2:
        return 0.0

    annual_return = statistics.mean(daily_returns) * 252
    annual_volatility = statistics.stdev(daily_returns) * math.sqrt(252)

    if annual_volatility <= 1e-10:
        return 0.0

    return (annual_return - risk_free_rate) / annual_volatility

def calculate_risk_level(volatility):

    if volatility is None:
        return "Unknown"

    if volatility < 5:
        return "Low"

    if volatility < 15:
        return "Moderate"

    return "High"


def get_nav_for_years(nav_history, years):
    """
    Find the NAV closest to N years ago.
    """

    latest_date = parse_date(nav_history[0]["date"])

    target_date = latest_date - timedelta(days=365 * years)

    closest = min(
        nav_history,
        key=lambda x: abs(
            parse_date(x["date"]) - target_date
        )
    )

    return float(closest["nav"])