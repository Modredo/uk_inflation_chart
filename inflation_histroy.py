import matplotlib.pyplot as plt

# Approximate UK annual inflation rates (in %) keyed by year
# Pre-1970 figures are based on older indices, so treat them as broad estimates.
uk_inflation_data = {
    # 1950s
    1950: 2.8,
    1951: 9.0,
    1952: 5.9,
    1953: 3.1,
    1954: 0.9,
    1955: 4.5,
    1956: 4.9,
    1957: 3.7,
    1958: 3.0,
    1959: 0.5,
    # 1960s
    1960: 1.0,
    1961: 2.6,
    1962: 2.7,
    1963: 1.3,
    1964: 3.3,
    1965: 4.8,
    1966: 3.9,
    1967: 2.5,
    1968: 4.7,
    1969: 5.0,
    # 1970s
    1970: 6.4,
    1971: 9.4,
    1972: 7.1,
    1973: 9.2,
    1974: 16.0,
    1975: 24.2,
    1976: 16.5,
    1977: 15.8,
    1978: 8.3,
    1979: 13.4,
    # 1980s
    1980: 18.0,
    1981: 11.9,
    1982: 8.6,
    1983: 4.6,
    1984: 5.0,
    1985: 6.1,
    1986: 3.4,
    1987: 4.2,
    1988: 4.9,
    1989: 7.8,
    # 1990s
    1990: 9.5,
    1991: 5.9,
    1992: 3.7,
    1993: 1.6,
    1994: 2.0,
    1995: 2.9,
    1996: 2.4,
    1997: 3.1,
    1998: 3.4,
    1999: 1.3,
    # 2000s
    2000: 1.0,
    2001: 1.2,
    2002: 1.3,
    2003: 1.4,
    2004: 1.3,
    2005: 2.1,
    2006: 2.3,
    2007: 2.3,
    2008: 3.6,
    2009: 2.2,
    # 2010s
    2010: 3.3,
    2011: 4.5,
    2012: 2.8,
    2013: 2.6,
    2014: 1.5,
    2015: 0.0,
    2016: 0.7,
    2017: 2.7,
    2018: 2.5,
    2019: 1.8,
    # 2020s
    2020: 0.9,
    2021: 2.6,
    2022: 9.1,
}

years = list(uk_inflation_data.keys())
inflation_rates = list(uk_inflation_data.values())

plt.figure(figsize=(16, 6))
plt.bar(years, inflation_rates, color='navy')

plt.title("Approximate Historical UK Inflation by Year (1950–2022)")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.grid(axis='y', linestyle='--', alpha=0.5)

# To avoid clutter, show an x-axis tick only for every 5th year
plt.xticks([year for year in years if year % 5 == 0])

plt.show()
