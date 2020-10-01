import pandas as pd


def dialogue_text(df, search_term):
    '''
    Takes dataframe of lines of dialogue and converts it to a text file

    Parameters
    ----------
    df: pd.DataFrame
    search_term: str

    Returns:
    -------
    None

    Text is written to file
    '''

    outfile = f'{search_term}_dlg.txt'
    _name = f"Dialogue Results for {search_term}\n\n\n"

    write_title(_name, outfile)

    for idx, row in df.iterrows():
        if pd.isnull(row.VoiceOverComment):
            comment = ""
        else:
            comment = " ({})".format(row.VoiceOverComment)

        with open(outfile, 'w') as f:
            f.write('{}{}:\n{}\n\n'.format(row.Speaker, comment, row.Text))


def codex_text(df, search_term):
    _name = f"Codex Results for {search_term}"

    with open(f'{search_term}_cdx.txt', 'w') as f:
        f.write(_name)

    for i, row in df.iterrows():

        outfile = f'{search_term}_cdx.txt'
        codex_name = row.Title

        write_title(codex_name, outfile)

        if not row.Summary or pd.isnull(row.Summary):
            summary = ""
        else:
            summary = "{}\n\n".format(row.Summary)

        with open('{}_cdx.txt'.format(search_term), 'w') as f:
            f.write('{}{}\n\n'.format(summary, row.Contents))


def write_title(title: str, outfile: str):
    t_b = ''.join(['*'] * (len(title) * 3))
    pad = ''.join(['-'] * len(title))
    inner = pad + title + pad

    with open(outfile, 'w') as f:
        f.write('{}\n{}\n{}\n\n\n'.format(t_b, inner, t_b))
