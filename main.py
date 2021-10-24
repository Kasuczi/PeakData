import pandas as pd


def main():
    """
    The func genrates a .csv file contains author and institution info
    :return: DataFrame
    """
    main_data = pd.read_csv('publications_min.csv.gz', compression='gzip', index_col=False,
                            dtype={'authors': str, 'affiliations': str})
    if 'Unnamed: 0' in main_data.columns:
        del main_data['Unnamed: 0']
    main_data = main_data[['authors', 'affiliations']]
    main_data = main_data[main_data['authors'].isna() is False]
    main_data['authors'] = main_data.authors.apply(lambda x: x[1:-1].split(','))
    main_data = main_data.explode('authors').drop_duplicates()
    main_data['authors'] = main_data['authors'].replace({"'": ''}, regex=True)
    main_data['authors'] = main_data['authors'].replace({'"': ''}, regex=True)
    main_data['affiliations'] = main_data['affiliations'].replace({",": ''}, regex=True)
    main_data['authors'] = main_data['authors'].str.strip()
    main_data['affiliations'] = main_data['affiliations'].str.strip()
    main_data = main_data.drop_duplicates()
    if user_dec == 'Y':
        main_data = main_data[main_data['affiliations'].str.contains('[A-Za-z]', na=False)]
    return main_data


if __name__ == '__main__':
    user_dec = input('Would You like to find only those authors which has any affiliations ? Y/N : ')
    main().to_csv(r'PeakData.csv', sep='|', index=False, encoding='utf-8-sig', compression='gzip')



